from app.modules.item_module.item_router import router as item_router
from fastapi import FastAPI
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(item_router, prefix="/api/v1/items", tags=["items"])