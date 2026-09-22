import xarray as xr

ds = xr.open_zarr("data/test_b04.zarr")

print(ds)
print()
print(f"Dimensions: {ds.dims}")
print(f"Variables:  {list(ds.data_vars)}")