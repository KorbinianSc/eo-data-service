from app.storage import read_object


def test_read_object_from_minio() -> None:
    data = read_object(
        "s3://eo-data/sentinel-2/test_b04_cog.tif"
    )

    assert len(data) > 0