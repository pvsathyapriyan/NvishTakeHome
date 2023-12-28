from pydantic import BaseModel


class AuthResponse(BaseModel):
    isAuthenticated: bool
    message: str

