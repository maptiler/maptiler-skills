# OGC API

The MapTiler **OGC API** provides endpoints that conform to the OGC (Open Geospatial Consortium) Web API standards, specifically the OGC API - Tiles v1.0 specification.

URL: `https://docs.maptiler.com/cloud/api/ogc/`

## Endpoints

### 1. OGC API - Tiles (for Tilesets)
`GET https://api.maptiler.com/tiles/{tilesId}/tiles`
- **Description:** Tileset landing page of the tiles. Can be used in software supporting the OGC API - Tiles v1.0 specification.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
- **Response:** `200 application/json`

### 2. OGC API - Tiles (for Maps)
`GET https://api.maptiler.com/maps/{mapId}/tiles`
- **Description:** Tileset landing page of the rasterized map tiles. Can be used in software supporting the OGC API - Tiles v1.0 specification.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
- **Response:** `200 application/json`

### 3. OGC API TileMatrixSets (for Tilesets)
`GET https://api.maptiler.com/tiles/{tilesId}/tiles/WebMercatorQuad`
- **Description:** Description of the tileset tile matrix sets according to the OGC Web API. This resource is linked from the OGC API - Tiles endpoint.
- **Path Parameters:**
  - `tilesId` (string, required) - Identifier of the tileset.
- **Response:** `200 application/json`

### 4. OGC API TileMatrixSets (for Maps)
`GET https://api.maptiler.com/maps/{mapId}/tiles/WebMercatorQuad`
- **Description:** Description of the map tile matrix sets according to the OGC Web API. This resource is linked from the OGC API - Tiles endpoint.
- **Path Parameters:**
  - `mapId` (string, required) - Identifier of the map.
- **Response:** `200 application/json`

### 5. OGC API conformance classes
`GET https://api.maptiler.com/conformance`
- **Description:** Declaration of the implemented OGC conformance classes.
- **Response:** `200 application/json`

---

## Query Parameters

All requests require your valid API key to be passed as a query parameter: `?key=YOUR_MAPTILER_API_KEY`.
