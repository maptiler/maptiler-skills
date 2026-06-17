# Source: https://docs.maptiler.com/sdk-js/examples/custom-control/

# Add custom zoom control

The custom zoom control in this example shows the exact current zoom level on a map. It helps set up [zoom-based style rules](/guides/map-design/style-by-the-zoom-range/) or understand data resolution.

Adding [custom controls](/sdk-js/api/controls/#icontrol) can make your application stand out. Before you start making your controls, check out the premade [MapTiler SDK controls](/sdk-js/api/controls/) ([Geolocate](/sdk-js/api/controls/#maptilergeolocatecontrol), [Scale](/sdk-js/api/controls/#scalecontrol), [terrain](/sdk-js/api/controls/#maptilerterraincontrol), ...).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// --- Custom Map Control Implementation ---

    // This class will define how your custom control behaves and looks
    // Read more about Icontrol https://docs.maptiler.com/sdk-js/api/controls/#icontrol
    class ZoomControl {
      onAdd(map) {
        this._map = map;
        this._container = document.createElement('div'); // Create a new div element
        this._container.className = 'maplibregl-ctrl custom-map-control'; // Add SDK's control class and your custom class

        this._updateZoomHandler = () => {
          this._container.innerHTML = `${map.getZoom().toFixed(2)}`;
        };
        // Initial text with current zoom
        this._updateZoomHandler();
        // Add event listener for zoom changes
        map.on('zoomend', this._updateZoomHandler);
        return this._container;
      }

      onRemove() {
        this._container.parentNode.removeChild(this._container);
        this._map = undefined;
      }
    }

    map.addControl(new ZoomControl(), 'top-right');
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add custom zoom control</title>
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
            zoom: 0
        });

        // --- Custom Map Control Implementation ---

            // This class will define how your custom control behaves and looks
            // Read more about Icontrol https://docs.maptiler.com/sdk-js/api/controls/#icontrol
            class ZoomControl {
              onAdd(map) {
                this._map = map;
                this._container = document.createElement('div'); // Create a new div element
                this._container.className = 'maplibregl-ctrl custom-map-control'; // Add SDK's control class and your custom class

                this._updateZoomHandler = () => {
                  this._container.innerHTML = `${map.getZoom().toFixed(2)}`;
                };
                // Initial text with current zoom
                this._updateZoomHandler();
                // Add event listener for zoom changes
                map.on('zoomend', this._updateZoomHandler);
                return this._container;
              }

              onRemove() {
                this._container.parentNode.removeChild(this._container);
                this._map = undefined;
              }
            }

            map.addControl(new ZoomControl(), 'top-right');
    </script>
</body>
</html>
```
