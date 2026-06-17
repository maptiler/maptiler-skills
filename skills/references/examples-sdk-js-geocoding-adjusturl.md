# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-adjusturl/

# MapTiler Geocoding control adjustUrl

Use the `adjustUrl` option when initializing the geocoding control to modify the geocoding URL prior to fetching.  This options supersedes the **deprecated** `adjustUrlQuery` option. Thanks to this capability you can have full control over how the search control behaves.

In this example, we will use the option to customize the URL specifically for coordinate-based searches (reverse geocoding) to display only results of the address type and limit the output to 3 entries. For other search types, it returns all kinds of elements. For instance, entering `41.394442, 2.156936` in the search box, it will return a list of 3 addresses.

<sup>Click on the map or type a coordinate in the search box to search for addresses</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control enable reverse and adjustUrl for reverse geocoding
    const gc = new maptilerGeocoder.GeocodingControl({
      enableReverse: "always",
      adjustUrl(url) {
        // for reverse geocoding use only address type
        if (/\/\d+\.?\d*%2C\d+.?\d*.json$/.test(url.pathname)) {
          url.searchParams.set("types", "address");
          url.searchParams.set("limit", "3");
        }
      },
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
    <title>MapTiler Geocoding control adjustUrl</title>
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
            style: maptilersdk.MapStyle.STREETS,
            center: [0, 0],
            zoom: 0
        });

        //set geocoding control enable reverse and adjustUrl for reverse geocoding
            const gc = new maptilerGeocoder.GeocodingControl({
              enableReverse: "always",
              adjustUrl(url) {
                // for reverse geocoding use only address type
                if (/\/\d+\.?\d*%2C\d+.?\d*.json$/.test(url.pathname)) {
                  url.searchParams.set("types", "address");
                  url.searchParams.set("limit", "3");
                }
              },
            });

            map.addControl(gc, 'top-left');
    </script>
</body>
</html>
```
