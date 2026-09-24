import rioxarray
from rasterio.io import MemoryFile

from app.ndvi import calculate_ndvi
from app.stac import load_sentinel2_item
from app.storage import read_object

item = load_sentinel2_item()

red_asset = item.assets["B04"]
nir_asset = item.assets["B08"]


red_data = read_object(red_asset.href)
nir_data = read_object(nir_asset.href)


with MemoryFile(red_data) as red_memfile, red_memfile.open() as red_src:
    red = rioxarray.open_rasterio(red_src).squeeze("band").load()

with MemoryFile(nir_data) as nir_memfile, nir_memfile.open() as nir_src:
    nir = rioxarray.open_rasterio(nir_src).squeeze("band").load()


ndvi = calculate_ndvi(red, nir)


print(f"Dimensions: {ndvi.dims}")
print(f"Shape:      {ndvi.shape}")
print(f"Mean NDVI:  {ndvi.mean().item():.3f}")