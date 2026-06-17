# Source: https://docs.maptiler.com/sdk-js/examples/polygon-popup-on-click/

# Show polygon information on click

When a user clicks on a polygon, a [`Popup`](/sdk-js/api/markers/#popup) will appear displaying additional details. This feature allows you to show the attributes of the selected element.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        // Add a source for the state polygons.
        map.addSource('states', {
            'type': 'geojson',
            'data':
                'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_shp.geojson'
        });

        // Add a layer showing the state polygons.
        map.addLayer({
            'id': 'states-layer',
            'type': 'fill',
            'source': 'states',
            'paint': {
                'fill-color': 'rgba(200, 100, 240, 0.4)',
                'fill-outline-color': 'rgba(200, 100, 240, 1)'
            }
        });

        // When a click event occurs on a feature in the states layer, open a popup at the
        // location of the click, with description HTML from its properties.
        map.on('click', 'states-layer', function (e) {
            new maptilersdk.Popup()
                .setLngLat(e.lngLat)
                .setHTML(e.features[0].properties.name)
                .addTo(map);
        });

        // Change the cursor to a pointer when the mouse is over the states layer.
        map.on('mouseenter', 'states-layer', function () {
            map.getCanvas().style.cursor = 'pointer';
        });

        // Change it back to a pointer when it leaves.
        map.on('mouseleave', 'states-layer', function () {
            map.getCanvas().style.cursor = '';
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
    <title>Show polygon information on click</title>
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
            center: [-100.04, 38.907],
            zoom: 3
        });

        map.on('load', function () {
                // Add a source for the state polygons.
                map.addSource('states', {
                    'type': 'geojson',
                    'data':
                        'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_1_states_provinces_shp.geojson'
                });

                // Add a layer showing the state polygons.
                map.addLayer({
                    'id': 'states-layer',
                    'type': 'fill',
                    'source': 'states',
                    'paint': {
                        'fill-color': 'rgba(200, 100, 240, 0.4)',
                        'fill-outline-color': 'rgba(200, 100, 240, 1)'
                    }
                });

                // When a click event occurs on a feature in the states layer, open a popup at the
                // location of the click, with description HTML from its properties.
                map.on('click', 'states-layer', function (e) {
                    new maptilersdk.Popup()
                        .setLngLat(e.lngLat)
                        .setHTML(e.features[0].properties.name)
                        .addTo(map);
                });

                // Change the cursor to a pointer when the mouse is over the states layer.
                map.on('mouseenter', 'states-layer', function () {
                    map.getCanvas().style.cursor = 'pointer';
                });

                // Change it back to a pointer when it leaves.
                map.on('mouseleave', 'states-layer', function () {
                    map.getCanvas().style.cursor = '';
                });
            });
    </script>
</body>
</html>
```
