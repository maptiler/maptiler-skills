# Source: https://docs.maptiler.com/sdk-js/examples/custom-points-icon-png/

# Add custom icon (PNG) to a point layer

This example shows how to make a map with pins to display a point layer from a [MapTiler Tileset](https://cloud.maptiler.com/tiles/) using a custom PNG icon.

Download the [underground sample icon](./underground.png), The icon is from the [Maps Icons Collection](https://mapicons.mapsmarker.com).

<span class="api-key-inline">Replace `YOUR_MAPTILER_TILESET_ID_HERE` with your actual [MapTiler Tileset ID](https://cloud.maptiler.com/tiles/).</span>

<span class="api-key-inline">Replace `YOUR_TILESET_LAYER_HERE` with your actual **Layer ID**. [How to get the Layer ID](/guides/general/how-to-get-tileset-layer-id/).</span>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function() {
      const image = await map.loadImage('./underground.png');

      map.addImage('pinMetro', image.data);

      map.addSource('points', {
        type: 'vector',
        url: "https://api.maptiler.com/tiles/9537e49b-39c3-43ce-a6b9-9cf3d26b6d93/tiles.json"
      });

      map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'points',
        'source-layer': 'stations',
        'layout': {
          'icon-image': 'pinMetro',
          'icon-size': ['*', ['get', 'scalerank'] ,0.01]
        },
        'paint': {}
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
    <title>Add custom icon (PNG) to a point layer</title>
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
            style: maptilersdk.MapStyle.BASE,
            center: [-73.9066, 40.7314],
            zoom: 10.21
        });

        map.on('load', async function() {
              const image = await map.loadImage('./underground.png');

              map.addImage('pinMetro', image.data);

              map.addSource('points', {
                type: 'vector',
                url: "https://api.maptiler.com/tiles/9537e49b-39c3-43ce-a6b9-9cf3d26b6d93/tiles.json"
              });

              map.addLayer({
                'id': 'points',
                'type': 'symbol',
                'source': 'points',
                'source-layer': 'stations',
                'layout': {
                  'icon-image': 'pinMetro',
                  'icon-size': ['*', ['get', 'scalerank'] ,0.01]
                },
                'paint': {}
              });

            });
    </script>
</body>
</html>
```
