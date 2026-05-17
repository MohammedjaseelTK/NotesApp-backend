# NotesApp Backend (Django + DRF)

##  Project Overview
This is a backend API for Notes Application built using Django and Django REST Framework.  
It supports user authentication and full CRUD operations for notes.

---

##  Features

- User Registration
- JWT Authentication (Login)
- Create Notes
- View Notes (User-specific)
- Update Notes
- Delete Notes
- Favorite Notes support
- Protected API routes
- CORS enabled for frontend

---

##  Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite / PostgreSQL

---

##  Authentication

JWT Token is used.

### Login Response:
```json
{
  "access": "token",
  "refresh": "token"
}

📡 API Endpoints
Register
POST /api/register/

Login
POST /api/login/

Notes CRUD
GET    /api/notes/
POST   /api/notes/
PUT    /api/notes/<id>/
DELETE /api/notes/<id>/

 Setup Instructions

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

 Environment Variables

SECRET_KEY
DEBUG
DATABASE_URL

 Author

Mohammed Jaseel