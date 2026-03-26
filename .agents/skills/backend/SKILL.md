---
name: backend-setup
description: Instructions for setting up and managing the FastAPI backend for Student Management Pro, deployed on Render
---

# Backend Section - FastAPI on Render

## Overview
This skill covers everything related to the **FastAPI** backend, deployed on **Render**, for the Student Management Pro project.

## Service Details
- **Framework:** FastAPI (Python)
- **Hosting:** Render
- **Token Name:** student-management-pro (Render API token)
- **Location:** `backend/` folder in project root

## Folder Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── config.py             # Configuration & env vars
│   ├── database.py           # Database connection setup
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── course.py
│   │   ├── enrollment.py
│   │   ├── grade.py
│   │   └── attendance.py
│   ├── schemas/              # Pydantic schemas (request/response)
│   │   ├── __init__.py
│   │   ├── student.py
│   │   ├── course.py
│   │   └── auth.py
│   ├── routers/              # API route handlers
│   │   ├── __init__.py
│   │   ├── students.py
│   │   ├── courses.py
│   │   ├── enrollments.py
│   │   ├── grades.py
│   │   └── auth.py
│   ├── services/             # Business logic layer
│   │   └── __init__.py
│   └── middleware/           # Auth & CORS middleware
│       └── __init__.py
├── requirements.txt          # Python dependencies
├── render.yaml               # Render deployment config
├── .env.example              # Environment variables template
└── README.md                 # Backend documentation
```

## Key Dependencies
```
fastapi
uvicorn[standard]
sqlalchemy
asyncpg
psycopg2-binary
python-jose[cryptography]
passlib[bcrypt]
python-dotenv
pydantic
alembic
```

## API Endpoints (Planned)
| Method | Endpoint                 | Description              |
|--------|--------------------------|--------------------------|
| POST   | `/api/auth/login`        | User login               |
| POST   | `/api/auth/register`     | User registration        |
| GET    | `/api/students`          | List all students        |
| POST   | `/api/students`          | Create a student         |
| GET    | `/api/students/{id}`     | Get student details      |
| PUT    | `/api/students/{id}`     | Update student           |
| DELETE | `/api/students/{id}`     | Delete student           |
| GET    | `/api/courses`           | List all courses         |
| POST   | `/api/courses`           | Create a course          |
| GET    | `/api/enrollments`       | List enrollments         |
| POST   | `/api/enrollments`       | Enroll student in course |
| GET    | `/api/grades`            | List grades              |
| POST   | `/api/grades`            | Add grade                |

## Commands Reference
```bash
# Install dependencies
cd backend && pip install -r requirements.txt

# Run development server
cd backend && uvicorn app.main:app --reload --port 8000

# Access API docs
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

## Render Deployment
- Use `render.yaml` for infrastructure-as-code deployment
- Set environment variables in Render dashboard
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## Important Notes
- Use async endpoints for database operations
- CORS must be configured to allow frontend domain
- Use environment variables for all secrets (never hardcode)
- Render free tier spins down after inactivity - consider paid tier for production
