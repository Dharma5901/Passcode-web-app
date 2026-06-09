# FACE RECOGNITION ATTENDANCE APP 

A production-ready attendance management system built using Flask, OpenCV, and MediaPipe Face Landmarker. The application authenticates employees through a secure passcode-based workflow, captures facial images from multiple angles, and automatically records attendance through REST API integration.

## Overview

This project streamlines employee attendance registration by combining identity verification and computer vision technologies. The system performs real-time face pose analysis, captures high-quality facial images from multiple viewpoints, and integrates seamlessly with enterprise attendance management platforms.

## Key Features

### Employee Authentication

* Secure passcode-based employee verification
* REST API integration for credential validation
* Dynamic employee information retrieval

### Intelligent Face Capture

* Real-time face detection using MediaPipe Face Landmarker
* Head pose estimation and orientation tracking
* Guided multi-angle face acquisition:

  * Frontal View
  * Left Profile View
  * Right Profile View
* Automated image quality and pose validation

### Attendance Automation

* Automatic attendance submission upon successful face capture
* Employee attendance record synchronization via API
* Configurable check-in/check-out workflows

### System Configuration

* Environment variable-based configuration management
* Secure API key handling
* Flexible deployment across different environments

---

## Architecture

```text
User Authentication
        │
        ▼
Passcode Validation API
        │
        ▼
Employee Verification
        │
        ▼
Camera Initialization
        │
        ▼
Face Detection & Pose Analysis
        │
        ▼
Multi-Angle Face Capture
        │
        ▼
Attendance API Submission
        │
        ▼
Attendance Successfully Marked
```

---

## Technology Stack

### Backend Framework

* Python
* Flask

### Computer Vision & AI

* OpenCV
* MediaPipe Face Landmarker
* NumPy

### API Integration

* Requests
* RESTful APIs

### Environment Management

* Python Dotenv

---

## Project Structure

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

## Environment Variables

Create a `.env` file in the project root directory.

```env
LOGIN_API_URL=
ATTENDANCE_API_URL=
ENCKEY=

CHECKTYPE=I

LATITUDE=
LONGITUDE=
```

| Variable           | Description                 |
| ------------------ | --------------------------- |
| LOGIN_API_URL      | Employee authentication API |
| ATTENDANCE_API_URL | Attendance submission API   |
| ENCKEY             | API authentication key      |
| CHECKTYPE          | Attendance type (IN / OUT)  |
| LATITUDE           | Device latitude             |
| LONGITUDE          | Device longitude            |

---

## Installation

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

## Running the Application

```bash
python app.py
```

The application will be available at:

```text
http://localhost:5000
```

---

## Workflow

1. Employee enters a valid passcode.
2. Passcode is verified through the authentication service.
3. Employee information is retrieved.
4. Camera interface is launched.
5. Face pose is analyzed in real time.
6. Images are captured from multiple orientations.
7. Captured images are stored locally.
8. Attendance is automatically submitted through the attendance API.
9. Success confirmation is displayed to the user.

---

## Core Functionalities

### Passcode-Based Authentication

Validates employee credentials through an external authentication service before attendance processing begins.

### Face Pose Estimation

Uses MediaPipe Face Landmarker and OpenCV-based head pose estimation to determine user orientation and ensure accurate multi-angle image collection.

### Automated Attendance Registration

After successful face capture, the application automatically submits attendance records to the configured backend system.

---

## Future Enhancements

* Face Recognition Verification
* Face Liveness Detection
* Employee Attendance Dashboard
* Attendance Analytics & Reporting
* Multi-Camera Support
* Docker Deployment
* Kubernetes Deployment
* Cloud Storage Integration
* Audit Logs & Monitoring

---

## Use Cases

* Corporate Offices
* Manufacturing Facilities
* Educational Institutions
* Residential Communities
* Smart Building Access Management

---

## Author

**DHARMARAJ B**

AI/ML Engineer | Computer Vision Developer

### Expertise

* Computer Vision
* Face Recognition Systems
* Object Detection
* Real-Time Video Analytics
* Edge AI Deployment
* Deep Learning Applications

---

## License

This project is intended for educational, research, and enterprise automation purposes.
