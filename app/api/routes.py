from fastapi import APIRouter, HTTPException

from app.models import (
    Collection,
    CollectionResponse,
    StatisticsResponse,
)
from app.ndvi import calculate_ndvi, load_raster_from_storage

# from app.stac get_sentinel2_items, import get_sentinel2_item
from app.stac import load_sentinel2_item, load_sentinel2_items
from app.statistics import calculate_asset_statistics

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/collections", response_model=CollectionResponse)
def get_collections() -> CollectionResponse:
    return CollectionResponse(
        collections=[
            Collection(
                id="sentinel-2",
                title="Sentinel-2",
                description="Multispectral Earth Observation imagery",
            )
        ]
    )


@router.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str) -> Collection:
    if collection_id != "sentinel-2":
        raise HTTPException(
            status_code=404,
            detail=f"Collection '{collection_id}' not found",
        )

    return Collection(
        id="sentinel-2",
        title="Sentinel-2",
        description="Multispectral Earth Observation imagery",
    )


@router.get("/items")
def get_items() -> dict:
    # items = get_sentinel2_items()
    items = load_sentinel2_items()
    
    return items.to_dict()


@router.get("/items/{item_id}")
def get_item(item_id: str) -> dict:
    # item = get_sentinel2_item()
    item = load_sentinel2_item()

    if item.id != item_id:
        raise HTTPException(
            status_code=404,
            detail=f"Item '{item_id}' not found",
        )

    return item.to_dict()


@router.get("/ndvi/{item_id}")
def get_ndvi(item_id: str) -> dict[str, float | str]:
    item = load_sentinel2_item()

    if item.id != item_id:
        raise HTTPException(
            status_code=404,
            detail=f"Item '{item_id}' not found",
        )

    red_asset = item.assets["B04"]
    nir_asset = item.assets["B08"]
    
    red = load_raster_from_storage(red_asset.href)
    nir = load_raster_from_storage(nir_asset.href)

    ndvi = calculate_ndvi(red, nir)

    return {
        "item_id": item.id,
        "mean_ndvi": float(ndvi.mean().item()),
        "min_ndvi": float(ndvi.min().item()),
        "max_ndvi": float(ndvi.max().item()),
    }


@router.get(
    "/statistics/{item_id}",
    response_model=StatisticsResponse,
)
def get_statistics(
    item_id: str,
    asset: str = "B04",
) -> StatisticsResponse:
    try:
        statistics = calculate_asset_statistics(
            item_id,
            asset,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    return StatisticsResponse(**statistics)

# @router.get("/items", response_model=ItemResponse)
# def get_items() -> ItemResponse:
#     return ItemResponse(
#         items=[
#             Item(
#                 stac_version="1.1.0",
#                 stac_extensions=[
#                     "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
#                 ],
#                 id="S2A_20250815T101031",
#                 collection="sentinel-2",
#                 geometry={
#                     "type": "Polygon",
#                     "coordinates": [
#                         [
#                             [11.0, 47.0],
#                             [11.2, 47.0],
#                             [11.2, 47.2],
#                             [11.0, 47.2],
#                             [11.0, 47.0],
#                         ]
#                     ],
#                 },
#                 bbox=[11.0, 47.0, 11.2, 47.2],
#                 datetime="2025-08-15T10:10:31Z",
#                 properties={
#                     "cloud_cover": 12.5,
#                     "platform": "sentinel-2a",
#                     "instruments": ["msi"],
#                 },
#                 assets={
#                     "B04": {
#                         "href": "data/test_b04_cog.tif",
#                         "media_type": "image/tiff; application=geotiff; profile=cloud-optimized",
#                         "title": "Sentinel-2 Red Band (B04)",
#                         "roles": ["data"],
#                     },
#                     "B08": {
#                         "href": "data/test_b04_cog.tif",
#                         "media_type": "image/tiff; application=geotiff; profile=cloud-optimized",
#                         "title": "Sentinel-2 NIR Band (B08)",
#                         "roles": ["data"],
#                     },
#                 },
#                 links=[
#                     Link(
#                         rel="collection",
#                         href="/collections/sentinel-2",
#                         type="application/json",
#                         title="Sentinel-2",
#                     ),
#                 ]
#             )
#         ]
#     )