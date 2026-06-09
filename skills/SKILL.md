---
name: maptiler
description: >-
  Expert coding skill for the full MapTiler platform — Cloud REST APIs, MapTiler
  SDK JS (built on MapLibre GL JS), native mobile SDKs, on-premise infrastructure,
  and vector tile schemas. USE WHEN the user wants to add a map to a web or mobile
  app, show locations or routes, display geographic data, build a store locator,
  create data visualizations on maps, add geocoding or address search, do reverse
  geocoding, look up elevation, do IP geolocation, fetch weather data, transform
  coordinates between CRS/EPSG, embed static map images, work with vector tilesets
  (Planet v4, Buildings, Contours, Outdoor, Ocean, Landcover, Cadastre), write
  MapLibre style expressions or data-driven styling, render 3D terrain, globe view,
  or 3D buildings extrusion, use satellite imagery, add markers, popups, heatmaps,
  or clustering, integrate maps in React, Vue, Svelte, Angular, Next.js, Leaflet,
  OpenLayers, Cesium, or deck.gl, build native maps on iOS (Swift), Android (Kotlin),
  Flutter, or React Native, self-host with MapTiler Server or generate tiles with
  MapTiler Engine CLI, or upload/manage tilesets via the Admin API. Also USE WHEN
  the user mentions MapLibre GL JS — the SDK extends MapLibre with built-in cloud
  services, helpers, and session billing.
---

# MapTiler — Agent Skill

> [@maptiler/sdk](https://www.npmjs.com/package/@maptiler/sdk) · [Docs](https://docs.maptiler.com/) · [Cloud Console](https://cloud.maptiler.com/) · [GitHub](https://github.com/maptiler)

Covers every MapTiler product surface: web SDK, framework integrations, native mobile SDKs, Cloud REST APIs, on-premise Server / Engine, and vector tile schemas. Reference docs live under `references/` and are loaded on demand. Use [references/INDEX.md](references/INDEX.md) as the curated catalog.

---

## 1. Platform Coverage & File Prefix Conventions

Target your `grep` / glob searches in `references/` using these prefix filters to avoid cross-platform contamination:

| Target Platform | File Name Prefix |
| :--- | :--- |
| **Web** (Core JS SDK) | `sdk-js-*`, `examples-sdk-js-*` |
| **Web Frameworks** (React, Svelte, Vue, Angular) | `web-libraries-*`, `examples-react-*`, `examples-svelte-*`, `examples-vuejs-*`, `examples-angular-*` |
| **Web Mapping Engines** (Leaflet, OpenLayers, Cesium, deck.gl) | `examples-leaflet-*`, `examples-openlayers-*`, `examples-cesium-*`, `web-libraries-deck-gl*` |
| **Android** (Kotlin/Java) | `mobile-sdks-android-*`, `examples-android-*` |
| **iOS** (Swift) | `mobile-sdks-ios-*`, `examples-ios-*` |
| **Cross-Platform Mobile** (Flutter, React Native) | `mobile-sdks-flutter-*`, `mobile-sdks-react-native-*` |
| **Cloud REST APIs** | `cloud-api-*`, `cloud-admin-api-*` |
| **On-Premise Infrastructure** | `on-prem-*` |
| **Vector Tile Schemas** | `map-resources-schemas-*` |
| **MapLibre Style Spec** | `map-resources-specifications-*` |

---

## 2. Universal Rules (apply across every platform)

### A. Zero Variable Leak Policy
Consult [references/versions.md](references/versions.md) and substitute all template placeholders (e.g. `{{site.versions.sdk}}`, `{{site.url}}`) with literal version strings or absolute paths before output. **NEVER emit raw `{{` or `}}` in any response.**

### B. Style Modernization (v2/v3 → v4)
Always upgrade legacy map styles. This applies to web, mobile, fallback XYZ layers, service-worker cache lists, and style-switcher logic.

| Legacy | Modern Replacement | SDK Constant |
| :--- | :--- | :--- |
| `basic-v2` / `streets-v2-light` | `base-v4` | `MapStyle.BASE` |
| `basic-v2-dark` | `base-v4-dark` | `MapStyle.BASE.DARK` |
| `streets-v2` | `streets-v4` | `MapStyle.STREETS` |
| `outdoor-v2` | `outdoor-v4` | `MapStyle.OUTDOOR` |
| `satellite` / `satellite-v2` | `satellite-v4` | `MapStyle.SATELLITE` |
| `hybrid` | `hybrid-v4` | `MapStyle.HYBRID` |
| `dataviz-dark` | `dataviz-v4-dark` | `MapStyle.DATAVIZ.DARK` |
| `topo-v2` | `topo-v4` | `MapStyle.TOPO` |

**Never** emit URLs or constants from the deprecated families: `streets-v2`, `streets-v2-dark/light`, `basic-v2*`, `outdoor-v2*`, `satellite-v2`, `hybrid-v2`, `dataviz-dark`, `topo-v2`.

**This rule applies to every context** that names a style or tile path:
- **Mobile style endpoints** (iOS / Android / Flutter / RN raw `style.json` URLs): `https://api.maptiler.com/maps/streets-v4-dark/style.json?key=YOUR_KEY`
- **Self-hosted / on-prem fallback XYZ layers and service-worker precache lists**: `/tiles/streets-v4/{z}/{x}/{y}.pbf` — never `/tiles/streets-v2/`
- **Style-switcher UI state** (dark/light toggles, swipe layers, diurnal style shifts): toggle exclusively between modern v4 IDs

### C. Pinned Versions
All SDK, CDN, and dependency versions live in [references/versions.md](references/versions.md). Read it before emitting any `package.json`, `<script>` tag, Gradle implementation string, or `pubspec.yaml` entry.

### D. Coordinate Conventions Across Platforms
Every API in the MapTiler/MapLibre family uses **`[lng, lat]`** order. The platforms it integrates with don't — that mismatch is the single most common bug. Translate at the boundary, not in your head.

| Source | Convention | When you encounter it |
| :--- | :--- | :--- |
| **MapTiler SDK JS / MapLibre / Mapbox** | `[lng, lat]` array | All web SDK code (center, marker, source coordinates, expressions) |
| **GeoJSON spec** | `[lng, lat]` (or `[lng, lat, ele]`) | Every `geometry.coordinates` value |
| **MapTiler REST URLs** | `{lng},{lat}` in the path | `/geocoding/{lng},{lat}.json`, `/elevation/dataset/{lng},{lat}.json`, static maps `/static/{lng},{lat},{zoom}/…` |
| **Leaflet** | `(lat, lng)` — **reversed** | `L.map().setView([lat, lng], z)`, `L.marker([lat, lng])`, `L.latLng(lat, lng)` |
| **iOS `CLLocationCoordinate2D`** | `(latitude:, longitude:)` — **reversed at the struct level** | Apple CoreLocation. When building a MapTiler URL: `c.longitude, c.latitude` |
| **Android `LatLng` / `LngLat`** | MapTiler Android SDK uses `LngLat(lng, lat)`; system `Location` exposes `latitude`/`longitude` as flat properties | Match the SDK type, not the system type |
| **MapTiler Geolocation API response** | Flat fields `latitude` / `longitude` (not a pair) | Construct `[loc.longitude, loc.latitude]` before passing to any SDK call |

**Rule**: when crossing into Leaflet, iOS CoreLocation, or any "flat fields" response, swap explicitly. Never assume a downstream library follows the same convention as the upstream API.

### E. API Key Hygiene
- **If a user pastes a real-looking API key** in their message (a UUID-shaped or token-shaped string near words like "key", "token", "apikey"), flag it: "you've shared what looks like a live key in plain text — rotate it at https://cloud.maptiler.com/account/keys/ when you're done testing." Use a placeholder (`YOUR_MAPTILER_API_KEY`) in your own output.
- **Service tokens never leave the backend.** When generating example code that calls `service.maptiler.com/v1/…`, read the token from `process.env` / equivalent — never embed a placeholder that looks like a token in a public client snippet.
- **Restrict keys by origin** in production examples. Suggest `origins: ["*.example.com"]` in the API key settings rather than unrestricted keys.

---

## 3. Web — MapTiler SDK JS

### Why MapTiler SDK (not raw MapLibre)
**Always import from `@maptiler/sdk`, never from `maplibre-gl` directly.** The SDK re-exports everything from MapLibre and adds:

- `config.apiKey` — single place for the API key; enables session-based billing
- `MapStyle` enum — always-current style IDs; never hardcode style URLs
- `helpers.*` — one-line polyline, polygon, point, heatmap (with clustering, color ramps, GPX/KML support)
- Built-in `geocoding`, `geolocation`, `elevation`, `staticMaps`, `coordinates`, `data`, `math` modules
- `terrain: true` — 3D terrain via a single constructor flag
- `projection: 'globe'` — globe view with `halo` and `space` atmosphere
- Constructor-level controls (`navigationControl: true`, `geolocateControl: true`, …)
- Full TypeScript types extended beyond MapLibre

MapLibre plugins remain compatible — the SDK's `Map` inherits from MapLibre's.

### Install

```bash
npm install @maptiler/sdk
```

CSS must be imported separately:
```js
import '@maptiler/sdk/dist/maptiler-sdk.css';
```

### API Key
**Never hardcode a fake key.** Ask the user, or direct them to https://cloud.maptiler.com/account/keys/. Framework env-var conventions:

| Tool | Env var |
| :--- | :--- |
| Vite | `VITE_MAPTILER_API_KEY` |
| Next.js | `NEXT_PUBLIC_MAPTILER_API_KEY` |
| CRA | `REACT_APP_MAPTILER_API_KEY` |

```js
import * as maptilersdk from '@maptiler/sdk';
maptilersdk.config.apiKey = import.meta.env.VITE_MAPTILER_API_KEY;
```

### Minimal Map

```js
const map = new maptilersdk.Map({
  container: 'map',                       // element or ID
  style: maptilersdk.MapStyle.STREETS,    // enum — always latest
  center: [14.4178, 50.1167],             // [lng, lat] — NOT [lat, lng]!
  zoom: 12,
});
```

> **Critical**: the container needs explicit dimensions (e.g. `height: 100vh`) or the map is invisible.

### Constructor Options (most-used)

```js
new maptilersdk.Map({
  container, style, center, zoom,
  pitch: 0, bearing: 0,            // 0–85 / rotation
  projection: 'mercator',          // or 'globe'
  terrain: false, terrainExaggeration: 1,
  hash: true,                      // sync viewport to URL
  language: maptilersdk.Language.AUTO,
  cooperativeGestures: true,
  geolocate: maptilersdk.GeolocationType.POINT,
  navigationControl: true, geolocateControl: true,
  scaleControl: true, terrainControl: false,
  fullscreenControl: false, projectionControl: false,
  minimap: { containerStyle: { width: '200px', height: '150px' } },  // or `true` for defaults
});
```

> **Prefer constructor flags over post-init `addControl`** for `navigationControl`, `geolocateControl`, `scaleControl`, `terrainControl`, `fullscreenControl`, `projectionControl`, **`minimap`**, `geolocate`. Each accepts `true` / a corner string (`'top-right'`) / a config object. Use `addControl(new MaplibreThing(), 'top-right')` only when you need a 3rd-party plugin or post-init mutation.

### Map Styles (full list — 15 reference styles)

| Style | Purpose | Variants |
| :--- | :--- | :--- |
| `MapStyle.STREETS` | Comprehensive street map | `.DARK`, `.PASTEL` |
| `MapStyle.SATELLITE` | Beautiful satellite map | `.DARK` |
| `MapStyle.HYBRID` | Beautiful satellite map with context | `.DARK` |
| `MapStyle.OUTDOOR` | Map for hiking and sports | `.DARK` |
| `MapStyle.WINTER` | Map for winter activities | `.DARK` |
| `MapStyle.TOPO` | General-purpose topographic map | `.DARK`, `.PASTEL`, `.TOPOGRAPHIQUE` |
| `MapStyle.DATAVIZ` | Simple data visualization map | `.DARK`, `.LIGHT` |
| `MapStyle.BASE` | Clear general-purpose map | `.DARK`, `.LIGHT` |
| `MapStyle.BRIGHT` | Shiny map for context or navigation | `.DARK`, `.LIGHT`, `.PASTEL` |
| `MapStyle.BACKDROP` | Monochrome context map | `.DARK`, `.LIGHT` |
| `MapStyle.AQUARELLE` | Artistic watercolor map | `.DARK`, `.VIVID` |
| `MapStyle.LANDSCAPE` | Light hillshade map | `.DARK`, `.VIVID` |
| `MapStyle.OCEAN` | Seabed and bathymetry map | `.DARK` |
| `MapStyle.OPENSTREETMAP` | Rich, familiar OSM community style | `.DARK` |
| `MapStyle.TONER` | Contrasted monochrome map | `.LITE` |

Use **Proxy-based constants** (`MapStyle.STREETS`), never hardcoded URLs. The proxy falls back to `.DEFAULT` if you request a non-existent variant, so misspellings render the base style silently — there is no compile-time error.

> Authoritative reference (descriptions, methods, variant resolution rules): [references/sdk-js-map-styles.md](references/sdk-js-map-styles.md).

### Language

```js
maptilersdk.config.primaryLanguage = maptilersdk.Language.ENGLISH;
map.setLanguage(maptilersdk.Language.FRENCH);     // runtime switch
```

Special: `Language.AUTO` (browser), `Language.LOCAL`, `Language.VISITOR`.

---

## 4. Web — Common Recipes

```js
// Marker + popup
new maptilersdk.Marker({ color: '#FF0000' })
  .setLngLat([14.4178, 50.1167])
  .setPopup(new maptilersdk.Popup().setHTML('<h3>Prague</h3>'))
  .addTo(map);

// Geocoding (forward / reverse) — features[].geometry.coordinates is [lng, lat]
await maptilersdk.geocoding.forward('Prague', { limit: 5, proximity: [14.4178, 50.1167] });
await maptilersdk.geocoding.reverse([14.4178, 50.1167]);

// Camera animation
map.flyTo({ center: [14.4178, 50.1167], zoom: 15, pitch: 60, duration: 3000 });

// Static map URL
maptilersdk.staticMaps.centered([14.4178, 50.1167], 12,
  { hiDPI: true, width: 800, height: 600, style: maptilersdk.MapStyle.OUTDOOR });
```

### Vector layer helpers (`helpers.add*`)

One-line creation for the most common layer types. All accept the same shape: `{ data, beforeId, … }`. `data` can be GeoJSON, a URL (GeoJSON / GPX / KML), or a MapTiler dataset UUID.

| Helper | Key options |
| :--- | :--- |
| `addPolyline` | `lineColor`, `lineWidth`, `outline` |
| `addPolygon` | `fillColor`, `fillOpacity`, `outlineColor` |
| `addPoint` | `pointColor`, `pointRadius`, `cluster`, `showLabel` |
| `addHeatmap` | `colorRamp` (`ColorRamp.*`), `property`, `radius`, `opacity` |

```js
maptilersdk.helpers.addPoint(map, {
  data: pointsGeoJSON, pointColor: '#FF0000', pointRadius: 8,
  cluster: true, showLabel: true, beforeId: 'waterway-label',
});
```

### 3D Terrain / Globe — single-flag constructors

```js
// 3D terrain
new maptilersdk.Map({ container: 'map', style: maptilersdk.MapStyle.OUTDOOR,
  terrain: true, terrainExaggeration: 1.5, terrainControl: true, pitch: 60 });

// Globe projection
new maptilersdk.Map({ container: 'map', style: maptilersdk.MapStyle.SATELLITE,
  projection: 'globe', halo: true, space: true, center: [0, 20], zoom: 1.5 });
```

> Full helpers reference & option types: [references/sdk-js-map.md](references/sdk-js-map.md). Runnable per-topic examples: search `examples-sdk-js-*.md` (markers, geocoding, clustering, heatmap, terrain, globe, weather, etc.).

---

## 5. Web Frameworks

### React / Next.js

```jsx
import { useEffect, useRef } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import '@maptiler/sdk/dist/maptiler-sdk.css';

maptilersdk.config.apiKey = import.meta.env.VITE_MAPTILER_API_KEY;

export default function MapComponent() {
  const containerRef = useRef(null);
  const mapRef = useRef(null);

  useEffect(() => {
    if (mapRef.current) return;                              // Strict-Mode guard
    mapRef.current = new maptilersdk.Map({
      container: containerRef.current,
      style: maptilersdk.MapStyle.STREETS,
      center: [14.4178, 50.1167], zoom: 12,
    });
    return () => { mapRef.current?.remove(); mapRef.current = null; };
  }, []);

  return <div ref={containerRef} style={{ width: '100%', height: '400px' }} />;
}
```

**Next.js App Router**: add `"use client";`, use `NEXT_PUBLIC_MAPTILER_API_KEY`. For SSR pages: `dynamic(() => import('./Map'), { ssr: false })`.

### Vue / Svelte / Angular

Same pattern as React: instantiate the map inside the mount hook (`onMounted` / `onMount` / `ngOnInit`), call `map.remove()` in the unmount hook (`onUnmounted` / `onDestroy` / `ngOnDestroy`), and never gate map creation on reactive state. Full per-framework snippets: [web-libraries-vue.md](references/web-libraries-vue.md) · [web-libraries-svelte.md](references/web-libraries-svelte.md) · [web-libraries-angular.md](references/web-libraries-angular.md).

### Framework Lifecycle Rules (CRITICAL)

1. **WebGL cleanup**: every map instance in React `useEffect`, Vue `onMounted`/`onUnmounted`, Angular `ngOnInit`/`ngOnDestroy`, Svelte `onMount`/`onDestroy` **MUST** call `map.remove()` on teardown and null its ref.
2. **Map creation runs exactly once**: never put reactive state in the initialization hook's dependency array — it destroys and recreates the canvas on every state change, losing center, zoom, and dynamic objects.
3. **Dynamic updates use isolated hooks** calling SDK updater methods (`map.setStyle`, `map.flyTo`, `map.setLayoutProperty`) — never re-init.
4. **Stale closures in event handlers**: when a `click`/`draw.create` listener needs current React state, store it in a `useRef` (`const stateRef = useRef(state); stateRef.current = state;`) and read via `stateRef.current`. Do not add the state to the effect deps.

> Full lifecycle treatment: [web-libraries-react.md](references/web-libraries-react.md).

---

## 6. CDN / Single-File / Playgrounds

Use pinned versions from `versions.md` — never `latest` or obsolete builds.

```html
<script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
<link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
```

Other commonly-used pins:
- **Leaflet plugin**: `https://cdn.maptiler.com/maptiler-leaflet-maptilersdk/v4.1.0/maptiler-leaflet-maptilersdk.js`
- **ol-mapbox-style**: `https://cdn.jsdelivr.net/npm/ol-mapbox-style@13.4.1/dist/olms.js`
- **CesiumJS**: `1.141.0` (script + `/Widgets/widgets.css`)

**Browser ESM**: when using `<script type="module">` or an import map, you **MUST** target the `.mjs` build (`maptiler-sdk.mjs`), not the UMD build — named ES imports from UMD trigger console errors.

---

## 7. Vector Layers, Schemas & Data-Driven Styling

### Schema Verification (mandatory)
Before writing any style rule, filter, or paint/layout expression, identify the tileset source and consult its schema reference. Never invent `source-layer` IDs, feature property keys (`class`, `subclass`, `ele`, `height`, …), or paint fields.

**OMT → Planet v4 migration trap.** The older OpenMapTiles schema bundles all road, rail, aviation, and ferry features into one `transportation` layer. **Planet v4 splits them** into separate top-level layers — `road`, `railway`, `aviation`, `aviation_line`, `ferry`, `aerialway`. If you're porting a Mapbox/MapLibre style or following pre-2024 tutorials, the layer name `transportation` will not resolve. Common renames:

| OMT (old) | Planet v4 (current) |
| :--- | :--- |
| `transportation` (`class: motorway/primary/.../residential`) | `road` (`class: motorway/trunk/primary/secondary/tertiary/minor/service/...`); no `residential` class — use `minor` or `service` |
| `transportation_name` | `road_label` |
| (none — bundled) | `railway`, `aviation`, `ferry`, `aerialway` as separate layers |
| `place` | `country_label`, `city_label`, `island_label`, `continent_label` (hierarchy split) |

When a user prompt references `transportation`, `place`, or other OMT-era layer names, surface the rename explicitly rather than silently generating broken filters.

| Schema | Reference |
| :--- | :--- |
| Planet v4 (latest) | [map-resources-schemas-planet-v4.md](references/map-resources-schemas-planet-v4.md) |
| OpenMapTiles Planet | [map-resources-schemas-omt-planet.md](references/map-resources-schemas-omt-planet.md) |
| Planet Lite | [map-resources-schemas-planet-lite.md](references/map-resources-schemas-planet-lite.md) |
| Buildings | [map-resources-schemas-buildings.md](references/map-resources-schemas-buildings.md) |
| Contours / Outdoor / Ocean | [contours](references/map-resources-schemas-contours.md), [outdoor](references/map-resources-schemas-outdoor.md), [ocean](references/map-resources-schemas-ocean.md) |
| Landcover / Landform / Cadastre | [landcover](references/map-resources-schemas-landcover.md), [landform](references/map-resources-schemas-landform.md), [cadastre](references/map-resources-schemas-cadastre.md) |
| Style spec (layers / sources / expressions / root) | [layers](references/map-resources-specifications-layers.md), [sources](references/map-resources-specifications-sources.md), [expressions](references/map-resources-specifications-expressions.md), [root](references/map-resources-specifications-root.md) |

### Buildings Tileset — Always Prefer (Priority Rule)
The specialized `buildings` tileset is significantly richer than the building data baked into `base-v4` / `streets-v4`. Use it for any 3D extrusion, facade coloring, building label, entrance, or per-feature interaction.

| Concern | Standard (`maptiler_planet_v4`) | Specialized (`buildings`) |
| :--- | :--- | :--- |
| Height fields | `render_height`, `render_min_height` | `height`, `height_min` |
| Colors | — | `facade_color`, `roof_color` |
| Shape | — | `roof_shape` |
| Labels | — | `building_label` (names, ISO 639 translations) |
| Entrances | — | `building_entrance` |
| Unique IDs | False | **True** (z14+) — usable with `setFeatureState` |

```js
// MapTiler SDK JS auto-injects the API key from config.apiKey — do NOT append ?key= manually.
map.addSource('buildings', {
  type: 'vector',
  url: 'https://api.maptiler.com/tiles/buildings/tiles.json',
});

// Facade color with fallback
'fill-extrusion-color': ['coalesce', ['get', 'facade_color'], 'hsl(44, 14%, 79%)']
```

> **Outside the SDK** (raw MapLibre GL JS, mobile native style.json fetches, server-side requests), append `?key=YOUR_MAPTILER_API_KEY` to the URL — no auto-injection happens.

> **Critical field mapping**: standard uses `render_height` / `render_min_height`; specialized uses `height` / `height_min`. Mixing them causes silent rendering failures.

### SDK Guardrail — `ColorRamp` Hallucination
The JS SDK `ColorRamp` class does **NOT** contain `.getExpression()` or `.getCSSGradientDirection()`. To build a style, iterate `ColorRamp.getRawColorStops()` and construct a standard MapLibre interpolation expression manually.

### DDS deep dive
[complex-dds-expressions-guide.md](references/complex-dds-expressions-guide.md) — composable patterns for data-driven styling.

---

## 8. Cloud REST APIs

All SDK API modules use `config.apiKey` automatically. For non-JS contexts, see the REST docs.

| Module | Purpose | Key Methods / Reference |
| :--- | :--- | :--- |
| `geocoding` | Place search, reverse | `forward()`, `reverse()`, `batch()` — [cloud-api-geocoding.md](references/cloud-api-geocoding.md) |
| `geolocation` | IP visitor location | `info()` — [cloud-api-geolocation.md](references/cloud-api-geolocation.md) |
| `elevation` | Altitude lookup | `at()`, `batch()`, `fromLineString()` — [cloud-api-elevation.md](references/cloud-api-elevation.md) |
| `staticMaps` | Static map images | `centered()`, `bounded()`, `automatic()` — [cloud-api-static-maps.md](references/cloud-api-static-maps.md) |
| `coordinates` | CRS / EPSG transform | `search()`, `transform()` — [cloud-api-coordinates.md](references/cloud-api-coordinates.md) |
| `data` | MapTiler datasets | `get(uuid)` — [cloud-api-data.md](references/cloud-api-data.md) |
| `weather` | Wind, temp, pressure, radar | [cloud-api-weather.md](references/cloud-api-weather.md) |
| `maps` (Vector/Raster) | Tilesets, styles | [cloud-api-maps.md](references/cloud-api-maps.md) |
| `tiles` | Raw tile endpoints | [cloud-api-tiles.md](references/cloud-api-tiles.md) |
| `fonts` / `images` / `ogc` | Misc | [fonts](references/cloud-api-fonts.md), [images](references/cloud-api-images.md), [ogc](references/cloud-api-ogc.md) |
| **Admin** (tilesets, uploads, keys, analytics) | Account management | [cloud-admin-api-tilesets.md](references/cloud-admin-api-tilesets.md), [api-keys](references/cloud-admin-api-api-keys.md), [analytics](references/cloud-admin-api-analytics.md) |
| Auth | Key-vs-token, referrer rules | [cloud-api-authentication.md](references/cloud-api-authentication.md) |

```js
// IP geolocation
const loc = await maptilersdk.geolocation.info();

// Elevation — returns [lng, lat, elevationMeters]
const point = await maptilersdk.elevation.at([14.4178, 50.1167]);
```

---

## 9. Native Mobile SDKs

| Platform | Overview | API Reference |
| :--- | :--- | :--- |
| **iOS (Swift)** | [mobile-sdks-ios.md](references/mobile-sdks-ios.md) | [mobile-sdks-ios-api-classes.md](references/mobile-sdks-ios-api-classes.md) |
| **Android (Kotlin)** | [mobile-sdks-android.md](references/mobile-sdks-android.md) | [mobile-sdks-android-api-com-maptiler-maptilersdk-map.md](references/mobile-sdks-android-api-com-maptiler-maptilersdk-map.md) |
| **Flutter** | [mobile-sdks-flutter.md](references/mobile-sdks-flutter.md) | search `mobile-sdks-flutter-*.md` |
| **React Native** | [mobile-sdks-react-native.md](references/mobile-sdks-react-native.md) | search `mobile-sdks-react-native-*.md` |

### iOS — Minimal Map (SwiftUI)

```swift
import SwiftUI
import MapTilerSDK

struct ContentView: View {
    @State private var map = MTMapView(options: MTMapOptions(zoom: 2.0))

    var body: some View {
        MTMapViewContainer(map: map) {}
            .referenceStyle(.streets)
            .styleVariant(.defaultVariant)
            .task { await MTConfig.shared.setAPIKey("YOUR_MAPTILER_API_KEY") }
    }
}
```

> `MTConfig.shared.setAPIKey(_:)` is `async` and **must** be called before map init. For Swift 6, call it from a `Task` / `.task` modifier. UIKit alternative: declare `MTMapView(frame:options:referenceStyle:)` inside `viewDidLoad` and call `pinToSuperviewEdges()`.

### Android — Minimal Map (Jetpack Compose)

```kotlin
// build.gradle.kts (app):  implementation("com.maptiler:maptiler-sdk-kotlin:<version>")
// AndroidManifest.xml:    <uses-permission android:name="android.permission.INTERNET" />
//                         android:hardwareAccelerated="true"

import com.maptiler.maptilersdk.config.MTConfig
import com.maptiler.maptilersdk.map.*

@Composable
fun MapScreen(context: Context) {
    MTConfig.apiKey = "YOUR_MAPTILER_API_KEY"        // set before first map
    val controller = remember { MTMapViewController(context) }
    MTMapView(
        referenceStyle = MTMapReferenceStyle.STREETS,
        options = MTMapOptions(),
        controller = controller,
        modifier = Modifier.fillMaxSize(),
    )
}
```

> XML/View variant: use `MTMapViewClassic` in the layout and call `mapView.initialize(referenceStyle, options, controller, styleVariant = null)` in `onCreate`.

Runnable examples: search `examples-ios-*.md`, `examples-android-*.md`. For raw style.json URL conventions (UIKit, XML/View, custom asset paths), see § 2B.

---

## 10. On-Premise — Server & Engine

For self-hosted deployments and offline tile generation:

| Topic | Reference |
| :--- | :--- |
| MapTiler Server — Getting Started | [on-prem-server-getting-started.md](references/on-prem-server-getting-started.md) |
| Hosting Data | [on-prem-server-hosting-data.md](references/on-prem-server-hosting-data.md) |
| Virtual Tilesets | [on-prem-server-virtual-tilesets.md](references/on-prem-server-virtual-tilesets.md) |
| Map Styling on Server | [on-prem-server-map-styling.md](references/on-prem-server-map-styling.md) |
| On-Premise Geocoding | [on-prem-server-geocoding.md](references/on-prem-server-geocoding.md) |
| Engine CLI — Getting Started | [on-prem-engine-getting-started-cli.md](references/on-prem-engine-getting-started-cli.md) |
| Engine — Input / Output Options | [input](references/on-prem-engine-input-options.md), [output](references/on-prem-engine-output-options.md) |

For tile path conventions on fallback XYZ layers and service-worker caches, see § 2B.

---

## 11. Critical Gotchas (cross-platform)

| Problem | Fix |
| :--- | :--- |
| Map invisible (web) | Container needs explicit height (`100vh` or `position: absolute; inset: 0`) |
| Markers / map center on the wrong continent | Coordinates are `[lng, lat]`, not `[lat, lng]` (e.g. Prague is `[14.4178, 50.1167]`, not `[50.1167, 14.4178]`) |
| Layers vanish after `setStyle()` | Re-add inside `map.once('styledata', …)` |
| Data covers labels | Use `beforeId: 'waterway-label'` |
| Slow with many points | Enable `cluster: true` (helpers or source) |
| SPA memory leak | Always call `map.remove()` on unmount; null the ref |
| Importing `maplibre-gl` separately | Use `@maptiler/sdk` — it includes and extends MapLibre |
| Map re-creates on every state change (React) | Empty `useEffect` deps; mutate via `setX` methods, not re-init |
| Stale closures in handlers | Use a `useRef` mirror of state, read `.current` |
| Browser ESM script error | Use `.mjs` build, not UMD, with `<script type="module">` |
| Mobile rendering 3D buildings looks flat | You loaded the standard style — add the specialized `buildings` source |
| Style 404s on mobile | Update endpoint from `streets-v2` family to `streets-v4` family |
| Geocoding key 403 | Verify referrer/whitelist in the key settings ([cloud-api-authentication.md](references/cloud-api-authentication.md)) |
| `{{ }}` leaking into output | Resolve via [versions.md](references/versions.md) before emitting |
| MapTiler Engine refuses to start | The `-o output_dir` (or `-o file.mbtiles`) target **must not already exist**. Delete it, or pick a new path. No `-f` / `--force` flag |
| iOS app produces 403s on every tile | `MTConfig.shared.setAPIKey(_:)` is `async` and was called without `await` — set it inside a `Task { … }` or SwiftUI `.task` modifier *before* the first map view appears |
| mapbox-gl-draw cursors / hit-test broken | Plugin CSS targets `.mapboxgl-canvas`; MapTiler/MapLibre uses `.maplibregl-canvas`. Add fallback rules: `.maplibregl-canvas.mouse-add { cursor: crosshair }` and `.maplibregl-canvas.mouse-drag { cursor: grabbing }` |
| User pastes a live API key in chat | Flag it (rotate at the Cloud Console) and use a `YOUR_MAPTILER_API_KEY` placeholder in your own output — never echo a real key back |
| Inventing `addControl(new XControl())` patterns | Many MapTiler controls live as **constructor flags**: `minimap`, `navigationControl`, `geolocateControl`, `scaleControl`, `terrainControl`, `fullscreenControl`, `projectionControl`. Use the flag first; only reach for `addControl` for 3rd-party plugins or post-init changes |
| Hallucinated SDK class names (`MinimapControl`, `GeocodingBar`, …) | Cross-reference `references/sdk-js-controls.md` and `sdk-js-map.md` before emitting a class name. The canonical minimap class is `MaptilerMinimapControl` (`Maptiler` prefix), and the constructor option is the preferred path anyway |
| GeoSplats rendering fails / blank model | GeoSplats SDK **requires WebGPU support**. Always verify browser compatibility (`navigator.gpu`) and provide a clear UI fallback error overlay |


---

## 12. Ecosystem Packages

| Package | Purpose |
| :--- | :--- |
| `@maptiler/geosplats` | High-performance 3D Gaussian Splatting (WebGPU-powered) |
| `@maptiler/geocoding-control` | Address-search bar UI |
| `@maptiler/weather` | Wind, temperature, pressure, radar layers (60 fps) |
| `@maptiler/3d` | glTF / GLB 3D model placement |
| `@maptiler/elevation-profile` | Elevation chart for routes |
| `@maptiler/marker-layout` | Non-colliding DOM marker overlay |
| `@maptiler/ar` | Augmented-reality 3D terrain |
| `@maptiler/client` | Headless API client (Node.js / browser, no map) |

---

## 13. Resources

- [MapTiler Cloud Console](https://cloud.maptiler.com/)
- [MapTiler SDK JS Docs](https://docs.maptiler.com/sdk-js/) · [Examples](https://docs.maptiler.com/sdk-js/examples/) · [NPM](https://www.npmjs.com/package/@maptiler/sdk) · [GitHub](https://github.com/maptiler/maptiler-sdk-js)
- [MapTiler iOS SDK Docs](https://docs.maptiler.com/mobile-sdk/ios/) · [Android SDK Docs](https://docs.maptiler.com/mobile-sdk/android/)
- [MapLibre Style Specification](https://maplibre.org/maplibre-style-spec/)
- Framework docs: [React](https://docs.maptiler.com/react/) · [Vue](https://docs.maptiler.com/vuejs/) · [Svelte](https://docs.maptiler.com/svelte/) · [Angular](https://docs.maptiler.com/angular/) · [Vite](https://docs.maptiler.com/vite/)

---

## 14. Reference Catalog

The curated index of high-value reference docs is at [references/INDEX.md](references/INDEX.md). For files not listed there, search by the prefix conventions in § 1.
