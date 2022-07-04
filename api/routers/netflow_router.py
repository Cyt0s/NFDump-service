from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from core.models.file import File
import bootstrapper

router = APIRouter()


@router.post("/netflow")
async def upload_file_to_process(file: Request):
    data: bytes = await file.body()
    flow_file = File(path="", data=data)
    normalized_data = bootstrapper.orchestrator.orchestrate(flow_file)
    return JSONResponse(content=normalized_data)
