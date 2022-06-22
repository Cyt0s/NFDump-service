from abc import ABC,abstractmethod
from typing import List
from api.models.router import Router


class Application(ABC):
    @abstractmethod
    def add_router(self, router: Router):
        pass
