# Source: https://docs.maptiler.com/sdk-js/examples/line-across-180th-meridian/

# Display line that crosses 180th meridian

Draw a line across the 180th meridian using a [GeoJSON source](/gl-style-specification/sources/#geojson).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addLayer({
            'id': 'route',
            'type': 'line',
            'source': {
                'type': 'geojson',
                'data': {
                    'type': 'Feature',
                    'properties': {},
                    'geometry': createGeometry(false)
                }
            },
            'layout': { 'line-cap': 'round' },
            'paint': {
                'line-color': '#007296',
                'line-width': 4
            }
        });

        map.addLayer({
            'id': 'route-label',
            'type': 'symbol',
            'source': 'route',
            'layout': {
                'symbol-placement': 'line-center',
                'text-field': 'Crosses the world'
            }
        });

        map.addLayer({
            'id': 'route-two',
            'type': 'line',
            'source': {
                'type': 'geojson',
                'data': {
                    'type': 'Feature',
                    'properties': {},
                    'geometry': createGeometry(true)
                }
            },
            'layout': { 'line-cap': 'round' },
            'paint': {
                'line-color': '#F06317',
                'line-width': 4
            }
        });

        map.addLayer({
            'id': 'route-two-label',
            'type': 'symbol',
            'source': 'route-two',
            'layout': {
                'symbol-placement': 'line-center',
                'text-field': 'Crosses 180th meridian'
            }
        });

        function createGeometry(doesCrossAntimeridian) {
            const geometry = {
                'type': 'LineString',
                'coordinates': [
                    [-72.42187, -16.59408],
                    [140.27343, 35.67514]
                ]
            };

            // To draw a line across the 180th meridian,
            // if the longitude of the second point minus
            // the longitude of original (or previous) point is >= 180,
            // subtract 360 from the longitude of the second point.
            // If it is less than 180, add 360 to the second point.

            if (doesCrossAntimeridian) {
                const startLng = geometry.coordinates[0][0];
                const endLng = geometry.coordinates[1][0];

                if (endLng - startLng >= 180) {
                    geometry.coordinates[1][0] -= 360;
                } else if (endLng - startLng < 180) {
                    geometry.coordinates[1][0] += 360;
                }
            }

            return geometry;
        }
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display line that crosses 180th meridian</title>
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
            center: [-41.62667, 26.11598],
            zoom: 0
        });

        map.on('load', function () {
                map.addLayer({
                    'id': 'route',
                    'type': 'line',
                    'source': {
                        'type': 'geojson',
                        'data': {
                            'type': 'Feature',
                            'properties': {},
                            'geometry': createGeometry(false)
                        }
                    },
                    'layout': { 'line-cap': 'round' },
                    'paint': {
                        'line-color': '#007296',
                        'line-width': 4
                    }
                });

                map.addLayer({
                    'id': 'route-label',
                    'type': 'symbol',
                    'source': 'route',
                    'layout': {
                        'symbol-placement': 'line-center',
                        'text-field': 'Crosses the world'
                    }
                });

                map.addLayer({
                    'id': 'route-two',
                    'type': 'line',
                    'source': {
                        'type': 'geojson',
                        'data': {
                            'type': 'Feature',
                            'properties': {},
                            'geometry': createGeometry(true)
                        }
                    },
                    'layout': { 'line-cap': 'round' },
                    'paint': {
                        'line-color': '#F06317',
                        'line-width': 4
                    }
                });

                map.addLayer({
                    'id': 'route-two-label',
                    'type': 'symbol',
                    'source': 'route-two',
                    'layout': {
                        'symbol-placement': 'line-center',
                        'text-field': 'Crosses 180th meridian'
                    }
                });

                function createGeometry(doesCrossAntimeridian) {
                    const geometry = {
                        'type': 'LineString',
                        'coordinates': [
                            [-72.42187, -16.59408],
                            [140.27343, 35.67514]
                        ]
                    };

                    // To draw a line across the 180th meridian,
                    // if the longitude of the second point minus
                    // the longitude of original (or previous) point is >= 180,
                    // subtract 360 from the longitude of the second point.
                    // If it is less than 180, add 360 to the second point.

                    if (doesCrossAntimeridian) {
                        const startLng = geometry.coordinates[0][0];
                        const endLng = geometry.coordinates[1][0];

                        if (endLng - startLng >= 180) {
                            geometry.coordinates[1][0] -= 360;
                        } else if (endLng - startLng < 180) {
                            geometry.coordinates[1][0] += 360;
                        }
                    }

                    return geometry;
                }
            });
    </script>
</body>
</html>
```
