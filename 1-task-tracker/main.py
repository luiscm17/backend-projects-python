import sys
from src.services.task_service import TaskService
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler
from src.interfaces.cli import TaskCommands


def main():

    file_handler = FileHandler()
    repository = TaskRepository(file_handler)
    service = TaskService(repository)
    commands = TaskCommands()

    if len(sys.argv) < 2:
        print("Usage: task-cli <command> <args>")
        print("Example: task-cli add 'Buy groceries'")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Description is required")
            return
        description = " ".join(sys.argv[2:])

        try:

            task = service.add_task(description)
            print(f"Task added successfully (ID: {task.id})")

        except Exception as e:
            print(f"Error: {str(e)}")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Task ID and description are required")
            return
        try:
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            task = service.update_task(task_id, new_description)
            print(f"Task {task.id} updated successfully")

        except Exception as e:
            print(f"Error: {str(e)}")

    elif command == "list":

        if len(sys.argv) < 2:
            status = sys.argv[2].lower()
            try:
                tasks = service.list_tasks_by_status(status)
            except ValueError as e:
                print(f"Error: {str(e)}")
                return
        else:
            tasks = service.list_all_tasks()

        print(commands.format_task_list(tasks))

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Task ID is required")
            return
        try:
            task_id = int(sys.argv[2])
            service.delete_task(task_id)
            print(f"Task {task_id} deleted successfully")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    elif command == "in-progress":
        if len(sys.argv) < 3:
            print("Error: Task ID is required")

        try:
            task_id = int(sys.argv[2])
            task = service.mark_task_in_progress(task_id)
            print(f"Task {task_id} marked as in-progress")
        except ValueError as e:
            print(f"Error: {str(e)}")

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Task ID is required")
            return
        try:
            task_id = int(sys.argv[2])
            task = service.mark_task_done(task_id)
            print(f"Task {task_id} marked as done")
        except ValueError as e:
            print(f"Error: {str(e)}")

    else:
        print("Invalid command, use 'add' to add a task")


if __name__ == "__main__":
    main()
