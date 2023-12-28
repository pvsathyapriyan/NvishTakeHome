from pydantic import BaseModel


class Employee(BaseModel):
    empid: int
    name: str


class EmployeePayload(BaseModel):
    name: str


class EmployeeNotFound(BaseModel):
    message: str = "requested data not found"


class EmployeeBadRequest(BaseModel):
    message: str = "bad request received"


class EmployeeDelete(BaseModel):
    empid: int
    message: str = "deleted"
