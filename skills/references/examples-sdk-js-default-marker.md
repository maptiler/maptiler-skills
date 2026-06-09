# Source: https://docs.maptiler.com/sdk-js/examples/default-marker/

# Display a marker

This comprehensive step-by-step tutorial provides a detailed explanation of how to incorporate a default Marker onto a map. By following this tutorial you will be able to create a map with a pin.

<div class="tab-common-content" markdown="1">

1. Create a new marker using the .marker function. Set Lng/Lat of the marker using `.setLngLat()` function, and finally add it to the current map using `.addTo()` function.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js">

const marker = new maptilersdk.Marker()

.setLngLat([, ])

.addTo(map);

</code></pre>

</div>

<script>

document.addEventListener("pageReplaceText", function(event) {

if (mapPosition) {

const [zoom, lat, lng] = mapPosition.split('/');

replaceText('code[class*=language-]', 'setLngLat\\(\[\-?[0-9]*(\.[0-9]+)?, \-?[0-9]*(\.[0-9]+)?\]\\)', `setLngLat([${longitude}, ${latitude}])`, 'g');

}

});

</script>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [12.550343, 55.665957], // starting position [lng, lat]
      zoom: 9, // starting zoom
    });
    const marker = new maptilersdk.Marker()
      .setLngLat([12.550343, 55.665957])
      .addTo(map);
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a marker</title>
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
            center: [12.550343, 55.665957],
            zoom: 9
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [12.550343, 55.665957], // starting position [lng, lat]
              zoom: 9, // starting zoom
            });
            const marker = new maptilersdk.Marker()
              .setLngLat([12.550343, 55.665957])
              .addTo(map);
    </script>
</body>
</html>
```
