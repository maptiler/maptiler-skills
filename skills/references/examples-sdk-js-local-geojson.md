# Source: https://docs.maptiler.com/sdk-js/examples/local-geojson/

# View local GeoJSON

Download the example [Average Wind Speeds GeoJSON](https://data-roscoco.opendata.arcgis.com/datasets/0371f25602be4f5f9145e9b76e2de54b_0.geojson?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D). Instead of uploading the file to a server and reading it from there, the browser directly accesses the file locally, eliminating the need for any network transfer. If you wish to write to the file that has been opened, you can refer to the following example that utilizes the File System Access API: [View local GeoJSON (experimental)](/sdk-js/examples/local-geojson-experimental/).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
function handleFileSelect(evt) {
      const file = evt.target.files[0]; // Read first selected file

      const reader = new FileReader();

      reader.onload = function (theFile) {
        // Parse as (geo)JSON
        const geoJSONcontent = JSON.parse(theFile.target.result);

        // Add as source to the map
        map.addSource('uploaded-source', {
          'type': 'geojson',
          'data': geoJSONcontent
        });

        map.addLayer({
          'id': 'uploaded-polygons',
          'type': 'fill',
          'source': 'uploaded-source',
          'paint': {
            'fill-color': '#888888',
            'fill-outline-color': 'red',
            'fill-opacity': 0.4
          },
          // filter for (multi)polygons; for also displaying linestrings
          // or points add more layers with different filters
          'filter': ['==', '$type', 'Polygon']
        });
      };

      // Read the GeoJSON as text
      reader.readAsText(file, 'UTF-8');
    }

    document
      .getElementById('file')
      .addEventListener('change', handleFileSelect, false);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View local GeoJSON</title>
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
            center: [-8.3226655, 53.7654751],
            zoom: 8
        });

        function handleFileSelect(evt) {
              const file = evt.target.files[0]; // Read first selected file

              const reader = new FileReader();

              reader.onload = function (theFile) {
                // Parse as (geo)JSON
                const geoJSONcontent = JSON.parse(theFile.target.result);

                // Add as source to the map
                map.addSource('uploaded-source', {
                  'type': 'geojson',
                  'data': geoJSONcontent
                });

                map.addLayer({
                  'id': 'uploaded-polygons',
                  'type': 'fill',
                  'source': 'uploaded-source',
                  'paint': {
                    'fill-color': '#888888',
                    'fill-outline-color': 'red',
                    'fill-opacity': 0.4
                  },
                  // filter for (multi)polygons; for also displaying linestrings
                  // or points add more layers with different filters
                  'filter': ['==', '$type', 'Polygon']
                });
              };

              // Read the GeoJSON as text
              reader.readAsText(file, 'UTF-8');
            }

            document
              .getElementById('file')
              .addEventListener('change', handleFileSelect, false);
    </script>
</body>
</html>
```
