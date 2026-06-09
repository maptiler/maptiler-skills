# Source: https://docs.maptiler.com/sdk-js/examples/fill-pattern/

# Add a pattern to a polygon

Use the [`fill-pattern`](/gl-style-specification/layers/#paint-fill-fill-pattern) feature to draw a polygon by employing a repeating image pattern. This technique allows for the creation of visually appealing shapes by using a repeated image as a fill. To implement this, refer to the layer &#8702; fill &#8702; [fill-pattern](/gl-style-specification/layers/#fill-pattern) section in the GL Style Specification.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
        // Add GeoJSON data
        map.addSource('source', {
            'type': 'geojson',
            'data': {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                        [
                            [-30, -25],
                            [-30, 35],
                            [30, 35],
                            [30, -25],
                            [-30, -25]
                        ]
                    ]
                }
            }
        });

        // Load an image to use as the pattern
        const image = await map.loadImage(
            'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cat_silhouette.svg/64px-Cat_silhouette.svg.png');

        // Declare the image
        map.addImage('pattern', image.data);

        // Use it
        map.addLayer({
            'id': 'pattern-layer',
            'type': 'fill',
            'source': 'source',
            'paint': {
                'fill-pattern': 'pattern'
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
    <title>Add a pattern to a polygon</title>
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
            center: [0, 0],
            zoom: 1
        });

        map.on('load', async function () {
                // Add GeoJSON data
                map.addSource('source', {
                    'type': 'geojson',
                    'data': {
                        'type': 'Feature',
                        'properties': {},
                        'geometry': {
                            'type': 'Polygon',
                            'coordinates': [
                                [
                                    [-30, -25],
                                    [-30, 35],
                                    [30, 35],
                                    [30, -25],
                                    [-30, -25]
                                ]
                            ]
                        }
                    }
                });

                // Load an image to use as the pattern
                const image = await map.loadImage(
                    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Cat_silhouette.svg/64px-Cat_silhouette.svg.png');

                // Declare the image
                map.addImage('pattern', image.data);

                // Use it
                map.addLayer({
                    'id': 'pattern-layer',
                    'type': 'fill',
                    'source': 'source',
                    'paint': {
                        'fill-pattern': 'pattern'
                    }
                });
            });
    </script>
</body>
</html>
```
