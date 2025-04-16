from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session


from database import SessionLocal, engine
import models
import schemas
import crud
from tron_utils import get_wallet_info

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/wallet", response_model=schemas.WalletResponse)
def query_wallet(data: schemas.WalletRequest, db: Session = Depends(get_db)):
    try:
        info = get_wallet_info(data.address)
        wallet_data = schemas.WalletResponse(address=data.address, **info)
        crud.create_query_record(db, data.address, wallet_data)
        return wallet_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/wallets", response_model=schemas.PaginatedResponse)
def get_wallet_queries(skip: int = Query(0), limit: int = Query(10), db: Session = Depends(get_db)):
    total, results = crud.get_paginated_queries(db, skip, limit)

    # Преобразуем ORM-модели в Pydantic-схемы с нужными типами (timestamp → str)
    response_data = [
        schemas.WalletQueryInDB(
            address=item.address,
            balance=str(item.balance),
            bandwidth=str(item.bandwidth),
            energy=str(item.energy),
            timestamp=item.timestamp.isoformat()
        )
        for item in results
    ]

    return {"results": response_data, "total": total}
