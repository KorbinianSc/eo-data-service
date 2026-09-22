import rioxarray

da = rioxarray.open_rasterio(
    "data/test_b04_cog.tif",
    chunks={"x": 25, "y": 25},
)

print(da)
print()
print(f"Type:      {type(da.data)}")
print(f"Chunks:    {da.chunks}")

mean = da.mean()

print()
print(f"Mean object: {mean}")
print(f"Mean type:   {type(mean.data)}")

result = mean.compute()

print()
print(f"Computed mean: {result.item():.2f}")