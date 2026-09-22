import numpy as np
import rasterio
from rasterio.transform import from_origin

width = 100
height = 100

data = np.random.randint(
    0,
    10000,
    size=(height, width),
    dtype=np.uint16,
)

transform = from_origin(
    11.0,
    47.2,
    0.002,
    0.002,
)

with rasterio.open(
    "data/test_b04.tif",
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
