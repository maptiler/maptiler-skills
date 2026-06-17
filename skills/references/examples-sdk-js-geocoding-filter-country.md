# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-filter-country/

# MapTiler Geocoding search results to specified country(ies)

Restricting the search results to a specific country or countries is achievable through Geocoding control. By utilizing the `country` option in the control constructor, one can effectively search for places within the desired country or countries. For a comprehensive list of geocoding control options, refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options). To illustrate, consider the following example where we perform a search limited to Germany and France as the specified countries.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control search filter by Germany and France
    const gc = new maptilerGeocoder.GeocodingControl({
      country: ["DE", "FR"]
    });
    map.addControl(gc, "top-left");
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding search results to specified country(ies)</title>
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
            center: [6.273193, 48.451066],
            zoom: 4
        });

        //set geocoding control search filter by Germany and France
            const gc = new maptilerGeocoder.GeocodingControl({
              country: ["DE", "FR"]
            });
            map.addControl(gc, "top-left");
    </script>
</body>
</html>
```
