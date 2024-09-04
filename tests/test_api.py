from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_memory_info():
    response = client.get("/memory/?n=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
