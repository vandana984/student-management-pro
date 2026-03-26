---
name: database-setup
description: Instructions for setting up and managing the Neon PostgreSQL database for Student Management Pro
---

# Database Section - Neon PostgreSQL

## Overview
This skill covers everything related to the PostgreSQL database hosted on **Neon** for the Student Management Pro project.

## Service Details
- **Provider:** Neon (Serverless PostgreSQL)
- **Token Name:** student-management-pro
- **Location:** `db/` folder in project root

## Folder Structure
```
db/
├── schema/              # SQL schema files
│   ├── 01_create_tables.sql
│   ├── 02_indexes.sql
│   └── 03_constraints.sql
├── migrations/          # Database migrations
├── seeds/               # Sample/seed data
│   └── seed_data.sql
├── scripts/             # Utility scripts
│   └── test_connection.py
└── README.md            # DB documentation
```

## Connection Details
- Use the Neon API token from the `tokens` file in project root
- Connection string format: `postgresql://user:password@host/dbname?sslmode=require`
- Always use SSL mode for Neon connections

## Key Tables (Planned)
1. **students** - Student records (id, name, email, phone, enrollment_date, etc.)
2. **courses** - Course catalog (id, name, code, description, credits)
3. **enrollments** - Student-course mapping (student_id, course_id, semester)
4. **grades** - Grade records (enrollment_id, grade, exam_type)
5. **attendance** - Attendance tracking (student_id, course_id, date, status)
6. **users** - System users for auth (id, username, password_hash, role)

## Commands Reference
```bash
# Test Neon connection
python db/scripts/test_connection.py

# Run schema creation
psql $DATABASE_URL -f db/schema/01_create_tables.sql

# Seed sample data
psql $DATABASE_URL -f db/seeds/seed_data.sql
```

## Important Notes
- Never commit connection strings or tokens to Git
- Always use parameterized queries to prevent SQL injection
- Neon supports auto-scaling and branching for dev/staging environments
- Use connection pooling for production workloads
