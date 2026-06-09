# Source: https://docs.maptiler.com/sdk-js/examples/interactive-choropleth/

# Interactive Choropleth Map

Create an interactive choropleth map by utilizing events and feature states. Utilize events and [feature states](/sdk-js/api/map/#map#setfeaturestate) to develop an engaging choropleth map.

Enhance the level of interaction in your choropleth map by integrating an informative box that showcases the name of the state and its population density. Additionally, learn how to generate a legend that effectively represents the various values and categories depicted on the choropleth map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
let hoveredStateId = null;

    map.on('load', function () {
        map.addSource('states', {
            'type': 'geojson',
            'data':
                'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
        });

        // The feature-state dependent fill-opacity expression will render the hover effect
        // when a feature's hover state is set to true.
        map.addLayer({
            'id': 'state-fills',
            'type': 'fill',
            'source': 'states',
            'layout': {},
            'paint': {
                'fill-color': ["step",
                    ["get", "DENSITY"],
                    "#FFEDA0", 10,
                    "#FED976", 20,
                    "#FEB24C", 50,
                    "#FD8D3C", 100,
                    "#FC4E2A", 200,
                    "#E31A1C", 500,
                    "#BD0026", 1000,
                    "#800026"
                ],
                'fill-opacity': [
                    'case',
                    ['boolean', ['feature-state', 'hover'], false],
                    1,
                    0.8
                ],
                'fill-outline-color': "rgba(255, 255, 255, 0)"
            }
        });

        map.addLayer({
            'id': 'state-borders',
            'type': 'line',
            'source': 'states',
            'layout': {},
            'paint': {
                'line-color': '#FFFFFF',
                'line-width': [
                    'case',
                    ['boolean', ['feature-state', 'hover'], false],
                    3,
                    1
                ],
            }
        });

        // When the user moves their mouse over the state-fill layer, we'll update the
        // feature state for the feature under the mouse.
        map.on('mousemove', 'state-fills', function (e) {
            if (e.features.length > 0) {
                if (hoveredStateId) {
                    map.setFeatureState(
                        { source: 'states', id: hoveredStateId },
                        { hover: false }
                    );
                }
                hoveredStateId = e.features[0].id;
                map.setFeatureState(
                    { source: 'states', id: hoveredStateId },
                    { hover: true }
                );
            }
            document.getElementById('pd').innerHTML = `<h3>${e.features[0].properties.STATE_NAME}</h3>
            <p><strong><em>${e.features[0].properties.DENSITY}</strong> people per square mile</em></p>`;
        });

        // When the mouse leaves the state-fill layer, update the feature state of the
        // previously hovered feature.
        map.on('mouseleave', 'state-fills', function () {
            if (hoveredStateId) {
                map.setFeatureState(
                    { source: 'states', id: hoveredStateId },
                    { hover: false }
                );
            }
            hoveredStateId = null;
            document.getElementById('pd').innerHTML = `<p>Hover over a state!</p>`;
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
    <title>Interactive Choropleth Map</title>
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
            style: maptilersdk.MapStyle.DATAVIZ.LIGHT,
            center: [-100.486052, 37.830348],
            zoom: 3
        });

        let hoveredStateId = null;

            map.on('load', function () {
                map.addSource('states', {
                    'type': 'geojson',
                    'data':
                        'https://docs.maptiler.com/sdk-js/assets/us_states.geojson'
                });

                // The feature-state dependent fill-opacity expression will render the hover effect
                // when a feature's hover state is set to true.
                map.addLayer({
                    'id': 'state-fills',
                    'type': 'fill',
                    'source': 'states',
                    'layout': {},
                    'paint': {
                        'fill-color': ["step",
                            ["get", "DENSITY"],
                            "#FFEDA0", 10,
                            "#FED976", 20,
                            "#FEB24C", 50,
                            "#FD8D3C", 100,
                            "#FC4E2A", 200,
                            "#E31A1C", 500,
                            "#BD0026", 1000,
                            "#800026"
                        ],
                        'fill-opacity': [
                            'case',
                            ['boolean', ['feature-state', 'hover'], false],
                            1,
                            0.8
                        ],
                        'fill-outline-color': "rgba(255, 255, 255, 0)"
                    }
                });

                map.addLayer({
                    'id': 'state-borders',
                    'type': 'line',
                    'source': 'states',
                    'layout': {},
                    'paint': {
                        'line-color': '#FFFFFF',
                        'line-width': [
                            'case',
                            ['boolean', ['feature-state', 'hover'], false],
                            3,
                            1
                        ],
                    }
                });

                // When the user moves their mouse over the state-fill layer, we'll update the
                // feature state for the feature under the mouse.
                map.on('mousemove', 'state-fills', function (e) {
                    if (e.features.length > 0) {
                        if (hoveredStateId) {
                            map.setFeatureState(
                                { source: 'states', id: hoveredStateId },
                                { hover: false }
                            );
                        }
                        hoveredStateId = e.features[0].id;
                        map.setFeatureState(
                            { source: 'states', id: hoveredStateId },
                            { hover: true }
                        );
                    }
                    document.getElementById('pd').innerHTML = `<h3>${e.features[0].properties.STATE_NAME}</h3>
                    <p><strong><em>${e.features[0].properties.DENSITY}</strong> people per square mile</em></p>`;
                });

                // When the mouse leaves the state-fill layer, update the feature state of the
                // previously hovered feature.
                map.on('mouseleave', 'state-fills', function () {
                    if (hoveredStateId) {
                        map.setFeatureState(
                            { source: 'states', id: hoveredStateId },
                            { hover: false }
                        );
                    }
                    hoveredStateId = null;
                    document.getElementById('pd').innerHTML = `<p>Hover over a state!</p>`;
                });
            });
    </script>
</body>
</html>
```
