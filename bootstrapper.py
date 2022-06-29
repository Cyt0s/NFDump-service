from api.application_runners.uvicorn_application_runner import UvicornApplicationRunner
from api.models.fastapi_application import FastApiApplication
from api.models.fastapi_router import FastApiRouter
import api.routers.basic_router
import api.routers.netflow_router


class Bootstrapper(object):
    def __init__(self):
        self.routers = []

    def bootstrap(self):
        simple_router = FastApiRouter(router=api.routers.basic_router.router, router_configuration={})
        nfdump_router = FastApiRouter(router=api.routers.netflow_router.router, router_configuration={})
        self.routers.append(simple_router)
        self.routers.append(nfdump_router)
        api_application = FastApiApplication(self.routers).application
        return UvicornApplicationRunner(api_application)
