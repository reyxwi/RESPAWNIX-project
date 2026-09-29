# 📦 RESPAWNIX — Package Tracker Dashboard

RESPAWNIX is a desktop **Package Tracker Dashboard** built with Python and CustomTkinter.

The project provides separate panels for **Admin** and **User** roles, allowing packages to be created, tracked, searched, updated, and managed through a graphical interface.

---

## ✨ Features

### 🔐 Authentication

* User and Admin roles
* Login and Sign Up pages
* Role-based panel access
* Loading screen before entering the panel

### 👨‍💼 Admin Panel

* View all packages
* View package information in a Treeview
* Change package status
* Search packages
* Dashboard package statistics
* Status-based package management

### 👤 User Panel

* View personal packages
* Add packages
* Search packages
* Delete packages
* View package status
* Track package information

### 📊 Dashboard

The dashboard displays package statistics such as:

* All Packages
* On the Way
* Delivered
* Sent
* Unknown

---

## 🛠️ Technologies

* Python
* CustomTkinter
* Tkinter / ttk
* JSON
* Pillow
* Matplotlib
* CTkMessagebox

---

## 📁 Project Structure
RESPAWNIX/
│
├── run.py
├── _modules.py
│
├── auth/
│   ├── login.py
│   ├── signin.py
│   └── switch.py
│
├── admin/
│   ├── adminpanel.py
│   └── tree.py
│
├── userpanel/
│   ├── upanel.py
│   ├── logincon.py
│   ├── time.py
│   └── panel_options/
│       ├── dashboard.py
│       ├── addp.py
│       ├── repack.py
│       ├── packages.py
│       ├── deletepack.py
│       ├── deletere.py
│       └── search.py
│
├── back_panel/
│   ├── card1.py
│   └── logincon.py
│
├── options/
│   ├── pack.py
│   ├── jpack.py
│   ├── back.py
│   ├── users.py
│   └── userlog.py
│
├── data/
│   ├── packages.json
│   └── role.json
│
└── assests/
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Enter the project folder:

```bash
cd RESPAWNIX
```

Install the required libraries:

```bash
pip install customtkinter pillow CTkMessagebox matplotlib
```

Run the project from the main launcher:

```bash
python run.py
```

> **Important:** Run the project using `run.py` so that the project imports and file paths work correctly.

---

## 📦 Package Statuses

Packages can have different statuses:

```text
unknown
on the way
delivered
sent
```

Admins can update the status of packages from the Admin Panel.

---

## 🎨 UI

RESPAWNIX uses a custom desktop interface with a purple-themed authentication section and custom dashboard components.

The interface includes:

* CustomTkinter widgets
* Custom fonts
* Icons and images
* Package cards
* Treeviews
* Status controls
* Dashboard statistics

---

## 👩‍💻 Developer

**Reyhaneh Samadi**

Python / Computer Student

---

## 📌 Project Status

This project is a student final project and is actively being developed.
