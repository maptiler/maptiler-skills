# Source: https://docs.maptiler.com/sdk-js/examples/space-milkyway-halo/

# Globe with space background

Customize the map background to create a red Milky Way effect and create a *"toxic"* halo around the Earth.

This option **only takes effect** when used in conjunction with the `projection: 'globe'` parameter.

In this example, we'll use a Milky Way background, we will change the color of the stars to red and add a custom halo to create a toxic atmosphere effect.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.SATELLITE,
      projection: "globe",
      center: [83, 30.8],
      zoom: 0,
      halo: {
        scale: 1,
        stops: [
          [0.0, "rgba(77,51,15,1)"],
          [0.5, "rgba(255,111,0,0.5)"],
          [0.75, "rgba(250,0,0,0.0)"],
        ],
      },
      space: {
        color: "#ff0000",
        preset: "milkyway-bright",
      }
    });
    map.on('load', () => {
      map.flyTo({ //zoom out the map so that the background of the stars can be seen better.
        zoom: -1,
        essential: true
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
    <title>Globe with space background</title>
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
            style: maptilersdk.MapStyle.SATELLITE,
            center: [83, 30.8],
            zoom: 0
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.SATELLITE,
              projection: "globe",
              center: [83, 30.8],
              zoom: 0,
              halo: {
                scale: 1,
                stops: [
                  [0.0, "rgba(77,51,15,1)"],
                  [0.5, "rgba(255,111,0,0.5)"],
                  [0.75, "rgba(250,0,0,0.0)"],
                ],
              },
              space: {
                color: "#ff0000",
                preset: "milkyway-bright",
              }
            });
            map.on('load', () => {
              map.flyTo({ //zoom out the map so that the background of the stars can be seen better.
                zoom: -1,
                essential: true
              });
            });
    </script>
</body>
</html>
```
