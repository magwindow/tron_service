from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class WalletQuery(Base):
    __tablename__ = "wallet_queries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    balance = Column(String)
    bandwidth = Column(String)
    energy = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
