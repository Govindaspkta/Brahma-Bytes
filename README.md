# Brahma-Bytes

# Task Manager API

A simple REST API for managing tasks built with FastAPI and PostgreSQL.

## Features

- User registration and login
- JWT based authentication
- CRUD operations for tasks
- Each user can only access their own tasks
- Protected routes

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- python-jose for JWT
- Pydantic
- Passlib bcrypt for password hashing

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/Govindaspkta/brahma_task.git
cd brahma_task
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file in root folder

SECRET_KEY=your_random_secret_key
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/task_manager

### 5. Create database in pgAdmin named task_manager

### 6. Run the server

```bash
uvicorn app.main:app --reload
```

API runs at http://127.0.0.1:8000


## API Endpoints

### Register
POST /auth/register
{
"username": "govinda",
"email": "govinda@gmail.com",
"password": "pass1234"
}

### Login

POST /auth/login
{
"username": "govinda",
"password": "pass1234"
}

### Create Task
POST /tasks/

Authorization: Bearer your_token
{
"title": "Finish assignment",
"description": "Complete and push to github"
}

### Get All Tasks
GET /tasks/
Authorization: Bearer your_token

### Get Single Task
GET /tasks/1
Authorization: Bearer your_token

### Update Task
PATCH /tasks/1
Authorization: Bearer your_token
{
"title": "Updated title"
}

### Delete Task
DELETE /tasks/1
Authorization: Bearer your_token

## Note

All task routes are protected. Without a token you will get 401 Unauthorized.
EOF