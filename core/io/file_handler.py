from core.io.handler import Handler
from core.models.file import File
import uuid
import os


class FileHandler(Handler):
    def __init__(self, working_dir):
        self.__working_dir = working_dir

    def create(self, file: File):
        generated_uuid = uuid.uuid4()
        file.path = "{}{}".format(self.__working_dir, str(generated_uuid))
        with open(file.path, "wb") as fd:
            fd.write(file.data)

    def delete(self, file: File):
        os.remove(file.path)
