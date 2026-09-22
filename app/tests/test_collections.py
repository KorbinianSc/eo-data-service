from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_collections() -> None:
    response = client.get("/collections")

    assert response.status_code == 200

    data = response.json()

    assert "collections" in data
    assert len(data["collections"]) == 1
    assert data["collections"][0]["id"] == "sentinel-2"
