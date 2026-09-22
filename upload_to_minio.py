import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1",
)

bucket = "eo-data"
source = "data/test_b04_cog.tif"
key = "sentinel-2/test_b04_cog.tif"

s3.upload_file(
    source,
    bucket,
    key,
)

print(f"Uploaded: {source}")
print(f"s3://{bucket}/{key}")