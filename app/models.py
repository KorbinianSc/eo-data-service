from datetime import datetime

from pydantic import BaseModel, Field


class Asset(BaseModel):
    href: str
    media_type: str
    title: str
    roles: list[str]


class Geometry(BaseModel):
    type: str
    coordinates: list[list[list[float]]]


class ItemProperties(BaseModel):
    cloud_cover: float = Field(alias="eo:cloud_cover")
    platform: str
    instruments: list[str]

    model_config = {
        "populate_by_name": True,
    }

class Link(BaseModel):
    rel: str
    href: str
    type: str | None = None
    title: str | None = None


class Item(BaseModel):
    stac_version: str
    stac_extensions: list[str] = []
    id: str
    collection: str
    geometry: Geometry
    bbox: list[float]
    datetime: datetime
    properties: ItemProperties
    assets: dict[str, Asset]
    links: list[Link]


class Collection(BaseModel):
    id: str
    title: str
    description: str


class CollectionResponse(BaseModel):
    collections: list[Collection]


class ItemResponse(BaseModel):
    items: list[Item]


class StatisticsResponse(BaseModel):
    item_id: str
    asset: str
    min: float
    max: float
    mean: float