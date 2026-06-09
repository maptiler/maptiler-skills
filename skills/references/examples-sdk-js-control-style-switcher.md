# Source: https://docs.maptiler.com/sdk-js/examples/control-style-switcher/

# Display a style switcher control

This tutorial demonstrates the process of showcasing a control for switching styles on the map.

<div class="tab-common-content" markdown="1">

1. Create the list of styles. In the list of styles use as key the ID of the map in [MapTiler](https://cloud.maptiler.com/maps/){:target="_blank" rel="noopener"}.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="18-28"><code class="language-js"><!--

const baseMaps = {

"STREETS": {

img: "https://cloud.maptiler.com/static/img/maps/.png"

},

"WINTER": {

img: "https://cloud.maptiler.com/static/img/maps/.png"

},

"HYBRID": {

img: "https://cloud.maptiler.com/static/img/maps/.png"

}

}

--></code></pre>

1.  Select the initial style from the list and update the map style URL.

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="29, 32"><code class="language-js"><!--

const initialStyle = maptilersdk.MapStyle[Object.keys(baseMaps)[0]];

const map = new maptilersdk.Map({

container: 'map', // container id

style: initialStyle,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

--></code></pre>

1.  Create the `styleSwitcherControl` and add it to the map. This code is an adaptation of the [maplibre-gl-basemaps](https://github.com/ka7eh/maplibre-gl-basemaps){:target="\_blank" rel="noopener"} plugins.

<pre class="line-numbers" data-start="36" data-line-offset="35" data-line="36-93"><code class="language-js"><!--

class layerSwitcherControl {

constructor(options) {

this._options = {...options};

this._container = document.createElement("div");

this._container.classList.add("maplibregl-ctrl");

this._container.classList.add("maplibregl-ctrl-basemaps");

this._container.classList.add("closed");

switch (this._options.expandDirection || "right") {

case "top":

this._container.classList.add("reverse");

case "down":

this._container.classList.add("column");

break;

case "left":

this._container.classList.add("reverse");

case "right":

this._container.classList.add("row");

}

this._container.addEventListener("mouseenter", () => {

this._container.classList.remove("closed");

});

this._container.addEventListener("mouseleave", () => {

this._container.classList.add("closed");

});

}

onAdd(map) {

this._map = map;

const basemaps = this._options.basemaps;

Object.keys(basemaps).forEach((layerId) => {

const base = basemaps[layerId];

const basemapContainer = document.createElement("img");

basemapContainer.src = base.img;

basemapContainer.classList.add("basemap");

basemapContainer.dataset.id = layerId;

basemapContainer.addEventListener("click", () => {

const activeElement = this._container.querySelector(".active");

activeElement.classList.remove("active");

basemapContainer.classList.add("active");

map.setStyle(maptilersdk.MapStyle[layerId]);

});

basemapContainer.classList.add("hidden");

this._container.appendChild(basemapContainer);

if (this._options.initialBasemap.id === layerId) {

basemapContainer.classList.add("active");

}

});

return this._container;

}

onRemove(){

this._container.parentNode?.removeChild(this._container);

delete this._map;

}

}

map.addControl(new layerSwitcherControl({basemaps: baseMaps, initialBasemap: initialStyle}), 'bottom-left');

--></code></pre>

1.  Create the `styleSwitcherControl` css style. Add the SwitcherControl style to your stylesheet.

<pre><code class="language-css"><!--

/*layerSwitcherControl*/

.maplibregl-ctrl-basemaps {

display: flex;

flex-direction: row;

pointer-events: auto;

bottom: 15px;

position: relative;

}

.maplibregl-ctrl-basemaps.reverse {

flex-direction: row-reverse;

}

.maplibregl-ctrl-basemaps.column {

flex-direction: column;

}

.maplibregl-ctrl-basemaps.column.reverse {

flex-direction: column-reverse;

}

.maplibregl-ctrl-basemaps .basemap {

width: 64px;

height: 64px;

margin: 2px;

border: 2px solid #ccc;

box-shadow: 0 1px 5px rgba(0, 0, 0, 0.65);

cursor: pointer;

}

.maplibregl-ctrl-basemaps .basemap.active {

border-color: orange;

box-shadow: 2px 2px 4px #000;

}

.maplibregl-ctrl-basemaps.closed .basemap {

display: none;

}

.maplibregl-ctrl-basemaps.closed .basemap.active {

display: block;

border: 2px solid #ccc;

}

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const urlParams = new URLSearchParams(window.location.search); const key = urlParams.get('key') || 'YOUR_MAPTILER_API_KEY_HERE';
    const fallback_key = urlParams.get('fallback_key') || urlParams.get('key');
    const baseMaps = {
      "STREETS": {
        img: "https://cloud.maptiler.com/static/img/maps/streets-v4.png"
      },
      "WINTER": {
        img: "https://cloud.maptiler.com/static/img/maps/winter-v4.png"
      },
      "HYBRID": {
        img: "https://cloud.maptiler.com/static/img/maps/hybrid-v4.png"
      }
    }
    const initialStyle = maptilersdk.MapStyle[Object.keys(baseMaps)[0]];
      container: 'map', // container's id or the HTML element to render the map
      style: initialStyle,
      center: [100.507, 13.7231], // starting position [lng, lat]
      zoom: 10.82, // starting zoom
    });

    class layerSwitcherControl {

      constructor(options) {
        this._options = { ...options };
        this._container = document.createElement("div");
        this._container.classList.add("maplibregl-ctrl");
        this._container.classList.add("maplibregl-ctrl-basemaps");
        this._container.classList.add("closed");
        switch (this._options.expandDirection || "right") {
          case "top":
            this._container.classList.add("reverse");
          case "down":
            this._container.classList.add("column");
            break;
          case "left":
            this._container.classList.add("reverse");
          case "right":
            this._container.classList.add("row");
        }
        this._container.addEventListener("mouseenter", () => {
          this._container.classList.remove("closed");
        });
        this._container.addEventListener("mouseleave", () => {
          this._container.classList.add("closed");
        });
      }

      onAdd(map) {
        this._map = map;
        const basemaps = this._options.basemaps;
        Object.keys(basemaps).forEach((layerId) => {
          const base = basemaps[layerId];
          const basemapContainer = document.createElement("img");
          basemapContainer.src = base.img;
          basemapContainer.classList.add("basemap");
          basemapContainer.dataset.id = layerId;
          basemapContainer.addEventListener("click", () => {
            const activeElement = this._container.querySelector(".active");
            activeElement.classList.remove("active");
            basemapContainer.classList.add("active");
            map.setStyle(maptilersdk.MapStyle[layerId]);
          });
          basemapContainer.classList.add("hidden");
          this._container.appendChild(basemapContainer);
          if (this._options.initialBasemap.id === layerId) {
            basemapContainer.classList.add("active");
          }
        });
        return this._container;
      }

      onRemove() {
        this._container.parentNode?.removeChild(this._container);
        delete this._map;
      }
    }

    map.addControl(new layerSwitcherControl({ basemaps: baseMaps, initialBasemap: initialStyle }), 'bottom-left');
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a style switcher control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: initialStyle,
            center: [100.507, 13.7231],
            zoom: 10.82
        });

        const urlParams = new URLSearchParams(window.location.search); const key = urlParams.get('key') || 'YOUR_MAPTILER_API_KEY_HERE';
            const fallback_key = urlParams.get('fallback_key') || urlParams.get('key');
            const baseMaps = {
              "STREETS": {
                img: "https://cloud.maptiler.com/static/img/maps/streets-v4.png"
              },
              "WINTER": {
                img: "https://cloud.maptiler.com/static/img/maps/winter-v4.png"
              },
              "HYBRID": {
                img: "https://cloud.maptiler.com/static/img/maps/hybrid-v4.png"
              }
            }
            const initialStyle = maptilersdk.MapStyle[Object.keys(baseMaps)[0]];
              container: 'map', // container's id or the HTML element to render the map
              style: initialStyle,
              center: [100.507, 13.7231], // starting position [lng, lat]
              zoom: 10.82, // starting zoom
            });

            class layerSwitcherControl {

              constructor(options) {
                this._options = { ...options };
                this._container = document.createElement("div");
                this._container.classList.add("maplibregl-ctrl");
                this._container.classList.add("maplibregl-ctrl-basemaps");
                this._container.classList.add("closed");
                switch (this._options.expandDirection || "right") {
                  case "top":
                    this._container.classList.add("reverse");
                  case "down":
                    this._container.classList.add("column");
                    break;
                  case "left":
                    this._container.classList.add("reverse");
                  case "right":
                    this._container.classList.add("row");
                }
                this._container.addEventListener("mouseenter", () => {
                  this._container.classList.remove("closed");
                });
                this._container.addEventListener("mouseleave", () => {
                  this._container.classList.add("closed");
                });
              }

              onAdd(map) {
                this._map = map;
                const basemaps = this._options.basemaps;
                Object.keys(basemaps).forEach((layerId) => {
                  const base = basemaps[layerId];
                  const basemapContainer = document.createElement("img");
                  basemapContainer.src = base.img;
                  basemapContainer.classList.add("basemap");
                  basemapContainer.dataset.id = layerId;
                  basemapContainer.addEventListener("click", () => {
                    const activeElement = this._container.querySelector(".active");
                    activeElement.classList.remove("active");
                    basemapContainer.classList.add("active");
                    map.setStyle(maptilersdk.MapStyle[layerId]);
                  });
                  basemapContainer.classList.add("hidden");
                  this._container.appendChild(basemapContainer);
                  if (this._options.initialBasemap.id === layerId) {
                    basemapContainer.classList.add("active");
                  }
                });
                return this._container;
              }

              onRemove() {
                this._container.parentNode?.removeChild(this._container);
                delete this._map;
              }
            }

            map.addControl(new layerSwitcherControl({ basemaps: baseMaps, initialBasemap: initialStyle }), 'bottom-left');
    </script>
</body>
</html>
```
