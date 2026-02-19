from datetime import datetime


def format_event(event):
    type = event.get("type", "unkonown")
    actor = event.get("actor", {}).get("login", "Unknown")
    repo = event.get("repo", {}).get("name", "unknown/repo")
    created_at = event.get("created_at", "")

    if created_at:
        date = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        date_str = date.strftime("%Y-%m-$d %H:%M")
    else:
        date_str = "Unknown date"

    messages = {
        "PushEvent": f"Pushed commits to {repo}",
        "IssuesEvent": f"Opened/Closed issue in {repo}",
        "WatchEvent": f"Starred {repo}",
        "CreateEvent": f"Created {repo}",
        "DeleteEvent": f"Deleted from {repo}",
        "ForkEvent": f"Forked {repo}",
        "PullRequestEvent": f"Pull Request in {repo}",
    }

    message = messages.get(type, f"{type} in {repo}")

    return {
        "type": type,
        "actor": actor,
        "repo": repo,
        "created_at": date_str,
        "message": message,
    }


def format_activity(events, limit=10):
    if not events:
        return ["No activity found"]

    formatted_messages = []
    for event in events[:limit]:
        formatted = format_event(event)
        formatted_messages.append(f"{formatted['message']} - {formatted['created_at']}")

    return formatted_messages
