# Source: https://docs.maptiler.com/sdk-js/examples/custom-controls-declarative/

# MapTiler custom controls

Declarative controls offer a simple way to add interactive UI elements to the map by using HTML attributes alone. Instead of instantiating controls through JavaScript, developers annotate DOM elements and allow the SDK to discover and wire them automatically.

To activate declarative control detection set the `customControls` option to `true` in the map initialization configuration. Alternatively, customControls may be set to a **CSS selector string**, restricting autodetection to:

* Elements matching the selector directly

* Or elements whose **ancestor** matches the selector

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      customControls: true,
      navigationControl: false,
      geolocateControl: false,
      terrainExaggeration: 4,
    });

    //custom control (center map)
    document.querySelector(".home-button")?.addEventListener("click", () => map.easeTo({ center: [15, 50], zoom: 7 }));
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler custom controls</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:FILL@0..1" rel="stylesheet" />
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
            center: [15, 50],
            zoom: 7 }));
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              customControls: true,
              navigationControl: false,
              geolocateControl: false,
              terrainExaggeration: 4,
            });

            //custom control (center map)
            document.querySelector(".home-button")?.addEventListener("click", () => map.easeTo({ center: [15, 50], zoom: 7 }));
    </script>
</body>
</html>
```
