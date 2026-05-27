from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from app.modules.item_module.item_schema import ItemCreate
from app.modules.item_module.item_schema import ItemResponse
from app.modules.item_module.item_service import item_service
from app.core.database import SessionLocal
from fastapi import APIRouter

router = APIRouter()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=ItemResponse, status_code=201)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create(db, payload.name, payload.price)

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db:Session = Depends(get_db)):
    item = item_service.get_by_id(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
