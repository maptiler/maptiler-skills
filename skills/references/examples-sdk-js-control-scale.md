# Source: https://docs.maptiler.com/sdk-js/examples/control-scale/

# Display a scale control

This tutorial shows how to display a scale control on the map.

The measurement units for the scale control can be defined in the configuration object with options such as "metric," "imperial," or "nautical." The default unit is set to "metric."

<div class="tab-content cdn-steps" markdown="1">

1. Add options to the map to load the scale control to the map. The `scaleControl` shows a distance scale.

<pre class="line-numbers" data-line="23"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title></title>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<style>

body { margin: 0; padding: 0; }

</style>

</head>

<body>

<div id="map"></div>

<script>

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

scaleControl: true // add the scaleControl to the map

});

</script>

</body>

</html>

--></code></pre>

</div>

<div class="tab-content bundler-steps" markdown="1">

1. Include the following code in your JavaScript file (Example: app.js).

<pre class="line-numbers" data-line="9"><code class="language-js"><!--

import * as maptilersdk from '@maptiler/sdk';

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

scaleControl: true // add the scaleControl to the map

});

--></code></pre>

</div>

<div class="tab-common-content" markdown="1">

1.

1. Change the control position to display the control on the `bottom-left` corner of the map. By default, the control is showing on the `bottom-right` corner of the map if `true`. You can specify a corner position (`"top-left"`, `"top-right"`, `"bottom-left"`, `"bottom-right"`) to change the control position.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="23"><code class="language-js">

const map = new maptilersdk.Map({

container: 'map', // container id

style: ,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

scaleControl: "bottom-left" // add the scaleControl to the bottom-left corner of the map

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript

```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a scale control</title>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [-71.0131, 42.3585],
            zoom: 9.25
        });


    </script>
</body>
</html>
```
