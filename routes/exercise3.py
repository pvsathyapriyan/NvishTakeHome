from models.employees import Employee, EmployeePayload, EmployeeNotFound, EmployeeBadRequest, EmployeeDelete
from fastapi import APIRouter, Response, Request
from db import sqlite
from cache import redis_util
from utils import auth

router = APIRouter()


@router.get("/get/{empid}", responses={200: {"model": Employee},
                                            404: {"model": EmployeeNotFound},
                                            400: {"model": EmployeeBadRequest}})
async def read_employee(empid: int, request: Request, response: Response):
    key = request.headers.get("Authorization")
    isAuthenticated = auth.check_authentication(key)
    if not isAuthenticated:
        message = "authentication failed"
        response.status_code = 400
        return EmployeeBadRequest(message=message)

    emp_name = redis_util.read_from_redis(empid)
    if not emp_name:
        query = sqlite.employee_table.select().where(sqlite.employee_table.c.empid == empid)

        try:
            employee = (await sqlite.database.fetch_one(query))._asdict()
            pass
        except AttributeError:
            response.status_code = 404
            return EmployeeNotFound()
        else:
            emp_name = employee.get('name')
            redis_util.write_to_redis(empid, employee.get('name'))

    return Employee(empid=empid, name=emp_name)


@router.post("/save", responses={200: {"model": Employee},
                                      400: {"model": EmployeeBadRequest}})
async def create_employee(payload: EmployeePayload, request: Request, response: Response):
    key = request.headers.get("Authorization")
    isAuthenticated = auth.check_authentication(key)
    if not isAuthenticated:
        message = "authentication failed"
        response.status_code = 400
        return EmployeeBadRequest(message=message)

    query = sqlite.employee_table.insert().values(name=payload.name)
    last_record_id = await sqlite.database.execute(query)

    if not last_record_id:
        response.status_code = 400
        return EmployeeBadRequest()
    else:
        redis_util.write_to_redis(last_record_id, payload.name)

    return Employee(empid=last_record_id, name=payload.name)


@router.delete("/delete/{empid}", responses={200: {"model": Employee},
                                                  404: {"model": EmployeeBadRequest}})
async def delete_employee(empid: int, request: Request, response: Response):
    key = request.headers.get("Authorization")
    isAuthenticated = auth.check_authentication(key)
    if not isAuthenticated:
        message = "authentication failed"
        response.status_code = 400
        return EmployeeBadRequest(message=message)

    query = sqlite.employee_table.delete().where(sqlite.employee_table.c.empid == empid)

    try:
        await sqlite.database.execute(query)
    except Exception as e:
        response.status_code = 404
        return EmployeeBadRequest(message=str(e))

    return EmployeeDelete(empid=empid)