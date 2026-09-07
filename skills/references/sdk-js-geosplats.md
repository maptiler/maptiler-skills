# MapTiler GeoSplats SDK (JS Reference)

The MapTiler GeoSplats SDK enables high-performance 3D Gaussian Splatting integration inside interactive web maps. Built on top of **WebGPU**, it allows real-time interactive rendering of dense volumetric 3D models with proper geospatial positioning and camera synchronization.

---

## 1. Setup & Installation

### CDN Usage
For rapid prototyping or simple static sites, include the CSS file and import the ES module directly:

```html
<!-- GeoSplats SDK Stylesheet -->
<link rel="stylesheet" href="https://cdn.maptiler.com/maptiler-geosplats/v1.0.4/maptiler-geosplats.css">

<script type="module">
  import { Map, SplatModel, config } from "https://cdn.maptiler.com/maptiler-geosplats/v1.0.4/maptiler-geosplats.mjs";
  
  config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
</script>
```

### NPM / Package Manager Usage
Install the core package using your preferred package manager:

```bash
npm install @maptiler/geosplats
```

Import the module classes and the companion stylesheet in your project:

```javascript
import { Map, SplatModel, config } from '@maptiler/geosplats';
import '@maptiler/geosplats/dist/maptiler-geosplats.css';

config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
```

---

## 2. Core API Reference

### `config` (Variable)
The global configuration object used to authenticate and configure SDK requests.
* **Properties**:
  * `apiKey` (string): Your MapTiler API Key.

### `Map` (Class)
Extends MapTiler SDK JS Map or custom map wrapper with specific GeoSplat capabilities.
* **Constructor**: `new Map(options)`
  * `options` (object): Same as MapTiler SDK JS options, including:
    * `container` (string | HTMLElement): Container ID or element.
    * `apiKey` (string): Your MapTiler API key.
    * `center` (lngLat): Initial coordinates as `[lng, lat]`.
* **Methods**:
  * `addSplatModel(splatModel: SplatModel)`: Adds an instantiated SplatModel to the map.
  * `removeSplatModel(splatModel: SplatModel)`: Removes a SplatModel from the map.

### `SplatModel` (Class)
Represents a geospatial 3D Gaussian Splat model.
* **Constructor**: `new SplatModel(options)`
  * `options` (object):
    * `model` (string): The ID or URL of your MapTiler Splat Model.
    * `opacity` (number, optional): Opacity value between `0` and `1`. Default is `1.0`.
    * `visible` (boolean, optional): Initial visibility state. Default is `true`.
* **Properties / Setters / Getters**:
  * `opacity` (number): Get or set model transparency.
  * `visible` (boolean): Toggle visibility state on/off.

### `getVersion()` (Function)
Returns the current active version string of the GeoSplats SDK.

---

## 3. Interactive Map Events

The SDK exposes several specialized map-level events that fire during interactions with Splat models. Register listener callbacks using the standard `map.on(eventName, handler)` pattern:

| Event Name | Event Object Type | Description |
| :--- | :--- | :--- |
| `"splatmodelloaddone"` | `MapSplatModelLoadEvent` | Fires when a SplatModel is fully loaded and added to the scene. |
| `"splatmodelclick"` | `MapSplatModelClickEvent` | Fires when a user clicks on an active SplatModel. |
| `"splatmodelmouseover"` | `MapSplatModelMouseOverEvent` | Fires when the mouse pointer enters the bounding space of a model. |
| `"splatmodelmouseout"` | `MapSplatModelMouseOutEvent` | Fires when the mouse pointer exits the bounding space of a model. |
| `"splatmodelerror"` | `MapSplatModelErrorEvent` | Fires if a model fails to fetch, parse, or render properly. |
| `"splatmodelupdate"` | `MapSplatModelUpdateEvent` | Fires on coordinate updates or real-time layout transformations. |

---

## 4. WebGPU Compatibility & Fallbacks

> [!IMPORTANT]
> The MapTiler GeoSplats SDK **requires WebGPU support** in the user's browser. If WebGPU is missing or disabled, the map won't render Splat models.

Always verify WebGPU compatibility and display an overlay warning for unsupported browsers:

```javascript
if (!navigator.gpu) {
  const errorOverlay = document.getElementById("webGpuError");
  if (errorOverlay) {
    errorOverlay.textContent = "WebGPU is not supported by your browser. Please upgrade to a compatible browser (e.g. Chrome, Edge, Firefox Developer Edition) to view 3D GeoSplats.";
    errorOverlay.classList.remove("d-none");
  }
}
```

---

## 5. CDN Implementation Template

GeoSplat model IDs are account assets. Do not present a fake ID as runnable. This template expects the host page to define `window.MAPTILER_API_KEY` and `window.MAPTILER_SPLAT_MODEL_ID` using real, authorized values.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MapTiler GeoSplats Basic Example</title>
  <link rel="stylesheet" href="https://cdn.maptiler.com/maptiler-geosplats/v1.0.4/maptiler-geosplats.css">
  <style>
    body {
      margin: 0;
      overflow: hidden;
      font-family: system-ui, sans-serif;
    }
    #map {
      width: 100%;
      height: 100vh;
    }
    #webGpuError {
      position: absolute;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(220, 53, 69, 0.9);
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      z-index: 9999;
      font-weight: 500;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .d-none {
      display: none;
    }
  </style>
</head>
<body>

  <div id="webGpuError" class="d-none"></div>
  <div id="map"></div>

  <script type="module">
    import { Map, SplatModel, config } from "https://cdn.maptiler.com/maptiler-geosplats/v1.0.4/maptiler-geosplats.mjs";

    // 1. Check for WebGPU Support
    if (!navigator.gpu) {
      const errorOverlay = document.getElementById("webGpuError");
      errorOverlay.textContent = "WebGPU is not supported by your browser. Please upgrade or use a compatible browser to view the 3D GeoSplat.";
      errorOverlay.classList.remove("d-none");
      throw new Error("WebGPU is required by MapTiler GeoSplats.");
    }

    // 2. Validate configuration before initializing WebGPU or the map
    const apiKey = window.MAPTILER_API_KEY;
    const modelId = window.MAPTILER_SPLAT_MODEL_ID;
    if (!apiKey || !modelId) {
      throw new Error(
        "Define MAPTILER_API_KEY and MAPTILER_SPLAT_MODEL_ID with authorized values."
      );
    }
    config.apiKey = apiKey;
    
    const map = new Map({
      apiKey: config.apiKey,
      container: "map",
      center: [7.86040, 46.686488], // Coordinates in [lng, lat]
      zoom: 16
    });
    map.on("error", ({ error }) => console.error("GeoSplats map error:", error));

    // 3. Load Splat Model upon map load
    map.on("load", () => {
      const splatModel = new SplatModel({
        model: modelId,
      });
      
      map.addSplatModel(splatModel);
    });
  </script>
</body>
</html>
```
