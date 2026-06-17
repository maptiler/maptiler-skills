# Source: https://docs.maptiler.com/sdk-js/examples/hillshade/

# Add hillshade

To improve the visual appeal of a map, this demonstration incorporates raster hillshading. This is achieved by integrating the [MapTiler Terrain-DEM](https://www.maptiler.com/terrain/) raster tileset, as a raster-dem source for the hillshade layer. By doing so, the map gains a realistic representation of terrain elevation and shading.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      map.addSource("terrain", {
        "type": "raster-dem",
        "url": `https://api.maptiler.com/tiles/terrain-rgb-v2/tiles.json`
      });

      map.addLayer(
        {
          'id': 'hillshading',
          'source': 'terrain',
          'type': 'hillshade'
        },
        'Residential'
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
    <title>Add hillshade</title>
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
            style: maptilersdk.MapStyle.BASE.LIGHT,
            center: [0, 20],
            zoom: 0.3
        });

        map.on('load', function () {
              map.addSource("terrain", {
                "type": "raster-dem",
                "url": `https://api.maptiler.com/tiles/terrain-rgb-v2/tiles.json`
              });

              map.addLayer(
                {
                  'id': 'hillshading',
                  'source': 'terrain',
                  'type': 'hillshade'
                },
                'Residential'
              );
            });
    </script>
</body>
</html>
```
