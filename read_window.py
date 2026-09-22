import rasterio
from rasterio.windows import Window

with rasterio.open("data/test_b04_cog.tif") as src:
    window = Window(
        col_off=25,
        row_off=25,
        width=20,
        height=20,
    )

    data = src.read(1, window=window)

    print(f"Window shape: {data.shape}")
    print(f"Minimum:      {data.min()}")
    print(f"Maximum:      {data.max()}")
    print(f"Mean:         {data.mean():.2f}")
