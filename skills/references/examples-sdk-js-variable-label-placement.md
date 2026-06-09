# Source: https://docs.maptiler.com/sdk-js/examples/variable-label-placement/

# Variable label placement

Use [`text-variable-anchor`](/gl-style-specification/layers/#layout-symbol-text-variable-anchor) feature to enable the relocation of high-priority labels to ensure their visibility on the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        // Add a GeoJSON source containing place coordinates and information.
        map.addSource('places', {
            'type': 'geojson',
            'data': places
        });

        map.addLayer({
            'id': 'poi-labels',
            'type': 'symbol',
            'source': 'places',
            'layout': {
                'text-field': ['get', 'description'],
                'text-variable-anchor': ['top', 'bottom', 'left', 'right'],
                'text-radial-offset': 0.5,
                'text-justify': 'auto',
                'icon-image': ['get', 'icon']
            }
        });

        map.rotateTo(180, { duration: 10000 });
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Variable label placement</title>
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
            center: [-77.04, 38.907],
            zoom: 11.15
        });

        map.on('load', function () {
                // Add a GeoJSON source containing place coordinates and information.
                map.addSource('places', {
                    'type': 'geojson',
                    'data': places
                });

                map.addLayer({
                    'id': 'poi-labels',
                    'type': 'symbol',
                    'source': 'places',
                    'layout': {
                        'text-field': ['get', 'description'],
                        'text-variable-anchor': ['top', 'bottom', 'left', 'right'],
                        'text-radial-offset': 0.5,
                        'text-justify': 'auto',
                        'icon-image': ['get', 'icon']
                    }
                });

                map.rotateTo(180, { duration: 10000 });
            });
    </script>
</body>
</html>
```
