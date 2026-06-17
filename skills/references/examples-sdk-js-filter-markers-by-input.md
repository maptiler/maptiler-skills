# Source: https://docs.maptiler.com/sdk-js/examples/filter-markers-by-input/

# Filter symbols by text input

Filter [symbols](/gl-style-specification/layers/#symbol) by icon name by typing in a text input.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      // Add a GeoJSON source containing place coordinates and information.
      map.addSource('places', {
        'type': 'geojson',
        'data': places
      });

      places.features.forEach(function (feature) {
        const symbol = feature.properties['icon'];
        const layerID = 'poi-' + symbol;

        // Add a layer for this symbol type if it hasn't been added already.
        if (!map.getLayer(layerID)) {
          map.addLayer({
            'id': layerID,
            'type': 'symbol',
            'source': 'places',
            'layout': {
              'icon-image': symbol,
              'icon-overlap': 'always',
              'text-field': symbol,
              'text-font': [
                'Open Sans Bold',
                'Arial Unicode MS Bold'
              ],
              'text-size': 11,
              'text-transform': 'uppercase',
              'text-letter-spacing': 0.05,
              'text-offset': [0, 1.5]
            },
            'paint': {
              'text-color': '#202',
              'text-halo-color': '#fff',
              'text-halo-width': 2
            },
            'filter': ['==', 'icon', symbol]
          });

          layerIDs.push(layerID);
        }
      });

      filterInput.addEventListener('keyup', function (e) {
        // If the input value matches a layerID set
        // it's visibility to 'visible' or else hide it.
        const value = e.target.value.trim().toLowerCase();
        layerIDs.forEach(function (layerID) {
          map.setLayoutProperty(
            layerID,
            'visibility',
            layerID.indexOf(value) > -1 ? 'visible' : 'none'
          );
        });
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
    <title>Filter symbols by text input</title>
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

              places.features.forEach(function (feature) {
                const symbol = feature.properties['icon'];
                const layerID = 'poi-' + symbol;

                // Add a layer for this symbol type if it hasn't been added already.
                if (!map.getLayer(layerID)) {
                  map.addLayer({
                    'id': layerID,
                    'type': 'symbol',
                    'source': 'places',
                    'layout': {
                      'icon-image': symbol,
                      'icon-overlap': 'always',
                      'text-field': symbol,
                      'text-font': [
                        'Open Sans Bold',
                        'Arial Unicode MS Bold'
                      ],
                      'text-size': 11,
                      'text-transform': 'uppercase',
                      'text-letter-spacing': 0.05,
                      'text-offset': [0, 1.5]
                    },
                    'paint': {
                      'text-color': '#202',
                      'text-halo-color': '#fff',
                      'text-halo-width': 2
                    },
                    'filter': ['==', 'icon', symbol]
                  });

                  layerIDs.push(layerID);
                }
              });

              filterInput.addEventListener('keyup', function (e) {
                // If the input value matches a layerID set
                // it's visibility to 'visible' or else hide it.
                const value = e.target.value.trim().toLowerCase();
                layerIDs.forEach(function (layerID) {
                  map.setLayoutProperty(
                    layerID,
                    'visibility',
                    layerID.indexOf(value) > -1 ? 'visible' : 'none'
                  );
                });
              });
            });
    </script>
</body>
</html>
```
