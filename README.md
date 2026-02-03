# 🧠 ThoughtBox

*A light-weight, local-first journaling desktop application built with Python & Qt.*

ThoughtBox is a minimalist journaling app designed to help you capture thoughts quickly, privately, and without distractions. All data is stored **locally**, giving you full ownership and peace of mind—no accounts, no cloud, no tracking.

---

## 📚 Table of Contents

1. [Tech Stack](#-tech-stack)
2. [Project Structure](#-project-structure)
3. [Installation](#-installation)
4. [Running the App](#-running-the-app)
5. [Configuration & Permissions](#-configuration--permissions)
6. [Database](#-database)
7. [Development](#-development)
8. [Roadmap](#-roadmap)
9. [License](#-license)

---

## ✨ Features

* 📝 Create, edit, and delete journal entries
* 💾 Local-first SQLite database (no internet required)
* 🎨 Modern Fluent UI with dark theme styling
* 🔒 Explicit user permission handling for transparency
* ⚡ Fast startup & lightweight footprint
* 🧩 Clean separation of UI, logic, and data layers

---

## 📸 Screenshots

> *(Add screenshots here once ready)*
> Example:
>
> ```md
> ![Dashboard](docs/screenshots/dashboard.png)
> ```

---

## 🛠 Tech Stack

* **Python** 3.12+
* **PySide6 (Qt)** – Desktop UI
* **QFluentWidgets** – Fluent design system
* **SQLAlchemy 2.x** – ORM & database access
* **SQLite** – Embedded local database
* **python-dotenv** – Environment configuration

---

## 🗂 Project Structure

```text
thought-box/
├── app/
│   ├── app.py              # Main window (MSFluentWindow)
│   ├── core/
│   │   └── logic.py        # Business logic layer
│   ├── database/
│   │   └── db.py           # SQLAlchemy engine & session
│   ├── models/
│   │   └── entry.py        # Entry ORM model
│   ├── pages/
│   │   └── dashboard.py   # Main dashboard UI
│   ├── utils/
│   │   └── color_theme.py # Centralized theme config
│   └── storage/
│       ├── main.db         # SQLite database (generated)
│       └── config.json    # User permissions
│
├── main.py                 # Application entry point
├── pyproject.toml          # Packaging & dependencies
├── LICENSE.txt
└── README.md
```

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mek0124/thought-box.git
cd thought-box
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r pyproject.toml
```

---

## ▶️ Running the App

```bash
python3 main.py
```

Or, if installed as a script:

```bash
momentum-gui
```

---

## 🔐 Configuration & Permissions

On first launch, ThoughtBox will ask for:

* 📁 **Read/Write permissions**
  Used *only* to store the local database and config file and allows app to perform CRUD operations on database **only**

* 🌐 **Browser usage permission**
  Used *only when you explicitly click* links like:

  * About the App
  * About the Developer
  * Support

All permissions are stored locally in:

```text
app/storage/config.json
```

No data is accessed outside the application directory.

---

## 🗄 Database

* **Engine:** SQLite
* **ORM:** SQLAlchemy
* **Location:**

  ```text
  app/storage/main.db
  ```

The database schema is created automatically on first run, after permission acceptance.

### Entry Model

Each journal entry includes:

* `id` – Auto-incremented primary key
* `title` – Unique title
* `content` – Full journal text
* `created_at` – Timestamp
* `updated_at` – Auto-updated timestamp

---

## 🧪 Development

Includes:

* 🧹 `black` – Code formatting
* 🧠 `ruff` – Linting
* 🔍 `mypy` – Type checking
* 🧪 `pytest`, `pytest-qt` – Testing

---

## 🛣 Roadmap

* [ ] Entry search & filtering 🔍
* [ ] Tags / categories 🏷
* [ ] Rich text or markdown support ✍️
* [ ] Export entries (PDF / Markdown) 📄
* [ ] Encrypted entries 🔐
* [ ] Plugin system 🧩

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software.
See [`LICENSE.txt`](LICENSE.txt) for full details.
