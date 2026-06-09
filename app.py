from flask import Flask, render_template, request, jsonify
import os
import base64
import cv2
import numpy as np
import time
import requests
from dotenv import load_dotenv
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

LOGIN_API_URL = os.getenv("LOGIN_API_URL", "").strip()
ATTENDANCE_API_URL = os.getenv("ATTENDANCE_API_URL", "").strip()
ENCKEY = os.getenv("ENCKEY", "").strip()
CHECKTYPE = os.getenv("CHECKTYPE", "I").strip()
LATITUDE = os.getenv("LATITUDE", "11.0346474").strip()
LONGITUDE = os.getenv("LONGITUDE", "77.0188038").strip()

app = Flask(__name__)

FACE_DIR = "/home/va-nuc/Desktop/face_attendance/new_working_code/gallery"
MODEL_PATH = "models/face_landmarker.task"

os.makedirs(FACE_DIR, exist_ok=True)

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_facial_transformation_matrixes=True,
    num_faces=1
)

landmarker = vision.FaceLandmarker.create_from_options(options)

capture_state = {
    "phase": "frontal",
    "count": {
        "frontal": 0,
        "left": 0,
        "right": 0
    },
    "last_capture": 0,
    "attendance_uploaded": False
}


def verify_passcode(passcode):
    try:
        url = f"{LOGIN_API_URL}?Password={passcode}"

        headers = {
            "Enckey": ENCKEY
        }

        res = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print("LOGIN STATUS:", res.status_code)
        print("LOGIN RESPONSE:", res.text)

        return res.json()

    except Exception as e:
        print("LOGIN ERROR:", str(e))
        return None


def upload_attendance(emp_id, image_path):
    try:
        headers = {
            "Enckey": ENCKEY
        }

        with open(image_path, "rb") as f:
            files = {
                "file": f
            }

            payload = {
                "empid": emp_id,
                "checktype": CHECKTYPE,
                "Latitude": LATITUDE,
                "Longitude": LONGITUDE
            }

            res = requests.post(
                ATTENDANCE_API_URL,
                headers=headers,
                data=payload,
                files=files,
                timeout=30
            )

        print("ATTENDANCE STATUS:", res.status_code)
        print("ATTENDANCE RESPONSE:", res.text)

        return res.json()

    except Exception as e:
        print("ATTENDANCE ERROR:", str(e))
        return None


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/verify", methods=["POST"])
def verify():
    try:
        passcode = request.form.get("passcode", "").strip()

        if not passcode:
            return jsonify({
                "status": "fail",
                "message": "Passcode missing"
            })

        login_result = verify_passcode(passcode)

        if not login_result:
            return jsonify({
                "status": "fail",
                "message": "Login API failed"
            })

        if not login_result.get("Status"):
            return jsonify({
                "status": "fail",
                "message": "Invalid passcode"
            })

        employee_details = login_result.get("Data", {}).get("EmployeeDetails", {})

        employee_id = employee_details.get("id")

        if not employee_id:
            return jsonify({
                "status": "fail",
                "message": "Employee ID missing"
            })

        return jsonify({
            "status": "success",
            "name": employee_details.get("fullName", "Employee"),
            "emp_id": employee_id,
            "designation": employee_details.get("designation_name", "Employee"),
            "team": "N/A"
        })

    except Exception as e:
        print("VERIFY ERROR:", str(e))
        return jsonify({
            "status": "fail",
            "message": str(e)
        })


@app.route("/capture/<passcode>/<emp_id>")
def capture(passcode, emp_id):
    global capture_state

    capture_state = {
        "phase": "frontal",
        "count": {
            "frontal": 0,
            "left": 0,
            "right": 0
        },
        "last_capture": 0,
        "attendance_uploaded": False
    }

    return render_template(
        "capture.html",
        passcode=passcode,
        emp_id=emp_id
    )


@app.route("/success")
def success():
    return render_template("success.html")


def detect_pose(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_img = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = landmarker.detect(mp_img)

    if not result.face_landmarks:
        return None, None

    lm = result.face_landmarks[0]
    h, w, _ = frame.shape

    xs = [p.x * w for p in lm]
    ys = [p.y * h for p in lm]

    bbox = [
        int(min(xs)),
        int(min(ys)),
        int(max(xs)),
        int(max(ys))
    ]

    face2d = []
    face3d = []

    for idx in [1, 152, 33, 263, 61, 291]:
        p = lm[idx]

        x = int(p.x * w)
        y = int(p.y * h)

        face2d.append([x, y])
        face3d.append([x, y, p.z])

    face2d = np.array(face2d, dtype=np.float64)
    face3d = np.array(face3d, dtype=np.float64)

    cam_matrix = np.array([
        [w, 0, w / 2],
        [0, w, h / 2],
        [0, 0, 1]
    ])

    dist = np.zeros((4, 1))

    success, rot_vec, _ = cv2.solvePnP(
        face3d,
        face2d,
        cam_matrix,
        dist
    )

    if not success:
        return None, None

    rmat, _ = cv2.Rodrigues(rot_vec)
    angles, *_ = cv2.RQDecomp3x3(rmat)

    yaw = angles[1] * 360

    return yaw, bbox


def crop_face(frame, bbox):
    x1, y1, x2, y2 = bbox
    h, w, _ = frame.shape

    size = max(x2 - x1, y2 - y1)

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    pad = int(size * 0.4)

    nx1 = max(0, cx - size // 2 - pad)
    ny1 = max(0, cy - size // 2 - pad)
    nx2 = min(w, cx + size // 2 + pad)
    ny2 = min(h, cy + size // 2 + pad)

    return frame[ny1:ny2, nx1:nx2]


@app.route("/process_frame", methods=["POST"])
def process_frame():
    global capture_state

    data = request.json

    employee_id = data.get("emp_id")
    image_data = data.get("image")

    folder = os.path.join(FACE_DIR, employee_id)
    os.makedirs(folder, exist_ok=True)

    img = base64.b64decode(image_data.split(",")[1])

    frame = cv2.imdecode(
        np.frombuffer(img, np.uint8),
        cv2.IMREAD_COLOR
    )

    yaw, bbox = detect_pose(frame)

    if yaw is None:
        return jsonify({"status": "no_face"})

    phase = capture_state["phase"]
    matched = False

    if phase == "frontal" and -20 < yaw < 20:
        matched = True
    elif phase == "left" and 10 < yaw < 80:
        matched = True
    elif phase == "right" and -80 < yaw < -10:
        matched = True

    if matched and time.time() - capture_state["last_capture"] > 0.4:
        face = crop_face(frame, bbox)

        count = capture_state["count"][phase]
        saved_path = os.path.join(folder, f"{phase}_{count}.jpg")

        cv2.imwrite(saved_path, face)

        capture_state["count"][phase] += 1
        capture_state["last_capture"] = time.time()

    if capture_state["count"]["frontal"] >= 8:
        capture_state["phase"] = "left"

    if capture_state["count"]["left"] >= 6:
        capture_state["phase"] = "right"

    total = sum(capture_state["count"].values())

    if total >= 20 and not capture_state["attendance_uploaded"]:
        final_image = os.path.join(
            folder,
            f"right_{capture_state['count']['right'] - 1}.jpg"
        )

        if os.path.exists(final_image):
            #upload_attendance(employee_id, final_image)
            capture_state["attendance_uploaded"] = True

            return jsonify({"done": True})

    return jsonify({
        "phase": capture_state["phase"],
        "total": total,
        "done": False
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)