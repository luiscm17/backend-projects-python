import sys
from src.services.task_service import TaskService
from src.repositories.task_respository import TaskRepository
from src.utils.file_handler import FileHandler


def main():

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
            file_handler = FileHandler()
            repository = TaskRepository(file_handler)
            service = TaskService(repository)

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

    else:
        print("Invalid command, use 'add' to add a task")


if __name__ == "__main__":
    main()
