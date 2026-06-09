# Source: https://docs.maptiler.com/sdk-js/examples/add-image/

# Add an icon to the map

Add an icon onto the map by utilizing an external URL and incorporate it into a [symbol layer](/gl-style-specification/layers/#symbol) as specified in the style specification for layers.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', async function () {
      const image = await map.loadImage(
        'https://upload.wikimedia.org/wikipedia/commons/7/7c/201408_cat.png');

      map.addImage('cat', image.data);
      map.addSource('point', {
        'type': 'geojson',
        'data': {
          'type': 'FeatureCollection',
          'features': [
            {
              'type': 'Feature',
              'geometry': {
                'type': 'Point',
                'coordinates': [0, 0]
              }
            }
          ]
        }
      });
      map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'point',
        'layout': {
          'icon-image': 'cat',
          'icon-size': 0.25
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
    <title>Add an icon to the map</title>
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
            center: [0, 0],
            zoom: 2
        });

        map.on('load', async function () {
              const image = await map.loadImage(
                'https://upload.wikimedia.org/wikipedia/commons/7/7c/201408_cat.png');

              map.addImage('cat', image.data);
              map.addSource('point', {
                'type': 'geojson',
                'data': {
                  'type': 'FeatureCollection',
                  'features': [
                    {
                      'type': 'Feature',
                      'geometry': {
                        'type': 'Point',
                        'coordinates': [0, 0]
                      }
                    }
                  ]
                }
              });
              map.addLayer({
                'id': 'points',
                'type': 'symbol',
                'source': 'point',
                'layout': {
                  'icon-image': 'cat',
                  'icon-size': 0.25
                }
              });
            });
    </script>
</body>
</html>
```
