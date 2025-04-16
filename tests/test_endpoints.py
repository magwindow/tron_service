from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_wallet():
    address = "TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT"
    response = client.post("/wallet", json={"address": address})
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data


def test_get_wallets():
    response = client.get("/wallets?skip=0&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
