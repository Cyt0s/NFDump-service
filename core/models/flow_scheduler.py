from pydantic import BaseModel
from typing import List
from core.normalizers.logics.logic import Logic


class FlowScheduler(BaseModel):
    preprocess_logics: List[Logic]
    process_logics: List[Logic]

    class Config:
        arbitrary_types_allowed = True