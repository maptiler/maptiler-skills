# Analytics (Service API)

Retrieve API usage analytics for your MapTiler Cloud account.

Base URL: `https://service.maptiler.com/v1/`

## Endpoints

### 1. Get usage analytics timeline
`GET /analytics/api_usage/timeline`
- **Description:** Retrieve a timeline of API usage over a specified period.

#### Query Parameters
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `period` | string | | **Required.** Allowed values: `current_billing_period`, `last_billing_period`, `past_30_days`, `past_90_days`, `past_12_billing_periods`, `past_12_months`, `all`. Note: For classifiers `api_keys` and `service_credentials`, only daily periods are supported (first 4 options). |
| `classifier` | string | | **Required.** Classifies datasets. Allowed values: `services`, `api_keys`, `service_credentials`. |
| `group` | string | | Group ID filter. **Mandatory for CSV format.** Allowed values: `request`, `session`, `export`. |
| `format` | string | `json` | Response media type. Allowed values: `json`, `csv`. |

#### Responses
- **`200 OK`**: Returns a `TimelineResponse` object (in JSON or CSV).
  - JSON Schema includes `since`, `until`, `datasets` (containing `group_id`, `item_id`, `data`, and `estimated_data`), and `legend` arrays.
  - CSV Format: Header row is `date,item,count`.
- **`400 Bad Request`**:
  - `period_not_found`: Selected time period does not exist.
  - `account_over_limit`: Account currently has too many entities.
  - `response_too_large`: There were too much data in the result.

---

### 2. Get top usage analytics
`GET /analytics/api_usage/top`
- **Description:** Retrieve top usage analytics aggregated over a specified period.

#### Query Parameters
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `period` | string | | **Required.** Allowed values: `current_billing_period`, `last_billing_period`, `past_30_days`, `past_90_days`, `past_12_billing_periods`, `past_12_months`, `all`. |
| `classifier` | string | | **Required.** Classifies datasets. Allowed values: `services`, `api_keys`, `service_credentials`. |
| `group` | string | | Group ID filter. **Mandatory for CSV format.** Allowed values: `request`, `session`, `export`. |
| `format` | string | `json` | Response media type. Allowed values: `json`, `csv`. |
| `limit` | integer| `10` | Number of top items within response group. |

#### Responses
- **`200 OK`**: Returns a `TopResponse` object (in JSON or CSV).
  - JSON Schema includes `since`, `until`, `datasets` (containing `group_id`, `data`), and `legend` arrays.
  - CSV Format: Header row is `item,count`.
- **`400 Bad Request`**:
  - `period_not_found`: Selected time period does not exist.
