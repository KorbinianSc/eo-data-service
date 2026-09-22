from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_collection() -> None:
    response = client.get("/collections/sentinel-2")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == "sentinel-2"
    assert data["title"] == "Sentinel-2"


def test_get_unknown_collection() -> None:
    response = client.get("/collections/unknown")

    assert response.status_code == 404