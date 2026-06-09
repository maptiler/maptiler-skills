# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-filter-bbox/

# MapTiler Geocoding control filter by bbox

Restrict the search results of the geocoding control to the specific area (bounding box). Use the `bbox` options in the control constructor to filter the results specifically within this defined area. The Bounding box is represented as an array, following the format [minX, minY, maxX, maxY]. For a comprehensive list of geocoding control options, refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options). To illustrate, let's consider an example where we limit the search results to the Paris area.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control filter search results to the Paris area
    const gc = new maptilerGeocoder.GeocodingControl({
      bbox: bbox
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
    <title>MapTiler Geocoding control filter by bbox</title>
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

        //set geocoding control filter search results to the Paris area
            const gc = new maptilerGeocoder.GeocodingControl({
              bbox: bbox
            });

            map.addControl(gc, 'top-left');
    </script>
</body>
</html>
```
