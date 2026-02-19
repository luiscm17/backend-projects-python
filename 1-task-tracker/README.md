# Task Tracker CLI

A powerful command-line interface (CLI) application to track and manage tasks efficiently. Built with Python using clean architecture, dependency injection, and SQLite database storage.

## Features

- Add new tasks with descriptions
- List all tasks or filter by status (todo, in-progress, done)
- Mark tasks as todo, in-progress, or done
- Update task descriptions
- Delete tasks
- Persistent SQLite database storage
- Clean architecture with dependency injection
- Comprehensive test coverage
- Type hints and error handling

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

1. Install dependencies (if using uv):

```bash
uv run python main.py --help
```

## Usage

### Add a new task

```bash
python main.py add "Buy groceries"
```

Output: `Task ID:1 added successfully`

### List all tasks

```bash
python main.py list
```

### List tasks by status

```bash
python main.py list all
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
python main.py todo 1
python main.py in-progress 1
python main.py done 1
```

### Delete task

```bash
python main.py delete 1
```

### Show help

```bash
python main.py
```

## Architecture

The project follows clean architecture principles with dependency injection:

```text
src/
├── models/          # Data models (Task)
├── repositories/    # Data persistence (TaskRepositoryDB)
├── services/        # Business logic (TaskService)
├── utils/          # Database utilities (DBHandler)
├── cli/            # Command-line interface
├── container/       # Dependency injection container
└── data/           # SQLite database (auto-created)
```

### Components

- **Task Model**: Defines task structure with id, description, status, and timestamps
- **DBHandler**: Manages SQLite database operations with connection management
- **TaskRepositoryDB**: Handles data persistence and ID generation
- **TaskService**: Implements business logic and validation
- **DI Container**: Centralized dependency management with lazy loading
- **CLI Interface**: Command pattern with dependency injection
- **Command Classes**: Individual command implementations (Add, Update, Delete, List, etc.)

## Database Schema

Tasks are stored in SQLite database with the following schema:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'todo',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    CHECK (status IN ('todo', 'in-progress', 'done'))
);
```

## Task Statuses

- `todo`: Task not started
- `in-progress`: Task currently being worked on
- `done`: Task completed

## Error Handling

The application handles:

- Empty task descriptions
- Invalid task IDs
- Database connection errors
- Invalid status transitions
- Command-line argument validation

## Development

### Running application

```bash
cd 1-task-tracker
python main.py --help
```

### Running tests

```bash
cd 1-task-tracker
python -m pytest tests/ -v
```

### Project structure

- Follows clean architecture principles
- Dependency injection container for testability
- Separation of concerns
- Type hints for better code quality
- Comprehensive error handling
- Command pattern implementation

## Performance

- SQLite database for efficient data storage
- Lazy loading of dependencies
- Proper connection management
- Database-level constraints for data integrity

## Contributing

1. Follow commit convention in `../docs/commits.md`
2. Ensure all features are tested
3. Update documentation as needed
4. Run tests before submitting

## License

This project is open source and available under MIT License.
