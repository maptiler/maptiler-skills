# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-filter-types/

# MapTiler Geocoding control filter by types

The search results filter in the geocoding control can be customized by specifying the type (`poi`) and giving higher priority to results near the user's location. To search for points of interest (POIs) near the user, you can use the `types` and `proximity` options in the control constructor. The geographical point is represented by latitude and longitude coordinates [lat, lng]. For a complete list of geocoding control options, please refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options). In the example provided, we want to prioritize results near Times Square in New York, such as "hotels" and "bars". To see the list of available place types, please check the [place types list](/cloud/api/geocoding/#PlaceType) in the geocoding API documentation.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control search filter by type POIs
    const gc = new maptilerGeocoder.GeocodingControl({
      types: ['poi']
    });
    map.addControl(gc, 'top-left');
    map.on('load', function () {
      //set higher priority for the results near the user's location.
      const userLocation = map.getCenter();
      gc.setOptions({
        proximity: [userLocation.lat, userLocation.lng]
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
    <title>MapTiler Geocoding control filter by types</title>
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
            style: maptilersdk.MapStyle.STREETS.PASTEL,
            center: [0, 0],
            zoom: 0
        });

        //set geocoding control search filter by type POIs
            const gc = new maptilerGeocoder.GeocodingControl({
              types: ['poi']
            });
            map.addControl(gc, 'top-left');
            map.on('load', function () {
              //set higher priority for the results near the user's location.
              const userLocation = map.getCenter();
              gc.setOptions({
                proximity: [userLocation.lat, userLocation.lng]
              });
            });
    </script>
</body>
</html>
```
