# 🌐 Pulse 

Pulse demonstrates the integration of **Python (Flask)** with **MySQL** to build a functional and visually appealing social media–style web application.

This project is designed strictly for **educational purposes** and follows CBSE-level concepts.

---

## 📌 Project Overview

**Project Title:** Pulse  
**Language Used:** Python  
**Framework:** Flask  
**Database:** MySQL  
**Level:** Class XII

Pulse allows users to register, log in, create posts, and like posts. An admin module is also included to manage and moderate content.

---

## ✨ Features

### 👤 User Features
- User Registration
- Secure Login & Logout
- Create text-based posts
- View posts from all users
- Like posts

### 🛡️ Admin Features
- Admin Login (password protected)
- View all user posts
- Delete inappropriate or unwanted posts

### 🎨 User Interface
- Modern gradient-based UI
- Icons using Font Awesome
- Custom graphical logo
- Clean and student-friendly design

---

## 🛠️ Technologies Used

| Component | Technology |
|--------|------------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS |
| Database | MySQL |
| Connector | mysql-connector-python |

---

## 🗄️ Database Design

### 📋 Users Table
| Field Name | Description |
|---------|-------------|
| user_id | Primary Key |
| username | Stores username |
| password_hash | Stores password |
| email | Stores email ID |

### 📝 Posts Table
| Field Name | Description |
|---------|-------------|
| post_id | Primary Key |
| user_id | Foreign Key |
| content | Post text |
| likes | Number of likes |

---

## 🔐 Admin Credentials

- **Admin Password:** `godofthunder2407`

---

## 🚀 How to Run the Project

### Step 1: Install Required Packages
```bash
pip install flask mysql-connector-python
```

### Step 2: Create Database
Create a MySQL database named `Pulse` and required tables.

### Step 3: Update Database Credentials
Edit `app.py` and update:
- host
- user
- password

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Browser
```
http://127.0.0.1:5000
```

---

## 📸 Pages Included

- Login Page
- Register Page
- User Feed Page
- Admin Login Page
- Admin Panel

---

## 🎓 Viva Explanation (Sample)

> “Pulse is a Flask-based mini social media web application developed using Python and MySQL. It demonstrates user authentication, database connectivity, and admin moderation features.”

---

## 📚 Learning Outcomes

- Understanding Flask framework basics
- Python–MySQL integration
- CRUD operations
- Web application workflow
- UI/UX design principles

---

## ⚠️ Limitations

- No image or video upload
- Passwords are not encrypted
- Suitable only for small-scale use

---

## ⭐ Conclusion

Pulse successfully demonstrates the practical implementation of Python, Flask, and MySQL to build a mini web application. The project meets all the learning objectives of a Class XII Computer Science curriculum.

---

## 👨‍🎓 Developer Details

**Name:** R. L. Yuwin  
**Class:** XII-A  
**Project Type:** Computer Science Practical  

---

**End of README**
