# Source: https://docs.maptiler.com/sdk-js/examples/center-on-symbol/

# Center the map on a clicked symbol

Use events and [`flyTo`](/sdk-js/api/map/#map#flyto) to center the map on a [`symbol`](/gl-style-specification/layers/#symbol).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
        // Add an image to use as a custom marker
        const image = await map.loadImage(
            'https://docs.maptiler.com/sdk-js/assets/custom_marker.png');
        map.addImage('custom-marker', image.data);
        // Add a GeoJSON source with 3 points.
        map.addSource('points', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'properties': {},
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [
                                -91.395263671875,
                                -0.9145729757782163
                            ]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {},
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [
                                -90.32958984375,
                                -0.6344474832838974
                            ]
                        }
                    },
                    {
                        'type': 'Feature',
                        'properties': {},
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [
                                -91.34033203125,
                                0.01647949196029245
                            ]
                        }
                    }
                ]
            }
        });

        // Add a symbol layer
        map.addLayer({
            'id': 'symbols',
            'type': 'symbol',
            'source': 'points',
            'layout': {
                'icon-image': 'custom-marker'
            }
        });

        // Center the map on the coordinates of any clicked symbol from the 'symbols' layer.
        map.on('click', 'symbols', function (e) {
            map.flyTo({
                center: e.features[0].geometry.coordinates
            });
        });

        // Change the cursor to a pointer when the it enters a feature in the 'symbols' layer.
        map.on('mouseenter', 'symbols', function () {
            map.getCanvas().style.cursor = 'pointer';
        });

        // Change it back to a pointer when it leaves.
        map.on('mouseleave', 'symbols', function () {
            map.getCanvas().style.cursor = '';
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
    <title>Center the map on a clicked symbol</title>
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
            center: [-90.96, -0.47],
            zoom: 7.5
        });

        map.on('load', async function () {
                // Add an image to use as a custom marker
                const image = await map.loadImage(
                    'https://docs.maptiler.com/sdk-js/assets/custom_marker.png');
                map.addImage('custom-marker', image.data);
                // Add a GeoJSON source with 3 points.
                map.addSource('points', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'properties': {},
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [
                                        -91.395263671875,
                                        -0.9145729757782163
                                    ]
                                }
                            },
                            {
                                'type': 'Feature',
                                'properties': {},
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [
                                        -90.32958984375,
                                        -0.6344474832838974
                                    ]
                                }
                            },
                            {
                                'type': 'Feature',
                                'properties': {},
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [
                                        -91.34033203125,
                                        0.01647949196029245
                                    ]
                                }
                            }
                        ]
                    }
                });

                // Add a symbol layer
                map.addLayer({
                    'id': 'symbols',
                    'type': 'symbol',
                    'source': 'points',
                    'layout': {
                        'icon-image': 'custom-marker'
                    }
                });

                // Center the map on the coordinates of any clicked symbol from the 'symbols' layer.
                map.on('click', 'symbols', function (e) {
                    map.flyTo({
                        center: e.features[0].geometry.coordinates
                    });
                });

                // Change the cursor to a pointer when the it enters a feature in the 'symbols' layer.
                map.on('mouseenter', 'symbols', function () {
                    map.getCanvas().style.cursor = 'pointer';
                });

                // Change it back to a pointer when it leaves.
                map.on('mouseleave', 'symbols', function () {
                    map.getCanvas().style.cursor = '';
                });
            });
    </script>
</body>
</html>
```
