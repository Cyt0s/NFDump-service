import uvicorn
from api.application_runners.base_application_runner import BaseApplicationRunner


class UvicornApplicationRunner(BaseApplicationRunner):

    def __init__(self, app):
        self.app = app

    def start(self):
        uvicorn.run(self.app)
