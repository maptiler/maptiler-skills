# Source: https://docs.maptiler.com/sdk-js/examples/fallback-image/

# Use a fallback image

Use a [`coalesce`](/gl-style-specification/expressions/#coalesce) expression to display another image when a requested image is not available.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('points', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [
                                -77.03238901390978,
                                38.913188059745586
                            ]
                        },
                        'properties': {
                            'title': 'Washington DC',
                            'icon': 'monument'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-79.9959, 40.4406]
                        },
                        'properties': {
                            'title': 'Pittsburgh',
                            'icon': 'bridges'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-76.2859, 36.8508]
                        },
                        'properties': {
                            'title': 'Norfolk',
                            'icon': 'harbor'
                        }
                    }
                ]
            }
        });
        map.addLayer({
            'id': 'points',
            'type': 'symbol',
            'source': 'points',
            'layout': {
                'icon-image': [
                    'coalesce',
                    ['image', ['concat', ['get', 'icon'], '-15']],
                    ['image', 'zoo']
                ],
                'text-field': ['get', 'title'],
                'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
                'text-offset': [0, 0.6],
                'text-anchor': 'top'
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
    <title>Use a fallback image</title>
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
            center: [-77, 38.75],
            zoom: 5
        });

        map.on('load', function () {
                map.addSource('points', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [
                                        -77.03238901390978,
                                        38.913188059745586
                                    ]
                                },
                                'properties': {
                                    'title': 'Washington DC',
                                    'icon': 'monument'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-79.9959, 40.4406]
                                },
                                'properties': {
                                    'title': 'Pittsburgh',
                                    'icon': 'bridges'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-76.2859, 36.8508]
                                },
                                'properties': {
                                    'title': 'Norfolk',
                                    'icon': 'harbor'
                                }
                            }
                        ]
                    }
                });
                map.addLayer({
                    'id': 'points',
                    'type': 'symbol',
                    'source': 'points',
                    'layout': {
                        'icon-image': [
                            'coalesce',
                            ['image', ['concat', ['get', 'icon'], '-15']],
                            ['image', 'zoo']
                        ],
                        'text-field': ['get', 'title'],
                        'text-font': ['Open Sans Semibold', 'Arial Unicode MS Bold'],
                        'text-offset': [0, 0.6],
                        'text-anchor': 'top'
                    }
                });
            });
    </script>
</body>
</html>
```
