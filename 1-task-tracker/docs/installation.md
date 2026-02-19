# Task Tracker CLI - Installation Guide

Complete installation and setup instructions for Task Tracker CLI application.

## 📋 Prerequisites

### Required Software

- **Python 3.8+**: Download from [python.org](https://python.org)
- **Git**: For version control (recommended)
- **uv** (recommended): Modern Python package manager
- **pip** (alternative): Standard Python package manager

## 🚀 Installation Methods

### Method 1: Using uv (Recommended)

uv is a modern Python package manager that's faster and more reliable than pip.

1. **Install uv** (if not already installed):

```bash
# Windows (PowerShell)
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. **Clone the repository**:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. **Install dependencies and run**:

```bash
uv run python main.py --help
```

### Method 2: Using pip

Traditional Python package manager.

1. **Clone the repository**:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. **Create virtual environment** (recommended):

```bash
# Create virtual environment
python -m venv task-tracker-env

# Activate on Windows
task-tracker-env\Scripts\activate

# Activate on macOS/Linux
source task-tracker-env/bin/activate
```

1. **Install dependencies**:

```bash
# Install dependencies (if requirements.txt existed)
pip install -r requirements.txt

# Or run directly (no external dependencies required)
python main.py --help
```

### Method 3: System-wide Installation

For system-wide access to the command.

1. **Clone the repository**:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. **Install in development mode**:

```bash
# Using uv
uv pip install -e .

# Using pip
pip install -e .
```

1. **Add to PATH** (optional):

```bash
# Add current directory to PATH (temporary)
export PATH="$(pwd):$PATH"

# Or create a global script (advanced)
# See Development Setup section
```

## ✅ Verification

### Test Installation

Verify that the installation was successful:

```bash
# Check application works
python main.py --help

# Should show:
# Usage: task-cli <command> [arguments]
# Available commands:
#  add <description>       - Add a new task
#  ...
```

### Test Database Creation

Verify that the database is created correctly:

```bash
# Add a test task
python main.py add "Installation test task"

# Check that it was saved
python main.py list

# Should show:
# ID: 1
# Description: Installation test task
# Status: todo
# ...
```

## 🔧 Development Setup

### For Users Who Want to Modify Code

1. **Clone repository**:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. **Set up development environment**:

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows

# Install in development mode
uv pip install -e .
```

1. **Verify installation**:

```bash
python main.py add "Development setup test"
python main.py list
```

1. **Run tests**:

```bash
python -m pytest tests/ -v
```

## 🗂️ File Structure After Installation

```yml
1-task-tracker/
├── main.py                 # Application entry point
├── src/                    # Source code
│   ├── models/             # Task model
│   ├── repositories/       # Data access layer
│   ├── services/           # Business logic
│   ├── utils/              # Database utilities
│   ├── cli/                # Command interface
│   ├── container/           # Dependency injection
│   └── __init__.py
├── tests/                   # Test suites
├── docs/                    # Documentation
├── data/                    # Database (auto-created)
│   └── tasks.db            # SQLite database
└── README.md                # Project information
```

## 🔍 Troubleshooting Installation

### Common Issues

#### Python Not Found

```bash
python: command not found
```

**Solutions**:

1. **Install Python** from python.org
2. **Add Python to PATH**:
   - Windows: Add Python installation directory to PATH
   - macOS: Use Homebrew or installer with PATH option
   - Linux: Use package manager (apt, yum, etc.)

#### Permission Denied

```bash
Error: Permission denied: 'src/data'
```

**Solutions**:

1. **Check directory permissions**:

   ```bash
   ls -la src/
   ```

2. **Fix permissions**:

   ```bash
   chmod 755 src/
   chmod 755 src/data/
   ```

3. **Run as administrator** (Windows):

   ```powershell
   Start-Process python main.py --help -Verb RunAs
   ```

#### Module Import Errors

```bash
ModuleNotFoundError: No module named 'src'
```

**Solutions**:

1. **Check Python path**:

   ```bash
   python -c "import sys; print(sys.path)"
   ```

2. **Run from correct directory**:

   ```bash
   cd 1-task-tracker
   python main.py --help
   ```

3. **Use module syntax**:

   ```bash
   python -m src.main --help
   ```

#### Database Creation Failed

```bash
Error: unable to open database file
```

**Solutions**:

1. **Check disk space**:

   ```bash
   df -h
   ```

2. **Verify directory permissions**:

   ```bash
   ls -la src/data/
   ```

3. **Create directory manually**:

   ```bash
   mkdir -p src/data
   chmod 755 src/data/
   ```

## 🚀 Next Steps

After successful installation:

1. **Read the [User Guide](user-guide.md)** for usage instructions
2. **Try the Quick Start examples**:

   ```bash
   python main.py add "My first task"
   python main.py list
   ```

---
