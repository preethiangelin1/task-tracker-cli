# Task Tracker CLI 📝

A lightweight and user-friendly command-line task manager built with Python.

Task Tracker CLI allows you to manage your daily tasks directly from the terminal — add, update, delete, list, and mark tasks as completed — all with persistent local storage.

---

## 🚀 Features

- ✅ Add new tasks
- ✏️ Update existing tasks
- 🗑 Delete tasks
- ✔️ Mark tasks as completed
- 📋 List all tasks in a formatted table
- 💾 Persistent storage using JSON
- 🧩 Clean layered architecture (CLI → Service → Storage → Models)
- 📦 Installable as a real CLI command (`task-cli`)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

2️⃣ Create a virtual environment (recommended)
```bash
python3 -m venv venv
```

Activate the environment:

Mac/Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```

3️⃣ Install in editable mode
```bash
pip install -e .
```
This will create the task-cli command in your environment.

🖥 Usage

After installation, use:

```bash
$ task-cli add "Read a book"
Task added successfully.

$ task-cli list
ID  Description     Status
1   Read a book     Pending

$ task-cli mark 1
Task marked as completed.

$ task-cli list
ID  Description     Status
1   Read a book     Completed
```

## ⚙️ Technologies Used

- **Python 3**
- **argparse** – CLI argument parsing
- **rich** – Formatted terminal output
- **JSON** – Local data persistence
- **setuptools** – Packaging and CLI entry point

---

## 📚 What I Learned

This project helped me understand:

- How to structure a Python project using modular architecture
- Separation of concerns (CLI layer, Service layer, Storage layer)
- How to build CLI applications using `argparse`
- How to format terminal output using `rich`
- How Python packaging works using `pyproject.toml`
- How `console_scripts` create real CLI commands
- How editable installs (`pip install -e .`) work
- The difference between:
  - `requirements.txt`
  - `pyproject.toml`