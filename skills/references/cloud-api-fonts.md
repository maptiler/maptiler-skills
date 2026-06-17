# Fonts API

The MapTiler **Fonts API** generates font glyphs required for displaying vector maps.

URL: `https://docs.maptiler.com/cloud/api/fonts/`

## Endpoints

### 1. Font glyphs
`GET https://api.maptiler.com/fonts/{fontstack}/{start}-{end}.pbf`
- **Description:** Generates the glyphs (Protocol Buffers format) for the requested fonts. Used when displaying vector maps to render text labels.
- **Path Parameters:**
  - `fontstack` (string, required) - Font name, or multiple comma-separated font names.
  - `start` (integer, required) - Start of the glyph range. Must be a multiple of 256.
  - `end` (integer, required) - End of the glyph range (last glyph index).

---

## Query Parameters

All requests require your valid API key to be passed as a query parameter: `?key=YOUR_MAPTILER_API_KEY`.

---

## Response Format

### Success Response (200 OK)
Returns a Protocol Buffer binary file (`application/x-protobuf`) containing the requested font glyphs.

### Error Responses
- **`400`**: Invalid glyph range.
- **`403`**: Forbidden (Invalid, missing, or restricted API key)
