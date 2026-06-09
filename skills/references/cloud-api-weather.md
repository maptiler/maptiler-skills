# Weather API

The MapTiler **Weather API** provides a complete catalog of current weather-related variables, their metadata, and individual keyframes (forecast times).

URL: `https://docs.maptiler.com/cloud/api/weather/`

## Endpoints

### 1. Weather catalog
`GET https://api.maptiler.com/weather/latest.json`
- **Description:** List current weather-related variables, their metadata, and individual keyframes. This is essential for discovering what weather data is available and the specific timestamps (keyframes) required to fetch the corresponding tile layers.

---

## Query Parameters

No specific query parameters other than the required MapTiler API key (`?key=YOUR_MAPTILER_API_KEY`).

---

## Response Format

The API returns a JSON object containing a catalog of available weather variables.

### Success Response (200 OK)
Returns a `WeatherCatalogResult` object containing an array of `variables`.

```json
{
  "variables": [
    {
      "spatial_ref_sys": {
        "auth_name": "EPSG",
        "auth_srid": "3857",
        "wkt": "PROJCRS[\"WGS 84 / Pseudo-Mercator\",...]"
      },
      "bounds": [-20037481.18, -20037508.34, 20008180.55, 20037508.34],
      "tile_format": "png",
      "tile_matrix_set": {
        "bounds": [-20037481.18, -20037508.34, 20008180.55, 20037508.34],
        "items": [
           { "zoom_level": 0, "matrix_width": 1, "matrix_height": 1, "tile_width": 256, "tile_height": 256, "pixel_x_size": 156543.03, "pixel_y_size": 156543.03 }
        ]
      },
      "metadata": {
        "weather_variable": {
          "name": "Wind",
          "description": "Wind at 10 m above ground [m/s]",
          "attribution": "GFS",
          "variable_id": "wind-10m:gfs",
          "unit": "ms",
          "release_timestamp": "2023-03-01T06:00:00+00:00",
          "timestamp": "2023-03-01T11:00:00+00:00",
          "decoding": {
            "channels": "rg",
            "min": -75,
            "max": 75
          }
        }
      },
      "keyframes": [
        {
          "id": "abc-123-uuid",
          "timestamp": "2023-03-01T11:00:00+00:00"
        }
      ]
    }
  ]
}
```

### WeatherCatalogResult Properties
- **`variables`**: Array of `TilesetDefinition` objects extended with `keyframes`.
  - **`spatial_ref_sys`**: Projection info (`auth_name`, `auth_srid`, `wkt`).
  - **`bounds`**: 4-number array `[minx, miny, maxx, maxy]` in the given projection.
  - **`tile_format`**: Format of individual tiles (e.g. `png`).
  - **`tile_matrix_set`**: Defines the zoom levels, resolutions, and matrix sizes.
  - **`keyframes`**: Array of available keyframes (forecast slices).
    - `id`: UUID of the specific tileset frame.
    - `timestamp`: ISO timestamp of the specific frame.
  - **`metadata.weather_variable`**:
    - `name` (string): Human-friendly name (e.g., "Wind").
    - `description` (string): Human-friendly description.
    - `attribution` (string): Data source (e.g., "GFS").
    - `variable_id` (string): Unique ID for grouping (e.g., "wind-10m:gfs").
    - `unit` (string): Unit of values (e.g., "ms").
    - `release_timestamp` (string): ISO timestamp of the whole batch release.
    - `timestamp` (string): ISO timestamp of this specific forecast frame.
    - `decoding` (object): How to decode values from the pixel colors.
      - `channels`: `r`, `g`, `b`, `rg`, `rb`, `gb`, or `rgb`.
      - `min`: Minimum data boundary.
      - `max`: Maximum data boundary.

### Error Responses
- **`403`**: Forbidden (Invalid, missing, or restricted API key)
