# Tiles API

The MapTiler **Tiles API** provides direct access to the underlying vector or raster XYZ tiles for a given dataset/tileset, along with metadata documents like TileJSON and WMTS Capabilities.

URL: `https://docs.maptiler.com/cloud/api/tiles/`

## Endpoints

### 1. Embeddable HTML viewer
`GET https://api.maptiler.com/tiles/{tilesId}/`
- **Description:** Returns an embeddable HTML viewer for the tileset.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
- **Response:** `200 text/html`

### 2. XYZ tiles
`GET https://api.maptiler.com/tiles/{tilesId}/{z}/{x}/{y}`
- **Description:** The individual tiles. Can be used with various libraries to display the tiles (e.g., Leaflet, OpenLayers). Note: It's usually better to use the TileJSON rather than using the tile URL directly.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
  - `z` (integer, required) - Zoom level. Specifies the tile's zoom level.
  - `x` (integer, required) - Column. Specifies the tile's column.
  - `y` (integer, required) - Row. Specifies the tile's row.

### 3. TileJSON
`GET https://api.maptiler.com/tiles/{tilesId}/tiles.json`
- **Description:** TileJSON describing the metadata of the tiles as well as link to the XYZ tiles. Can be used with various libraries to display the tiles.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
- **Response:** `200 application/json` containing the TileJSON schema.

### 4. WMTS Capabilities
`GET https://api.maptiler.com/tiles/{tilesId}/WMTSCapabilities.xml`
- **Description:** WMTS Capabilities XML document describing the metadata of the tiles as well as link to the XYZ tiles. Can be used with various GIS software (e.g., QGIS) to display the tiles.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
- **Response:** `200 text/xml`

---

## Query Parameters

All requests require your valid API key to be passed as a query parameter: `?key=YOUR_MAPTILER_API_KEY`.

---

## Response Formats (XYZ Tiles)

When requesting individual XYZ tiles:
- **`200 OK`**: Returns the tile data.
- **`204 No Content`**: Tile not present -- presumed empty (empty response).
- **`400 Bad Request`**: Out of bounds.

## Standard Error Codes

All of the listed endpoints might return these error responses:
- **`403`**: Key is missing, invalid or restricted.
- **`404`**: The item does not exist.
- **`414`**: URI Too Long. Maximum allowed length is 8192 bytes.
