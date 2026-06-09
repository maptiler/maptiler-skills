# API Keys (Service API)

Manage your MapTiler API keys programmatically.

Base URL: `https://service.maptiler.com/v1/`

## Endpoints

### 1. List API keys
`GET /api_keys`
- **Description:** List all API keys belonging to the account.
- **Query Parameters:**
  - `cursor` (string): Page cursor.
  - `limit` (integer): Page limit (min: 10, max: 100, default: 50).
- **Response:** `200 OK`
  Returns an `APIKeyPage` object containing:
  - `cursor` (string): Next page cursor.
  - `total_count` (integer): Total number of keys.
  - `items` (array): Array of `APIKey` objects.

### 2. Create new key
`POST /api_keys`
- **Description:** Generate a new API key.
- **Request Body (JSON):** `APIKeySettings` object.
  - `name` (string, optional): Will be generated automatically unless provided explicitly.
  - `description` (string, optional)
  - `user_agent` (string, optional): Processes only requests where the `User-Agent` header contains this exact substring. Leave empty to allow any user-agent.
  - `origins` (array of strings, optional): Which HTTP origins are allowed (e.g., `["mydomain.com", "*.mydomain.com"]`). Use `?` to explicitly allow unknown origins.
- **Response:** `200 OK` (Returns the newly created `APIKey` object).

### 3. Get key details
`GET /api_keys/{key_id}`
- **Description:** Get details of a specific API key.
- **Path Parameters:**
  - `key_id` (string, required): Identifier of API Key (uuid).
- **Response:** `200 OK` (Returns the `APIKey` object).

### 4. Update key settings
`POST /api_keys/{key_id}/change_settings`
- **Description:** Update the settings of a specific API key.
- **Path Parameters:**
  - `key_id` (string, required): Identifier of API Key (uuid).
- **Request Body (JSON):** `APIKeySettings` object (same structure as Create new key).
- **Response:** `200 OK` (Returns the updated `APIKey` object).

### 5. Delete key
`DELETE /api_keys/{key_id}`
- **Description:** Delete a specific API key.
- **Path Parameters:**
  - `key_id` (string, required): Identifier of API Key (uuid).
- **Response:** `200 OK` (Successfully deleted).

---

## Response Schemas

### APIKey Object
When returned, the APIKey object contains the following properties:
- **`id`** (uuid)
- **`token`** (string): The actual API key string used for authentication.
- **`name`** (string)
- **`description`** (string, nullable)
- **`user_agent`** (string, nullable)
- **`origins`** (array of strings)
- **`created`** (date-time)
- **`changed`** (date-time)
