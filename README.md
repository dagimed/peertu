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
---
# API Routes

## Users
| Method | Endpoint               | Description           |
|--------|----------------------|----------------------|
| POST   | /api/users/register/  | Register a new user  |
| POST   | /api/token/           | Obtain JWT token     |
| POST   | /api/token/refresh/   | Refresh JWT token    |

## Subjects
| Method | Endpoint                | Description         |
|--------|------------------------|-------------------|
| GET    | /api/subjects/         | List all subjects  |
| POST   | /api/subjects/         | Create a subject   |
| GET    | /api/subjects/<id>/    | Get a subject      |
| PUT    | /api/subjects/<id>/    | Update a subject   |
| DELETE | /api/subjects/<id>/    | Delete a subject   |

## Tutors
| Method | Endpoint                | Description              |
|--------|------------------------|--------------------------|
| GET    | /api/tutors/           | List all tutor profiles  |
| POST   | /api/tutors/           | Create tutor profile     |
| GET    | /api/tutors/<id>/      | Get tutor profile        |
| PUT    | /api/tutors/<id>/      | Update tutor profile     |
| DELETE | /api/tutors/<id>/      | Delete tutor profile     |

## Lessons (Tutoring Sessions)
| Method | Endpoint                | Description                   |
|--------|------------------------|-------------------------------|
| GET    | /api/lessons/          | List all sessions             |
| POST   | /api/lessons/          | Schedule a tutoring session   |
| GET    | /api/lessons/<id>/     | Get session details           |
| PUT    | /api/lessons/<id>/     | Update session                |
| DELETE | /api/lessons/<id>/     | Cancel session                |

## Chat
| Method | Endpoint                | Description               |
|--------|------------------------|---------------------------|
| GET    | /api/chats/            | List all messages         |
| POST   | /api/chats/            | Send a message            |
| GET    | /api/chats/<id>/       | Get a specific message    |
| DELETE | /api/chats/<id>/       | Delete a message          |

## Reviews
| Method | Endpoint                | Description             |
|--------|------------------------|-------------------------|
| GET    | /api/reviews/          | List all reviews        |
| POST   | /api/reviews/          | Create a review         |
| GET    | /api/reviews/<id>/     | Get a review            |
| PUT    | /api/reviews/<id>/     | Update a review         |
| DELETE | /api/reviews/<id>/     | Delete a review         |
---