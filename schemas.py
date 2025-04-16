from pydantic import BaseModel
from typing import List


class WalletRequest(BaseModel):
    address: str


class WalletResponse(BaseModel):
    address: str
    balance: str
    bandwidth: str
    energy: str


class WalletQueryInDB(WalletResponse):
    timestamp: str


class PaginatedResponse(BaseModel):
    results: List[WalletQueryInDB]
    total: int
