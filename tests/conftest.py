from app.modules.item_module.item_router import get_db
from app.main import app
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
TEST_DATABASE_URL = "postgresql+psycopg2://postgres:posql@localhost:5432/item"

engine = create_engine(TEST_DATABASE_URL)
Base.metadata.create_all(bind=engine)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)

    def get_test_db():
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = get_test_db

    with TestClient(app) as c:
        yield c

    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()