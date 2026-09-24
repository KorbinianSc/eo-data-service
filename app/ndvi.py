import rioxarray
import xarray as xr
from rasterio.io import MemoryFile

from app.storage import read_object


def calculate_ndvi(red: xr.DataArray, nir: xr.DataArray) -> xr.DataArray:
    """Calculate NDVI from red and NIR raster data."""

    red_float = red.astype("float32")
    nir_float = nir.astype("float32")

    return (nir_float - red_float) / (nir_float + red_float)


def load_raster_from_storage(href: str) -> xr.DataArray:
    """Load a raster asset from object storage into an Xarray DataArray."""

    data = read_object(href)

    with MemoryFile(data) as memfile, memfile.open() as src:
        return rioxarray.open_rasterio(src).squeeze("band").load()