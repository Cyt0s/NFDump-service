from pydantic import BaseModel


class Router(BaseModel):
    router_configuration: dict
