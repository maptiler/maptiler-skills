# Source: https://docs.maptiler.com/sdk-js/examples/drag-a-point/

# Create a draggable point

Drag the point to a new location on a map and populate its coordinates in a display.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const canvas = map.getCanvasContainer();

    const geojson = {
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
    };

    function onMove(e) {
      const coords = e.lngLat;

      // Set a UI indicator for dragging.
      canvas.style.cursor = 'grabbing';

      // Update the Point feature in `geojson` coordinates
      // and call setData to the source layer `point` on it.
      geojson.features[0].geometry.coordinates = [coords.lng, coords.lat];
      map.getSource('point').setData(geojson);
    }

    function onUp(e) {
      const coords = e.lngLat;

      // Print the coordinates of where the point had
      // finished being dragged to on the map.
      coordinates.style.display = 'block';
      coordinates.innerHTML =
        'Longitude: ' + coords.lng + '<br />Latitude: ' + coords.lat;
      canvas.style.cursor = '';

      // Unbind mouse/touch events
      map.off('mousemove', onMove);
      map.off('touchmove', onMove);
    }

    map.on('load', function () {
      // Add a single point to the map
      map.addSource('point', {
        'type': 'geojson',
        'data': geojson
      });

      map.addLayer({
        'id': 'point',
        'type': 'circle',
        'source': 'point',
        'paint': {
          'circle-radius': 10,
          'circle-color': '#3887be'
        }
      });

      // When the cursor enters a feature in the point layer, prepare for dragging.
      map.on('mouseenter', 'point', function () {
        map.setPaintProperty('point', 'circle-color', '#3bb2d0');
        canvas.style.cursor = 'move';
      });

      map.on('mouseleave', 'point', function () {
        map.setPaintProperty('point', 'circle-color', '#3887be');
        canvas.style.cursor = '';
      });

      map.on('mousedown', 'point', function (e) {
        // Prevent the default map drag behavior.
        e.preventDefault();

        canvas.style.cursor = 'grab';

        map.on('mousemove', onMove);
        map.once('mouseup', onUp);
      });

      map.on('touchstart', 'point', function (e) {
        if (e.points.length !== 1) return;

        // Prevent the default map drag behavior.
        e.preventDefault();

        map.on('touchmove', onMove);
        map.once('touchend', onUp);
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
    <title>Create a draggable point</title>
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

        const canvas = map.getCanvasContainer();

            const geojson = {
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
            };

            function onMove(e) {
              const coords = e.lngLat;

              // Set a UI indicator for dragging.
              canvas.style.cursor = 'grabbing';

              // Update the Point feature in `geojson` coordinates
              // and call setData to the source layer `point` on it.
              geojson.features[0].geometry.coordinates = [coords.lng, coords.lat];
              map.getSource('point').setData(geojson);
            }

            function onUp(e) {
              const coords = e.lngLat;

              // Print the coordinates of where the point had
              // finished being dragged to on the map.
              coordinates.style.display = 'block';
              coordinates.innerHTML =
                'Longitude: ' + coords.lng + '<br />Latitude: ' + coords.lat;
              canvas.style.cursor = '';

              // Unbind mouse/touch events
              map.off('mousemove', onMove);
              map.off('touchmove', onMove);
            }

            map.on('load', function () {
              // Add a single point to the map
              map.addSource('point', {
                'type': 'geojson',
                'data': geojson
              });

              map.addLayer({
                'id': 'point',
                'type': 'circle',
                'source': 'point',
                'paint': {
                  'circle-radius': 10,
                  'circle-color': '#3887be'
                }
              });

              // When the cursor enters a feature in the point layer, prepare for dragging.
              map.on('mouseenter', 'point', function () {
                map.setPaintProperty('point', 'circle-color', '#3bb2d0');
                canvas.style.cursor = 'move';
              });

              map.on('mouseleave', 'point', function () {
                map.setPaintProperty('point', 'circle-color', '#3887be');
                canvas.style.cursor = '';
              });

              map.on('mousedown', 'point', function (e) {
                // Prevent the default map drag behavior.
                e.preventDefault();

                canvas.style.cursor = 'grab';

                map.on('mousemove', onMove);
                map.once('mouseup', onUp);
              });

              map.on('touchstart', 'point', function (e) {
                if (e.points.length !== 1) return;

                // Prevent the default map drag behavior.
                e.preventDefault();

                map.on('touchmove', onMove);
                map.once('touchend', onUp);
              });
            });
    </script>
</body>
</html>
```
