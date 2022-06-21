from api.application_runners.uvicorn_application_runner import UvicornApplicationRunner
from api.models.fastapi_application import FastApiApplication
from api.models.fastapi_router import FastApiRouter
import api.routers.basic_router

class Bootstrapper(object):
    def __init__(self):
        self.routers = []

    def bootstrap(self):
        simple_router = FastApiRouter(api.routers.basic_router.router, {})
        self.routers.append(simple_router)
        api_application = FastApiApplication(self.routers).application
        return UvicornApplicationRunner(api_application)
