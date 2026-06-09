# Source: https://docs.maptiler.com/sdk-js/examples/halo-custom/

# Globe with halo

Use the `halo` option in the map constructor to create a custom halo. You can define a radial gradient with scale and stops to add a custom atmospheric glow around the globe.

This option **only takes effect** when used in conjunction with the `projection: 'globe'` parameter.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.HYBRID,
      projection: "globe",
      halo: {
        scale: 1.5, // Halo size in multiples of the Earth's radius
        stops: [
          [0.0, "rgba(135,206,250,1)"],
          [0.5, "rgba(0,0,250,0.75)"],
          [0.75, "rgba(250,0,0,0.0)"],
        ],
      }
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Globe with halo</title>
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
            center: [0, 0],
            zoom: 0
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.HYBRID,
              projection: "globe",
              halo: {
                scale: 1.5, // Halo size in multiples of the Earth's radius
                stops: [
                  [0.0, "rgba(135,206,250,1)"],
                  [0.5, "rgba(0,0,250,0.75)"],
                  [0.75, "rgba(250,0,0,0.0)"],
                ],
              }
            });
    </script>
</body>
</html>
```
