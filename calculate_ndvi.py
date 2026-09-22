import rioxarray

from app.stac import load_sentinel2_item

item = load_sentinel2_item()

red_asset = item.assets["B04"]
nir_asset = item.assets["B08"]

red = rioxarray.open_rasterio(red_asset.href).squeeze("band")
nir = rioxarray.open_rasterio(nir_asset.href).squeeze("band")

ndvi = (nir - red) / (nir + red)

print(ndvi)
print()
print(f"Dimensions: {ndvi.dims}")
print(f"Shape:      {ndvi.shape}")
print(f"Mean NDVI:  {ndvi.mean().item():.3f}")