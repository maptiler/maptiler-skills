# Source: https://docs.maptiler.com/sdk-js/examples/elevation-profile-control-gpx/

# Elevation profile control

The elevation profile control for MapTiler SDK is a super easy way to show the elevation profile of any GPX (GPS) trace or GeoJSON. By utilizing elevation data from MapTiler, this feature allows you to effortlessly showcase the elevation profile of your hiking routes, bicycle routes, trail runs, and more.

Following this step-by-step example, you can easily view the profile of various activities.

<sup><b>Drag and drop</b> a GPX file onto the map to view your track profile.</sup>

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save @maptiler/sdk @maptiler/elevation-profile-control

--></code></pre>

1. Create the map style. Add the map style to your stylesheet. The div must have a non-zero height.

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

<pre><code class="language-js"><!--

import { config, Map, helpers, MapStyle } from '@maptiler/sdk';

config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new Map({

container: 'map', // container's id or the HTML element in which SDK will render the map

style: MapStyle.OUTDOOR,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

--></code></pre>

1.

1. We are going to define some variables that we will use later in the tutorial.

<pre><code class="language-js"><!--

let polyline, epc, marker;

--></code></pre>

1. Add a GPX trace to the map. You can use a GPX directly from a URL or upload your GPX to the MapTiler. Check out the [How to edit your data in MapTiler](/guides/map-tiling-hosting/data-hosting/how-to-edit-your-vector-data-in-maptiler-cloud){:target="_blank" rel="noopener"} tutorial. Download the [Cervinia Valtournenche mountain bike sample data](/sdk-js/assets/cervinia-valtournenche.gpx)

<pre><code class="language-js"><!--

map.on('load', async () => {

polyline = await helpers.addPolyline(map, {

data: '/sdk-js/assets/cervinia-valtournenche.gpx', //from a URL or a MapTiler Data UUID

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

});

--></code></pre>

1. Add the `Marker` object to the `@maptiler/sdk` import.

<pre><code class="language-js"><!--

import { config, Map, helpers, MapStyle, Marker } from '@maptiler/sdk';

--></code></pre>

1. Create a marker and add it to the map. We will use this marker to display the location of the elevation profile cursor with the position of the marker on the map.

<pre><code class="language-js"><!--

map.on('load', async () => {

polyline = await helpers.addPolyline(map, {

data: '/sdk-js/assets/cervinia-valtournenche.gpx', //from a URL or a MapTiler Data UUID

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

marker = new Marker()

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

map.on('load', async () => {

polyline = await helpers.addPolyline(map, {

data: '/sdk-js/assets/cervinia-valtournenche.gpx', //from a URL or a MapTiler Data UUID

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

marker = new Marker()

.setLngLat([0, 0])

.addTo(map);

// Create an instance

epc = new ElevationProfileControl({

container: "profileContainer",

visible: true,

showButton: false,

profileLineColor: "#66f",

profileBackgroundColor: "#a103fc11",

displayTooltip: true,

onMove: (data) => {

marker.setLngLat(data.position)

},

});

// Add it to your map

map.addControl(epc);

// Add some data (from a URL or a MapTiler Data UUID)

const sourceObject = map.getSource(polyline.polylineSourceId);

epc.setData(sourceObject._data);

moveMarkerToGPXStart(sourceObject._data);

});

--></code></pre>

1. Move the Marker to the GPX start point

<pre><code class="language-js"><!--

function moveMarkerToGPXStart(data) {

marker.setLngLat(data.features[0].geometry.coordinates[0])

}

--></code></pre>

1. Let's add some styling to the profile control to see the track profile on the map along with your GPS track.

<pre><code class="language-css"><!--

background:#fff;

width: 50vw;

height: 200px;

margin-top: 20px;

position: absolute;

bottom: 10px;

opacity: 0.9;

}

--></code></pre>

1. With these steps, you have your map where the GPX track is shown with its elevation profile. In the following steps, we will see how to add the functionality of dragging and dropping a GPX file on the map to view the new track along with its profile.

1. Use the [HTML Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API){:target="_blank" rel="noopener"} to drag a file onto our map.

<pre><code class="language-js"><!--

document.getElementById('map').addEventListener('drop', function(ev) {

ev.preventDefault();

if (ev.dataTransfer.files) {

// Use DataTransfer interface to access the file(s)

[...ev.dataTransfer.files].forEach((file, i) => {

readGPXFile(file);

});

} else {

// Use DataTransferItemList interface to access the file(s)

[...ev.dataTransfer.items].forEach((item, i) => {

// If dropped items aren't files, reject them

if (item.kind === "file") {

const file = item.getAsFile();

readGPXFile(file);

}

});

}

});

document.getElementById('map').addEventListener('dragover', function(ev) {

ev.preventDefault();

});

--></code></pre>

1. Add the `gpx` function and the `LngLatBounds` object to the `@maptiler/sdk` import.

<pre><code class="language-js"><!--

import { config, Map, helpers, MapStyle, Marker, gpx, LngLatBounds } from '@maptiler/sdk';

--></code></pre>

1. Read the GPX file data. To read the content of the file in the browser without having to upload it to any server, we will use the [FileReader object](https://developer.mozilla.org/en-US/docs/Web/API/FileReader){:target="_blank" rel="noopener"}.

<pre><code class="language-js"><!--

function readGPXFile(file){

if (file.name.split('.').pop().toLowerCase() !== 'gpx') {

return;

}

const reader = new FileReader();

reader.onload = function (event) {

const sourceObject = map.getSource(polyline.polylineSourceId);

sourceObject.setData(gpx(event.target.result));

epc.setData(sourceObject._data);

fitToDataBounds(sourceObject._data);

};

reader.readAsText(file, 'UTF-8');

}

--></code></pre>

1. Adjust the map view to the newly loaded track and move the marker to the track start point.

<pre><code class="language-js"><!--

function fitToDataBounds(data) {

// Geographic coordinates of the LineString

const coordinates = data.features[0].geometry.coordinates;

// Pass the first coordinates in the LineString to `lngLatBounds` &

// wrap each coordinate pair in `extend` to include them in the bounds

// result. A variation of this technique could be applied to zooming

// to the bounds of multiple Points or Polygon geomteries - it just

// requires wrapping all the coordinates with the extend method.

const bounds = coordinates.reduce((bounds, coord) => {

return bounds.extend(coord);

}, new LngLatBounds(coordinates[0], coordinates[0]));

map.fitBounds(bounds, {

padding: 20

});

moveMarkerToGPXStart(data);

}

--></code></pre>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
}
  });
  document.getElementById('map').addEventListener('dragover', function(ev) {
    ev.preventDefault();
  });

  function readGPXFile(file){
    if (file.name.split('.').pop().toLowerCase() !== 'gpx') {
      return;
    }
    const reader = new FileReader();
    reader.onload = function (event) {
      const sourceObject = map.getSource(polyline.polylineSourceId);
      sourceObject.setData(maptilersdk.gpx(event.target.result));

      epc.setData(sourceObject._data);
      fitToDataBounds(sourceObject._data);
    };
    reader.readAsText(file, 'UTF-8');
  }

  function fitToDataBounds(data) {
    // Geographic coordinates of the LineString
    const coordinates = data.features[0].geometry.coordinates;

    // Pass the first coordinates in the LineString to `lngLatBounds` &
    // wrap each coordinate pair in `extend` to include them in the bounds
    // result. A variation of this technique could be applied to zooming
    // to the bounds of multiple Points or Polygon geomteries - it just
    // requires wrapping all the coordinates with the extend method.
    const bounds = coordinates.reduce((bounds, coord) => {
        return bounds.extend(coord);
    }, new maptilersdk.LngLatBounds(coordinates[0], coordinates[0]));

    map.fitBounds(bounds, {
      padding: 20
    });
    moveMarkerToGPXStart(data);
  }
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
            center: [7.6011,45.9078],
            zoom: 11.39
        });

        }
          });
          document.getElementById('map').addEventListener('dragover', function(ev) {
            ev.preventDefault();
          });

          function readGPXFile(file){
            if (file.name.split('.').pop().toLowerCase() !== 'gpx') {
              return;
            }
            const reader = new FileReader();
            reader.onload = function (event) {
              const sourceObject = map.getSource(polyline.polylineSourceId);
              sourceObject.setData(maptilersdk.gpx(event.target.result));

              epc.setData(sourceObject._data);
              fitToDataBounds(sourceObject._data);
            };
            reader.readAsText(file, 'UTF-8');
          }

          function fitToDataBounds(data) {
            // Geographic coordinates of the LineString
            const coordinates = data.features[0].geometry.coordinates;

            // Pass the first coordinates in the LineString to `lngLatBounds` &
            // wrap each coordinate pair in `extend` to include them in the bounds
            // result. A variation of this technique could be applied to zooming
            // to the bounds of multiple Points or Polygon geomteries - it just
            // requires wrapping all the coordinates with the extend method.
            const bounds = coordinates.reduce((bounds, coord) => {
                return bounds.extend(coord);
            }, new maptilersdk.LngLatBounds(coordinates[0], coordinates[0]));

            map.fitBounds(bounds, {
              padding: 20
            });
            moveMarkerToGPXStart(data);
          }
    </script>
</body>
</html>
```
