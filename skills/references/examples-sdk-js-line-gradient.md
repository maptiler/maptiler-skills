# Source: https://docs.maptiler.com/sdk-js/examples/line-gradient/

# Create a gradient line using an expression

Use the [`line-gradient`](/gl-style-specification/layers/#paint-line-line-gradient) paint property and an expression to visualize distance from the starting point of a line.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                    'coordinates': [
                        [-77.044211, 38.852924],
                        [-77.045659, 38.860158],
                        [-77.044232, 38.862326],
                        [-77.040879, 38.865454],
                        [-77.039936, 38.867698],
                        [-77.040338, 38.86943],
                        [-77.04264, 38.872528],
                        [-77.03696, 38.878424],
                        [-77.032309, 38.87937],
                        [-77.030056, 38.880945],
                        [-77.027645, 38.881779],
                        [-77.026946, 38.882645],
                        [-77.026942, 38.885502],
                        [-77.028054, 38.887449],
                        [-77.02806, 38.892088],
                        [-77.03364, 38.892108],
                        [-77.033643, 38.899926]
                    ],
                    'type': 'LineString'
                }
            }
        ]
    };

    map.on('load', function () {
        // 'line-gradient' can only be used with GeoJSON sources
        // and the source must have the 'lineMetrics' option set to true
        map.addSource('line', {
            type: 'geojson',
            lineMetrics: true,
            data: geojson
        });

        // the layer must be of type 'line'
        map.addLayer({
            type: 'line',
            source: 'line',
            id: 'line',
            paint: {
                'line-color': 'red',
                'line-width': 14,
                // 'line-gradient' must be specified using an expression
                // with the special 'line-progress' property
                'line-gradient': [
                    'interpolate',
                    ['linear'],
                    ['line-progress'],
                    0,
                    'blue',
                    0.1,
                    'royalblue',
                    0.3,
                    'cyan',
                    0.5,
                    'lime',
                    0.7,
                    'yellow',
                    1,
                    'red'
                ]
            },
            layout: {
                'line-cap': 'round',
                'line-join': 'round'
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
    <title>Create a gradient line using an expression</title>
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
            center: [-77.035, 38.875],
            zoom: 12
        });

        const geojson = {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'properties': {},
                        'geometry': {
                            'coordinates': [
                                [-77.044211, 38.852924],
                                [-77.045659, 38.860158],
                                [-77.044232, 38.862326],
                                [-77.040879, 38.865454],
                                [-77.039936, 38.867698],
                                [-77.040338, 38.86943],
                                [-77.04264, 38.872528],
                                [-77.03696, 38.878424],
                                [-77.032309, 38.87937],
                                [-77.030056, 38.880945],
                                [-77.027645, 38.881779],
                                [-77.026946, 38.882645],
                                [-77.026942, 38.885502],
                                [-77.028054, 38.887449],
                                [-77.02806, 38.892088],
                                [-77.03364, 38.892108],
                                [-77.033643, 38.899926]
                            ],
                            'type': 'LineString'
                        }
                    }
                ]
            };

            map.on('load', function () {
                // 'line-gradient' can only be used with GeoJSON sources
                // and the source must have the 'lineMetrics' option set to true
                map.addSource('line', {
                    type: 'geojson',
                    lineMetrics: true,
                    data: geojson
                });

                // the layer must be of type 'line'
                map.addLayer({
                    type: 'line',
                    source: 'line',
                    id: 'line',
                    paint: {
                        'line-color': 'red',
                        'line-width': 14,
                        // 'line-gradient' must be specified using an expression
                        // with the special 'line-progress' property
                        'line-gradient': [
                            'interpolate',
                            ['linear'],
                            ['line-progress'],
                            0,
                            'blue',
                            0.1,
                            'royalblue',
                            0.3,
                            'cyan',
                            0.5,
                            'lime',
                            0.7,
                            'yellow',
                            1,
                            'red'
                        ]
                    },
                    layout: {
                        'line-cap': 'round',
                        'line-join': 'round'
                    }
                });
            });
    </script>
</body>
</html>
```
