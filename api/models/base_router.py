from abc import ABC,abstractmethod

from starlette.routing import Router


class BaseRouter(ABC):

    def __init__(self,router,router_configuraion: dict):
        self.router = router
        self.configuration = router_configuraion