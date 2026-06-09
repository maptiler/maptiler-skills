# Source: https://docs.maptiler.com/sdk-js/examples/add-image-missing-generated/

# Generate and add a missing icon to the map

Dynamically generate a missing icon at runtime and add it to the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('styleimagemissing', function (e) {
        const id = e.id; // id of the missing image

        // check if this missing icon is one this function can generate
        const prefix = 'square-rgb-';
        if (id.indexOf(prefix) !== 0) return;

        // extract the color from the id
        const rgb = id.replace(prefix, '').split(',').map(Number);

        const width = 64; // The image will be 64 pixels square
        const bytesPerPixel = 4; // Each pixel is represented by 4 bytes: red, green, blue, and alpha.
        const data = new Uint8Array(width * width * bytesPerPixel);

        for (let x = 0; x < width; x++) {
            for (let  y = 0; y < width; y++) {
                const offset = (y * width + x) * bytesPerPixel;
                data[offset + 0] = rgb[0]; // red
                data[offset + 1] = rgb[1]; // green
                data[offset + 2] = rgb[2]; // blue
                data[offset + 3] = 255; // alpha
            }
        }

        map.addImage(id, { width: width, height: width, data: data });
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
                            'coordinates': [0, 0]
                        },
                        'properties': {
                            'color': '255,0,0'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [50, 0]
                        },
                        'properties': {
                            'color': '255,209,28'
                        }
                    },
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [-50, 0]
                        },
                        'properties': {
                            'color': '242,127,32'
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
                'icon-image': ['concat', 'square-rgb-', ['get', 'color']]
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
    <title>Generate and add a missing icon to the map</title>
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
            zoom: 2
        });

        map.on('styleimagemissing', function (e) {
                const id = e.id; // id of the missing image

                // check if this missing icon is one this function can generate
                const prefix = 'square-rgb-';
                if (id.indexOf(prefix) !== 0) return;

                // extract the color from the id
                const rgb = id.replace(prefix, '').split(',').map(Number);

                const width = 64; // The image will be 64 pixels square
                const bytesPerPixel = 4; // Each pixel is represented by 4 bytes: red, green, blue, and alpha.
                const data = new Uint8Array(width * width * bytesPerPixel);

                for (let x = 0; x < width; x++) {
                    for (let  y = 0; y < width; y++) {
                        const offset = (y * width + x) * bytesPerPixel;
                        data[offset + 0] = rgb[0]; // red
                        data[offset + 1] = rgb[1]; // green
                        data[offset + 2] = rgb[2]; // blue
                        data[offset + 3] = 255; // alpha
                    }
                }

                map.addImage(id, { width: width, height: width, data: data });
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
                                    'coordinates': [0, 0]
                                },
                                'properties': {
                                    'color': '255,0,0'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [50, 0]
                                },
                                'properties': {
                                    'color': '255,209,28'
                                }
                            },
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [-50, 0]
                                },
                                'properties': {
                                    'color': '242,127,32'
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
                        'icon-image': ['concat', 'square-rgb-', ['get', 'color']]
                    }
                });
            });
    </script>
</body>
</html>
```
