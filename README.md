<div align="center">

# 🎯 FACE RECOGNITION ATTENDANCE APP

### Intelligent Attendance Automation using Flask, OpenCV & MediaPipe

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge\&logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge\&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Tracking-orange?style=for-the-badge)
![License](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)

A production-ready face-based attendance management system that combines employee authentication, real-time face pose estimation, and automated attendance registration.

</div>

---

## 📌 Overview

This application enables employees to securely mark attendance using a passcode verification workflow combined with AI-powered facial analysis.

The system guides users through multiple face orientations, captures high-quality facial images, and automatically submits attendance records through enterprise APIs.

---

## ✨ Features

### 🔐 Authentication

* Passcode-based employee verification
* Secure API integration
* Employee information retrieval

### 🎥 Face Detection & Pose Analysis

* Real-time face detection
* MediaPipe Face Landmarker integration
* Head pose estimation
* Multi-angle face capture

### 📸 Guided Face Capture

* Frontal Face Detection
* Left Face Detection
* Right Face Detection
* Automatic image saving

### ⚡ Attendance Automation

* Attendance API integration
* Automatic attendance submission
* Employee attendance synchronization

### 🛡️ Configuration Management

* Environment variable support
* Secure API key handling
* Easy deployment configuration

---

## 🏗️ System Workflow

```text
Employee Login
      │
      ▼
Passcode Verification
      │
      ▼
Employee Validation
      │
      ▼
Camera Activation
      │
      ▼
Face Detection
      │
      ▼
Pose Analysis
      │
      ▼
Multi-Angle Capture
      │
      ▼
Attendance Upload
      │
      ▼
Success Confirmation
```

---

## 🛠️ Technology Stack

| Category          | Technologies      |
| ----------------- | ----------------- |
| Backend           | Python, Flask     |
| Computer Vision   | OpenCV, MediaPipe |
| Data Processing   | NumPy             |
| API Communication | Requests          |
| Configuration     | Python Dotenv     |
| Deployment        | Linux / Ubuntu    |

---

## 📂 Project Structure

```text
Face_Recognition_Attendance_App/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── models/
│   └── face_landmarker.task
│
├── templates/
│   ├── login.html
│   ├── capture.html
│   └── success.html
│
├── gallery/
│   └── employee_images/
│
└── static/
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root directory.

```env
LOGIN_API_URL=
ATTENDANCE_API_URL=
ENCKEY=

CHECKTYPE=I

LATITUDE=
LONGITUDE=
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone git@github.com:Dharma5901/Face_Recognition_Attendance_App.git
cd Face_Recognition_Attendance_App
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Application will be available at:

```text
http://localhost:5000
```

---

## 🔄 Application Flow

1. Employee enters a valid passcode.
2. Authentication API validates the employee.
3. Employee information is retrieved.
4. Camera interface is initialized.
5. Face pose estimation begins.
6. Frontal, left, and right facial images are captured.
7. Images are stored locally.
8. Attendance is automatically submitted.
9. Success page is displayed.

---

## 🎯 Core Functionalities

### Employee Verification

Validates employee credentials through a secure backend authentication service.

### Face Pose Estimation

Uses MediaPipe Face Landmarker and OpenCV-based head pose estimation to accurately determine user orientation.

### Automated Attendance Submission

Automatically uploads attendance records once the face capture process is completed.

---

## 🔮 Future Enhancements

* Face Recognition Verification
* Face Liveness Detection
* Employee Dashboard
* Attendance Reports
* Docker Deployment
* Kubernetes Support
* Cloud Storage Integration
* Multi-Camera Support
* Role-Based Access Control

---

## 💼 Use Cases

* Corporate Offices
* Manufacturing Plants
* Smart Buildings
* Educational Institutions
* Residential Communities
* Access Control Systems

---

## 👨‍💻 Author

### Dharmaraj B

**AI/ML Engineer | Computer Vision Developer**

#### Skills

* Computer Vision
* Face Recognition
* Object Detection
* Deep Learning
* Real-Time Video Analytics
* Edge AI Deployment

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star.

Built with ❤️ using Python, Flask, OpenCV and MediaPipe

</div>
