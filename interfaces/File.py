# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.
from abc import ABC, abstractmethod

class File(ABC):
    __path = None

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def get_extension(self):
        pass

    @abstractmethod
    def is_instance(self):
        pass
