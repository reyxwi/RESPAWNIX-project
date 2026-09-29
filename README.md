# RESPAWNIX 📦

**RESPAWNIX** is a desktop Package Tracker Dashboard built with Python and CustomTkinter.

The application provides a simple interface for managing and tracking packages with separate panels for users and administrators.

## ✨ Features

* 🔐 Login and Sign Up system
* 👤 User and Admin roles
* 📦 Package management
* 🚚 Package status tracking
* 📊 Dashboard with package statistics
* 📈 Package status chart
* 🔄 Navigation between different panels
* 🧩 Modular project structure
* 🎨 CustomTkinter-based user interface

## 📌 Package Statuses

Packages can be categorized into different statuses:

* **On the way**
* **Delivered**
* **Sent**
* **Unknown**

The dashboard displays the current package statistics and visualizes them using a chart.

## 🛠️ Technologies

* Python
* CustomTkinter
* Tkinter
* Matplotlib
* Pillow

## 📁 Project Structure

RESPAWNIX/
│
├── adminpanel/
│   └── ...
│
├── auth/
│   ├── login.py
│   ├── signin.py
│   └── switch.py
│
├── options/
│   ├── back.py
│   └── users.py
│
├── assets/
│   └── images/
│
├── _modules.py
├── run.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 How to Run

First, make sure Python is installed.

Install the required libraries:

```bash
pip install customtkinter matplotlib requests pillow flask
```

Then run the project from the main launcher:

```bash
python run.py
```

> **Important:** Run the project from `run.py` because the project uses a centralized module/import structure.

## 🎨 Interface

RESPAWNIX uses a custom red-themed interface with separate sections for authentication, dashboard, package management, and reports.

## 📊 Dashboard

The dashboard provides an overview of package activity and displays package statistics using a graphical chart.

The chart is generated dynamically from the package data instead of using fixed values.

## 👥 Roles

### User

Users can access the user panel and view/manage their package-related information.

### Admin

Administrators have access to the admin panel and additional package management and reporting features.

## 📚 Project Purpose

This project was created as a modular Python desktop application for learning and practicing:

* GUI development
* Python functions
* Modular programming
* File and data management
* Authentication
* Data visualization

## 👩‍💻 Developer

**Reyhane Samadi**

Computer Student
