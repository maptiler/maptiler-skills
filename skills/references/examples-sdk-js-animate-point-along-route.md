# Source: https://docs.maptiler.com/sdk-js/examples/animate-point-along-route/

# Animate a point along a route

You can utilize the [Turf](https://turfjs.org/) library to create seamless animations of a point moving along the length of a line.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// San Francisco
    const origin = [-122.414, 37.776];

    // Washington DC
    const destination = [-77.032, 38.913];

    // A simple line from origin to destination.
    const route = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [origin, destination]
                }
            }
        ]
    };

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

    // Calculate the distance in kilometers between route start/end point.
    const lineDistance = turf.length(route.features[0], 'kilometers');

    const arc = [];

    // Number of steps to use in the arc and animation, more steps means
    // a smoother arc and animation, but too many steps will result in a
    // low frame rate
    const steps = 500;

    // Draw an arc between the `origin` & `destination` of the two points
    for (let i = 0; i < lineDistance; i += lineDistance / steps) {
        const segment = turf.along(route.features[0], i, 'kilometers');
        arc.push(segment.geometry.coordinates);
    }

    // Update the route with calculated arc coordinates
    route.features[0].geometry.coordinates = arc;

    // Used to increment the value of the point measurement against the route.
    let counter = 0;

    map.on('load', function () {
        // Add a source and layer displaying a point which will be animated in a circle.
        map.addSource('route', {
            'type': 'geojson',
            'data': route
        });

        map.addSource('point', {
            'type': 'geojson',
            'data': point
        });

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
                'icon-image': 'airport',
                'icon-rotate': ['get', 'bearing'],
                'icon-rotation-alignment': 'map',
                'icon-overlap': 'always',
                'icon-ignore-placement': true
            }
        });

        function animate() {
            // Update point geometry to a new position based on counter denoting
            // the index to access the arc.
            point.features[0].geometry.coordinates =
                route.features[0].geometry.coordinates[counter];

            // Calculate the bearing to ensure the icon is rotated to match the route arc
            // The bearing is calculate between the current point and the next point, except
            // at the end of the arc use the previous point and the current point
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

            // Update the source with this new data.
            map.getSource('point').setData(point);

            // Request the next frame of animation so long the end has not been reached.
            if (counter < steps) {
                requestAnimationFrame(animate);
            }

            counter = counter + 1;
        }

        document
            .getElementById('replay')
            .addEventListener('click', function () {
                // Set the coordinates of the original point back to origin
                point.features[0].geometry.coordinates = origin;

                // Update the source layer
                map.getSource('point').setData(point);

                // Reset the counter
                counter = 0;

                // Restart the animation.
                animate(counter);
            });

        // Start the animation.
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
    <title>Animate a point along a route</title>
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
            center: [-96, 37.8],
            zoom: 3
        });

        // San Francisco
            const origin = [-122.414, 37.776];

            // Washington DC
            const destination = [-77.032, 38.913];

            // A simple line from origin to destination.
            const route = {
                'type': 'FeatureCollection',
                'features': [
                    {
                        'type': 'Feature',
                        'geometry': {
                            'type': 'LineString',
                            'coordinates': [origin, destination]
                        }
                    }
                ]
            };

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

            // Calculate the distance in kilometers between route start/end point.
            const lineDistance = turf.length(route.features[0], 'kilometers');

            const arc = [];

            // Number of steps to use in the arc and animation, more steps means
            // a smoother arc and animation, but too many steps will result in a
            // low frame rate
            const steps = 500;

            // Draw an arc between the `origin` & `destination` of the two points
            for (let i = 0; i < lineDistance; i += lineDistance / steps) {
                const segment = turf.along(route.features[0], i, 'kilometers');
                arc.push(segment.geometry.coordinates);
            }

            // Update the route with calculated arc coordinates
            route.features[0].geometry.coordinates = arc;

            // Used to increment the value of the point measurement against the route.
            let counter = 0;

            map.on('load', function () {
                // Add a source and layer displaying a point which will be animated in a circle.
                map.addSource('route', {
                    'type': 'geojson',
                    'data': route
                });

                map.addSource('point', {
                    'type': 'geojson',
                    'data': point
                });

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
                        'icon-image': 'airport',
                        'icon-rotate': ['get', 'bearing'],
                        'icon-rotation-alignment': 'map',
                        'icon-overlap': 'always',
                        'icon-ignore-placement': true
                    }
                });

                function animate() {
                    // Update point geometry to a new position based on counter denoting
                    // the index to access the arc.
                    point.features[0].geometry.coordinates =
                        route.features[0].geometry.coordinates[counter];

                    // Calculate the bearing to ensure the icon is rotated to match the route arc
                    // The bearing is calculate between the current point and the next point, except
                    // at the end of the arc use the previous point and the current point
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

                    // Update the source with this new data.
                    map.getSource('point').setData(point);

                    // Request the next frame of animation so long the end has not been reached.
                    if (counter < steps) {
                        requestAnimationFrame(animate);
                    }

                    counter = counter + 1;
                }

                document
                    .getElementById('replay')
                    .addEventListener('click', function () {
                        // Set the coordinates of the original point back to origin
                        point.features[0].geometry.coordinates = origin;

                        // Update the source layer
                        map.getSource('point').setData(point);

                        // Reset the counter
                        counter = 0;

                        // Restart the animation.
                        animate(counter);
                    });

                // Start the animation.
                animate(counter);
            });
    </script>
</body>
</html>
```
