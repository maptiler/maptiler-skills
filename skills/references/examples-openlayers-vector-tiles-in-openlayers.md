# Source: https://docs.maptiler.com/openlayers/examples/vector-tiles-in-openlayers/

# Example

Vector tiles maps are made of mathematical interpretations of geometric features such as points, curves or polygons. Vector tiles are rendered on the client’s side with a style, which is a small text file that defines how certain map elements look and how they are displayed. Read more about Vector tiles in this article [What are vector tiles and why you should care?](https://www.maptiler.com/news/2019/02/what-are-vector-tiles-and-why-you-should-care/)

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
olms.apply(map, styleJson);
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
    </script>
</body>
</html>
```
