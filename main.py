from fastapi import FastAPI
from app.core.db import engine, Base
from app.routes.clients import router as clients_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SAMTIK API")
app.include_router(clients_router)
