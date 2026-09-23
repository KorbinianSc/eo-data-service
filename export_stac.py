from app.stac import create_sentinel2_item

item = create_sentinel2_item()

item.validate()

item.save_object(
    include_self_link=False,
    dest_href="data/sentinel2_item.json",
)

print("STAC Item saved.")   