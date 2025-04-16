from sqlalchemy.orm import Session
from models import WalletQuery
from schemas import WalletResponse


def create_query_record(db: Session, address: str, data: WalletResponse):
    record = WalletQuery(
        address=address,
        balance=data.balance,
        bandwidth=data.bandwidth,
        energy=data.energy
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def get_paginated_queries(db: Session, skip: int = 0, limit: int = 10):
    total = db.query(WalletQuery).count()
    results = db.query(WalletQuery).order_by(WalletQuery.timestamp.desc()).offset(skip).limit(limit).all()
    return total, results
