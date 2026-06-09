# Elevation API

The MapTiler **Elevation API** allows you to get the elevation at given locations.

URL: `https://docs.maptiler.com/cloud/api/elevation/`

## Endpoints

### 1. Get elevation
`GET https://api.maptiler.com/elevation/{locations}.json`
- **Description:** Get the elevation at given locations. If the `unit` query parameter is omitted, elevation values are returned in meters.
- **Path Parameters:** 
  - `locations` (string, required) - List of `lng,lat` WGS 84 positions separated by `;` delimiter (Max 50 positions). Longitude values must be `> -180 < 180`. Latitudes must be `>= -85 <= 85`. Example: `17,50;-133.5,58.39`.

---

## Query Parameters

The following query parameters can be appended to the API requests (along with your `?key=YOUR_MAPTILER_API_KEY`).

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `unit` | string (`meters`, `feet`) | `meters` | Unit of the returned elevation. |

---

## Response Format

The API returns a JSON array containing elevation data for the requested locations.

### Success Response (200 OK)
Returns an array of locations with elevation format `[lng, lat, ele]`.

```json
[
  [17, 50, 364.20001220703125],
  [-133.5, 58.39, 1323.800048828125]
]
```

### Error Responses
- **`400`**: Out of bounds (e.g. coordinates outside valid ranges).
- **`403`**: Forbidden (Invalid, missing, or restricted API key)
