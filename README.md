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