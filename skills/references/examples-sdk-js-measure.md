# Source: https://docs.maptiler.com/sdk-js/examples/measure/

# Measure distances

To calculate distances on the map, simply click on different points to create lines that will measure the distances using the [turf.length](https://turfjs.org/docs/#length) function. This feature allows you to accurately determine the distance between any two points on the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const distanceContainer = document.getElementById('distance');

    // GeoJSON object to hold our measurement features
    const geojson = {
      'type': 'FeatureCollection',
      'features': []
    };

    // Used to draw a line between points
    const linestring = {
      'type': 'Feature',
      'geometry': {
        'type': 'LineString',
        'coordinates': []
      }
    };

    map.on('load', function () {
      map.addSource('geojson', {
        'type': 'geojson',
        'data': geojson
      });

      // Add styles to the map
      map.addLayer({
        id: 'measure-points',
        type: 'circle',
        source: 'geojson',
        paint: {
          'circle-radius': 5,
          'circle-color': '#000'
        },
        filter: ['in', '$type', 'Point']
      });
      map.addLayer({
        id: 'measure-lines',
        type: 'line',
        source: 'geojson',
        layout: {
          'line-cap': 'round',
          'line-join': 'round'
        },
        paint: {
          'line-color': '#000',
          'line-width': 2.5
        },
        filter: ['in', '$type', 'LineString']
      });

      map.on('click', function (e) {
        const features = map.queryRenderedFeatures(e.point, {
          layers: ['measure-points']
        });

        // Remove the linestring from the group
        // So we can redraw it based on the points collection
        if (geojson.features.length > 1) geojson.features.pop();

        // Clear the Distance container to populate it with a new value
        distanceContainer.innerHTML = '';

        // If a feature was clicked, remove it from the map
        if (features.length) {
          const id = features[0].properties.id;
          geojson.features = geojson.features.filter(function (point) {
            return point.properties.id !== id;
          });
        } else {
          const point = {
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [e.lngLat.lng, e.lngLat.lat]
            },
            'properties': {
              'id': String(new Date().getTime())
            }
          };

          geojson.features.push(point);
        }

        if (geojson.features.length > 1) {
          linestring.geometry.coordinates = geojson.features.map(
            function (point) {
              return point.geometry.coordinates;
            }
          );

          geojson.features.push(linestring);

          // Populate the distanceContainer with total distance
          const value = document.createElement('pre');
          value.textContent =
            'Total distance: ' +
            turf.length(linestring).toLocaleString() +
            'km';
          distanceContainer.appendChild(value);
        }

        map.getSource('geojson').setData(geojson);
      });
    });

    map.on('mousemove', function (e) {
      const features = map.queryRenderedFeatures(e.point, {
        layers: ['measure-points']
      });
      // UI indicator for clicking/hovering a point on the map
      map.getCanvas().style.cursor = features.length
        ? 'pointer'
        : 'crosshair';
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Measure distances</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/@turf/turf@7.3.5/turf.min.js"></script>
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
            center: [2.3399, 48.8555],
            zoom: 12
        });

        const distanceContainer = document.getElementById('distance');

            // GeoJSON object to hold our measurement features
            const geojson = {
              'type': 'FeatureCollection',
              'features': []
            };

            // Used to draw a line between points
            const linestring = {
              'type': 'Feature',
              'geometry': {
                'type': 'LineString',
                'coordinates': []
              }
            };

            map.on('load', function () {
              map.addSource('geojson', {
                'type': 'geojson',
                'data': geojson
              });

              // Add styles to the map
              map.addLayer({
                id: 'measure-points',
                type: 'circle',
                source: 'geojson',
                paint: {
                  'circle-radius': 5,
                  'circle-color': '#000'
                },
                filter: ['in', '$type', 'Point']
              });
              map.addLayer({
                id: 'measure-lines',
                type: 'line',
                source: 'geojson',
                layout: {
                  'line-cap': 'round',
                  'line-join': 'round'
                },
                paint: {
                  'line-color': '#000',
                  'line-width': 2.5
                },
                filter: ['in', '$type', 'LineString']
              });

              map.on('click', function (e) {
                const features = map.queryRenderedFeatures(e.point, {
                  layers: ['measure-points']
                });

                // Remove the linestring from the group
                // So we can redraw it based on the points collection
                if (geojson.features.length > 1) geojson.features.pop();

                // Clear the Distance container to populate it with a new value
                distanceContainer.innerHTML = '';

                // If a feature was clicked, remove it from the map
                if (features.length) {
                  const id = features[0].properties.id;
                  geojson.features = geojson.features.filter(function (point) {
                    return point.properties.id !== id;
                  });
                } else {
                  const point = {
                    'type': 'Feature',
                    'geometry': {
                      'type': 'Point',
                      'coordinates': [e.lngLat.lng, e.lngLat.lat]
                    },
                    'properties': {
                      'id': String(new Date().getTime())
                    }
                  };

                  geojson.features.push(point);
                }

                if (geojson.features.length > 1) {
                  linestring.geometry.coordinates = geojson.features.map(
                    function (point) {
                      return point.geometry.coordinates;
                    }
                  );

                  geojson.features.push(linestring);

                  // Populate the distanceContainer with total distance
                  const value = document.createElement('pre');
                  value.textContent =
                    'Total distance: ' +
                    turf.length(linestring).toLocaleString() +
                    'km';
                  distanceContainer.appendChild(value);
                }

                map.getSource('geojson').setData(geojson);
              });
            });

            map.on('mousemove', function (e) {
              const features = map.queryRenderedFeatures(e.point, {
                layers: ['measure-points']
              });
              // UI indicator for clicking/hovering a point on the map
              map.getCanvas().style.cursor = features.length
                ? 'pointer'
                : 'crosshair';
            });
    </script>
</body>
</html>
```
