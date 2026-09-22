import os

import boto3
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url=os.environ["MINIO_ENDPOINT"],
        aws_access_key_id=os.environ["MINIO_ACCESS_KEY"],
        aws_secret_access_key=os.environ["MINIO_SECRET_KEY"],
        region_name="us-east-1",
    )


def parse_s3_href(href: str) -> tuple[str, str]:
    if not href.startswith("s3://"):
        raise ValueError(f"Unsupported asset href: {href}")

    path = href.removeprefix("s3://")
    bucket, key = path.split("/", 1)

    return bucket, key


def read_object(href: str) -> bytes:
    bucket, key = parse_s3_href(href)

    s3 = get_s3_client()

    response = s3.get_object(
        Bucket=bucket,
        Key=key,
    )

    return response["Body"].read()