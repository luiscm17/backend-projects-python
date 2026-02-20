import json
import os
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CACHE_DIR = SCRIPT_DIR / "cache"
CACHE_DURATION = timedelta(minutes=5)


def get_cache_key(username):
    """Get the cache key for a username

    Args:
        username (_type_): _description_

    Returns:
        _type_: _description_
    """
    return CACHE_DIR / f"{username}.activity.json"


def save_cache(username, data):
    """Save the cache data

    Args:
        username (_type_): _description_
        data (_type_): _description_
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_file = get_cache_key(username)

    cache_data = {"timestamp": datetime.now().isoformat(), "data": data}

    with open(str(cache_file), "w") as f:
        json.dump(cache_data, f)


def load_cache(username):
    """Load the cache data

    Args:
        username (_type_): _description_

    Returns:
        _type_: _description_
    """
    cache_file = get_cache_key(username)

    if not cache_file.exists():
        return None

    try:
        with open(str(cache_file), "r") as f:
            cache_data = json.load(f)

        timestamp = datetime.fromisoformat(cache_data["timestamp"])
        if datetime.now() - timestamp < CACHE_DURATION:
            return cache_data["data"]
        else:
            cache_file.unlink()
            return None
    except:
        return None
