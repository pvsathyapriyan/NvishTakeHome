from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.exercise1 import router as exercise1_router
from routes.exercise2 import router as exercise2_router
from routes.exercise3 import router as exercise3_router


app = FastAPI(openapi_url="/nvish/openapi.json", docs_url="/nvish/docs", redoc_url="/nvish/redocs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"]
)

app.include_router(exercise1_router, prefix="/nvish", tags=["ping"])
app.include_router(exercise2_router, prefix="/nvish", tags=["auth"])
app.include_router(exercise3_router, prefix="/nvish", tags=["auth"])


def fetch_app():
    return app

