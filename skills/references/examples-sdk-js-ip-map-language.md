# Source: https://docs.maptiler.com/sdk-js/examples/ip-map-language/

# Change the map labels language based on visitor's location

This tutorial demonstrates the process of automatically adjusting the language of map labels based on the visitor's location using the [MapTiler Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"}.

By utilizing the MapTiler Geolocation API, it becomes possible to dynamically change the language of map labels to match the user's location main language. This feature enhances the user experience by providing map information in a language that is familiar and easily understood by the visitor. With the MapTiler Geolocation API, businesses and websites can seamlessly integrate this functionality into their mapping applications, ensuring a personalized and localized experience for their users.

<div class="tab-common-content" markdown="1">

1. Add event handler for map `load` event. You will add code to change disputed borders according to your map visitor's location in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-26"><code class="language-js"><!--

map.on('load', async () => {

});

--></code></pre>

1. Get the user's IP country languages codes.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-26"><code class="language-js"><!--

map.on('load', async () => {

const geolocationIP = await maptilersdk.geolocation.info();

const {country_languages} = geolocationIP;

});

--></code></pre>

1. Change the language of the map. In this example we will use the first language of the language array of the visitor's country.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="27"><code class="language-js"><!--

map.on('load', async () => {

const geolocationIP = await maptilersdk.geolocation.info();

const {country_languages} = geolocationIP;

map.setLanguage(`name:${country_languages[0]}`);

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
      center: [20, 50], // starting position [lng, lat]
      zoom: 4, // starting zoom
    });
    map.on('load', async () => {
      const geolocationIP = await maptilersdk.geolocation.info();
      const {country_languages} = geolocationIP;
      map.setLanguage(`name:${country_languages[0]}`);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change the map labels language based on visitor's location</title>
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
            center: [20, 50],
            zoom: 4
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [20, 50], // starting position [lng, lat]
              zoom: 4, // starting zoom
            });
            map.on('load', async () => {
              const geolocationIP = await maptilersdk.geolocation.info();
              const {country_languages} = geolocationIP;
              map.setLanguage(`name:${country_languages[0]}`);
            });
    </script>
</body>
</html>
```
