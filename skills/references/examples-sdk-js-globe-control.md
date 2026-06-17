# Source: https://docs.maptiler.com/sdk-js/examples/globe-control/

# MapTiler Projection control

This tutorial provides instructions on how to add the projection control that toggles the map between "mercator" and "globe" projection.

<div class="tab-common-content" markdown="1">

1. To add the control to the map, all you have to do is indicate it in the map builder options.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="23"><code class="language-js"><!--

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element to render the map

style: maptilersdk.MapStyle.STREETS,

center: [16.62662018, 49.2125578], // starting position [lng, lat]

zoom: 1, // starting zoom

projectionControl: true //enable the projection control

});

--></code></pre>

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: (typeof mapId === 'string' || mapId instanceof String) ? `${mapId}` : mapId,
        center: [16.62662018, 49.2125578], // starting position [lng, lat]
        zoom: 1, // starting zoom
        projectionControl: true //enable the globe control
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Projection control</title>
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
            center: [16.62662018, 49.2125578],
            zoom: 1
        });

        container: 'map', // container's id or the HTML element to render the map
                style: (typeof mapId === 'string' || mapId instanceof String) ? `${mapId}` : mapId,
                center: [16.62662018, 49.2125578], // starting position [lng, lat]
                zoom: 1, // starting zoom
                projectionControl: true //enable the globe control
              });
    </script>
</body>
</html>
```
