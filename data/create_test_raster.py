import numpy as np
import rasterio
from rasterio.transform import from_origin

width = 2048
height = 2048

rng = np.random.default_rng(42)

red = rng.integers(
    2000,
    6000,
    size=(height, width),
    dtype=np.uint16,
)

nir = rng.integers(
    4000,
    9000,
    size=(height, width),
    dtype=np.uint16,
)

transform = from_origin(
    11.0,
    47.2,
    0.002,
    0.002,
)

for filename, data in [
    ("data/test_b04.tif", red),
    ("data/test_b08.tif", nir),
]:
    with rasterio.open(
        filename,
        "w",
        driver="GTiff",
        width=width,
        height=height,
        count=1,
        dtype=data.dtype,
        crs="EPSG:4326",
        transform=transform,
    ) as dst:
        dst.write(data, 1)
