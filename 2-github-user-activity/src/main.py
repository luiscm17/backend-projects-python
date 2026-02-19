import sys
from github_api import gh_activity
from formatter import format_activity


def validate_args():
    if len(sys.argv) != 2:
        print("Usage: python serc/main.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    if not username.strip():
        print("Username cannot be empty")
        sys.exit(1)

    return username


def main():
    print("GitHub User Activity CLI")
    print("Usage: python src/main.py <username>")
    username = validate_args()
    print(f"Searching for user: {username}")
    activity = gh_activity(username)
    if isinstance(activity, str):
        print(activity)
    else:
        messages = format_activity(activity)
        print(f"User: {username}")
        for message in messages:
            print(message)


if __name__ == "__main__":
    main()
