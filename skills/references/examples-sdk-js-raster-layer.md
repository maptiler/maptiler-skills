# Source: https://docs.maptiler.com/sdk-js/examples/raster-layer/

# Display a raster image

This tutorial provides step-by-step instructions on how to incorporate a raster image overlay onto the map.

<div class="tab-common-content" markdown="1">

1. Add event handler for map load event. You will add code to create an image source and image layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

map.on('load', function() {

});

</code></pre>

1. Create image source. Here you can get the example image [aerial_wgs84.png](img/aerial_wgs84.png)

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-55"><code class="language-js">

map.on('load', function() {

map.addSource("aerial-source", {

"type": "image",

"url": "img/aerial_wgs84.png",

"coordinates": [

[4.639663696289062, 50.900867668253724],

[4.642066955566406, 50.900867668253724],

[4.642066955566406, 50.89935199434383],

[4.639663696289062, 50.89935199434383]

]

});

});

</code></pre>

1. Add the image layer

<pre class="line-numbers" data-start="36" data-line-offset="35" data-line="36-43"><code class="language-js">

map.addLayer({

"id": "overlay",

"source": "aerial-source",

"type": "raster",

"paint": {

"raster-opacity": 0.85

}

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
            style: maptilersdk.MapStyle.STREETS,
            center: [4.64086758, 50.9001362], // starting position [lng, lat]
            zoom: 17, // starting zoom
        });
        map.on('load', function() {
            map.addSource("aerial-source", {
                "type": "image",
                "url": "./aerial_wgs84.png",
                "coordinates": [
                    [4.639663696289062, 50.900867668253724],
                    [4.642066955566406, 50.900867668253724],
                    [4.642066955566406, 50.89935199434383],
                    [4.639663696289062, 50.89935199434383]
                ]
            });
            map.addLayer({
                "id": "overlay",
                "source": "aerial-source",
                "type": "raster",
                "paint": {
                    "raster-opacity": 0.85
                }
            });
        });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a raster image</title>
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
            center: [4.64086758, 50.9001362],
            zoom: 17
        });

        container: 'map', // container's id or the HTML element to render the map
                    style: maptilersdk.MapStyle.STREETS,
                    center: [4.64086758, 50.9001362], // starting position [lng, lat]
                    zoom: 17, // starting zoom
                });
                map.on('load', function() {
                    map.addSource("aerial-source", {
                        "type": "image",
                        "url": "./aerial_wgs84.png",
                        "coordinates": [
                            [4.639663696289062, 50.900867668253724],
                            [4.642066955566406, 50.900867668253724],
                            [4.642066955566406, 50.89935199434383],
                            [4.639663696289062, 50.89935199434383]
                        ]
                    });
                    map.addLayer({
                        "id": "overlay",
                        "source": "aerial-source",
                        "type": "raster",
                        "paint": {
                            "raster-opacity": 0.85
                        }
                    });
                });
    </script>
</body>
</html>
```
