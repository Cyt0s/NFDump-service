from api.models.base_router import BaseRouter


class FastApiRouter(BaseRouter):

    def __init__(self, router, router_configuration: dict):
        super().__init__(router, router_configuration)
