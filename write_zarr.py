import rioxarray

da = rioxarray.open_rasterio(
    "data/test_b04_cog.tif",
    chunks={"x": 25, "y": 25},
)

da.to_zarr("data/test_b04.zarr", mode="w")

print("Zarr dataset written.")