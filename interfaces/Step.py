# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.from abc import ABC, abstractmethod

class Step(ABC):
    __steps = None
    __preconditions = None

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def enchain_step(self, step):
        pass