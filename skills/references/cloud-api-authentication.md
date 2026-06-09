# Authentication
URL: https://docs.maptiler.com/cloud/api/authentication/

Authentication is a way of proving someone's identity. In the case of MapTiler's online maps and services, every API request must be authenticated, so that we know it's you or your map users making the request.

For example, if you embed a MapTiler map on your website, then whenever someone visits that page, their browser sends a request to MapTiler servers to get the map. This request must be authenticated, otherwise the map won't show up on the page.

## How to authenticate?

MapTiler offers two authentication methods. Which one is best depends on your needs:

### 1. API key

An **API key** is a simple and easy-to-use authentication for client-side use such as web apps. If you want to use a map on your website or build a mobile application using MapTiler's online maps and API services, an API key is ideal.

- **How to use:** Append `?key=YOUR_API_KEY` to the end of your MapTiler API URL endpoints.
- **Reference Index:** For a complete directory of client-side APIs, see the [Cloud REST API Index](cloud-api-index.md).

### 2. Service token

A **service token** provides advanced and highly secure authentication for backend use. You'll need it in these scenarios:

- You're planning to use the Service API (Admin API). These API calls make it possible to not only read, but also modify and delete your cloud resources, so the highest security is in order.
- You're building a map application, but you don't want to use an API key. Using a service token for better security is possible, but remember! The token itself must never get exposed, so if your app's source code is public (for example on the web frontend), you'll need to do some extra work to keep the token hidden in the backend.

- **How to use:** Provide the token in the HTTP `Authorization` header as a Token (e.g., `Authorization: Token YOUR_SERVICE_TOKEN`).
- **Reference Index:** For the admin and resource management APIs, see the [MapTiler Service API (Admin API) Index](cloud-admin-api-index.md).
