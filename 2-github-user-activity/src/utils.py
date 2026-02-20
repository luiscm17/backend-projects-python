import re
import time


def validate_name(username):
    if not username:
        return False, "Username is required"

    if len(username) > 39:
        return False, "Username is too long"

    if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?$", username):
        return False, "Username can only contain letters, numbers and underscores"

    return True, "Username is valid"


def rate_limit(response_headers):
    reset_time = response_headers.get("X-RateLimit-Reset")
    if reset_time:
        timeout = int(reset_time) - int(time.time())
        if timeout > 0:
            print(f"Rate limit exceeded. Waiting for {timeout} seconds...")
            time.sleep(min(timeout, 60))
            return True
    return False
