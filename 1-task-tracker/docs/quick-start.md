# Task Tracker CLI - Quick Start Guide

Get started with Task Tracker CLI in under 5 minutes!

## ⚡ 5-Minute Quick Start

### Step 1: Get the Application

```bash
# Clone the repository
git clone <repository-url>
cd backend-learn/1-task-tracker
```

### Step 2: Verify Installation

```bash
# Test the application
python main.py --help
```

You should see:

```
Usage: task-cli <command> [arguments]
Available commands:
 add <description>       - Add a new task
 update <id> <description> - Update a task
 delete <id>             - Delete a task
 list [status]           - List all tasks
 list all                - List all tasks
 list todo               - List tasks with todo status
 list in-progress        - List tasks with in-progress status
 list done               - List tasks with done status
 todo <id>               - Mark a task as todo
 in-progress <id>        - Mark a task as in progress
 done <id>               - Mark a task as done
```

### Step 3: Add Your First Task

```bash
python main.py add "Learn Task Tracker CLI"
```

Output: `Task ID:1 added successfully`

### Step 4: View Your Tasks

```bash
python main.py list
```

### Step 5: Complete a Task

```bash
python main.py done 1
python main.py list done
```

🎉 **Congratulations! You're now using Task Tracker CLI!**

## 🎯 Essential Commands

### Task Management

```bash
# Add tasks
python main.py add "Buy groceries"
python main.py add "Call mom"
python main.py add "Finish project report"

# View all tasks
python main.py list

# Update a task
python main.py update 1 "Buy groceries and cook dinner"

# Delete a task
python main.py delete 2
```

### Status Management

```bash
# Start working on a task
python main.py in-progress 1

# Mark as complete
python main.py done 1

# Reset to todo
python main.py todo 1
```

### Filtering Tasks

```bash
# View todo tasks
python main.py list todo

# View tasks in progress
python main.py list in-progress

# View completed tasks
python main.py list done
```

## 📋 Real-World Example

### Daily Workflow

```bash
# Morning planning
python main.py add "Team standup meeting"
python main.py add "Review pull requests"
python main.py add "Fix authentication bug"
python main.py add "Write documentation"

# Start working
python main.py in-progress 1
# ... after meeting ...
python main.py done 1
python main.py in-progress 2

# Check progress
python main.py list
```

### Project Management

```bash
# Project tasks
python main.py add "Design database schema"
python main.py add "Implement user model"
python main.py add "Create API endpoints"
python main.py add "Write unit tests"

# Work through tasks
python main.py in-progress 1
python main.py done 1
python main.py in-progress 2
python main.py done 2

# Check project status
python main.py list
```

## 🔧 Common Tasks

### Task Organization

```bash
# Create categories in task names
python main.py add "WORK: Prepare presentation"
python main.py add "PERSONAL: Schedule dentist appointment"
python main.py add "LEARNING: Complete Python course"

# Filter by category (manually)
python main.py list | grep "WORK:"
```

### Task Prioritization

```bash
# Use priority in task names
python main.py add "HIGH: Fix critical bug"
python main.py add "MEDIUM: Update documentation"
python main.py add "LOW: Clean up code comments"

# View high priority tasks
python main.py list | grep "HIGH:"
```

### Time Tracking (Manual)

```bash
# Add time estimates
python main.py add "Write API docs (2 hours)"
python main.py add "Test user authentication (1 hour)"

# Mark start time in description
python main.py update 1 "Write API docs (2 hours) - Started at 9:00 AM"
```

## 🚀 Next Steps

### Explore More Features

1. **Read the [User Guide](user-guide.md)** for detailed instructions
2. **Check the [API Reference](api-reference.md)** for all commands
3. **Learn about the [Architecture](architecture.md)** for technical insights

### Productivity Tips

1. **Daily Review**: Check `python main.py list` every morning
2. **Status Updates**: Keep task status current
3. **Regular Cleanup**: Delete old completed tasks
4. **Consistent Naming**: Use clear, descriptive task names

### Integration Ideas

1. **Git Integration**: Track development tasks alongside code
2. **Team Collaboration**: Share task lists with team members
3. **Project Planning**: Use for project milestone tracking

## 🔍 Quick Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `add "description"` | Create new task | `python main.py add "Buy milk"` |
| `list` | Show all tasks | `python main.py list` |
| `list todo` | Show todo tasks | `python main.py list todo` |
| `update <id> "desc"` | Update task | `python main.py update 1 "Buy milk and bread"` |
| `delete <id>` | Remove task | `python main.py delete 1` |
| `todo <id>` | Mark as todo | `python main.py todo 1` |
| `in-progress <id>` | Mark as in-progress | `python main.py in-progress 1` |
| `done <id>` | Mark as complete | `python main.py done 1` |

## 💡 Pro Tips

### Task Naming

- **Be Specific**: "Fix login bug" vs "Fix bug"
- **Include Context**: "Update user profile API" vs "Update profile"
- **Add Details**: "Call mom about birthday plans" vs "Call mom"

### Workflow Management

- **One Task at a Time**: Keep only one task "in-progress"
- **Regular Updates**: Update status as you work
- **Daily Review**: Check tasks each morning

### Data Management

- **Backup**: Copy `src/data/tasks.db` regularly
- **Cleanup**: Delete old completed tasks
- **Export**: Use `python main.py list > tasks.txt` for export

## 🆘 Quick Help

### If Something Goes Wrong

1. **Check Command Syntax**:

   ```bash
   python main.py --help
   ```

2. **Verify Task ID**:

   ```bash
   python main.py list
   ```

3. **Check Database**:
   - Ensure `src/data/tasks.db` exists
   - Check file permissions

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Task with id X not found` | Wrong task ID | Check `python main.py list` for correct ID |
| `Description cannot be empty` | Empty task description | Provide meaningful description |
| `Invalid status` | Wrong status filter | Use: todo, in-progress, done, or all |

---

**Ready to dive deeper? Check out the [User Guide](user-guide.md) for comprehensive documentation!** 🚀
