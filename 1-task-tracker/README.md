# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage tasks efficiently. Built with Python using a clean architecture pattern.

## Features

- ✅ Add new tasks with descriptions
- 📝 List all tasks or filter by status
- 🔄 Mark tasks as in-progress or done
- 🗑️ Delete completed tasks
- 💾 Persistent JSON storage

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. Ensure Python 3.8+ is installed:

```bash
python --version
```

## Usage

### Add a new task

```bash
python main.py add "Buy groceries"
```

Output: `Task added successfully (ID: 1)`

### List all tasks

```bash
python main.py list
```

### List tasks by status

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

### Update task description

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Mark task status

```bash
python main.py mark-in-progress 1
python main.py mark-done 1
```

### Delete task

```bash
python main.py delete 1
```

## Architecture

The project follows a clean architecture pattern:

```text
src/
├── models/          # Data models (Task)
├── repositories/    # Data persistence (TaskRepository)
├── services/        # Business logic (TaskService)
├── utils/          # Utilities (FileHandler)
└── data/           # JSON storage (auto-created)
```

### Components

- **Task Model**: Defines task structure with id, description, status, and timestamps
- **FileHandler**: Manages JSON file operations with automatic directory creation
- **TaskRepository**: Handles data persistence and ID generation
- **TaskService**: Implements business logic and validation
- **CLI Interface**: Command-line argument parsing and user interaction

## Data Storage

Tasks are stored in `src/data/tasks.json` with the following structure:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "created_at": "2024-02-18T00:30:00.000000",
    "updated_at": "2024-02-18T00:30:00.000000"
  }
]
```

## Task Statuses

- `todo`: Task not started
- `in-progress`: Task currently being worked on
- `done`: Task completed

## Error Handling

The application handles:

- Empty task descriptions
- Invalid task IDs
- File system errors
- JSON parsing errors

## Development

### Running the application

```bash
cd 1-task-tracker
python main.py --help
```

### Project structure

- Follows clean architecture principles
- Separation of concerns
- Type hints for better code quality
- Comprehensive error handling

## Contributing

1. Follow the commit convention in `../docs/commits.md`
2. Ensure all features are tested
3. Update documentation as needed

## License

This project is open source and available under the MIT License.
