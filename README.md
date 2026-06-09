# Face Recognition Attendance App

A Flask-based Face Recognition Attendance System that verifies employees using a passcode and captures multiple face poses (frontal, left, and right) for attendance registration.

## Features

* Employee authentication using Passcode API
* Real-time face detection using MediaPipe Face Landmarker
* Automatic face pose estimation (Frontal, Left, Right)
* Multi-angle face image capture
* Attendance API integration
* Secure environment variable configuration
* Web-based user interface using Flask
* Automatic attendance submission after successful face capture

---

## Technology Stack

### Backend

* Python
* Flask

### Computer Vision

* OpenCV
* MediaPipe Face Landmarker
* NumPy

### APIs & Networking

* Requests
* REST API Integration

### Configuration

* Python Dotenv

---

## Project Workflow

1. Employee enters a passcode.
2. System validates the passcode through the Login API.
3. Employee details are fetched from the server.
4. Camera opens and starts face capture.
5. User is guided through:

   * Frontal Face
   * Left Face
   * Right Face
6. Captured face images are stored locally.
7. Final image is uploaded through the Attendance API.
8. Attendance is marked successfully.

---

## Project Structure

```text
project/
│
├── app.py
├── .env
├── models/
│   └── face_landmarker.task
│
├── gallery/
│   └── employee_images/
│
├── templates/
│   ├── login.html
│   ├── capture.html
│   └── success.html
│
└── requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
LOGIN_API_URL=
ATTENDANCE_API_URL=
ENCKEY=

CHECKTYPE=I

LATITUDE=11.0346474
LONGITUDE=77.0188038
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Face_Recognition_Attendance_App.git

cd Face_Recognition_Attendance_App
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will start at:

```text
http://localhost:5000
```

---

## Key Functionalities

### Passcode Verification

Validates employee credentials using a remote authentication API.

### Face Pose Detection

Uses MediaPipe Face Landmarker and head pose estimation to detect:

* Frontal Face
* Left Face
* Right Face

### Attendance Upload

Uploads employee attendance data along with the captured face image to the attendance server.

---

## Future Improvements

* Face Recognition Matching
* Face Liveness Detection
* Attendance Dashboard
* Employee Management Portal
* Attendance Reports
* Docker Deployment
* Multi-Camera Support

---

## Author

Dharmaraj B

AI/ML Engineer | Computer Vision Developer

Specialized in:

* Face Recognition
* Object Detection
* Real-Time Video Analytics
* AI-Based Automation Systems
