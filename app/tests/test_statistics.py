from app.statistics import calculate_asset_statistics


def test_calculate_asset_statistics() -> None:
    statistics = calculate_asset_statistics(
        "S2A_20250815T101031",
        "B04",
    )

    assert statistics["item_id"] == "S2A_20250815T101031"
    assert statistics["asset"] == "B04"
    assert statistics["min"] == 0.0
    assert statistics["max"] == 9999.0
    assert 4900.0 < statistics["mean"] < 5000.0
