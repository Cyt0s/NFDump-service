from abc import ABC,abstractmethod
from typing import List

from api.models.fastapi_router import FastApiRouter
from api.models.base_router import BaseRouter

class BaseApplication(ABC):

    def __init__(self,routers: List[BaseRouter]):
        self.routers = routers

    @abstractmethod
    def add_router(self, router: BaseRouter):
        pass
