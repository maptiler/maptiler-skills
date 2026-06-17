# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-filter-proximity/

# MapTiler Geocoding control filter by proximity

To enhance search results, the geocoding control prioritizes locations that are closer to a specific geographical point. By utilizing the `proximity` options in the control constructor, results near the provided point are ranked higher.

In the given example, we aim to prioritize results that are near Times Square in New York (e.g., "Park Avenue"). We are using a define a geographical point by its latitude and longitude [lng, lat], for this you must use the `fixed` option.

``` js

proximity: [

{

type: "fixed",

coordinates: [lng, lat],

},

]

```

You can also use the map center coordinates instead of a specific coordinate. For example:

``` js

proximity: [

{

"type":"map-center",

"minZoom":12

}

]

```

For a complete list of geocoding control options, refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options).

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control prioritize results near Time Square in New York
    const gc = new maptilerGeocoder.GeocodingControl({
      proximity: [
        {
          type: "fixed",
          coordinates: [-73.986644, 40.75614],
        },
      ]
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
    <title>MapTiler Geocoding control filter by proximity</title>
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
            style: maptilersdk.MapStyle.STREETS.DARK,
            center: [-73.986644, 40.756140],
            zoom: 14
        });

        //set geocoding control prioritize results near Time Square in New York
            const gc = new maptilerGeocoder.GeocodingControl({
              proximity: [
                {
                  type: "fixed",
                  coordinates: [-73.986644, 40.75614],
                },
              ]
            });
            map.addControl(gc, 'top-left');
    </script>
</body>
</html>
```
