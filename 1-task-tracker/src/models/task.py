from datetime import datetime
from typing import Dict, Any


class Task:
    def __init__(self, id: int, description: str, status: str = "all"):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def update_description(self, new_description: str):
        """Update task description and timestamp"""
        self.description = new_description
        self.updated_at = datetime.now().isoformat()
