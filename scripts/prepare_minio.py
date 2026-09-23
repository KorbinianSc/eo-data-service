import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ["MINIO_ENDPOINT"]
ACCESS_KEY = os.environ["MINIO_ACCESS_KEY"]
SECRET_KEY = os.environ["MINIO_SECRET_KEY"]
BUCKET = "eo-data"
OBJECT_KEY = "sentinel-2/test_b04_cog.tif"
LOCAL_FILE = Path("data/test_b04_cog.tif")


s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name="us-east-1",
)


try:
    s3.head_bucket(Bucket=BUCKET)
except s3.exceptions.ClientError:
    s3.create_bucket(Bucket=BUCKET)


s3.upload_file(
    str(LOCAL_FILE),
    BUCKET,
    OBJECT_KEY,
)

print(f"Uploaded {LOCAL_FILE} to s3://{BUCKET}/{OBJECT_KEY}")