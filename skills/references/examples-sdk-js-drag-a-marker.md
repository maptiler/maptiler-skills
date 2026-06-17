# Source: https://docs.maptiler.com/sdk-js/examples/drag-a-marker/

# Create a draggable Marker

Drag the [`Marker`](/sdk-js/api/markers/#marker) to a new location on a map and populate its coordinates in a display.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const marker = new maptilersdk.Marker({
      draggable: true
    })
      .setLngLat([0, 0])
      .addTo(map);

    function onDragEnd() {
      const lngLat = marker.getLngLat();
      coordinates.style.display = 'block';
      coordinates.innerHTML =
        'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
    }

    marker.on('dragend', onDragEnd);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create a draggable Marker</title>
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

        const marker = new maptilersdk.Marker({
              draggable: true
            })
              .setLngLat([0, 0])
              .addTo(map);

            function onDragEnd() {
              const lngLat = marker.getLngLat();
              coordinates.style.display = 'block';
              coordinates.innerHTML =
                'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
            }

            marker.on('dragend', onDragEnd);
    </script>
</body>
</html>
```
