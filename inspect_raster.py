import rasterio

with rasterio.open("data/test_b04_cog.tif") as src:
    print(f"Width:       {src.width}")
    print(f"Height:      {src.height}")
    print(f"Bands:       {src.count}")
    print(f"Data type:   {src.dtypes[0]}")
    print(f"CRS:         {src.crs}")
    print(f"Bounds:      {src.bounds}")
    print(f"Transform:   {src.transform}")
    print(f"Block shapes: {src.block_shapes}")
    print(f"Overviews:   {src.overviews(1)}")