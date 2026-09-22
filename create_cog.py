import rasterio
from rasterio.shutil import copy

source = "data/test_b04.tif"
destination = "data/test_b04_cog.tif"

with rasterio.open(source) as src:
    profile = src.profile.copy()

    profile.update(
        driver="COG",
        compress="deflate",
        blocksize=256,
        overview_resampling="nearest",
    )

    copy(
        source,
        destination,
        **profile,
    )

print(f"COG created: {destination}")