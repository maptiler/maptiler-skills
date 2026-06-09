# MapTiler Cloud REST API Index

The **MapTiler Cloud REST APIs** let you retrieve map styles, vector and raster tiles, static map images, weather data, geocoding results, elevation profiles, and coordinate conversions directly from MapTiler's high-speed global Content Delivery Network (CDN).

These APIs are optimized for fast client-side loading, high concurrency, and low latency.

---

## Getting Started & Authentication

All requests to the client-side Cloud REST APIs must be authenticated. The standard authentication method is using an **API Key**.

To authenticate, simply append your API key as a query parameter to your request URLs:
`?key=YOUR_MAPTILER_API_KEY`

Get your API keys in your MapTiler account on the [API Keys page](https://cloud.maptiler.com/keys/).

---

## API Catalog

MapTiler Cloud offers 12 specialized REST APIs. Below is the complete catalog of endpoints and their corresponding reference documents:

| API Name | Endpoint Base Path | Reference File | Purpose / Description |
| :--- | :--- | :--- | :--- |
| **Maps API** | `/maps/` | [cloud-api-maps.md](cloud-api-maps.md) | Retrieve vector tile schemas, map style JSON, sprites, fonts, and raster basemaps. |
| **Static Maps** | `/maps/{mapId}/static/` | [cloud-api-static-maps.md](cloud-api-static-maps.md) | Generate high-quality static images of maps, including custom paths and markers. |
| **Geocoding API** | `/geocoding/` | [cloud-api-geocoding.md](cloud-api-geocoding.md) | Search for locations by place name (forward), coordinates (reverse), or batch queries. |
| **Weather API** | `/weather/` | [cloud-api-weather.md](cloud-api-weather.md) | Query GFS/ECMWF weather variables, forecast keyframes, and raw decoding channels. |
| **Elevation API** | `/elevation/` | [cloud-api-elevation.md](cloud-api-elevation.md) | Retrieve elevation profiles or specific terrain heights for coordinate locations. |
| **Geolocation API**| `/geolocation/` | [cloud-api-geolocation.md](cloud-api-geolocation.md) | Locate visitors and return client country/city details using server-side IP matching. |
| **Coordinates** | `/coordinates/` | [cloud-api-coordinates.md](cloud-api-coordinates.md) | Search coordinate systems (EPSG) and transform coordinates between projections. |
| **Data API** | `/data/` | [cloud-api-data.md](cloud-api-data.md) | Manage, fetch, and query custom GeoJSON datasets and features hosted on your account. |
| **Tiles API** | `/tiles/` | [cloud-api-tiles.md](cloud-api-tiles.md) | Direct low-level raster or vector tile retrieval for custom tilesets and overlays. |
| **OGC API** | `/conformance`, `/tiles`| [cloud-api-ogc.md](cloud-api-ogc.md) | Access map layers conforming to OGC standards (WebMercatorQuad tile matrix sets). |
| **Fonts API** | `/fonts/` | [cloud-api-fonts.md](cloud-api-fonts.md) | Retrieve font stack glyph subsets (.pbf) for text and label rendering on vector maps. |
| **Images API** | `/images/` | [cloud-api-images.md](cloud-api-images.md) | Query and display hosted raster imagery and custom tileset sources. |

---

## Standard Error Codes

All client-side Cloud REST APIs return standard HTTP status codes to signal success or failure:

- **`200 OK`**: The request was successful, and the response body contains the requested data.
- **`400 Bad Request`**: The request had invalid parameters, malformed query syntax, or went over query limits (e.g. searching a query that is too long).
- **`403 Forbidden`**:
  - **`key_missing`**: The `key` query parameter was not provided.
  - **`key_invalid`**: The provided API key is invalid or has been deleted.
  - **`key_restricted`**: The request originated from an origin, user-agent, or IP address that is not allowed under your API key's security restrictions.
- **`429 Too Many Requests`**: You have exceeded the rate limit or the monthly request quota associated with your billing plan.
- **`500 Internal Server Error`**: An unexpected error occurred on MapTiler's servers.
