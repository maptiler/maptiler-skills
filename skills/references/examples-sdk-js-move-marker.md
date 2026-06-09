# Source: https://docs.maptiler.com/sdk-js/examples/move-marker/

# Move a marker

This example demonstrates how to reposition a marker by clicking on the map. By utilizing the map's `click` event, we can dynamically update the marker's location to match the exact coordinates where the user has clicked. This interactive functionality allows for seamless marker placement and movement across the map.

<sup>Click on the map to move the marker.</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [12.550343, 55.665957], // starting position [lng, lat]
      zoom: 9, // starting zoom
    });
    const marker = new maptilersdk.Marker()
      .setLngLat([lng, lat])
      .addTo(map);

    map.on('click', (evt) => {
      marker.setLngLat(evt.lngLat);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Move a marker</title>
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
            center: [12.550343, 55.665957],
            zoom: 9
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [12.550343, 55.665957], // starting position [lng, lat]
              zoom: 9, // starting zoom
            });
            const marker = new maptilersdk.Marker()
              .setLngLat([lng, lat])
              .addTo(map);

            map.on('click', (evt) => {
              marker.setLngLat(evt.lngLat);
            });
    </script>
</body>
</html>
```
