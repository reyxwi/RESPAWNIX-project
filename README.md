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
RESPAWNIX/
│
├── run.py
├── _modules.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── auth/
│   ├── login.py
│   ├── signin.py
│   └── switch.py
│
├── adminpanel/
│   ├── apanel.py
│   ├── chart.py
│   ├── dashboarda.py
│   ├── status.py
│   └── tree.py
│
├── userpanel/
│   ├── upanel.py
│   ├── dashboard.py
│   ├── logincon.py
│   ├── time.py
│   │
│   └── panel_options/
│       ├── addp.py
│       ├── dashboard.py
│       ├── delete.py
│       ├── deletepack.py
│       ├── deletere.py
│       ├── reveiw.py
│       ├── search.py
│       └── treeveiw.py
│
├── back_panel/
│   ├── card1.py
│   ├── confrim.py
│   ├── empty2.py
│   ├── logincon.py
│   ├── numbers.py
│   └── out.py
│
├── back_panela/
│   └── seaacha.py
│
├── loading_page/
│   ├── main.py
│   └── back.py
│
├── options/
│   ├── back.py
│   ├── jpack.py
│   ├── pack.py
│   ├── userlog.py
│   └── users.py
│
├── validation/
│   ├── validation.py
│   ├── empty.py
│   └── emptylog.py
│
├── data/
│   ├── packages.json
│   └── role.json
│
└── assests/
    ├── fonts/
    │
    │   ├── GROSTE.ttf
    │   ├── Nova Bomb Semi-bold.ttf
    │   ├── PixelO10Bott-Regular.ttf
    │
    │   
    │
    ├── images/
    │   ├── banner.png
    │   ├── banner2.png
    │   ├── box.png
    │   ├── box (2).png
    │   ├── clock.png
    │   ├── eye.png
    │   ├── loading.gif
    │   ├── log.png
    │   ├── que.png
    │   ├── tick.png
    │   ├── track.png
    │   ├── tracking.png
    │   └── user.png
    │
    └── sound/
        ├── error.mp3
        └── succes.mp3
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
