import urllib.request
import urllib.error
import json


def gh_activity(username):
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
