from app.stac import create_sentinel2_item


def test_load_sentinel2_item() -> None:
    from app.stac import load_sentinel2_item

    item = load_sentinel2_item()

    item.validate()

    assert item.id == "S2A_20250815T101031"
    assert item.collection_id == "sentinel-2"
    assert "B04" in item.assets
    assert "B08" in item.assets
    
def test_sentinel2_item_is_valid() -> None:
    item = create_sentinel2_item()

    item.validate()

    assert item.id == "S2A_20250815T101031"
    assert item.collection_id == "sentinel-2"
    assert "B04" in item.assets
    assert "B08" in item.assets

def test_get_sentinel2_item() -> None:
    from app.stac import get_sentinel2_item

    item = get_sentinel2_item()

    assert item.id == "S2A_20250815T101031"
