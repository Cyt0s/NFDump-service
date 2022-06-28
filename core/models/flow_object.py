from pydantic import BaseModel
from pandas import DataFrame


class FlowObject(BaseModel):
    data: DataFrame

    class Config:
        arbitrary_types_allowed = True
