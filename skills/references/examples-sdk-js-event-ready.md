# Source: https://docs.maptiler.com/sdk-js/examples/event-ready/

# Ready event

The `ready` event happens just after the `load` event but waits until all the controls managed by the `Map` constructor are dealt with, some having an asynchronous logic to set up.

Since the `ready` event waits until all the basic controls are nicely positioned, it is **safer** to use `ready` than `load` if you plan to add other custom controls with the `.addControl()` method.

In this example, we will wait for the ready event to add the terrain control to the map.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// Set an event listener that fires
    // when the map has finished loading.
    map.on('ready', function () {
      console.log('A ready event occurred.');
      const terrainControl = new maptilersdk.MaptilerTerrainControl();
      map.addControl(terrainControl);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ready event</title>
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
            style: maptilersdk.MapStyle.OUTDOOR,
            center: [-77.60308, -9.1135],
            zoom: 12.32
        });

        // Set an event listener that fires
            // when the map has finished loading.
            map.on('ready', function () {
              console.log('A ready event occurred.');
              const terrainControl = new maptilersdk.MaptilerTerrainControl();
              map.addControl(terrainControl);
            });
    </script>
</body>
</html>
```
