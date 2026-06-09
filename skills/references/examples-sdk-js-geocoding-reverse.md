# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-reverse/

# MapTiler Geocoding control reverse geocoding

Activate the `enableReverse` option during geocoding control initialization to support coordinate-based searches.

Setting this option to `"always"` lets you locate features using names, addresses, and coordinate pairs. For example typing `41.874836, -87.628261` in the search box will display items that match those coordinates, addresses, regions, states, etc.

Geocoding (forward geocoding and reverse geocoding) is a technique for place identification - either by name or coordinates. See the [Geocoding page](https://www.maptiler.com/cloud/geocoding/) for more details.

<sup>Click on the map or type a coordinate in the search box to search for addresses</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control search by coodinates (reverse geocoding)
    const gc = new maptilerGeocoder.GeocodingControl({
      enableReverse: "always",
    });

    map.addControl(gc, 'top-left');
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding control reverse geocoding</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/maptilersdk.umd.js"></script>
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
            style: maptilersdk.MapStyle.STREETS.LIGHT,
            center: [0, 0],
            zoom: 0
        });

        //set geocoding control search by coodinates (reverse geocoding)
            const gc = new maptilerGeocoder.GeocodingControl({
              enableReverse: "always",
            });

            map.addControl(gc, 'top-left');
    </script>
</body>
</html>
```
