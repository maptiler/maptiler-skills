# Source: https://docs.maptiler.com/leaflet/examples/helpers-point/

# Vector Tiles in Leaflet JS

Learn how to handle thousands or millions of location points with Leaflet JavaScript library using the leaflet-maptilersdk plugin. Download the [Public School sample data](/sdk-js/assets/Public_School_Characteristics_2020-21_no_prop.geojson).

In this Leaflet JS example, the size and color of points are scaled by the number of students in each school. You can load millions of points into Leaflet without affecting the performance of your application.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
mtLayer.on("ready", () => {     
        // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
        mtLayer.addPoint({
          data: 'Public_School_Characteristics_2020-21_no_prop.geojson',
          property: "students",
          pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(200, 2000).resample("ease-out-sqrt"),
          pointOpacity: 0.8,
          minPointRadius: 6,
          maxPointRadius: 30,
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
    <title>Vector Tiles in Leaflet JS</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/leaflet-maptilersdk/v4.1.0/leaflet-maptilersdk.umd.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';

        const map = L.map('map').setView([36.69, -92.570801], 5);
              const mtLayer = L.maptiler.maptilerLayer({
                apiKey: 'YOUR_MAPTILER_API_KEY_HERE',
                style: L.maptiler.MapStyle.DATAVIZ.DARK, // optional
              }).addTo(map);

              mtLayer.on("ready", () => {     
                // Leverage the MapTiler SDK layer helpers to easily add polyline / point / polygon / heatmap layers
                mtLayer.addPoint({
                  data: 'Public_School_Characteristics_2020-21_no_prop.geojson',
                  property: "students",
                  pointColor: maptilersdk.ColorRampCollection.PORTLAND.scale(200, 2000).resample("ease-out-sqrt"),
                  pointOpacity: 0.8,
                  minPointRadius: 6,
                  maxPointRadius: 30,
                });

              });
    </script>
</body>
</html>
```
