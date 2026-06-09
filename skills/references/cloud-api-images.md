# Images API

The MapTiler **Images API** provides access to metadata and individual XYZ tiles for hosted images.

URL: `https://docs.maptiler.com/cloud/api/images/`

## Endpoints

### 1. ImageJSON
`GET https://api.maptiler.com/images/{imageId}/image.json`
- **Description:** JSON describing the metadata of the image. Can be used with MapTiler SDK to display the image.
- **Path Parameters:**
  - `imageId` (string, required) - Identifier of the image.

### 2. XYZ tiles
`GET https://api.maptiler.com/images/{imageId}/{z}/{x}/{y}`
- **Description:** The individual tiles. Can be used with various libraries to display the image. Note: It's better to use the ImageJSON endpoint with MapTiler SDK rather than using the tile URL directly.
- **Path Parameters:**
  - `imageId` (string, required) - Identifier of the image.
  - `z` (integer, required) - Zoom level.
  - `x` (integer, required) - X coordinate.
  - `y` (integer, required) - Y coordinate.

---

## Query Parameters

No specific query parameters other than the required MapTiler API key (`?key=YOUR_MAPTILER_API_KEY`).

---

## Response Formats

### 1. ImageJSON Response (200 OK)
Returns an `ImageJSON` object containing metadata.

```json
{
  "id": "my-image-id",
  "description": "Optional description",
  "attribution": "Optional attribution",
  "width": 2048,
  "height": 1024,
  "minzoom": 0,
  "maxzoom": 5,
  "tileSize": 256
}
```

#### ImageJSON Properties
- **`width`** (integer, required): Image width in pixels.
- **`height`** (integer, required): Image height in pixels.
- **`minzoom`** (integer, required): Minimum available zoom level.
- **`maxzoom`** (integer, required): Maximum available zoom level.
- **`tileSize`** (integer, required): Tile size in pixels.
- **`id`** (string, optional): Identifier of the image.
- **`description`** (string, optional): Description of the image.
- **`attribution`** (string, optional): Attribution for the image.

### 2. XYZ Tiles Response
- **`200 OK`**: Returns the image tile content.
- **`204 No Content`**: Tile not present -- presumed empty.
- **`400 Bad Request`**: Out of bounds.
- **`403 Forbidden`**: Invalid, missing, or restricted API key.
- **`404 Not Found`**: Image or tile not found.
