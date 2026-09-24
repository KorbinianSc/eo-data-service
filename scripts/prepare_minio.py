import os
import subprocess
import sys
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ["MINIO_ENDPOINT"]
ACCESS_KEY = os.environ["MINIO_ACCESS_KEY"]
SECRET_KEY = os.environ["MINIO_SECRET_KEY"]
BUCKET = "eo-data"


def prepare_test_data() -> None:
    subprocess.run(
        [sys.executable, "data/create_test_raster.py"],
        check=True,
    )

    subprocess.run(
        [sys.executable, "create_cog.py"],
        check=True,
    )


def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name="us-east-1",
    )


def ensure_bucket(s3) -> None:
    try:
        s3.head_bucket(Bucket=BUCKET)
    except s3.exceptions.ClientError:
        s3.create_bucket(Bucket=BUCKET)


def upload_cogs(s3) -> None:
    for band in ["b04", "b08"]:
        local_file = Path(f"data/test_{band}_cog.tif")
        object_key = f"sentinel-2/test_{band}_cog.tif"

        s3.upload_file(
            str(local_file),
            BUCKET,
            object_key,
        )

        print(f"Uploaded {local_file} to s3://{BUCKET}/{object_key}")


def main() -> None:
    prepare_test_data()

    s3 = get_s3_client()
    ensure_bucket(s3)
    upload_cogs(s3)


if __name__ == "__main__":
    main()