import numpy as np
import xarray as xr

from app.ndvi import calculate_ndvi


def test_calculate_ndvi():
    red = xr.DataArray(
        np.array([[1000, 2000]], dtype=np.uint16),
        dims=("y", "x"),
    )

    nir = xr.DataArray(
        np.array([[3000, 4000]], dtype=np.uint16),
        dims=("y", "x"),
    )

    ndvi = calculate_ndvi(red, nir)

    expected = np.array([
        [(3000 - 1000) / (3000 + 1000),
         (4000 - 2000) / (4000 + 2000)]
    ], dtype=np.float32)

    np.testing.assert_allclose(ndvi.values, expected)

    assert ndvi.dtype == np.float32