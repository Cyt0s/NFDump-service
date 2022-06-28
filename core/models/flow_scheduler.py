from pydantic import BaseModel


class FlowScheduler(BaseModel):
    preprocess_logics: list
    process_logics: list
