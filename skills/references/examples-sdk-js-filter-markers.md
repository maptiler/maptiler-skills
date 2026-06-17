# Source: https://docs.maptiler.com/sdk-js/examples/filter-markers/

# Filter symbols by toggling a list

Filter a set of [symbols](/gl-style-specification/layers/#symbol) based on a property value in the data.

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
              'icon-overlap': 'always'
            },
            'filter': ['==', 'icon', symbol]
          });

          // Add checkbox and label elements for the layer.
          const input = document.createElement('input');
          input.type = 'checkbox';
          input.id = layerID;
          input.checked = true;
          filterGroup.appendChild(input);

          const label = document.createElement('label');
          label.setAttribute('for', layerID);
          label.textContent = symbol;
          filterGroup.appendChild(label);

          // When the checkbox changes, update the visibility of the layer.
          input.addEventListener('change', function (e) {
            map.setLayoutProperty(
              layerID,
              'visibility',
              e.target.checked ? 'visible' : 'none'
            );
          });
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
    <title>Filter symbols by toggling a list</title>
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
                      'icon-overlap': 'always'
                    },
                    'filter': ['==', 'icon', symbol]
                  });

                  // Add checkbox and label elements for the layer.
                  const input = document.createElement('input');
                  input.type = 'checkbox';
                  input.id = layerID;
                  input.checked = true;
                  filterGroup.appendChild(input);

                  const label = document.createElement('label');
                  label.setAttribute('for', layerID);
                  label.textContent = symbol;
                  filterGroup.appendChild(label);

                  // When the checkbox changes, update the visibility of the layer.
                  input.addEventListener('change', function (e) {
                    map.setLayoutProperty(
                      layerID,
                      'visibility',
                      e.target.checked ? 'visible' : 'none'
                    );
                  });
                }
              });
            });
    </script>
</body>
</html>
```
