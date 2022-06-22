from api.models.router import Router
from fastapi import APIRouter


class FastApiRouter(Router):
    router: APIRouter

    class Config:
        arbitrary_types_allowed = True
