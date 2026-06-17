# Source: https://docs.maptiler.com/sdk-js/examples/canvas-source/

# Add a canvas source

Add a [`CanvasSource`](/sdk-js/api/sources/#canvassource) to the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('canvas-source', {
            type: 'canvas',
            canvas: 'canvasID',
            coordinates: [
                [91.4461, 21.5006],
                [100.3541, 21.5006],
                [100.3541, 13.9706],
                [91.4461, 13.9706]
            ],
            // Set to true if the canvas source is animated. If the canvas is static, animate should be set to false to improve performance.
            animate: true
        });

        map.addLayer({
            id: 'canvas-layer',
            type: 'raster',
            source: 'canvas-source'
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
    <title>Add a canvas source</title>
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
            center: [95.899147, 18.088694],
            zoom: 5
        });

        map.on('load', function () {
                map.addSource('canvas-source', {
                    type: 'canvas',
                    canvas: 'canvasID',
                    coordinates: [
                        [91.4461, 21.5006],
                        [100.3541, 21.5006],
                        [100.3541, 13.9706],
                        [91.4461, 13.9706]
                    ],
                    // Set to true if the canvas source is animated. If the canvas is static, animate should be set to false to improve performance.
                    animate: true
                });

                map.addLayer({
                    id: 'canvas-layer',
                    type: 'raster',
                    source: 'canvas-source'
                });
            });
    </script>
</body>
</html>
```
