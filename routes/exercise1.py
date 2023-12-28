from models.ping import PingResponse
from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", response_model=PingResponse)
async def ping():
    return PingResponse(isSuccess=True)



