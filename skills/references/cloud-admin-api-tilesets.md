# Tilesets & Dataset Ingests (Service API)

Manage your tilesets and ingest new datasets into MapTiler Cloud.

Base URL: `https://service.maptiler.com/v1/`

## Tileset Endpoints

### 1. List tilesets
`GET /tiles`
- **Description:** List tilesets belonging to your account.
- **Query Parameters:**
  - `cursor` (string): Page cursor.
  - `limit` (integer): Page limit (min: 10, max: 100, default: 50).
- **Response:** `200 OK` (TilesetPage object containing `cursor` and array of `items`).

### 2. Get tileset details
`GET /tiles/{document_id}`
- **Description:** Get details of a specific tileset.
- **Path Parameters:**
  - `document_id` (uuid, required)
- **Response:** `200 OK` (Tileset object).

### 3. Change tileset metadata
`POST /tiles/{document_id}/change_metadata`
- **Description:** Change the metadata (title, description, attribution) of a tileset.
- **Path Parameters:**
  - `document_id` (uuid, required)
- **Request Body (JSON):**
  - `title` (string, required)
  - `description` (string, required)
  - `attribution` (string, required)
- **Response:** `200 OK` (Updated Tileset object).

### 4. Delete tileset
`DELETE /tiles/{document_id}`
- **Description:** Delete a specific tileset.
- **Path Parameters:**
  - `document_id` (uuid, required)
- **Response:** `200 OK` (Resource marked for deletion).

---

## Dataset Ingest Endpoints

### 1. Create a new ingest (New Dataset)
`POST /datasets/ingest`
- **Description:** Initialize an ingest for a dataset container into a new dataset.
- **Request Body (JSON):**
  - `filename` (string, required): Name of the file (max 255 bytes).
  - `size` (integer, required): Size in bytes.
  - `output` (object, optional): Specify `type` (`raster_tileset`, `raster_terrain`, `vector_features`, `vector_terrain`, `vector_tileset`, `image`). If not set, output type is determined based on the input file.
- **Response:** `200 OK` (DatasetIngest object including an `upload_url`).

### 2. Create a new ingest (Existing Tileset)
`POST /datasets/{document_id}/ingest`
- **Description:** Initialize an ingest for a dataset container into an *existing* tileset.
- **Path Parameters:**
  - `document_id` (uuid, required)
- **Request Body (JSON):** Same as above.
- **Response:** `200 OK` (DatasetIngest object).

### 3. Get dataset ingest details
`GET /datasets/ingest/{ingest_id}`
- **Description:** Check the status of an ongoing ingest.
- **Path Parameters:**
  - `ingest_id` (uuid, required)
- **Response:** `200 OK` (DatasetIngest object. Status can be `upload`, `processing`, `completed`, `canceled`, or `failed`).

### 4. Start processing
`POST /datasets/ingest/{ingest_id}/process`
- **Description:** Start processing the dataset ingest after the file has been fully uploaded to the provided `upload_url`.
- **Path Parameters:**
  - `ingest_id` (uuid, required)
- **Response:** `200 OK` (DatasetIngest object).

### 5. Cancel dataset ingest
`POST /datasets/ingest/{ingest_id}/cancel`
- **Description:** Cancel an ongoing dataset ingest.
- **Path Parameters:**
  - `ingest_id` (uuid, required)
- **Response:** `200 OK` (DatasetIngest object marked as canceled).
