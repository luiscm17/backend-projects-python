from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from pathlib import Path
import json
from models.expense import Expense
from models.exceptions import RepositoryError
from utils.config import get_expenses_file_path


class StorageInterface(ABC):
    """
    Storage interface for expenses.
    Abstract base class for storage implementations.
    """

    @abstractmethod
    def save_expense(self, expense: Expense) -> Expense:
        """
        Save an expense to the storage.
        """
        pass

    @abstractmethod
    def get_expense(self, id: int) -> Optional[Expense]:
        """
        Get an expense by id.
        """
        pass

    @abstractmethod
    def get_all_expenses(self) -> List[Expense]:
        """
        Get all expenses.
        """
        pass

    @abstractmethod
    def update_expense(self, expense: Expense) -> Expense:
        """
        Update an expense.
        """
        pass

    @abstractmethod
    def delete_expense(self, id: int) -> bool:
        """
        Delete an expense by id.
        """
        pass


class JsonStorage(StorageInterface):
    """Implementación de almacenamiento usando archivos JSON."""

    def __init__(self, file_path: Optional[Path] = None):
        """
        Inicializa el almacenamiento JSON.

        Args:
            file_path: Ruta al archivo JSON (opcional)
        """
        self._file_path = get_expenses_file_path() or file_path

    def _load_data(self) -> List[Dict[str, Any]]:
        """
        Carga los datos desde el archivo JSON.

        Returns:
            List[Dict]: Lista de diccionarios con los datos

        Raises:
            RepositoryError: Si hay error al leer el archivo
        """
        try:
            if not self._file_path.exists():
                return []

            with open(self._file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            return data if isinstance(data, list) else []

        except json.JSONDecodeError as e:
            raise RepositoryError(f"Invalid JSON format: {e}")
        except Exception as e:
            raise RepositoryError(f"Error reading file: {e}")

    def _save_data(self, data: List[Dict[str, Any]]) -> None:
        """
        Guarda los datos al archivo JSON.

        Args:
            data: Datos a guardar

        Raises:
            RepositoryError: Si hay error al escribir el archivo
        """
        try:
            with open(self._file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)

        except Exception as e:
            raise RepositoryError(f"Error writing file: {e}")

    def _expense_to_dict(self, expense: Expense) -> Dict[str, Any]:
        """Convierte un Expense a diccionario."""
        return {
            "id": expense.id,
            "description": expense.description,
            "amount": expense.amount,
            "date": expense.date.isoformat(),
            "category": expense.category,
        }

    def _dict_to_expense(self, data: Dict[str, Any]) -> Expense:
        """Convierte un diccionario a Expense."""
        from datetime import datetime

        return Expense(
            id=data["id"],
            description=data["description"],
            amount=data["amount"],
            date=datetime.fromisoformat(data["date"]),
            category=data.get("category"),
        )

    def save_expense(self, expense: Expense) -> Expense:
        """Guarda un gasto."""
        data = self._load_data()

        # Verificar si ya existe un gasto con ese ID
        data = [d for d in data if d["id"] != expense.id]
        data.append(self._expense_to_dict(expense))

        self._save_data(data)
        return expense

    def get_expense(self, id: int) -> Optional[Expense]:
        """Obtiene un gasto por ID."""
        data = self._load_data()

        for item in data:
            if item["id"] == id:
                return self._dict_to_expense(item)

        return None

    def get_all_expenses(self) -> List[Expense]:
        """Obtiene todos los gastos."""
        data = self._load_data()
        return [self._dict_to_expense(item) for item in data]

    def delete_expense(self, id: int) -> bool:
        """Elimina un gasto."""
        data = self._load_data()
        original_length = len(data)

        data = [item for item in data if item["id"] != id]

        if len(data) == original_length:
            return False

        self._save_data(data)
        return True

    def update_expense(self, expense: Expense) -> Expense:
        """Actualiza un gasto."""
        data = self._load_data()

        for i, item in enumerate(data):
            if item["id"] == expense.id:
                data[i] = self._expense_to_dict(expense)
                self._save_data(data)
                return expense

        # Si no existe, lo agrega
        return self.save_expense(expense)
