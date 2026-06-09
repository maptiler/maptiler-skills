# Source: https://docs.maptiler.com/sdk-js/examples/live-update-feature/

# Update a feature in realtime

Change an existing feature on your map in real-time by updating its data.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        // We use D3 to fetch the JSON here so that we can parse and use it separately
        // from GL JS's use in the added source. You can use any request method (library
        // or otherwise) that you want.
        d3.json(
            'https://docs.maptiler.com/sdk-js/assets/hike.geojson',
            function (err, data) {
                if (err) throw err;

                // save full coordinate list for later
                const coordinates = data.features[0].geometry.coordinates;

                // start by showing just the first coordinate
                data.features[0].geometry.coordinates = [coordinates[0]];

                // add it to the map
                map.addSource('trace', { type: 'geojson', data: data });
                map.addLayer({
                    'id': 'trace',
                    'type': 'line',
                    'source': 'trace',
                    'paint': {
                        'line-color': 'yellow',
                        'line-opacity': 0.75,
                        'line-width': 5
                    }
                });

                // setup the viewport
                map.jumpTo({ 'center': coordinates[0], 'zoom': 14 });
                map.setPitch(30);

                // on a regular basis, add more coordinates from the saved list and update the map
                let i = 0;
                const timer = window.setInterval(function () {
                    if (i < coordinates.length) {
                        data.features[0].geometry.coordinates.push(
                            coordinates[i]
                        );
                        map.getSource('trace').setData(data);
                        map.panTo(coordinates[i]);
                        i++;
                    } else {
                        window.clearInterval(timer);
                    }
                }, 10);
            }
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
    <title>Update a feature in realtime</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://d3js.org/d3.v3.min.js"></script>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [0, 0],
            zoom: 0
        });

        map.on('load', function () {
                // We use D3 to fetch the JSON here so that we can parse and use it separately
                // from GL JS's use in the added source. You can use any request method (library
                // or otherwise) that you want.
                d3.json(
                    'https://docs.maptiler.com/sdk-js/assets/hike.geojson',
                    function (err, data) {
                        if (err) throw err;

                        // save full coordinate list for later
                        const coordinates = data.features[0].geometry.coordinates;

                        // start by showing just the first coordinate
                        data.features[0].geometry.coordinates = [coordinates[0]];

                        // add it to the map
                        map.addSource('trace', { type: 'geojson', data: data });
                        map.addLayer({
                            'id': 'trace',
                            'type': 'line',
                            'source': 'trace',
                            'paint': {
                                'line-color': 'yellow',
                                'line-opacity': 0.75,
                                'line-width': 5
                            }
                        });

                        // setup the viewport
                        map.jumpTo({ 'center': coordinates[0], 'zoom': 14 });
                        map.setPitch(30);

                        // on a regular basis, add more coordinates from the saved list and update the map
                        let i = 0;
                        const timer = window.setInterval(function () {
                            if (i < coordinates.length) {
                                data.features[0].geometry.coordinates.push(
                                    coordinates[i]
                                );
                                map.getSource('trace').setData(data);
                                map.panTo(coordinates[i]);
                                i++;
                            } else {
                                window.clearInterval(timer);
                            }
                        }, 10);
                    }
                );
            });
    </script>
</body>
</html>
```
