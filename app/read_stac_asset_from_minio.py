import boto3
from rasterio.io import MemoryFile

from app.stac import load_sentinel2_item


def parse_s3_href(href: str) -> tuple[str, str]:
    if not href.startswith("s3://"):
        raise ValueError(f"Unsupported asset href: {href}")

    path = href.removeprefix("s3://")
    bucket, key = path.split("/", 1)

    return bucket, key


s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1",
)

item = load_sentinel2_item()
asset = item.assets["B04"]
print (item)
print()
print (asset.href)
print()
print()
bucket, key = parse_s3_href(asset.href)

print(f"Asset:  {asset.title}")
print(f"Bucket: {bucket}")
print(f"Key:    {key}")

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