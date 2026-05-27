from sqlalchemy.orm import Session
from .item_model import Item
class ItemService:
    def get_by_id(self, db:Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()
    
    def create(self, db:Session, name: str, price: float):
        db_item = Item(name=name, price=price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    
item_service = ItemService()