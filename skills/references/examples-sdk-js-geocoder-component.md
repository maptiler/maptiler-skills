# Source: https://docs.maptiler.com/sdk-js/examples/geocoder-component/

# MapTiler Geocoding control

This tutorial shows how to use the [geocoding control](/sdk-js/modules/geocoding/) module to add a **place search box** to your map or another application.

<div class="tab-content cdn-steps" markdown="1">

<ol>

<li>

Include the geocoder component JavaScript and CSS files in the <code class="language-plain">&lt;head&gt;</code> of your HTML file.

<pre><code class="language-html"><!--

<script src="https://cdn.maptiler.com/maptiler-geocoding-control//maptilersdk.umd.js"></script>

--></code></pre>

</li>

<li>

Add the geocoder control to the map.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

const gc = new maptilerGeocoder.GeocodingControl();

map.addControl(gc, 'top-left');

--></code></pre>

</li>

</ol>

</div>

<div class="tab-content bundler-steps" markdown="1">

<ol start="6">

<li>

Install the Geocoding control using npm.

<pre><code class="language-bash"><!--

npm install --save @maptiler/geocoding-control

--></code></pre>

</li>

<li>

Import the Geocoding control component and CSS in your mapping application.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2"><code class="language-js"><!--

import * as maptilersdk from '@maptiler/sdk';

import { GeocodingControl } from "@maptiler/geocoding-control/maptilersdk";

import "@maptiler/sdk/dist/maptiler-sdk.css";

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

});

--></code></pre>

</li>

<li>

Add the geocoder control to the map.

<pre class="line-numbers" data-start="7" data-line-offset="6" data-line="14-16"><code class="language-js"><!--

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

});

const gc = new GeocodingControl();

map.addControl(gc, 'top-left');

--></code></pre>

</li>

</ol>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [16.62662018, 49.2125578], // starting position [lng, lat]
      zoom: 14, // starting zoom
    });

    const gc = new maptilerGeocoder.GeocodingControl({});

    map.addControl(gc, 'top-left');
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/maptilersdk.umd.js"></script>
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
            center: [16.62662018, 49.2125578],
            zoom: 14
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [16.62662018, 49.2125578], // starting position [lng, lat]
              zoom: 14, // starting zoom
            });

            const gc = new maptilerGeocoder.GeocodingControl({});

            map.addControl(gc, 'top-left');
    </script>
</body>
</html>
```
