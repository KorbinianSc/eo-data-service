from datetime import datetime

import pystac
from pystac.extensions.eo import EOExtension

item = pystac.Item(
    id="S2A_20250815T101031",
    collection="sentinel-2",
    geometry={
        "type": "Polygon",
        "coordinates": [
            [
                [11.0, 47.0],
                [11.2, 47.0],
                [11.2, 47.2],
                [11.0, 47.2],
                [11.0, 47.0],
            ]
        ],
    },
    bbox=[11.0, 47.0, 11.2, 47.2],
    datetime=datetime.fromisoformat("2025-08-15T10:10:31+00:00"),
    properties={
        "platform": "sentinel-2a",
        "instruments": ["msi"],
    },
)
item.ext.add("eo")
EOExtension.ext(item).cloud_cover = 12.5

item.add_asset(
    "B04",
    pystac.Asset(
        href="data/test_b04_cog.tif",
        media_type="image/tiff; application=geotiff; profile=cloud-optimized",
        title="Sentinel-2 Red Band (B04)",
        roles=["data"],
    ),
)

item.add_asset(
    "B08",
    pystac.Asset(
        href="data/test_b04_cog.tif",
        media_type="image/tiff; application=geotiff; profile=cloud-optimized",
        title="Sentinel-2 NIR Band (B08)",
        roles=["data"],
    ),
)

item.add_link(
    pystac.Link(
        rel="collection",
        target="/collections/sentinel-2",
        media_type="application/json",
        title="Sentinel-2",
    )
)

print(item.to_dict())

item.validate()

print("STAC validation: OK")