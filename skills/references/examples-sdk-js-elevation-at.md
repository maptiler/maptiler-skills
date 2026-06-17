# Source: https://docs.maptiler.com/sdk-js/examples/elevation-at/

# Elevation at point

How to get the elevation in meters from any location. MapTiler [SDK elevation](/client-js/#%EF%B8%8F-elevation) functions provide convenient access to get the elevation in meters from any location. It’s possible to look up and compute the elevation from: a single location, provide a batch of points, a GeoJSON LineString or a GeoJSON MultiLineString.

<sup>Click on the map to get the elevation at this location</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.on('click', async function (ev) {
          const {lng, lat} = ev.lngLat;
          //get the elevation at a given position
          const elevatedPosition = await maptilersdk.elevation.at([lng, lat]);
          const popup = new maptilersdk.Popup()
            .setLngLat([lng, lat])
            .setHTML(`<h2>Elevation</h2>
            <h3>${elevatedPosition[2].toFixed(0)} mts</h3>`)
            .addTo(map);
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
    <title>Elevation at point</title>
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
            style: maptilersdk.MapStyle.HYBRID,
            center: [-70.02454, -33.81356],
            zoom: 12
        });

        map.on('load', function () {
                map.on('click', async function (ev) {
                  const {lng, lat} = ev.lngLat;
                  //get the elevation at a given position
                  const elevatedPosition = await maptilersdk.elevation.at([lng, lat]);
                  const popup = new maptilersdk.Popup()
                    .setLngLat([lng, lat])
                    .setHTML(`<h2>Elevation</h2>
                    <h3>${elevatedPosition[2].toFixed(0)} mts</h3>`)
                    .addTo(map);
                });
            });
    </script>
</body>
</html>
```
