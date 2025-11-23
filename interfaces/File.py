# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.
from abc import ABC, abstractmethod
from pathlib import Path

class File(ABC):
    def __init__(self, path: str):
        self._path = Path(path)

    def read(self) -> str:
        """
        Read the entire file as text.
        Override in subclasses if binary or special logic is needed.
        """
        with self._path.open("r", encoding="utf-8") as f:
            return f.read()

    @abstractmethod
    def get_extension(self) -> str:
        """Return the canonical extension of this file type."""
        pass

    @abstractmethod
    def is_instance(self) -> bool:
        """Return True if this file matches its type."""
        pass

