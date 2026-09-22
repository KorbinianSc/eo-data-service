from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_items() -> None:
    response = client.get("/items")

    assert response.status_code == 200

    data = response.json()

    assert data["type"] == "FeatureCollection"
    assert "features" in data
    assert len(data["features"]) == 1

    item = data["features"][0]

    assert item["id"] == "S2A_20250815T101031"
    assert item["collection"] == "sentinel-2"
    assert "B04" in item["assets"]
    assert "B08" in item["assets"]

    assert item["assets"]["B04"]["href"] == (
        "s3://eo-data/sentinel-2/test_b04_cog.tif"
    )

def test_get_unknown_item() -> None:
    response = client.get("/items/unknown")

    assert response.status_code == 404