# Source: https://docs.maptiler.com/sdk-js/examples/vector-source/

# Add a vector tile source

Enhance your map by incorporating a [vector source](/gl-style-specification/sources/#vector).

With the help of the [MapTiler Engine](https://www.maptiler.com/engine/), you can convert your data into vector tiles effortlessly. These tiles can then be [uploaded to the MapTiler](/guides/map-tiling-hosting/data-processing/how-to-upload-a-tileset-to-maptiler-cloud) with just a simple click, allowing you to seamlessly integrate your data into all of your web mapping applications.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('contours', {
            type: 'vector',
            url:
                `https://api.maptiler.com/tiles/contours/tiles.json`
        });
        map.addLayer({
            'id': 'terrain-data',
            'type': 'line',
            'source': 'contours',
            'source-layer': 'contour',
            'layout': {
                'line-join': 'round',
                'line-cap': 'round'
            },
            'paint': {
                'line-color': '#ff69b4',
                'line-width': 1
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
    <title>Add a vector tile source</title>
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
            center: [-122.447303, 37.753574],
            zoom: 13
        });

        map.on('load', function () {
                map.addSource('contours', {
                    type: 'vector',
                    url:
                        `https://api.maptiler.com/tiles/contours/tiles.json`
                });
                map.addLayer({
                    'id': 'terrain-data',
                    'type': 'line',
                    'source': 'contours',
                    'source-layer': 'contour',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#ff69b4',
                        'line-width': 1
                    }
                });
            });
    </script>
</body>
</html>
```
