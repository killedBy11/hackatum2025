# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Precondition(ABC):
    @abstractmethod
    def is_satisfied(self):
        pass

