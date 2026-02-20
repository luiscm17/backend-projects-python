import urllib.request
import urllib.error
import json
from cache import load_cache, save_cache


def gh_activity(username):
    """Get the GitHub activity for a username

    Args:
        username (str): GitHub username

    Returns:
        list: List of GitHub events
    """
    url = f"https://api.github.com/users/{username}/events"

    headers = {"User-Agent": "Github-Activity-CLI"}

    try:
        request = urllib.request.Request(url=url, headers=headers)
        with urllib.request.urlopen(request) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                return data
            else:
                return f"Error: {response.status}"
    except urllib.error.HTTPError as e:
        return f"Error: {e.code} - {e.reason}"
    except urllib.error.URLError as e:
        return f"Error: {e.reason}"


def get_user_activity(username):
    """Get the GitHub activity for a username

    Args:
        username (str): GitHub username

    Returns:
        list: List of GitHub events
    """
    cache_data = load_cache(username)
    if cache_data:
        print("Using cached data...")
        return cache_data
    data = gh_activity(username)

    if not isinstance(data, str):
        save_cache(username, data)

    return data
