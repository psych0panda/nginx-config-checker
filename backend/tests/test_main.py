import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/docs")
    assert response.status_code == 200

def test_check_nginx_config():
    with open("/app/tests/test_nginx.conf", "rb") as file:
        response = client.post("/api/v1/config/check-config/", files={"file": file})
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Конфигурация корректна."}