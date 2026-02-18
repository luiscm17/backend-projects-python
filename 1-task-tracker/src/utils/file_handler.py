import json
import os
from typing import List, Dict, Any


class FileHandler:
    def __init__(self, filename: str = "tasks.json"):

        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        self.filename = os.path.join(data_dir, filename)

    def read_task(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def write_task(self, tasks: List[Dict[str, Any]]) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
