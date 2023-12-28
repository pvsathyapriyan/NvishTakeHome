from models.auth import AuthResponse
from fastapi import APIRouter, Request, Response
from utils import auth

router = APIRouter()


@router.get("/authorize", response_model=AuthResponse, status_code=200)
async def authorize(request: Request, response: Response):
    key = request.headers.get("Authorization")
    isAuthenticated = auth.check_authentication(key)
    if isAuthenticated:
        message = "success"
    else:
        message = "authentication failed"
        response.status_code = 400

    return AuthResponse(isAuthenticated=isAuthenticated, message=message)
