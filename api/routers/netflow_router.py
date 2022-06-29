from fastapi import APIRouter, UploadFile
from core.orchestrator_bootstraper import orchestrator


router = APIRouter()


@router.post("/netflow")
def upload_file_to_process(file: UploadFile):
    print(file.filename)
    return "OK"
