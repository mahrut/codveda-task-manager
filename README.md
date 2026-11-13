
# Codveda Task Manager CLI

## Project Overview

The Codveda Task Manager CLI is a Python command-line application
that allows users to manage daily tasks.

The application supports task creation, viewing, updating,
deletion, completion tracking, priorities, and due dates.

Task information is stored persistently using JSON.

## Features

- Add new tasks
- View all tasks
- View individual task details
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Assign High, Medium, and Low priorities
- Set task due dates
- Persistent JSON storage
- Input validation and exception handling

## Technologies Used

- Python 3.12
- JSON
- Pytest
- Git and GitHub

## Project Structure

```text
codveda-task-manager/
|
|-- main.py
|-- task_manager.py
|-- storage.py
|-- tasks.json
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- tests/
    |-- test_task_manager.py
    |-- test_storage.py
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd codveda-task-manager
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

## Run Tests

```bash
python -m pytest tests -v
```

## Data Storage

Tasks are stored in tasks.json.

The JSON file maintains task information
between application sessions.

## Author

Codveda Python Development Internship Project.

## License

This project is developed for educational
and internship purposes.
