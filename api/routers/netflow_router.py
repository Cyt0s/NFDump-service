from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from core.orchestrator_bootstraper import orchestrator
from core.models.file import File

router = APIRouter()


@router.post("/netflow")
async def upload_file_to_process(file: Request):
    data: bytes = await file.body()
    flow_file = File(path="", data=data)
    normalized_data = orchestrator.orchestrate(flow_file)
    return JSONResponse(content=normalized_data)
