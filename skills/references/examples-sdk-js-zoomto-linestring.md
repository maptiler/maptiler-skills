# Source: https://docs.maptiler.com/sdk-js/examples/zoomto-linestring/

# Fit to the bounds of a LineString

Get the bounds of a LineString by passing its first coordinates to [`LngLatBounds`](/sdk-js/api/geography/#lnglatbounds) and chaining [`extend`](/sdk-js/api/geography/#lnglatbounds#extend) to include the last coordinates.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
      map.addSource('LineString', {
        'type': 'geojson',
        'data': geojson
      });
      map.addLayer({
        'id': 'LineString',
        'type': 'line',
        'source': 'LineString',
        'layout': {
          'line-join': 'round',
          'line-cap': 'round'
        },
        'paint': {
          'line-color': '#BF93E4',
          'line-width': 5
        }
      });

      document
        .getElementById('zoomto')
        .addEventListener('click', function () {
          // Geographic coordinates of the LineString
          const coordinates = geojson.features[0].geometry.coordinates;

          // Pass the first coordinates in the LineString to `lngLatBounds` &
          // wrap each coordinate pair in `extend` to include them in the bounds
          // result. A variation of this technique could be applied to zooming
          // to the bounds of multiple Points or Polygon geomteries - it just
          // requires wrapping all the coordinates with the extend method.
          const bounds = coordinates.reduce(function (bounds, coord) {
            return bounds.extend(coord);
          }, new maptilersdk.LngLatBounds(coordinates[0], coordinates[0]));

          map.fitBounds(bounds, {
            padding: 20
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
    <title>Fit to the bounds of a LineString</title>
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
            center: [-77.0214, 38.897],
            zoom: 12
        });

        map.on('load', function () {
              map.addSource('LineString', {
                'type': 'geojson',
                'data': geojson
              });
              map.addLayer({
                'id': 'LineString',
                'type': 'line',
                'source': 'LineString',
                'layout': {
                  'line-join': 'round',
                  'line-cap': 'round'
                },
                'paint': {
                  'line-color': '#BF93E4',
                  'line-width': 5
                }
              });

              document
                .getElementById('zoomto')
                .addEventListener('click', function () {
                  // Geographic coordinates of the LineString
                  const coordinates = geojson.features[0].geometry.coordinates;

                  // Pass the first coordinates in the LineString to `lngLatBounds` &
                  // wrap each coordinate pair in `extend` to include them in the bounds
                  // result. A variation of this technique could be applied to zooming
                  // to the bounds of multiple Points or Polygon geomteries - it just
                  // requires wrapping all the coordinates with the extend method.
                  const bounds = coordinates.reduce(function (bounds, coord) {
                    return bounds.extend(coord);
                  }, new maptilersdk.LngLatBounds(coordinates[0], coordinates[0]));

                  map.fitBounds(bounds, {
                    padding: 20
                  });
                });
            });
    </script>
</body>
</html>
```
