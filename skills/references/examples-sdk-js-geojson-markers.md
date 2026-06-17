# Source: https://docs.maptiler.com/sdk-js/examples/geojson-markers/

# Draw GeoJSON points

Draw points from a GeoJSON collection to a map. In this example, we show the points with a custom image and display a label that shows the value of a property of the GeoJSON data.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
        // Add an image to use as a custom marker
        const image = await map.loadImage(
            'https://docs.maptiler.com/sdk-js/assets/osgeo-logo.png');

        map.addImage('custom-marker', image.data);
        // Add a GeoJSON source with 15 points
        map.addSource('conferences', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [100.4933, 13.7551]
                        },
                        'properties': { 'year': '2004' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [6.6523, 46.5535]
                        },
                        'properties': { 'year': '2006' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-123.3596, 48.4268]
                        },
                        'properties': { 'year': '2007' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [18.4264, -33.9224]
                        },
                        'properties': { 'year': '2008' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [151.195, -33.8552]
                        },
                        'properties': { 'year': '2009' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [2.1404, 41.3925]
                        },
                        'properties': { 'year': '2010' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-104.8548, 39.7644]
                        },
                        'properties': { 'year': '2011' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-1.1665, 52.9539]
                        },
                        'properties': { 'year': '2013' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-122.6544, 45.5428]
                        },
                        'properties': { 'year': '2014' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [126.974, 37.5651]
                        },
                        'properties': { 'year': '2015' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [7.1112, 50.7255]
                        },
                        'properties': { 'year': '2016' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-71.0314, 42.3539]
                        },
                        'properties': { 'year': '2017' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [39.2794, -6.8173]
                        },
                        'properties': { 'year': '2018' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [26.0961, 44.4379]
                        },
                        'properties': { 'year': '2019' }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-114.0879, 51.0279]
                        },
                        'properties': { 'year': '2020' }
                    }
                ]
            }
        });

        // Add a symbol layer
        map.addLayer({
            'id': 'conferences',
            'type': 'symbol',
            'source': 'conferences',
            'layout': {
                'icon-image': 'custom-marker',
                // get the year from the source's "year" property
                'text-field': ['get', 'year'],
                'text-font': [
                    'Open Sans Semibold',
                    'Arial Unicode MS Bold'
                ],
                'text-offset': [0, 1.25],
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
    <title>Draw GeoJSON points</title>
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
            style: maptilersdk.MapStyle.BASE.LIGHT,
            center: [0, 0],
            zoom: 1
        });

        map.on('load', async function () {
                // Add an image to use as a custom marker
                const image = await map.loadImage(
                    'https://docs.maptiler.com/sdk-js/assets/osgeo-logo.png');

                map.addImage('custom-marker', image.data);
                // Add a GeoJSON source with 15 points
                map.addSource('conferences', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [100.4933, 13.7551]
                                },
                                'properties': { 'year': '2004' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [6.6523, 46.5535]
                                },
                                'properties': { 'year': '2006' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-123.3596, 48.4268]
                                },
                                'properties': { 'year': '2007' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [18.4264, -33.9224]
                                },
                                'properties': { 'year': '2008' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [151.195, -33.8552]
                                },
                                'properties': { 'year': '2009' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [2.1404, 41.3925]
                                },
                                'properties': { 'year': '2010' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-104.8548, 39.7644]
                                },
                                'properties': { 'year': '2011' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-1.1665, 52.9539]
                                },
                                'properties': { 'year': '2013' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-122.6544, 45.5428]
                                },
                                'properties': { 'year': '2014' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [126.974, 37.5651]
                                },
                                'properties': { 'year': '2015' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [7.1112, 50.7255]
                                },
                                'properties': { 'year': '2016' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-71.0314, 42.3539]
                                },
                                'properties': { 'year': '2017' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [39.2794, -6.8173]
                                },
                                'properties': { 'year': '2018' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [26.0961, 44.4379]
                                },
                                'properties': { 'year': '2019' }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-114.0879, 51.0279]
                                },
                                'properties': { 'year': '2020' }
                            }
                        ]
                    }
                });

                // Add a symbol layer
                map.addLayer({
                    'id': 'conferences',
                    'type': 'symbol',
                    'source': 'conferences',
                    'layout': {
                        'icon-image': 'custom-marker',
                        // get the year from the source's "year" property
                        'text-field': ['get', 'year'],
                        'text-font': [
                            'Open Sans Semibold',
                            'Arial Unicode MS Bold'
                        ],
                        'text-offset': [0, 1.25],
                        'text-anchor': 'top'
                    }
                });
            });
    </script>
</body>
</html>
```
