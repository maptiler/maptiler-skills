# Source: https://docs.maptiler.com/sdk-js/examples/local-geojson-experimental/

# View local GeoJSON (experimental)

Download the example [Average Wind Speeds GeoJSON](https://data-roscoco.opendata.arcgis.com/datasets/0371f25602be4f5f9145e9b76e2de54b_0.geojson?outSR=%7B%22latestWkid%22%3A2157%2C%22wkid%22%3A2157%7D). This particular example showcases the usage of the File System Access API in newer versions of Chrome and Edge browsers (see the article [The File System Access API: simplifying access to local files](https://web.dev/file-system-access/) and the [file system access explanation](https://github.com/WICG/file-system-access/blob/main/EXPLAINER.md)). Instead of uploading the file to a server and then retrieving it, the browser directly accesses the file locally, eliminating the need for any network transfer. Unlike the File API, this example also allows writing to the file, although that functionality is not implemented here. It's important to note that this example is experimental as the `window.showOpenFilePicker` is not supported by all major browsers. For details on browser compatibility, please refer to the [browser compatibility page](https://developer.mozilla.org/en-US/docs/Web/API/Window/showOpenFilePicker#browser_compatibility).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const viewbutton = document.getElementById('viewbutton');

    async function buttonClickHandler() {
      let fileHandle;
      [fileHandle] = await window.showOpenFilePicker({
        // allow only single file
        multiple: false,

        // apply filter for GeoJSON files
        types: [
          {
            description: 'GeoJSON',
            accept: { 'application/geo+json': ['.geojson'] }
          }
        ],

        // start in download directory
        startIn: 'downloads'
      });

      // get file handle and read content
      const file = await fileHandle.getFile();
      const contents = await file.text();

      // parse file as json and add as source to the map
      map.addSource('uploaded-source', {
        'type': 'geojson',
        'data': JSON.parse(contents)
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
    }

    if ('showOpenFilePicker' in window) {
      viewbutton.addEventListener('click', buttonClickHandler);
    } else {
      viewbutton.innerText =
        'Your browser does not support File System Access API';
      // If you want a fallback, try <input type="file">; but this uses classical file upload
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View local GeoJSON (experimental)</title>
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

        const viewbutton = document.getElementById('viewbutton');

            async function buttonClickHandler() {
              let fileHandle;
              [fileHandle] = await window.showOpenFilePicker({
                // allow only single file
                multiple: false,

                // apply filter for GeoJSON files
                types: [
                  {
                    description: 'GeoJSON',
                    accept: { 'application/geo+json': ['.geojson'] }
                  }
                ],

                // start in download directory
                startIn: 'downloads'
              });

              // get file handle and read content
              const file = await fileHandle.getFile();
              const contents = await file.text();

              // parse file as json and add as source to the map
              map.addSource('uploaded-source', {
                'type': 'geojson',
                'data': JSON.parse(contents)
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
            }

            if ('showOpenFilePicker' in window) {
              viewbutton.addEventListener('click', buttonClickHandler);
            } else {
              viewbutton.innerText =
                'Your browser does not support File System Access API';
              // If you want a fallback, try <input type="file">; but this uses classical file upload
            }
    </script>
</body>
</html>
```
