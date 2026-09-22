import rasterio

from app.stac import load_sentinel2_item

item = load_sentinel2_item()

asset = item.assets["B04"]

print(f"Asset: {asset.title}")
print(f"Href:  {asset.href}")

with rasterio.open(asset.href) as src:
    print(f"Width:  {src.width}")
    print(f"Height: {src.height}")
    print(f"CRS:    {src.crs}")