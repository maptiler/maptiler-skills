# Source: https://docs.maptiler.com/sdk-js/examples/hash/

# Display a map with URL hash

To maintain the map view in the URL hash, you can utilize the `hash:true` option in the map constructor. This feature is particularly valuable for sharing links that lead to a specific map view or loading the map with a predetermined view other than the default.

By implementing this functionality, the map's position, including zoom level, center latitude, center longitude, bearing, and pitch (`#zoom/latitude/longitude/bearing/pitch`), will be synchronized with the hash fragment in the URL of the page. For instance, you can have a URL like: `http://path/to/my/page.html#15.21/46.234453/6.055004/23.2/57`.

This allows users to share and retrieve a particular map view by simply copying and pasting the URL. Whether it's for sharing, bookmarking, or customizing default map views, leveraging the URL hash feature is an excellent way to enhance the user experience and improve map navigation.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element in which the SDK will render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [16.62662018, 49.2125578], // starting position [lng, lat]
      zoom: 14, // starting zoom
      hash: true //keep the map view with the URL hash
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a map with URL hash</title>
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
            center: [16.62662018, 49.2125578],
            zoom: 14
        });

        container: 'map', // container's id or the HTML element in which the SDK will render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [16.62662018, 49.2125578], // starting position [lng, lat]
              zoom: 14, // starting zoom
              hash: true //keep the map view with the URL hash
            });
    </script>
</body>
</html>
```
