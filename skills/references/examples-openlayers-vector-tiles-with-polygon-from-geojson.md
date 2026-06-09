# Source: https://docs.maptiler.com/openlayers/examples/vector-tiles-with-polygon-from-geojson/

# Example

This tutorial shows how to add a polygon feature from external GeoJSON to your vector tiles map. If you don't know how to display vector tiles map follow this tutorial [Vector tiles in OpenLayers](../vector-tiles-in-openlayers/).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
olms.apply(map, styleJson);

    const geojsonLayers = new ol.layer.Vector({
      source: new ol.source.Vector({
        url: `https://api.maptiler.com/data/YOUR_DATA_ID/features.json?key=${key}`,
        format: new ol.format.GeoJSON(),
      }),
      style: new ol.style.Style({
        stroke: new ol.style.Stroke({
          color: 'grey',
          width: 1 // not connected with scale in screen resolution
        }),
        fill: new ol.style.Fill({
          color: 'rgba(165,80,51,0.8)',
        }),
      })
    });
    geojsonLayers.setZIndex(1);
    map.addLayer(geojsonLayers);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Example</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@10.9.0/ol.css">
    <script src="https://cdn.jsdelivr.net/npm/ol@10.9.0/dist/ol.js"></script>
    <script src="https://unpkg.com/ol-mapbox-style@13.4.1/dist/olms.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        const key = 'YOUR_MAPTILER_API_KEY';
            const styleJson = `https://api.maptiler.com/maps/streets-v4/style.json?key=${key}`;

            const attribution = new ol.control.Attribution({
              collapsible: false,
            });

            const map = new ol.Map({
              target: 'map',
              controls: ol.control.defaults.defaults({ attribution: false }).extend([attribution]),
              view: new ol.View({
                constrainResolution: true,
                center: ol.proj.fromLonLat([0, 0]),
                zoom: 2
              })
            });
            olms.apply(map, styleJson);

            const geojsonLayers = new ol.layer.Vector({
              source: new ol.source.Vector({
                url: `https://api.maptiler.com/data/YOUR_DATA_ID/features.json?key=${key}`,
                format: new ol.format.GeoJSON(),
              }),
              style: new ol.style.Style({
                stroke: new ol.style.Stroke({
                  color: 'grey',
                  width: 1 // not connected with scale in screen resolution
                }),
                fill: new ol.style.Fill({
                  color: 'rgba(165,80,51,0.8)',
                }),
              })
            });
            geojsonLayers.setZIndex(1);
            map.addLayer(geojsonLayers);
    </script>
</body>
</html>
```
