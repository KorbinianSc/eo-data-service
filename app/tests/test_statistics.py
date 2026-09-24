from app.statistics import calculate_asset_statistics


def test_calculate_asset_statistics() -> None:
    statistics = calculate_asset_statistics(
        "S2A_20250815T101031",
        "B04",
    )

    assert statistics["item_id"] == "S2A_20250815T101031"
    assert statistics["asset"] == "B04"
    assert 0.0 <= statistics["min"] <= 9999.0
    assert 0.0 <= statistics["max"] <= 9999.0
    assert statistics["min"] <= statistics["mean"] <= statistics["max"]
