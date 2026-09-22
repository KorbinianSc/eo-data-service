from rasterio.io import MemoryFile

from app.stac import load_sentinel2_item
from app.storage import read_object


def calculate_asset_statistics(
    item_id: str,
    asset_key: str,
) -> dict[str, float | str]:
    item = load_sentinel2_item()

    if item.id != item_id:
        raise ValueError(f"Item '{item_id}' not found")

    if asset_key not in item.assets:
        raise ValueError(f"Asset '{asset_key}' not found")

    asset = item.assets[asset_key]

    data = read_object(asset.href)

    with MemoryFile(data) as memfile, memfile.open() as src:
        raster_data = src.read(1)

    return {
        "item_id": item.id,
        "asset": asset_key,
        "min": float(raster_data.min()),
        "max": float(raster_data.max()),
        "mean": float(raster_data.mean()),
    }