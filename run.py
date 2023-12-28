from fastapi.openapi.utils import get_openapi
from main import app
import uvicorn


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Nvish Assignment",
        version="1.0.0",
        description="Bunch of APIs for the assignment",
        routes=app.routes,
        contact={"email": "pvsathyapriyan@gmail.com"}
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":

    uvicorn.run("run:app", host="0.0.0.0", port=80, reload=True)
