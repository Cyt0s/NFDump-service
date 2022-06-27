from pydantic import BaseModel


class ParsedObject(BaseModel):
    data: dict
