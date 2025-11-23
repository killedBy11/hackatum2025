# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.from abc import ABC, abstractmethod
from abc import ABC, abstractmethod

class Step(ABC):
    __steps = None
    __preconditions = None

    @abstractmethod
    def execute(self):
        pass

    def enchain_step(self, step):
        if self.__steps is None:
            self.__steps = []
        self.__steps.append(step)

    def add_precondition(self, precondition):
        if self.__preconditions is None:
            self.__preconditions = []
        self.__preconditions.append(precondition)