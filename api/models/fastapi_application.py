from typing import List
from fastapi import FastAPI
from api.models.fastapi_router import FastApiRouter
from api.models.application import Application


class FastApiApplication(Application):

    def __init__(self, routers: List[FastApiRouter]):
        self.application = FastAPI()
        for router in routers:
            self.add_router(router)

    def add_router(self, router: FastApiRouter):
        self.application.include_router(router.router)

