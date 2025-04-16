from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from crud import create_query_record
from schemas import WalletResponse

# Используем in-memory SQLite для чистоты
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)


def setup_module(module):
    Base.metadata.create_all(bind=engine)


# def teardown_module(module):
#     Base.metadata.drop_all(bind=engine)


def test_create_query():
    db = TestingSessionLocal()
    try:
        data = WalletResponse(address="TXYZ...", balance="10", bandwidth="1000", energy="500")
        record = create_query_record(db, "TXYZ...", data)
        assert record.address == "TXYZ..."
        assert record.balance == "10"
    finally:
        db.close()
