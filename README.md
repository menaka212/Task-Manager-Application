# 🚀 Task Manager App

A simple and responsive **Task Manager Application** built using **Django**, **Bootstrap 5**, and **Postgresql**. Users can register, log in, and efficiently manage their tasks through different stages such as **Todo**, **In Progress**, and **Done**.

---

# 🌐 Live Demo

🔗 **Live Application**

```text
https://task-manager-application-30q9.onrender.com
```

---

# ✨ Features

## 🔐 Authentication

* ✅ User Registration
* ✅ User Login
* ✅ User Logout
* ✅ Session-Based Authentication

---

## 📋 Task Management

* ✅ Create Tasks
* ✅ Delete Tasks
* ✅ Search Tasks
* ✅ Priority Levels

  * 🔴 High
  * 🟡 Medium
  * 🟢 Low
* ✅ Move Tasks Between Stages

  * 📌 Todo
  * 🚧 In Progress
  * 🎉 Done

---

## 📊 Dashboard

* ✅ Statistics Cards
* ✅ Kanban Board Layout
* ✅ Task List View
* ✅ Dark Mode Toggle
* ✅ Responsive Design

---

## 🎨 UI Features

* ✅ Bootstrap 5 Responsive Design
* ✅ SweetAlert Delete Confirmation
* ✅ Modern Dashboard Layout
* ✅ Mobile Friendly Interface

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Backend

* Django

## Database

* PostgreSQL

---

# ⚙️ Installation

## 📥 Clone Repository

```bash
git clone <repository-url>
cd task-manager
```

---

## 🐍 Create Virtual Environment

```bash
python -m venv venv
```

---

## ▶️ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Run Development Server

```bash
python manage.py runserver
```

Application will be available at:

```text
http://127.0.0.1:8000/
```

---

# 📁 Project Structure

```text
task-manager/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3 (Local Development)
```

---

# 📝 Assumptions

* 👤 Each user can access only their own tasks.
* 📋 Tasks are categorized into:

  * Todo
  * In Progress
  * Done
* 🔐 Session-based authentication is sufficient for this assignment.
* 🗄️ SQLite is used for local development and PostgreSQL is used for production deployment.

---

# ⚖️ Tradeoffs

* 🗄️ SQLite was used during development for simplicity, while PostgreSQL is used in production for better scalability and persistence.
* 🔐 Session Authentication is used instead of JWT Authentication.
* 🎯 Focus was given to core functionality and user experience.

---

# 🏗️ Technical Decisions

* ✅ Django Authentication for user management.
* ✅ SQLite for local development and PostgreSQL for production deployment.
* ✅ Bootstrap 5 for responsive design.
* ✅ SweetAlert for delete confirmations.
* ✅ Kanban Board layout for task tracking.
* ✅ Search functionality for better usability.

---

# 📸 Screenshots

## 🔐 Login Page

![Login](<Screenshot 2026-05-31 134749.png>)

---

## 📝 Register Page

> ![Register](<Screenshot 2026-05-31 134804.png>)

---

## 📊 Dashboard

### Welcome User
![Welcome](<Screenshot 2026-05-31 134658.png>)

---
### Create task
![create](<Screenshot 2026-05-31 134712.png>)

---
### Task Board
![Board](<Screenshot 2026-05-31 134727.png>)

---
## 📋 Task List
![List](<Screenshot 2026-05-31 134736.png>)


---

## 📱 Mobile Responsive View

![Mobile View](<Screenshot 2026-05-31 135750.png>)

---

# 🔮 Future Improvements

* ✏️ Edit Tasks
* 📅 Task Due Dates
* 🎯 Drag & Drop Kanban Board
* 🔔 Notifications & Reminders
* 🌐 REST API Support
* 🔑 JWT Authentication
* 📧 Email Notifications

---

# 👨‍💻 Author

**Menaka Manavalan**

📧 Email: menakamanavalan2@gmail.com

🔗 GitHub: https://github.com/menaka212

---

⭐ If you found this project useful, feel free to star the repository.
