# Source: https://docs.maptiler.com/sdk-js/examples/style-by-tunnel/

# How to change the style (light/dark) of the map based on the position in a route

In this example, we illustrate how to modify the map display (between light and dark modes) based on the location within a specific route.

To mimic the movement of a vehicle, we employ an animated point along the route. In this scenario, we simulate the vehicle entering a tunnel, prompting a switch to the dark map style. Subsequently, when the vehicle exits the tunnel, we revert back to the light map style. You can download the [vehicle image](./navigation.png){:target="_blank" rel="noopener"}, and obtain the [route geoJSON file](./tunnel_route.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
function getStyleByMode(mode) {
      return (mode == 'dark') ? maptilersdk.MapStyle.STREETS.DARK : maptilersdk.MapStyle.STREETS.LIGHT;
    }

    function switchMode(mode) {
      stop();
      activeMode = mode;
      const style = getStyleByMode(mode);
      map.setStyle(style);
    }

    function tunnelEntrance(counter) {
      return counter == 779;
    }

    function tunnelExit(counter) {
      return counter == 1131;
    }

    let playing = true;

    const origin = [6.856344820704434, 45.90164121615423];
    // A single point that animates along the route.
    // Coordinates are initially set to origin.
    const point = {
      'type': 'FeatureCollection',
      'features': [
        {
          'type': 'Feature',
          'properties': {},
          'geometry': {
            'type': 'Point',
            'coordinates': origin
          }
        }
      ]
    };

    // Number of steps to use in the animation, more steps means
    // a smoother animation, but too many steps will result in a
    // low frame rate
    const steps = 1500;

    //load the route GeoJSON form MapTiler Cloud
    maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE')
    .then((data) => {
      route = data;

      const options = {tolerance: 0.0001, highQuality: true};
      route = turf.simplify(route, options);

      // Calculate the distance in kilometers between route start/end point.
      const lineDistance = turf.length(route.features[0], 'kilometers');

      const arc = [];

      // Draw an arc between the `origin` & `destination` of the two points
      for (let i = 0; i < lineDistance; i += lineDistance / steps) {
          const segment = turf.along(route.features[0], i, 'kilometers');
          arc.push(segment.geometry.coordinates);
      }

      // Update the route with calculated arc coordinates
      route.features[0].geometry.coordinates = arc;

      map.on('load', function () {

        loadAnimationLayers();

        counter = 0;
        // Start the animation.
        animate(counter);
      });

      map.on('styledata', () => {
        const waiting = () => {
          if (!map.isStyleLoaded()) {
            setTimeout(waiting, 100);
          } else {
            loadAnimationLayers();
          }
        };
        waiting();
      });

    });

    async function loadAnimationLayers() {
      if (!map.hasImage('cat')) {
        const image = await map.loadImage('../navigation.png');
        map.addImage('cat', image.data);
      }

      // Add a source and layer displaying a point which will be animated in a circle.
      if (!map.getSource('route')) {
        map.addSource('route', {
          'type': 'geojson',
          'data': route
        });

        map.addSource('point', {
          'type': 'geojson',
          'data': point
        });
      }

      if (!map.getLayer('route')) {
        map.addLayer({
          'id': 'route',
          'source': 'route',
          'type': 'line',
          'paint': {
              'line-width': 2,
              'line-color': '#007cbf'
          }
        });

        map.addLayer({
          'id': 'point',
          'source': 'point',
          'type': 'symbol',
          'layout': {
            'icon-image': 'cat',
            'icon-size': 0.05,
            'icon-rotate': ['get', 'bearing'],
            'icon-rotation-alignment': 'map',
            'icon-overlap': 'always',
            'icon-ignore-placement': true
          }
        });

        playing = true;
        // Restart the animation.
        animate(counter);
      }
    }

    function stop() {
      playing = false;
    }

    function animate() {
      if (!playing) return;
      // Update point geometry to a new position based on counter denoting
      // the index to access the arc.
      point.features[0].geometry.coordinates =
        route.features[0].geometry.coordinates[counter];

      // Calculate the bearing to ensure the icon is rotated to match the route arc
      // The bearing is calculate between the current point and the next point, except
      // at the end of the arc use the previous point and the current point
      try {
        point.features[0].properties.bearing = turf.bearing(
          turf.point(
            route.features[0].geometry.coordinates[
              counter >= steps ? counter - 1 : counter
            ]
          ),
          turf.point(
            route.features[0].geometry.coordinates[
              counter >= steps ? counter : counter + 1
            ]
          )
        );
      } catch (error) {

      }

      // Update the source with this new data.
      map.getSource('point').setData(point);

      // Request the next frame of animation so long the end has not been reached.
      if (counter < steps - 1) {
        requestAnimationFrame(animate);
      }

      counter = counter + 1;

      if (tunnelEntrance(counter)) {
        switchMode('dark');
      } else if (tunnelExit(counter)) {
        switchMode('light');
      }
    }

    document.getElementById('replay').addEventListener('click', function () {
      // Set the coordinates of the original point back to origin
      point.features[0].geometry.coordinates = origin;

      // Update the source layer
      map.getSource('point').setData(point);

      // Reset the counter
      counter = 0;

      // Restart the animation.
      animate(counter);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>How to change the style (light/dark) of the map based on the position in a route</title>
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
            style: maptilersdk.MapStyle.STREETS.LIGHT,
            center: [6.7979, 45.8515],
            zoom: 10
        });

        function getStyleByMode(mode) {
              return (mode == 'dark') ? maptilersdk.MapStyle.STREETS.DARK : maptilersdk.MapStyle.STREETS.LIGHT;
            }

            function switchMode(mode) {
              stop();
              activeMode = mode;
              const style = getStyleByMode(mode);
              map.setStyle(style);
            }

            function tunnelEntrance(counter) {
              return counter == 779;
            }

            function tunnelExit(counter) {
              return counter == 1131;
            }

            let playing = true;

            const origin = [6.856344820704434, 45.90164121615423];
            // A single point that animates along the route.
            // Coordinates are initially set to origin.
            const point = {
              'type': 'FeatureCollection',
              'features': [
                {
                  'type': 'Feature',
                  'properties': {},
                  'geometry': {
                    'type': 'Point',
                    'coordinates': origin
                  }
                }
              ]
            };

            // Number of steps to use in the animation, more steps means
            // a smoother animation, but too many steps will result in a
            // low frame rate
            const steps = 1500;

            //load the route GeoJSON form MapTiler Cloud
            maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE')
            .then((data) => {
              route = data;

              const options = {tolerance: 0.0001, highQuality: true};
              route = turf.simplify(route, options);

              // Calculate the distance in kilometers between route start/end point.
              const lineDistance = turf.length(route.features[0], 'kilometers');

              const arc = [];

              // Draw an arc between the `origin` & `destination` of the two points
              for (let i = 0; i < lineDistance; i += lineDistance / steps) {
                  const segment = turf.along(route.features[0], i, 'kilometers');
                  arc.push(segment.geometry.coordinates);
              }

              // Update the route with calculated arc coordinates
              route.features[0].geometry.coordinates = arc;

              map.on('load', function () {

                loadAnimationLayers();

                counter = 0;
                // Start the animation.
                animate(counter);
              });

              map.on('styledata', () => {
                const waiting = () => {
                  if (!map.isStyleLoaded()) {
                    setTimeout(waiting, 100);
                  } else {
                    loadAnimationLayers();
                  }
                };
                waiting();
              });

            });

            async function loadAnimationLayers() {
              if (!map.hasImage('cat')) {
                const image = await map.loadImage('../navigation.png');
                map.addImage('cat', image.data);
              }

              // Add a source and layer displaying a point which will be animated in a circle.
              if (!map.getSource('route')) {
                map.addSource('route', {
                  'type': 'geojson',
                  'data': route
                });

                map.addSource('point', {
                  'type': 'geojson',
                  'data': point
                });
              }

              if (!map.getLayer('route')) {
                map.addLayer({
                  'id': 'route',
                  'source': 'route',
                  'type': 'line',
                  'paint': {
                      'line-width': 2,
                      'line-color': '#007cbf'
                  }
                });

                map.addLayer({
                  'id': 'point',
                  'source': 'point',
                  'type': 'symbol',
                  'layout': {
                    'icon-image': 'cat',
                    'icon-size': 0.05,
                    'icon-rotate': ['get', 'bearing'],
                    'icon-rotation-alignment': 'map',
                    'icon-overlap': 'always',
                    'icon-ignore-placement': true
                  }
                });

                playing = true;
                // Restart the animation.
                animate(counter);
              }
            }

            function stop() {
              playing = false;
            }

            function animate() {
              if (!playing) return;
              // Update point geometry to a new position based on counter denoting
              // the index to access the arc.
              point.features[0].geometry.coordinates =
                route.features[0].geometry.coordinates[counter];

              // Calculate the bearing to ensure the icon is rotated to match the route arc
              // The bearing is calculate between the current point and the next point, except
              // at the end of the arc use the previous point and the current point
              try {
                point.features[0].properties.bearing = turf.bearing(
                  turf.point(
                    route.features[0].geometry.coordinates[
                      counter >= steps ? counter - 1 : counter
                    ]
                  ),
                  turf.point(
                    route.features[0].geometry.coordinates[
                      counter >= steps ? counter : counter + 1
                    ]
                  )
                );
              } catch (error) {

              }

              // Update the source with this new data.
              map.getSource('point').setData(point);

              // Request the next frame of animation so long the end has not been reached.
              if (counter < steps - 1) {
                requestAnimationFrame(animate);
              }

              counter = counter + 1;

              if (tunnelEntrance(counter)) {
                switchMode('dark');
              } else if (tunnelExit(counter)) {
                switchMode('light');
              }
            }

            document.getElementById('replay').addEventListener('click', function () {
              // Set the coordinates of the original point back to origin
              point.features[0].geometry.coordinates = origin;

              // Update the source layer
              map.getSource('point').setData(point);

              // Reset the counter
              counter = 0;

              // Restart the animation.
              animate(counter);
            });
    </script>
</body>
</html>
```
