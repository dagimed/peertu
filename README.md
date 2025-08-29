# PeerTu 📚 – Peer Tutoring Platform

PeerTu is a Django REST API for connecting university students for **peer-to-peer tutoring**.

---

## 🚀 Features
- JWT Authentication (Login / Register)
- Tutor Profiles (bio, availability, subjects)
- Subjects CRUD
- Session Booking (Learner ↔ Tutor)
- Messaging System (per session)
- Reviews & Ratings
- Permissions & Role-based Access

---

## 🛠 Tech Stack
- Django 4.x
- Django REST Framework (DRF)
- SimpleJWT for authentication
- SQLite 

---
# 📚 PeerTu API Routes

Welcome to the **PeerTu API**.  
Base URL (local): `http://localhost:8000/`

---

## 🏠 Home
- **Endpoint:** `GET /`
- **Description:** Returns a welcome JSON message.

Sample Response:
```json
{
  "message": "Welcome to PeerTu API! Visit /api/ for endpoints."
}
```

---

## 👤 Users & Auth

### Register
- **Endpoint:** `POST /api/auth/register/`
- **Description:** Register a new user.
- **Sample Request Body:**
```json
{
  "username": "student1",
  "email": "student1@example.com",
  "password": "1234@pass"
}
```

### Login (JWT)
- **Endpoint:** `POST /api/auth/login/`
- **Description:** Login and get JWT token.
- **Sample Request Body:**
```json
{
  "username": "student1",
  "password": "1234@pass"
}
```

### Refresh Token
- **Endpoint:** `POST /api/auth/refresh/`
- **Description:** Refresh access token with a refresh token.

---

## 📘 Subjects

### List Subjects
- **Endpoint:** `GET /api/subjects/`
- **Description:** Retrieve all subjects.  
- **Auth:** Required

### Create Subject
- **Endpoint:** `POST /api/subjects/`
- **Sample Request Body:**
```json
{
  "name": "Mathematics"
}
```

### Update Subject
- **Endpoint:** `PUT /api/subjects/{id}/`
- **Sample Request Body:**
```json
{
  "name": "Advanced Mathematics"
}
```

### Delete Subject
- **Endpoint:** `DELETE /api/subjects/{id}/`

---

## 👩‍🏫 Tutors

### List Tutors
- **Endpoint:** `GET /api/tutors/`

### Create Tutor Profile
- **Endpoint:** `POST /api/tutors/`
- **Sample Request Body:**
```json
{
  "bio": "I am a math tutor",
  "subject_ids": [1, 2],
  "availability_text": "Mon-Fri 9AM-5PM"
}
```

### Update Tutor Profile
- **Endpoint:** `PUT /api/tutors/{id}/`
- **Sample Request Body:**
```json
{
  "bio": "Updated bio",
  "subject_ids": [1, 3]
}
```

### Delete Tutor Profile
- **Endpoint:** `DELETE /api/tutors/{id}/`

---

## 📅 Sessions (Lessons)

### List Sessions
- **Endpoint:** `GET /api/lessons/`

### Book a Session
- **Endpoint:** `POST /api/lessons/`
- **Sample Request Body:**
```json
{
  "tutor": 2,
  "learner": 1,
  "subject": 1,
  "start_time": "2025-09-01T10:00:00Z",
  "duration_minutes": 60
}
```

---

## 💬 Chat

### List Messages
- **Endpoint:** `GET /api/chat/?session={id}`

### Send Message
- **Endpoint:** `POST /api/chat/`
- **Sample Request Body:**
```json
{
  "session": 1,
  "sender": 1,
  "message": "Hello, I have a question."
}
```

---

## ⭐ Reviews

### List Reviews
- **Endpoint:** `GET /api/reviews/`

### Create Review
- **Endpoint:** `POST /api/reviews/`
- **Sample Request Body:**
```json
{
  "session": 1,
  "reviewer": 1,
  "rating": 5,
  "comment": "Great tutoring session!"
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/dagimed/peertu.git
cd peertu
python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
.venv\Scripts\activate      # on Windows
python manage.py migrate
python manage.py runserver
```