# Source: https://docs.maptiler.com/sdk-js/examples/visualize-population-density/

# Visualize population density

Use a [variable binding expression](/gl-style-specification/expressions/#variable-binding) to calculate and display population density.

In this example, we use the population and area variables to create a choropleth map that visually represents the population density.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('rwanda-provinces', {
            'type': 'geojson',
            'data':
                'https://docs.maptiler.com/sdk-js/assets/rwanda-provinces.geojson'
        });
        map.addLayer({
            'id': 'rwanda-provinces',
            'type': 'fill',
            'source': 'rwanda-provinces',
            'layout': {},
            'paint': {
                'fill-color': [
                    'let',
                    'density',
                    ['/', ['get', 'population'], ['get', 'sq-km']],
                    [
                        'interpolate',
                        ['linear'],
                        ['zoom'],
                        8,
                        [
                            'interpolate',
                            ['linear'],
                            ['var', 'density'],
                            274,
                            ['to-color', '#edf8e9'],
                            1551,
                            ['to-color', '#006d2c']
                        ],
                        10,
                        [
                            'interpolate',
                            ['linear'],
                            ['var', 'density'],
                            274,
                            ['to-color', '#eff3ff'],
                            1551,
                            ['to-color', '#08519c']
                        ]
                    ]
                ],
                'fill-opacity': 0.7
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
    <title>Visualize population density</title>
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
            center: [30.0222, -1.9596],
            zoom: 7 // starting zoom
        });

        map.on('load', function () {
                map.addSource('rwanda-provinces', {
                    'type': 'geojson',
                    'data':
                        'https://docs.maptiler.com/sdk-js/assets/rwanda-provinces.geojson'
                });
                map.addLayer({
                    'id': 'rwanda-provinces',
                    'type': 'fill',
                    'source': 'rwanda-provinces',
                    'layout': {},
                    'paint': {
                        'fill-color': [
                            'let',
                            'density',
                            ['/', ['get', 'population'], ['get', 'sq-km']],
                            [
                                'interpolate',
                                ['linear'],
                                ['zoom'],
                                8,
                                [
                                    'interpolate',
                                    ['linear'],
                                    ['var', 'density'],
                                    274,
                                    ['to-color', '#edf8e9'],
                                    1551,
                                    ['to-color', '#006d2c']
                                ],
                                10,
                                [
                                    'interpolate',
                                    ['linear'],
                                    ['var', 'density'],
                                    274,
                                    ['to-color', '#eff3ff'],
                                    1551,
                                    ['to-color', '#08519c']
                                ]
                            ]
                        ],
                        'fill-opacity': 0.7
                    }
                });
            });
    </script>
</body>
</html>
```
