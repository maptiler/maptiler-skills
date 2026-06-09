# Source: https://docs.maptiler.com/sdk-js/examples/ip-country-map/

# Center map based on visitor's country bounds

In this tutorial, we will demonstrate the utilization of the `geolocate: maptilersdk.GeolocationType.COUNTRY` feature to center the map according to the boundaries of the visitor's country. This functionality is made possible through the implementation of the [MapTiler Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"}.

By utilizing this option, the map will automatically adjust its center based on the geographical location of the user, ensuring a personalized and seamless experience. This feature offers a convenient way to provide contextually relevant information or tailor the map view to suit the user's needs. Get started with implementing this feature today to enhance your mapping application and provide a more personalized experience for your users.

<div class="tab-common-content" markdown="1">

1. Modify the map options. Remove the center and zoom options and add the geolocate option.

<pre class="line-numbers" data-start="18" data-line-offset="17"><code class="language-diff-js diff-highlight"><!--

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element in which SDK will render the map

style: maptilersdk.MapStyle.STREETS,

- center: [16.62662018, 49.2125578], // starting position [lng, lat]

- zoom: 10, // starting zoom

+ geolocate: maptilersdk.GeolocationType.COUNTRY

});

--></code></pre>

1. Now the map options should look like this.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="21"><code class="language-js"><!--

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element in which SDK will render the map

style: maptilersdk.MapStyle.STREETS,

geolocate: maptilersdk.GeolocationType.COUNTRY

});

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      geolocate: maptilersdk.GeolocationType.COUNTRY
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Center map based on visitor's country bounds</title>
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
            center: [0, 0],
            zoom: 0
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              geolocate: maptilersdk.GeolocationType.COUNTRY
            });
    </script>
</body>
</html>
```
