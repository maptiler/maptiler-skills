# Coordinates API

The MapTiler **Coordinates API** allows you to search for coordinate systems and transform coordinates between different reference systems.

URL: `https://docs.maptiler.com/cloud/api/coordinates/`

## Endpoints

### 1. Search coordinate systems
`GET https://api.maptiler.com/coordinates/search/{query}.json`
- **Description:** Search the catalog of coordinate reference systems (CRS), datums, operations, and units.
- **Path Parameters:**
  - `query` (string, required): Query string used to search the catalog. It accepts plain terms (such as locations) and `key:value` pairs for filtering.

#### Supported Filter Keys & Values:
- **`kind`**
  - `*` (All kinds)
  - `CRS` (All coordinate reference systems - default)
    - `CRS-PROJCRS` (Projected)
    - `CRS-GEOGCRS` (Geodetic)
    - `CRS-GEOG3DCRS` (Geodetic 3D)
    - `CRS-GCENCRS` (Geocentric)
    - `CRS-VERTCRS` (Vertical)
    - `CRS-ENGCRS` (Engineering)
    - `CRS-COMPOUNDCRS` (Compound)
    - `CRS-DRVDCRS` (Derived)
  - `COORDOP` (All operations)
    - `COORDOP-COPTRAN` (Transformations)
    - `COORDOP-COPCONO` (Compound operations)
    - `COORDOP-POIMOTO` (Point motion)
    - `COORDOP-COPCON` (Conversions)
  - `DATUM` (All datums)
  - `ELLIPSOID` (Ellipsoid)
  - `PRIMEM` (Prime meridian)
  - `METHOD` (Method / Projection)
  - `CS` (Coordinate systems)
  - `AXIS` (Axis)
  - `AREA` (Area)
  - `UNIT` (Unit)
- **`code`**: Full code of the resource (e.g., `code:4326`).
- **`trans`**: Code of the transformation.
- **`deprecated`**: `0` (active only - default), `1` (deprecated only), `*` (both).

#### Query Parameters
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `limit` | integer | `10` | Maximum number of results returned (1-50). |
| `offset` | integer | `0` | Starting position of returned list of results. |
| `transformations` | boolean | `false` | Show detailed transformations for each CRS. |
| `exports` | boolean | `false` | Show exports in WKT and Proj4 notations. |

---

### 2. Transform coordinates
`GET https://api.maptiler.com/coordinates/transform/{coordinates}.json`
- **Description:** Transform a list of coordinates between different Coordinate Reference Systems (CRS).
- **Path Parameters:**
  - `coordinates` (string, required): List of coordinate pairs separated by `;` delimiter (Max 50 pairs). Example: `17,50;17,50,300`.

#### Query Parameters
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `s_srs` | integer | `4326` | Source CRS code. |
| `t_srs` | integer | `4326` | Target CRS code. |
| `ops` | string | | List of codes of operations separated by a `|` (pipe) operator. Example: `1623`. |

---

## Response Formats

### 1. Search Response (200 OK)
Returns a `SearchResult` object containing an array of matched items and the total count.

```json
{
  "results": [
    {
      "id": { "authority": "EPSG", "code": 4326 },
      "kind": "CRS-GEOGCRS",
      "name": "WGS 84",
      "deprecated": false,
      "accuracy": 0.0,
      "area": "World",
      "bbox": [-180, -90, 180, 90],
      "default_transformation": { "authority": "EPSG", "code": 1188 },
      "unit": "degree",
      "exports": {
        "proj4": "+proj=longlat +datum=WGS84 +no_defs",
        "wkt": "GEOGCS[\"WGS 84\",...]"
      }
    }
  ],
  "total": 1
}
```

### 2. Transform Response (200 OK)
Returns a `TransformResult` object containing the transformed coordinates (`x`, `y`, `z`).

```json
{
  "results": [
    {
      "x": 1892431.34,
      "y": 6446275.84,
      "z": 0
    }
  ],
  "transformer_selection_strategy": "auto"
}
```
*Note: `transformer_selection_strategy` indicates how transformations were selected. If no `ops` parameter is given, `auto` strategy is used (tries listed transformation, fallback to towgs84 patching, then boundcrs).*
