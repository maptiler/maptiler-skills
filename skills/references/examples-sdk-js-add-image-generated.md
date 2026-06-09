# Source: https://docs.maptiler.com/sdk-js/examples/add-image-generated/

# Add a generated icon to the map

Add an icon to the map that was generated at runtime.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        const width = 64; // The image will be 64 pixels square
        const bytesPerPixel = 4; // Each pixel is represented by 4 bytes: red, green, blue, and alpha.
        const data = new Uint8Array(width * width * bytesPerPixel);

        for (let x = 0; x < width; x++) {
            for (let  y = 0; y < width; y++) {
                const offset = (y * width + x) * bytesPerPixel;
                data[offset + 0] = (y / width) * 255; // red
                data[offset + 1] = (x / width) * 255; // green
                data[offset + 2] = 128; // blue
                data[offset + 3] = 255; // alpha
            }
        }

        map.addImage('gradient', { width: width, height: width, data: data });

        map.addSource('point', {
            'type': 'geojson',
            'data': {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [0, 0]
                        }
                    }
                ]
            }
        });
        map.addLayer({
            'id': 'points',
            'type': 'symbol',
            'source': 'point',
            'layout': {
                'icon-image': 'gradient'
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
    <title>Add a generated icon to the map</title>
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

        map.on('load', function () {
                const width = 64; // The image will be 64 pixels square
                const bytesPerPixel = 4; // Each pixel is represented by 4 bytes: red, green, blue, and alpha.
                const data = new Uint8Array(width * width * bytesPerPixel);

                for (let x = 0; x < width; x++) {
                    for (let  y = 0; y < width; y++) {
                        const offset = (y * width + x) * bytesPerPixel;
                        data[offset + 0] = (y / width) * 255; // red
                        data[offset + 1] = (x / width) * 255; // green
                        data[offset + 2] = 128; // blue
                        data[offset + 3] = 255; // alpha
                    }
                }

                map.addImage('gradient', { width: width, height: width, data: data });

                map.addSource('point', {
                    'type': 'geojson',
                    'data': {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'geometry': {
                                    'type': 'Point',
                                    'coordinates': [0, 0]
                                }
                            }
                        ]
                    }
                });
                map.addLayer({
                    'id': 'points',
                    'type': 'symbol',
                    'source': 'point',
                    'layout': {
                        'icon-image': 'gradient'
                    }
                });
            });
    </script>
</body>
</html>
```
