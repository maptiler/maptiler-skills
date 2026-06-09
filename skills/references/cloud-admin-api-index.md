# MapTiler Service API (Admin API)

The **MapTiler Service API** gives you full access to your account including write operations. You can use it, for example, to upload/ingest new datasets, manage your tilesets, generate new API keys, or retrieve usage analytics.

Base URL: `https://service.maptiler.com/v1/`

## Authentication

**Important:** You need to authorize every request to the Service API with a **service token**. Get your service token in your MapTiler account, page [Credentials](https://cloud.maptiler.com/account/credentials/).

All requests must pass the token in the `Authorization` header:
`Authorization: Token YOUR_SERVICE_TOKEN`
*(Note: The schema specifies `Token <value>`, not `Bearer <value>` for the Service API)*.

## Sub-APIs

The Service API is divided into several sections:

- [Tilesets & Dataset Ingests](cloud-admin-api-tilesets.md)
- [API Keys](cloud-admin-api-api-keys.md)
- [Analytics](cloud-admin-api-analytics.md)

## Standard Error Codes

All of the listed endpoints might return these error responses:

- **`400` Bad Request**
- **`401` Not Authorized**
- **`403` Forbidden** (Might be returned if storage limit was exceeded)
- **`404` Not Found**
- **`410` Gone** (The requested resource is no longer available)
