import rasterio
from rasterio.shutil import copy

for band in ["b04", "b08"]:
    source = f"data/test_{band}.tif"
    destination = f"data/test_{band}_cog.tif"

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
