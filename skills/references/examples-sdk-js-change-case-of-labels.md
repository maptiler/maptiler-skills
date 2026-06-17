# Source: https://docs.maptiler.com/sdk-js/examples/change-case-of-labels/

# Change the case of labels

Use the [`upcase`](/gl-style-specification/expressions/#upcase) and [`downcase`](/gl-style-specification/expressions/#downcase) expressions to change the case of labels.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        // data from opendata.cityofboise.org/
        map.addSource('off-leash-areas', {
            'type': 'geojson',
            'data':
                'https://docs.maptiler.com/sdk-js/assets/boise.geojson'
        });
        map.addLayer({
            'id': 'off-leash-areas',
            'type': 'symbol',
            'source': 'off-leash-areas',
            'layout': {
                'icon-image': 'dog-park-11',
                'text-field': [
                    'format',
                    ['upcase', ['get', 'FacilityName']],
                    { 'font-scale': 0.8 },
                    '\n',
                    {},
                    ['downcase', ['get', 'Comments']],
                    { 'font-scale': 0.6 }
                ],
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
    <title>Change the case of labels</title>
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
            center: [-116.231, 43.604],
            zoom: 11 // starting zoom
        });

        map.on('load', function () {
                // data from opendata.cityofboise.org/
                map.addSource('off-leash-areas', {
                    'type': 'geojson',
                    'data':
                        'https://docs.maptiler.com/sdk-js/assets/boise.geojson'
                });
                map.addLayer({
                    'id': 'off-leash-areas',
                    'type': 'symbol',
                    'source': 'off-leash-areas',
                    'layout': {
                        'icon-image': 'dog-park-11',
                        'text-field': [
                            'format',
                            ['upcase', ['get', 'FacilityName']],
                            { 'font-scale': 0.8 },
                            '\n',
                            {},
                            ['downcase', ['get', 'Comments']],
                            { 'font-scale': 0.6 }
                        ],
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
