# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-reverse-json/

# Reverse geocoding

This example demonstrates the process of discovering locations by inputting coordinates (known as reverse geocoding) obtained from the user's current position. Reverse geocoding transforms coordinates into place names.

By default, the example displays the user's location, which is determined based on their IP address. However, you also have the option to manually enter specific coordinates in the designated text fields or utilize the map interface (click on the map) to search for places at those particular coordinates.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS.LIGHT,
      geolocate: maptilersdk.GeolocationType.POINT
    });

    map.on('click', async (e) => {
      const {lng, lat} = e.lngLat;
      document.getElementById('lat').value = lat;
      document.getElementById('lng').value = lng;
      reverseGeocoding(lng, lat);
    });
    
    map.on('load', function() {
      const {lng, lat} = map.getCenter();
      document.getElementById('lat').value = lat;
      document.getElementById('lng').value = lng;
      reverseGeocoding(lng, lat);
    });
    
    document.getElementById('btn-search-reverse').addEventListener('click', function() {
      const lng = parseFloat(document.getElementById('lng').value);
      const lat = parseFloat(document.getElementById('lat').value);
      reverseGeocoding(lng, lat);
    });
    
    let marker;
    
    async function reverseGeocoding(lng, lat){
      if (!lng || !lat || lng === "" || lat === "") {
        document.getElementById('results').innerHTML = "";
      } else{
        const result = await maptilersdk.geocoding.reverse([lng, lat]);
        document.getElementById('results').innerHTML = JSON.stringify(
          result,
          null,
          2
        );
        if (marker) {
          marker.setLngLat([lng, lat]);
        } else {
          marker = new maptilersdk.Marker()
          .setLngLat([lng, lat])
          .addTo(map);
        }
        map.flyTo({
          center: [
            lng,
            lat
          ],
          padding: {right: window.innerWidth/2},
          essential: true // this animation is considered essential with respect to prefers-reduced-motion
        });
      }
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reverse geocoding</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://docs.maptiler.com/styles/base.css" rel="stylesheet" />
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
            center: [
            lng,
            lat
          ],
            zoom: 0
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS.LIGHT,
              geolocate: maptilersdk.GeolocationType.POINT
            });

            map.on('click', async (e) => {
              const {lng, lat} = e.lngLat;
              document.getElementById('lat').value = lat;
              document.getElementById('lng').value = lng;
              reverseGeocoding(lng, lat);
            });

            map.on('load', function() {
              const {lng, lat} = map.getCenter();
              document.getElementById('lat').value = lat;
              document.getElementById('lng').value = lng;
              reverseGeocoding(lng, lat);
            });

            document.getElementById('btn-search-reverse').addEventListener('click', function() {
              const lng = parseFloat(document.getElementById('lng').value);
              const lat = parseFloat(document.getElementById('lat').value);
              reverseGeocoding(lng, lat);
            });

            let marker;

            async function reverseGeocoding(lng, lat){
              if (!lng || !lat || lng === "" || lat === "") {
                document.getElementById('results').innerHTML = "";
              } else{
                const result = await maptilersdk.geocoding.reverse([lng, lat]);
                document.getElementById('results').innerHTML = JSON.stringify(
                  result,
                  null,
                  2
                );
                if (marker) {
                  marker.setLngLat([lng, lat]);
                } else {
                  marker = new maptilersdk.Marker()
                  .setLngLat([lng, lat])
                  .addTo(map);
                }
                map.flyTo({
                  center: [
                    lng,
                    lat
                  ],
                  padding: {right: window.innerWidth/2},
                  essential: true // this animation is considered essential with respect to prefers-reduced-motion
                });
              }
            }
    </script>
</body>
</html>
```
