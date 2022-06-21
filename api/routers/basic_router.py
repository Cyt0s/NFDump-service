from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def open():
    return {"msg":"Hello world\n"}

@router.post("/data")
async def test_data(data):
    print(data)
    return {"sucess":""}