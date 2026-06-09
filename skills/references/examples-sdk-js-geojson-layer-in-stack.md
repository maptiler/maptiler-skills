# Source: https://docs.maptiler.com/sdk-js/examples/geojson-layer-in-stack/

# Add a new layer below labels

By utilizing the second parameter of the [`addLayer`](/sdk-js/api/map/#map#addlayer) function in the SDK-JS API, you can enhance the accuracy of adding a new layer beneath the labels or any other desire layer. This allows for more precise placement and control over the layer's position in relation to the rest of the map layers.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
    const layers = map.getStyle().layers;
    // Find the index of the first symbol layer in the map style
    // This approach works with our simple map styles for more advanced styles, e.g., Outdoor.
    // We recommend directly inserting the name of the last layer above your data. 
    // See the Learn more section below.
    const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

    map.addSource('urban-areas', {
      'type': 'geojson',
      'data':
        'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_urban_areas.geojson'
    });
    map.addLayer(
      {
        'id': 'urban-areas-fill',
        'type': 'fill',
        'source': 'urban-areas',
        'layout': {},
        'paint': {
          'fill-color': '#f08',
          'fill-opacity': 0.4
        }
        // This is the important part of this example: the addLayer
        // method takes 2 arguments: the layer as an object, and a string
        // representing another layer's name. if the other layer
        // exists in the stylesheet already, the new layer will be positioned
        // right before that layer in the stack, making it possible to put
        // 'overlays' anywhere in the layer stack.
        // Insert the layer beneath the first symbol layer.
      },
      firstSymbolId
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
    <title>Add a new layer below labels</title>
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
            center: [-88.13734351262877, 35.137451890638886],
            zoom: 4
        });

        map.on('load', function () {
            const layers = map.getStyle().layers;
            // Find the index of the first symbol layer in the map style
            // This approach works with our simple map styles for more advanced styles, e.g., Outdoor.
            // We recommend directly inserting the name of the last layer above your data. 
            // See the Learn more section below.
            const firstSymbolId = layers.find(layer => layer.type === 'symbol').id;

            map.addSource('urban-areas', {
              'type': 'geojson',
              'data':
                'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_urban_areas.geojson'
            });
            map.addLayer(
              {
                'id': 'urban-areas-fill',
                'type': 'fill',
                'source': 'urban-areas',
                'layout': {},
                'paint': {
                  'fill-color': '#f08',
                  'fill-opacity': 0.4
                }
                // This is the important part of this example: the addLayer
                // method takes 2 arguments: the layer as an object, and a string
                // representing another layer's name. if the other layer
                // exists in the stylesheet already, the new layer will be positioned
                // right before that layer in the stack, making it possible to put
                // 'overlays' anywhere in the layer stack.
                // Insert the layer beneath the first symbol layer.
              },
              firstSymbolId
            );
          });
    </script>
</body>
</html>
```
