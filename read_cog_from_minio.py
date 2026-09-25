import boto3
import rioxarray
from rasterio.io import MemoryFile

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1",
)

bucket = "eo-data"
key = "sentinel-2/test_b04_cog.tif"

response = s3.get_object(
    Bucket=bucket,
    Key=key,
)

data = response["Body"].read()

with MemoryFile(data) as memfile, memfile.open() as src:
    print(f"Width:  {src.width}")
    print(f"Height: {src.height}")
    print(f"CRS:    {src.crs}")
    print(f"Bounds: {src.bounds}")
    print(f"Dtype:  {src.dtypes[0]}")
    xarray_data = rioxarray.open_rasterio(src).squeeze("band")

    print()
    print(xarray_data)
    print()
    print(f"Dimensions: {xarray_data.dims}")
    print(f"Shape:      {xarray_data.shape}")
