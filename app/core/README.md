# Task Manager API

A simple REST API for managing tasks built with FastAPI.
This project was created as part of an assignment to practice FastAPI, SQLAlchemy and JWT authentication.

---

## Features

- User registration and login
- JWT based authentication
- Create, read, update, delete tasks
- Each user can only access their own tasks
- Protected routes — no token, no access

---

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (python-jose)
- Pydantic
- Passlib bcrypt for password hashing

---

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/yourusername/brahma_task.git
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

### 4. Create .env file in the root folder

SECRET_KEY=your_random_secret_key
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/task_manager

To generate a random secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
### 5. Create the database

Open pgAdmin and create a database called `task_manager`

### 6. Run the server
Create the database

Open pgAdmin and create a database called `task_manager`

## API Endpoints

### Register

POST /auth/register

{
"username": "creat_your_username",
"email": "your_email@gmail.com",
"password": "create_password"
}

### Login
POST/auth/login

{
"username": "govinda",
"password": "pass1234"
}

Copy the token from the response and add it to the Authorization header for all task routes.

### Create a task

POST /tasks/
Authorization: Bearer your_token
{
"title": "Finish assignment",
"description": "Complete and push to github"
}

### Get all tasks
GET /tasks/1
Authorization: Bearer your_token

### Update task
PATCH /tasks/1
Authorization: Bearer your_token
{
"title": "Updated title"
}

### Delete task

DELETE /tasks/1
Authorization: Bearer your_token

---

## Note

All task routes are protected. If you send a request without a token you will get a 401 Unauthorized error.