# Maps API

The MapTiler **Maps API** provides core access to MapTiler Cloud map styles, including style JSONs, raster tiles, map symbols, and embeddable viewers.

URL: `https://docs.maptiler.com/cloud/api/maps/`

## Endpoints

### 1. Embeddable HTML viewer
`GET https://api.maptiler.com/maps/{mapId}/`
- **Description:** Returns an embeddable HTML viewer for the map.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map (e.g., `streets-v4`).
- **Response:** `200 text/html`

### 2. Style JSON of the map
`GET https://api.maptiler.com/maps/{mapId}/style.json`
- **Description:** Style JSON describing the map cartography. Can be used with various libraries to display a vector map (e.g., MapLibre GL JS, OpenLayers).
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
- **Response:** `200 application/json` containing the StyleJSON schema.

### 3. Map symbols (sprites)
`GET https://api.maptiler.com/maps/{mapId}/sprite{scale}.{format}`
- **Description:** Map symbols (sprites) required to display the vector map.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
  - `scale` (string, optional) - Allowed enum values: `@2x` (use to get "retina"/HiDPI image).
  - `format` (string, required) - Allowed enum values: `png`, `json`.
- **Response:** `200 application/json` or `200 image/png` depending on the format requested.

### 4. Raster XYZ tiles
`GET https://api.maptiler.com/maps/{mapId}/{tileSize}/{z}/{x}/{y}{scale}.{format}`
- **Description:** Rasterized tiles (XYZ) of the map. Can be used with libraries like Leaflet or OpenLayers. Note: It's usually better to use the TileJSON rather than using the tile URL directly.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
  - `tileSize/` (integer, optional) - Allowed enum values: `256/` (note the trailing slash in the path if provided).
  - `z` (integer, required) - Zoom level. Specifies the tile's zoom level.
  - `x` (integer, required) - Column. Specifies the tile's column.
  - `y` (integer, required) - Row. Specifies the tile's row.
  - `scale` (string, optional) - Allowed enum values: `@2x` (use to get "retina"/HiDPI image).
  - `format` (string, required) - Image format. Allowed enum values: `png`, `jpg`, `webp`.
- **Response:** `200 OK` (rasterized image binary `image/*`) or `400 Bad Request` (Out of bounds / Invalid format).

### 5. TileJSON
`GET https://api.maptiler.com/maps/{mapId}/{tileSize}/tiles.json`
- **Description:** TileJSON describing the metadata of the map as well as link to the XYZ tiles.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
  - `tileSize/` (integer, optional) - Allowed enum values: `256/`.
- **Response:** `200 application/json` containing the TileJSON schema.

### 6. WMTS Capabilities
`GET https://api.maptiler.com/maps/{mapId}/WMTSCapabilities.xml`
- **Description:** WMTS Capabilities XML document describing the metadata of the map as well as link to the XYZ tiles. Can be used with GIS software (e.g., QGIS) to display the map.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
- **Response:** `200 text/xml`.

---

## Query Parameters

All requests require your valid API key to be passed as a query parameter: `?key=YOUR_MAPTILER_API_KEY`.

---

## Standard Error Codes

All of the listed endpoints might return these error responses:
- **`403`**: Key is missing, invalid or restricted.
- **`404`**: The item does not exist.
- **`414`**: URI Too Long. Maximum allowed length is 8192 bytes.
