# MapTiler Library Versions

This file contains the current official versions of all MapTiler SDKs, libraries, and external dependencies, extracted from the documentation's master configuration. Use these versions when generating CDN links, `package.json` dependencies, or Gradle implementation strings.

| Variable Name in Templates | Library Name | Version |
| :--- | :--- | :--- |
| `{{site.versions.sdk}}` | **MapTiler SDK JS** | `v4.1.0` |
| `{{site.versions.client}}` | **MapTiler Client JS** | `v3.0.2` |
| `{{site.versions.geocoding-control}}` | **Geocoding Control** | `v3.0.0` |
| `{{site.versions.marker-layout}}` | **Marker Layout** | `v2.0.1` |
| `{{site.versions.elevation-profile}}` | **Elevation Profile** | `v3.0.1` |
| `{{site.versions.leaflet-maptilersdk}}` | **Leaflet MapTiler SDK** | `v4.1.0` |
| `{{site.versions.ar-control}}` | **AR Control** | `3.0.4` |
| `{{site.versions.weather-js}}` | **MapTiler Weather JS** | `v3.1.1` |
| `{{site.versions.maptiler-3d}}` | **MapTiler 3D Plugin** | `v4.0.1` |
| `{{site.versions.geosplats}}` | **MapTiler GeoSplats SDK** | `v1.0.4` |
| - | **MapTiler iOS (Swift)** | `1.3.1` |
| - | **MapTiler Android (Kotlin)** | `1.3.0` |
| - | **Mapbox Android SDK** | `11.16.6` |
| `{{site.versions.leaflet}}` | **Leaflet** | `1.9.4` |
| `{{site.versions.openlayers}}` | **OpenLayers** | `10.9.0` |
| `{{site.versions.ol-mapbox-style}}` | **ol-mapbox-style** | `13.4.1` |
| `{{site.versions.cesium}}` | **Cesium** | `1.141.0` |
| `{{site.versions.maplibre-gl}}` | **MapLibre GL JS** | `4.7.1` |
| `{{site.versions.three-js}}` | **Three.js** | `0.184.0` |
| `{{site.versions.babylonjs}}` | **Babylon.js** | `9.9.1` |
| `{{site.versions.bootstrap}}` | **Bootstrap** | `5.3.8` |
| `{{site.versions.bootstrap-icons}}` | **Bootstrap Icons** | `1.13.1` |
| `{{site.versions.d3}}` | **D3** | `7.9.0` |
| `{{site.versions.turf}}` | **Turf** | `7.3.5` |
| `{{site.versions.lil-gui}}` | **lil-gui** | `0.19` |
| `{{site.versions.mapbox-gl-draw}}` | **Mapbox GL Draw** | `v1.4.2` |
| `{{site.versions.suncalc}}` | **SunCalc** | `1.9.0` |
| `{{site.versions.blueimp-md5}}` | **blueimp-md5** | `2.19.0` |

## Map Style Mappings
Use these modern style IDs when replacing map style variables or implementing style configurations. Using the modern SDK shorthand (e.g., `MapStyle.STREETS` in SDK JS) is always preferred over hardcoded URLs, as it automatically uses the latest version.

### Standard Template Variables
When resolving double-curly-brace template markers in the references database or user queries, **always** substitute them with these concrete, modern **V4** production-standard strings:

- `{{site.map-styles.streets}}` -> `streets-v4` (Classic default map style)
- `{{site.map-styles.satellite}}` -> `satellite-v4` (High-resolution plain satellite imagery)
- `{{site.map-styles.hybrid}}` -> `hybrid-v4` (Satellite imagery with road, place, and boundary overlays)
- `{{site.map-styles.dataviz-dark}}` -> `dataviz-v4-dark` (Minimalist dark style optimized for charts and dashboard overlays)
- `{{site.map-styles.winter}}` -> `winter-v4` (Specialized winter sports/ski style with slopes and lifts)

### Complete List of Modern SDK Built-In Styles & Shorthands
These are the current official constants exposed by the MapTiler JS SDK Proxy (`MapStyle`), along with their corresponding production-ready Cloud Style IDs (`<style-id>` for use in direct REST URLs `/maps/<style-id>/style.json` or mapping engines like Leaflet/OpenLayers):

| SDK Constant | Resolved Cloud Style ID (`<style-id>`) | Available Variants | Purpose / Description |
| :--- | :--- | :--- | :--- |
| `MapStyle.STREETS` | `streets-v4` | `.DARK` (`streets-v4-dark`), `.PASTEL` (`streets-v4-pastel`) | Classic default style, perfect for urban navigation and general mapping. |
| `MapStyle.BASE` | `base-v4` | `.DARK` (`base-v4-dark`), `.LIGHT` (`base-v4-light`), `.AI` (`base-v4-ai`) | Sleek minimalist base layout. Use instead of deprecated `basic-v2`. |
| `MapStyle.OUTDOOR` | `outdoor-v4` | `.DARK` (`outdoor-v4-dark`) | Topographic hiking/trail companion with detailed contour lines and hillshading. |
| `MapStyle.WINTER` | `winter-v4` | `.DARK` (`winter-v4-dark`) | Winter sports map focusing on ski trails, snow themes, and ski lifts. |
| `MapStyle.SATELLITE` | `satellite-v4` | `.DARK` (`satellite-v4-dark`) | High-resolution satellite imagery with no labels or overlays. |
| `MapStyle.HYBRID` | `hybrid-v4` | `.DARK` (`hybrid-v4-dark`) | High-resolution satellite imagery with roads, places, and borders overlay. |
| `MapStyle.DATAVIZ` | `dataviz-v4` | `.DARK` (`dataviz-v4-dark`), `.LIGHT` (`dataviz-v4-light`) | Minimalist data visualization style designed to put dashboards and overlays first. |
| `MapStyle.BACKDROP` | `backdrop-v4` | `.DARK` (`backdrop-v4-dark`), `.LIGHT` (`backdrop-v4-light`) | Ultra-clean layout focused primarily on bathymetry and terrain hillshading. |
| `MapStyle.OCEAN` | `ocean-v4` | `.DARK` (`ocean-v4-dark`) | Marine data view emphasizing seabed bathymetry and depth contours. |
| `MapStyle.LANDSCAPE` | `landscape-v4` | `.DARK` (`landscape-v4-dark`), `.VIVID` (`landscape-v4-vivid`) | Terrain map optimized for physical geography and land cover overlays. |
| `MapStyle.AQUARELLE` | `aquarelle-v4` | `.DARK` (`aquarelle-v4-dark`), `.VIVID` (`aquarelle-v4-vivid`) | Artistic, hand-painted watercolor styling for creative and non-standard maps. |
| `MapStyle.TOPO` | `topo-v4` | `.DARK` (`topo-v4-dark`), `.PASTEL` (`topo-v4-pastel`), `.TOPOGRAPHIQUE` (`topo-v4-topographique`) | Dedicated topographic research map with multi-variant options. |
| `MapStyle.BRIGHT` | `bright-v2` | `.DARK` (`bright-v2-dark`), `.LIGHT` (`bright-v2-light`), `.PASTEL` (`bright-v2-pastel`) | High-contrast colorful layouts. |
| `MapStyle.OPENSTREETMAP`| `openstreetmap` | `.DARK` (`openstreetmap-dark`) | Standard OSM vector rendering. |

> [!WARNING]
> The following reference style families are fully deprecated and will be removed in future versions:
> - `MapStyle.BASIC` (points to deprecated `basic-v2`, `basic-v2-dark`, `basic-v2-light`). **Action:** Always use `MapStyle.BASE` (`base-v4`) instead.
> - `MapStyle.TONER` (points to deprecated `toner-v2`, `toner-v2-background`, `toner-v2-lite`, `toner-v2-lines`). **Action:** Use `MapStyle.BASE` or `MapStyle.STREETS.DARK`.
> - `MapStyle.VOYAGER` (points to deprecated `voyager-v2` variants like `darkmatter`, `positron`, `vintage`). **Action:** Use `base-v4-dark` (for darkmatter), `base-v4-light` (for positron), or `streets-v4-pastel` (for vintage).

### Legacy-to-Modern Style Translation Table
If you encounter deprecated raw strings (such as `v2` keys) in the reference files or old documentation blocks, **dynamically translate them** in any output code or user-facing solution according to this table:

| Deprecated Key (v2) | Modern Equivalent Key (v4) | Modern SDK Constant Recommendation |
| :--- | :--- | :--- |
| `streets-v2` | `streets-v4` | `MapStyle.STREETS` |
| `streets-v2-dark` / `-night` | `streets-v4-dark` | `MapStyle.STREETS.DARK` |
| `streets-v2-pastel` | `streets-v4-pastel` | `MapStyle.STREETS.PASTEL` |
| `streets-v2-light` | `streets-v4` | `MapStyle.STREETS` |
| `basic-v2` | `base-v4` | `MapStyle.BASE` |
| `basic-v2-dark` | `base-v4-dark` | `MapStyle.BASE.DARK` |
| `basic-v2-light` | `base-v4-light` | `MapStyle.BASE.LIGHT` |
| `outdoor-v2` | `outdoor-v4` | `MapStyle.OUTDOOR` |
| `outdoor-v2-dark` | `outdoor-v4-dark` | `MapStyle.OUTDOOR.DARK` |
| `satellite` / `satellite-v2` | `satellite-v4` | `MapStyle.SATELLITE` |
| `hybrid` / `hybrid-v2` | `hybrid-v4` | `MapStyle.HYBRID` |
| `dataviz` / `dataviz-dark` | `dataviz-v4-dark` | `MapStyle.DATAVIZ.DARK` |
| `dataviz-light` | `dataviz-v4-light` | `MapStyle.DATAVIZ.LIGHT` |
| `backdrop` | `backdrop-v4` | `MapStyle.BACKDROP` |
| `backdrop-dark` | `backdrop-v4-dark` | `MapStyle.BACKDROP.DARK` |
| `ocean` | `ocean-v4` | `MapStyle.OCEAN` |
| `aquarelle` | `aquarelle-v4` | `MapStyle.AQUARELLE` |
| `landscape` | `landscape-v4` | `MapStyle.LANDSCAPE` |
| `topo-v2` | `topo-v4` | `MapStyle.TOPO` |
| `topo-v2-dark` | `topo-v4-dark` | `MapStyle.TOPO.DARK` |

## General Site Configuration
- `{{site.url}}` -> `https://api.maptiler.com`

## Usage for CDN
- **SDK JS Script:** `https://cdn.maptiler.com/maptiler-sdk-js/v4.1.0/maptiler-sdk.umd.min.js`
- **SDK JS CSS:** `https://cdn.maptiler.com/maptiler-sdk-js/v4.1.0/maptiler-sdk.css`

## Usage for Gradle (Android)
`implementation("com.maptiler:maptiler-sdk-kotlin:1.3.0")`

