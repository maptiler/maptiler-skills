# Geolocation API

The MapTiler **Geolocation API** allows you to obtain information about a visitor's location based on the IP address of the incoming request.

URL: `https://docs.maptiler.com/cloud/api/geolocation/`

## Endpoints

### 1. IP Geolocation
`GET https://api.maptiler.com/geolocation/ip.json`
- **Description:** Obtain information about visitor's location based on the IP address of the incoming request.

---

## Query Parameters

The following query parameters can be appended to the API requests (along with your `?key=YOUR_MAPTILER_API_KEY`).

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `elevation` | boolean | `false` | Include elevation (in meters) in the results. |

---

## Response Format

The API returns a JSON object containing detailed geolocation information.

### Success Response (200 OK)
Returns a `GeolocationResult` object.

```json
{
  "country": "Switzerland",
  "country_code": "CH",
  "country_bounds": [5.95538, 45.818852, 10.490936, 47.809357],
  "country_languages": ["de", "fr", "it"],
  "continent": "Europe",
  "continent_code": "EU",
  "eu": false,
  "city": "Zurich",
  "latitude": 47.36667,
  "longitude": 8.55,
  "postal": "8000",
  "region": "Zurich",
  "region_code": "ZH",
  "timezone": "Europe/Zurich",
  "elevation": 433
}
```

### GeolocationResult Properties
- **`country`** (string): Name of the country.
- **`country_code`** (string): Two-letter code of the country (ISO 3166-1 alpha-2).
- **`country_bounds`** (array of numbers): Bounds of the country in WGS84 degrees `[west, south, east, north]`.
- **`country_languages`** (array of strings): Official country languages in ISO 639-1 format.
- **`continent`** (string): Name of the continent.
- **`continent_code`** (string): Two-letter code of the continent.
- **`eu`** (boolean): Indicates whether the country is part of the European Union.
- **`city`** (string): Name of the city.
- **`latitude`** (number): Latitude of the location.
- **`longitude`** (number): Longitude of the location.
- **`postal`** (string): Postal code.
- **`region`** (string): If known, the ISO 3166-2 name for the first level region.
- **`region_code`** (string): If known, the ISO 3166-2 code for the first level region.
- **`timezone`** (string): Name of the timezone (e.g., `Europe/Zurich`).
- **`elevation`** (number): Elevation of the location in meters (only included if `elevation=true`).

### Error Responses
- **`403`**: Forbidden (Invalid, missing, or restricted API key)
