# Source: https://docs.maptiler.com/sdk-js/examples/custom-marker-icons/

# Add custom icons with Markers

Enhance your map by incorporating personalized icons using the [`Marker`](/sdk-js/api/markers/#marker) feature. This functionality allows you to include custom icons that align with your specific preferences.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// add markers to map
    geojson.features.forEach(function (marker) {
      // create a DOM element for the marker
      const el = document.createElement('div');
      el.className = 'marker';
      el.style.backgroundImage =
        `url(https://docs.maptiler.com/sdk-js/examples/custom-marker-icons/${marker.properties.iconSize[0]}.jpg)`;
      el.style.width = marker.properties.iconSize[0] + 'px';
      el.style.height = marker.properties.iconSize[1] + 'px';

      el.addEventListener('click', function () {
        window.alert(marker.properties.message);
      });

      // add marker to map
      new maptilersdk.Marker({ element: el })
        .setLngLat(marker.geometry.coordinates)
        .addTo(map);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add custom icons with Markers</title>
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
            center: [-65.017, -16.457],
            zoom: 5
        });

        // add markers to map
            geojson.features.forEach(function (marker) {
              // create a DOM element for the marker
              const el = document.createElement('div');
              el.className = 'marker';
              el.style.backgroundImage =
                `url(https://docs.maptiler.com/sdk-js/examples/custom-marker-icons/${marker.properties.iconSize[0]}.jpg)`;
              el.style.width = marker.properties.iconSize[0] + 'px';
              el.style.height = marker.properties.iconSize[1] + 'px';

              el.addEventListener('click', function () {
                window.alert(marker.properties.message);
              });

              // add marker to map
              new maptilersdk.Marker({ element: el })
                .setLngLat(marker.geometry.coordinates)
                .addTo(map);
            });
    </script>
</body>
</html>
```
