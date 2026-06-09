# Source: https://docs.maptiler.com/sdk-js/examples/elevation-profile-control-customized/

# Elevation profile control

The elevation profile control for MapTiler SDK provides various options for customization, allowing users to choose between metric and imperial units. With built-in defaults, the control effortlessly achieves a visually appealing appearance. Furthermore, it offers a wide range of customization features, including styling options, the ability to define a class for the container, and even the option to display the control in a separate container outside the map.

To demonstrate this, we will utilize specific styling options to personalize the control and create it within its dedicated container located outside the map.

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save @maptiler/sdk @maptiler/elevation-profile-control

--></code></pre>

1. Create the map style. Add the map style to your stylesheet. The div must have non-zero height.

<pre><code class="language-css">

body {

margin: 0;

padding: 0;

}

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

background: #252525;

width: 50vw;

height: 200px;

margin-top: 20px;

position: absolute;

bottom: 10px;

}

</code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre><code class="language-html"><!--

<div id="map"></div>

--></code></pre>

1. Create a `<div>` element with a certain id where you want your control to be.

Add `<div>` tag into your page. This div will be the container where the control will be loaded.

<pre><code class="language-html"><!--

<div id="profileContainer"></div>

--></code></pre>

1. Include the CSS file.

If you have a bundler that can handle CSS, you can import the CSS from @maptiler/sdk/dist/maptiler-sdk.css.

<pre><code class="language-js"><!--

import '@maptiler/sdk/dist/maptiler-sdk.css';

--></code></pre>

> [!INFO]

> Including the CSS file using a `<link>` in the head of the document via the CDN is the easiest way.

>

> ```html

> <link href='https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css' rel='stylesheet' />

> ```

>

1. Load the map with the style. Include the following code in your JavaScript.

<pre><code class="language-js">

import { config, Map, helpers, Marker, MapStyle } from '@maptiler/sdk';

config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new Map({

container: 'map', // container's id or the HTML element in which SDK will render the map

style: MapStyle.BACKDROP.DARK,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

</code></pre>

1.

1. Add a GeoJSON trace to the map. Check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial. Download the [Maupas Peak hiking sample data](/sdk-js/assets/my_trace.geojson)

<pre><code class="language-js"><!--

map.on('load', () => {

helpers.addPolyline(map, {

data: YOUR_MAPTILER_DATASET_ID_HERE, //from a URL or a MapTiler Data UUID

lineColor: '#a103fc',

outline: true,

outlineWidth: 1.5

});

});

--></code></pre>

1. Create a marker and add it to the map.

<pre><code class="language-js"><!--

map.on('load', () => {

helpers.addPolyline(map, {

data: YOUR_MAPTILER_DATASET_ID_HERE, //from a URL or a MapTiler Data UUID

lineColor: '#a103fc',

outline: true,

outlineWidth: 1.5

});

const marker = new Marker()

.setLngLat([0, 0])

.addTo(map);

});

--></code></pre>

1. Import the MapTiler elevation profile control

<pre><code class="language-js"><!--

import { ElevationProfileControl } from "@maptiler/elevation-profile-control";

--></code></pre>

1. Instantiate the control and add it to a `Map` instance, most likely inside a *map* `"load"` event callback

<pre><code class="language-js"><!--

map.on('load', () => {

helpers.addPolyline(map, {

data: YOUR_MAPTILER_DATASET_ID_HERE,

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

const marker = new Marker()

.setLngLat([0, 0])

.addTo(map);

// Create an instance (with the customize options)

const epc = new ElevationProfileControl({

container: "profileContainer",

visible: true,

showButton: false,

labelColor: "#FFF6",

elevationGridColor: "#FFF1",

tooltipTextColor: "#000b",

tooltipBackgroundColor: "#eeea",

profileLineColor: "#a103fc",

profileBackgroundColor: "#a103fc11",

crosshairColor: "#66f5",

displayTooltip: true,

unit: "imperial",

onMove: (data) => {

marker.setLngLat(data.position)

},

});

// Add it to your map

map.addControl(epc);

// Add some data (from a URL or a MapTiler Data UUID)

epc.setData('YOUR_MAPTILER_DATASET_ID_HERE');

});

--></code></pre>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
    style: (typeof mapId === 'string' || mapId instanceof String) ? `${mapId}` : mapId,
    center: [0.57722, 42.68994], // starting position [lng, lat]
    zoom: 12.22, // starting zoom
  });

  let polyline, epc, marker;

  map.on('load', async () => {
    polyline = await maptilersdk.helpers.addPolyline(map, {
      data: '40a41e21-8d5b-4393-837d-3f0a1edbb168', //from a URL or a MapTiler Data UUID
      lineColor: '#a103fc',
      outline: true,
      outlineWidth: 1.5
    });

    marker = new maptilersdk.Marker()
    .setLngLat([0, 0])
    .addTo(map);

    // Create an instance
    epc = new maptilerelevationprofilecontrol.ElevationProfileControl({
      container: "profileContainer",
      visible: true,
      showButton: false,
      labelColor: "#FFF6",
      elevationGridColor: "#FFF1",
      tooltipTextColor: "#000b",
      tooltipBackgroundColor: "#eeea",
      profileLineColor: "#a103fc",
      profileBackgroundColor: "#a103fc11",
      crosshairColor: "#66f5",
      displayTooltip: true,
      unit: "imperial",
      onMove: (data) => {
        marker.setLngLat(data.position)
      },
    });

    // Add it to your map
    map.addControl(epc);

    epc.setData('40a41e21-8d5b-4393-837d-3f0a1edbb168');

  });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Elevation profile control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-elevation-profile-control/v3.0.1/maptiler-elevation-profile-control.umd.min.js"></script>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [0.57722, 42.68994],
            zoom: 12.22
        });

        container: 'map', // container's id or the HTML element to render the map
            style: (typeof mapId === 'string' || mapId instanceof String) ? `${mapId}` : mapId,
            center: [0.57722, 42.68994], // starting position [lng, lat]
            zoom: 12.22, // starting zoom
          });

          let polyline, epc, marker;

          map.on('load', async () => {
            polyline = await maptilersdk.helpers.addPolyline(map, {
              data: '40a41e21-8d5b-4393-837d-3f0a1edbb168', //from a URL or a MapTiler Data UUID
              lineColor: '#a103fc',
              outline: true,
              outlineWidth: 1.5
            });

            marker = new maptilersdk.Marker()
            .setLngLat([0, 0])
            .addTo(map);

            // Create an instance
            epc = new maptilerelevationprofilecontrol.ElevationProfileControl({
              container: "profileContainer",
              visible: true,
              showButton: false,
              labelColor: "#FFF6",
              elevationGridColor: "#FFF1",
              tooltipTextColor: "#000b",
              tooltipBackgroundColor: "#eeea",
              profileLineColor: "#a103fc",
              profileBackgroundColor: "#a103fc11",
              crosshairColor: "#66f5",
              displayTooltip: true,
              unit: "imperial",
              onMove: (data) => {
                marker.setLngLat(data.position)
              },
            });

            // Add it to your map
            map.addControl(epc);

            epc.setData('40a41e21-8d5b-4393-837d-3f0a1edbb168');

          });
    </script>
</body>
</html>
```
