# Source: https://docs.maptiler.com/sdk-js/examples/ar-control-geojson-line/

# MapTiler AR Control

To create a three-dimensional (3D) representation of a cycling or hiking route on an augmented reality (AR) map, you have the option to add a GeoJSON, GPX, or KML line. Compatible with **WebXR** or **Apple Quick Look**.

In addition to lines, you can also incorporate various types of data, such as points and polygons, into your maps. These data can be viewed within the AR model.

If you're using iOS (Quick Look), the activateAR option in the control allows for automatic activation of the AR model as soon as the data becomes available.

Create GeoJSON source. Check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial. Publish the dataset and copy the geojson dataset ID. Download the sample data [here](../geojson-line/Line_GeoJSON_example.geojson){:target="_blank" rel="noopener"}.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Waiting for the map to be ready
      map.on("load", async (e) => {
        const arControl = new maptilerarcontrol.MaptilerARControl({
          activateAR: true //When the platform allows automatically activates the AR mode as soon as the data is ready
        });

        arControl.on("computeStart", (e) => {
          overlay.style.display = "inherit";
        })

        arControl.on("computeEnd", (e) => {
          overlay.style.display = "none";
        })

        map.addControl(arControl, "top-left");

        const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
        map.addSource('gps_tracks', {
          'type': 'geojson',
          'data': geojson
        });
        map.addLayer({
          'id': 'grand_teton',
          'type': 'line',
          'source': 'gps_tracks',
          'layout': {},
          'paint': {
            'line-color': '#e11',
            'line-width': 4
          }
        });
      })
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler AR Control</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-ar-control/3.0.4/maptiler-ar-control.umd.min.js"></script>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-110.75954, 43.72874],
            zoom: 13.5,
            pitch: 45,
            bearing: -7.2
        });

        // Waiting for the map to be ready
              map.on("load", async (e) => {
                const arControl = new maptilerarcontrol.MaptilerARControl({
                  activateAR: true //When the platform allows automatically activates the AR mode as soon as the data is ready
                });

                arControl.on("computeStart", (e) => {
                  overlay.style.display = "inherit";
                })

                arControl.on("computeEnd", (e) => {
                  overlay.style.display = "none";
                })

                map.addControl(arControl, "top-left");

                const geojson = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');
                map.addSource('gps_tracks', {
                  'type': 'geojson',
                  'data': geojson
                });
                map.addLayer({
                  'id': 'grand_teton',
                  'type': 'line',
                  'source': 'gps_tracks',
                  'layout': {},
                  'paint': {
                    'line-color': '#e11',
                    'line-width': 4
                  }
                });
              })
    </script>
</body>
</html>
```
