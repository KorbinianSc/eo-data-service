import rasterio
import xarray as xr

with rasterio.open("data/test_b04_cog.tif") as src:
    data = src.read(1)

    x = [src.xy(0, col)[0] for col in range(src.width)]
    y = [src.xy(row, 0)[1] for row in range(src.height)]

da = xr.DataArray(
    data,
    dims=("y", "x"),
    coords={
        "x": x,
        "y": y,
    },
    name="B04",
)

print(da)
print()
print(f"Dimensions: {da.dims}")
print(f"Shape:      {da.shape}")
print(f"X range:    {da.x.min().item():.3f} → {da.x.max().item():.3f}")
print(f"Y range:    {da.y.min().item():.3f} → {da.y.max().item():.3f}")
print(f"Mean:       {da.mean().item():.2f}")