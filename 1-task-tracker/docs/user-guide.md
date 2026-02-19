# Task Tracker CLI - User Guide

Complete guide for using the Task Tracker CLI application effectively.

## 🚀 Quick Start

### Installation

1. **Clone the repository**:

```bash
git clone <repository-url>
cd backend-learn/1-task-tracker
```

1. **Verify Python version** (requires 3.8+):

```bash
python --version
```

1. **Run the application**:

```bash
python main.py --help
```

### First Task

Let's create your first task:

```bash
python main.py add "Welcome to Task Tracker CLI"
```

Expected output:

```bash
Task ID:1 added successfully
```

## 📋 Commands Reference

### Task Management Commands

#### Add Task

Create a new task with description.

```bash
python main.py add "Task description"
```

**Example**:

```bash
python main.py add "Buy groceries for dinner party"
```

#### Update Task

Modify an existing task's description.

```bash
python main.py update <task-id> "New description"
```

**Example**:

```bash
python main.py update 1 "Buy groceries and drinks for dinner party"
```

#### Delete Task

Remove a task permanently.

```bash
python main.py delete <task-id>
```

**Example**:

```bash
python main.py delete 1
```

### Status Management Commands

#### Mark as Todo

Set task status to "todo" (not started).

```bash
python main.py todo <task-id>
```

#### Mark as In Progress

Set task status to "in-progress" (currently working on).

```bash
python main.py in-progress <task-id>
```

#### Mark as Done

Set task status to "done" (completed).

```bash
python main.py done <task-id>
```

### List Commands

#### List All Tasks

Display all tasks regardless of status.

```bash
python main.py list
```

#### List by Status

Display tasks filtered by specific status.

```bash
python main.py list <status>
```

**Available statuses**:

- `all` - Show all tasks (same as no status)
- `todo` - Show only todo tasks
- `in-progress` - Show only in-progress tasks
- `done` - Show only completed tasks

**Examples**:

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

## 📊 Task Output Format

When listing tasks, each task displays:

```bash
ID: 1
Description: Buy groceries for dinner party
Status: todo
Created at: 2026-02-18T20:45:30.123456
Updated at: 2026-02-18T20:45:30.123456
```

## 🔄 Typical Workflow

### 1. Project Planning

```bash
# Add multiple planning tasks
python main.py add "Research project requirements"
python main.py add "Design database schema"
python main.py add "Create project structure"

# View all planning tasks
python main.py list todo
```

### 2. Development Process

```bash
# Start working on a task
python main.py in-progress 1

# Mark as completed
python main.py done 1

# Start next task
python main.py in-progress 2
```

### 3. Project Review

```bash
# View all completed tasks
python main.py list done

# Update with review notes
python main.py update 1 "Research project requirements - COMPLETED: All requirements gathered"
```

## ⚡ Productivity Tips

### Daily Workflow

1. **Morning Planning**: Add all tasks for the day

   ```bash
   python main.py add "Morning team standup"
   python main.py add "Review yesterday's commits"
   python main.py add "Plan development tasks"
   ```

2. **Work Session**: Mark tasks as in-progress

   ```bash
   python main.py in-progress 1
   python main.py in-progress 2
   ```

3. **End of Day**: Review and update

   ```bash
   python main.py list
   python main.py done 1
   python main.py update 2 "Plan development tasks - COMPLETED: Architecture designed"
   ```

### Task Naming Best Practices

- **Be Specific**: "Fix login bug" vs "Fix authentication issue"
- **Include Context**: "Update user profile API endpoint" vs "Update profile"
- **Use Action Verbs**: "Implement", "Fix", "Refactor", "Update", "Review"
- **Add Estimates**: "Implement user authentication (2 hours)" vs "Implement user auth"

### Status Management Strategy

- **Todo**: Tasks ready to start
- **In Progress**: Currently being worked on (one at a time)
- **Done**: Completed and verified

## 🔧 Advanced Usage

### Batch Operations

```bash
# Add multiple tasks
python main.py add "Task 1"
python main.py add "Task 2"
python main.py add "Task 3"

# View all tasks
python main.py list

# Mark multiple as done
python main.py done 1
python main.py done 2
python main.py done 3
```

### Task Dependencies

While the app doesn't enforce dependencies, you can manage them manually:

```bash
# Create dependent tasks
python main.py add "Design database schema"
python main.py add "Implement database models"
python main.py add "Create migration scripts"

# Work in dependency order
python main.py in-progress 1  # Database schema first
python main.py done 1
python main.py in-progress 2  # Then models
python main.py done 2
python main.py in-progress 3  # Then migrations
```

## 🐛 Troubleshooting

### Common Issues

#### Task Not Found

```bash
python main.py update 999 "Updated task"
```

**Error**: `Error: Task with id 999 not found`

**Solution**: Check task ID with `python main.py list` first.

#### Empty Description

```bash
python main.py add ""
```

**Error**: `Error: Description cannot be empty`

**Solution**: Provide a meaningful description.

#### Invalid Status

```bash
python main.py list invalid
```

**Error**: `Error: Invalid status: Use 'all', 'todo', 'in-progress' or 'done'`

**Solution**: Use one of the valid statuses.

### Database Issues

#### Database Locked

If you see database access errors, ensure:

- Only one instance of the application is running
- The database file has proper permissions
- Sufficient disk space is available

#### Corrupted Database

If the database becomes corrupted:

1. Delete `src/data/tasks.db`
2. Restart the application (will create new database)
3. Add tasks again (fresh start)

## 📱 Integration Examples

### With Git Hooks

Add task tracking to your git workflow:

```bash
# Add task when starting work
git checkout -b feature/new-feature
python main.py add "Implement new feature"

# Mark task done when committing
python main.py done 1
git add .
git commit -m "feat: implement new feature"
```

### With IDE Integration

Most IDEs allow custom command integration:

**VS Code**:

1. Open Command Palette (Ctrl+Shift+P)
2. Search for "Configure Task Runner"
3. Add custom command for Task Tracker CLI

**PyCharm**:

1. Go to Settings → Tools → External Tools
2. Add Task Tracker CLI as external tool
3. Set up keyboard shortcuts

## 📈 Performance Tips

### Large Task Lists

For better performance with many tasks:

1. **Use Status Filtering**: View only relevant tasks

   ```bash
   python main.py list todo        # Only current tasks
   python main.py list in-progress  # Only active work
   ```

2. **Regular Cleanup**: Mark completed tasks regularly

   ```bash
   python main.py list done
   python main.py delete 1  # Remove old completed tasks
   ```

3. **Batch Operations**: Group similar operations

   ```bash
   # Mark multiple tasks as done
   python main.py done 1
   python main.py done 2
   python main.py done 3
   ```

## 🔒 Data Safety

### Backup Your Tasks

The SQLite database is stored in `src/data/tasks.db`. To backup:

```bash
# Copy database file
cp src/data/tasks.db backups/tasks-$(date +%Y%m%d).db

# Export all tasks
python main.py list > task-backup-$(date +%Y%m%d).txt
```

### Data Recovery

If you accidentally delete tasks:

1. Check your backup files
2. Use version control (git) to see recent changes
3. Recreate tasks from memory or documentation

---

Happy task management! 🚀
