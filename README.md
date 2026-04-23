# API-Security-layer
# 🔐 API Security Layer (FastAPI)

A beginner-friendly yet production-ready **API Security Layer** built using FastAPI.
This project demonstrates how to secure APIs using authentication, authorization, and validation techniques.

---

## 🚀 Features

* 🔑 JWT Authentication using JSON Web Token
* 🔐 Password Hashing with Passlib (bcrypt)
* 🛡 Role-Based Authorization (User/Admin)
* 📦 Input Validation using Pydantic
* 🔒 Protected Routes using dependency injection
* ⚙️ Clean and modular project structure
* 🧠 Beginner-friendly and scalable

---

## 📁 Project Structure

```bash
api_security_layer/
│
├── app/
│   ├── main.py
│   ├── core/
│   ├── auth/
│   ├── schemas/
│   ├── db/
│   ├── api/
│   └── utils/
│
├── .env
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/api-security-layer.git
cd api-security-layer
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

👉 Interactive Swagger UI for testing APIs

---

## 🔐 Authentication Flow

1. Register user → `/register`
2. Login → `/login`
3. Receive JWT token
4. Use token in headers:

```bash
Authorization: Bearer <your_token>
```

5. Access protected routes

---

## 🔌 API Endpoints

| Method | Endpoint  | Description         |
| ------ | --------- | ------------------- |
| POST   | /register | Register new user   |
| POST   | /login    | Login and get token |
| GET    | /profile  | Protected route     |
| GET    | /admin    | Admin-only route    |

---

## 🧠 Core Concepts Used

* Authentication (JWT)
* Authorization (Role-based)
* Password Security (Hashing)
* Dependency Injection (FastAPI)
* Data Validation (Pydantic)

---

## 🧪 Testing

Use:

* Postman
* Thunder Client (VS Code)
* Swagger UI

---

## ⚠️ Notes

* This project uses a **fake in-memory database**
* Replace with PostgreSQL for production
* Secret keys should be stored securely in `.env`

---

## 🚀 Future Improvements

* 🗄 Database Integration (PostgreSQL + SQLAlchemy)
* 🔁 Refresh Tokens
* 🐳 Docker Deployment
* 📊 Logging & Monitoring
* ⚡ Rate Limiting

---

## 👨‍💻 Author

**Satyam Kumar**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
