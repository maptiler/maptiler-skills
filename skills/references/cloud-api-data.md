# Data API

The MapTiler **Data API** provides direct access to datasets hosted on MapTiler Cloud in GeoJSON format.

URL: `https://docs.maptiler.com/cloud/api/data/`

## Endpoints

### 1. GeoJSON Features
`GET https://api.maptiler.com/data/{dataId}/features.json`
- **Description:** Returns the dataset as GeoJSON containing the vector features.
- **Path Parameters:**
  - `dataId` (string, required) - Identifier of the dataset.

---

## Query Parameters

No specific query parameters other than the required MapTiler API key (`?key=YOUR_MAPTILER_API_KEY`).

---

## Response Format

### Success Response (200 OK)
Returns a standard `GeoJSON` FeatureCollection object containing all vector features within the requested dataset.

## Standard Error Codes

All of the listed endpoints might return these error responses:
- **`403`**: Key is missing, invalid or restricted.
- **`404`**: The item does not exist.
- **`414`**: URI Too Long. Maximum allowed length is 8192 bytes.
