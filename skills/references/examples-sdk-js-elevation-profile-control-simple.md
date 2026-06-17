# Source: https://docs.maptiler.com/sdk-js/examples/elevation-profile-control-simple/

# Elevation profile control

The [Elevation Profile control](/sdk-js/modules/elevation-profile/) for MapTiler SDK is a super easy way to show the elevation profile of any GeoJSON or GPX (GPS) trace. By utilizing elevation data from MapTiler, this feature allows you to effortlessly showcase the elevation profile of your selected data source.

Following this step-by-step example, you can easily view the profile of various activities such as hiking routes, bicycle routes, trail runs, and more.

<div class="tab-content cdn-steps" markdown="1">

1. Include the MapTiler Elevation profile control JS file in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="9" data-line-offset="8" data-line="9"><code class="language-html"><!--

<script src="https://cdn.maptiler.com/maptiler-elevation-profile-control//maptiler-elevation-profile-control.umd.min.js"></script>

--></code></pre>

1. Add a GeoJSON trace to the map. Check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial. Download the [Maupas Peak hiking sample data](/sdk-js/assets/my_trace.geojson)

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="27-35"><code class="language-js"><!--

map.on('ready', () => {

maptilersdk.helpers.addPolyline(map, {

data: 'YOUR_MAPTILER_DATASET_ID_HERE', //from a URL or a MapTiler Data UUID

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

});

--></code></pre>

1. Instantiate the control and add it to a `Map` instance, most likely inside a *map* `"ready"` event callback

<pre class="line-numbers" data-start="27" data-line-offset="26" data-line="36-45"><code class="language-js"><!--

map.on('ready', () => {

maptilersdk.helpers.addPolyline(map, {

data: 'YOUR_MAPTILER_DATASET_ID_HERE',

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

// Create an instance

const epc = new maptilerelevationprofilecontrol.ElevationProfileControl({

visible: true

});

// Add it to your map

map.addControl(epc);

// Add some data (from a URL or a MapTiler Data UUID)

epc.setData('YOUR_MAPTILER_DATASET_ID_HERE');

});

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Install the elevation-profile-control npm package.

<pre><code class="language-bash"><!--

npm install --save @maptiler/elevation-profile-control

--></code></pre>

1. Import the MapTiler elevation profile control

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3"><code class="language-js"><!--

import * as maptilersdk from '@maptiler/sdk';

import '@maptiler/sdk/dist/maptiler-sdk.css';

import { ElevationProfileControl } from "@maptiler/elevation-profile-control";

--></code></pre>

1. Instantiate the control and add it to a `Map` instance, most likely inside a *map* `"ready"` event callback

<pre class="line-numbers" data-start="11" data-line-offset="10" data-line="11-31"><code class="language-js"><!--

map.on('ready', () => {

maptilersdk.helpers.addPolyline(map, {

data: 'YOUR_MAPTILER_DATASET_ID_HERE',

lineColor: '#66f',

lineWidth: 4,

outline: true,

outlineWidth: 2

});

// Create an instance

const epc = new ElevationProfileControl({

visible: true

});

// Add it to your map

map.addControl(epc);

// Add some data (from a URL or a MapTiler Data UUID)

epc.setData('YOUR_MAPTILER_DATASET_ID_HERE');

});

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.OUTDOOR,
      center: [0.57705, 42.68311], // starting position [lng, lat]
      zoom: 12.22, // starting zoom
    });

    map.on('ready', () => {
      maptilersdk.helpers.addPolyline(map, {
        data: 'YOUR_MAPTILER_DATASET_ID_HERE', //from a URL or a MapTiler Data UUID
        lineColor: '#66f', 
        lineWidth: 4, 
        outline: true, 
        outlineWidth: 2
      });

      // Create an instance
      const epc = new maptilerelevationprofilecontrol.ElevationProfileControl({
        visible: true
      });

      // Add it to your map
      map.addControl(epc);

      // Add some data (from a URL or a MapTiler Data UUID)
      epc.setData('YOUR_MAPTILER_DATASET_ID_HERE');
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [0.57705, 42.68311],
            zoom: 12.22
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.OUTDOOR,
              center: [0.57705, 42.68311], // starting position [lng, lat]
              zoom: 12.22, // starting zoom
            });

            map.on('ready', () => {
              maptilersdk.helpers.addPolyline(map, {
                data: 'YOUR_MAPTILER_DATASET_ID_HERE', //from a URL or a MapTiler Data UUID
                lineColor: '#66f', 
                lineWidth: 4, 
                outline: true, 
                outlineWidth: 2
              });

              // Create an instance
              const epc = new maptilerelevationprofilecontrol.ElevationProfileControl({
                visible: true
              });

              // Add it to your map
              map.addControl(epc);

              // Add some data (from a URL or a MapTiler Data UUID)
              epc.setData('YOUR_MAPTILER_DATASET_ID_HERE');
            });
    </script>
</body>
</html>
```
