# Source: https://docs.maptiler.com/sdk-js/examples/wms/

# Add a WMS source

Add an external [Web Map Service raster layer](https://www.ogc.org/standards/wms) to the map using the [`addSource`](/sdk-js/api/map/#map#addsource) function's [`tiles`](/gl-style-specification/sources/#raster-tiles) option. This will allow you to seamlessly integrate external content from the specified WMS URL into your map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.addSource('wms-test-source', {
            'type': 'raster',
            // use the tiles option to specify a WMS tile source URL
            // https://docs.maptiler.com/gl-style-specification/sources/
            'tiles': [
                'https://img.nj.gov/imagerywms/Natural2020?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&transparent=true&width=256&height=256&layers=Natural2020'
            ],
            'tileSize': 256
        });
        map.addLayer(
            {
                'id': 'wms-test-layer',
                'type': 'raster',
                'source': 'wms-test-source',
                'paint': {}
            },
            'Aeroway'
        );
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a WMS source</title>
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
            center: [-74.5447, 40.6892],
            zoom: 8
        });

        map.on('load', function () {
                map.addSource('wms-test-source', {
                    'type': 'raster',
                    // use the tiles option to specify a WMS tile source URL
                    // https://docs.maptiler.com/gl-style-specification/sources/
                    'tiles': [
                        'https://img.nj.gov/imagerywms/Natural2020?bbox={bbox-epsg-3857}&format=image/png&service=WMS&version=1.1.1&request=GetMap&srs=EPSG:3857&transparent=true&width=256&height=256&layers=Natural2020'
                    ],
                    'tileSize': 256
                });
                map.addLayer(
                    {
                        'id': 'wms-test-layer',
                        'type': 'raster',
                        'source': 'wms-test-source',
                        'paint': {}
                    },
                    'Aeroway'
                );
            });
    </script>
</body>
</html>
```
