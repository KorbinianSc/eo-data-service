## Testing & CI

The project uses GitHub Actions for continuous integration.

On every push to `main` and every pull request, the CI pipeline:

1. sets up Python 3.14
2. installs the project and development dependencies
3. starts a MinIO S3-compatible object storage service
4. prepares test EO data in MinIO
5. runs Ruff
6. runs the test suite with pytest

The test suite includes integration tests for reading EO data from MinIO and calculating raster statistics.

## Architecture

The service implements a small cloud-native Earth Observation data pipeline:

```text
STAC metadata
     │
     ▼
   MinIO
(S3 object storage)
     │
     ▼
   COG raster
     │
     ▼
Rasterio / Xarray
     │
     ▼
 EO processing
   (NDVI)
     │
     ▼
   FastAPI
     │
     ▼
   REST API
```

### Data flow

1. **STAC** describes the Sentinel-2 item and its raster assets.
2. **MinIO** provides S3-compatible object storage for the raster data.
3. Raster assets are stored as **Cloud Optimized GeoTIFFs (COGs)**.
4. The application reads the objects through the S3 API and loads them with **Rasterio/rioxarray/Xarray**.
5. EO processing is implemented in Python, including **NDVI calculation**.
6. **FastAPI** exposes the data and processing results through REST endpoints.
7. **Docker Compose** provides a reproducible local service environment.
8. **GitHub Actions** runs linting and automated tests on pushes and pull requests.