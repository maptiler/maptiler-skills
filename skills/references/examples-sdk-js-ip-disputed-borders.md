# Source: https://docs.maptiler.com/sdk-js/examples/ip-disputed-borders/

# Display disputed borders based on visitor's view

This tutorial shows how to automatically change disputed borders based on the geographical location of your map visitor's location using the [MapTiler Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"}.

By following this tutorial, you will be able to dynamically adjust disputed borders based on the location of the person accessing the map on your application or according to the official policy of the country your visitor joined from. The MapTiler Geolocation API serves as a powerful tool in achieving this functionality.

<div class="tab-common-content" markdown="1">

1. Create the `showDisputedBorders` function. This function changes the filters of the disputed border layers to show or hide the borders depending on the country's policy.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-35"><code class="language-js"><!--

const showDisputedBorders = (map, country_code) => {

/*You can uncomment the following line to force a country code to see the map boundaries changes. Use the country code you want to test.*/

//country_code = "IN";

const claimed_by_countries = ["RU", "UA", "XN", "AM", "XK", "IN", "PK", "CN", "NP", "BT", "TR", "SY", "PS", "IL", "SY", "ET", "EH", "SD", "SS", "KE"];

if (!claimed_by_countries.includes(country_code)){ //if the country code is not in the list of disputed ones, do nothing and return

return;

}

if ( map.getLayer("Disputed border")) {

const boundary_disputed = map.getLayer("Disputed border");

map.setFilter("Disputed border", [...boundary_disputed.filter, ["==", "claimed_by", country_code]]);

}

}

--></code></pre>

1. Add event handler for map `load` event. You will add code to change disputed borders according to your map visitor's location in this handler.

<pre class="line-numbers" data-start="36" data-line-offset="35" data-line="36-38"><code class="language-js"><!--

map.on('load', async () => {

});

--></code></pre>

1. Get the user's IP country code and call the `showDisputedBorders` function.

<pre class="line-numbers" data-start="36" data-line-offset="35" data-line="37-39"><code class="language-js"><!--

map.on('load', async () => {

const geolocationIP = await maptilersdk.geolocation.info();

const {country_code} = geolocationIP;

showDisputedBorders(map, country_code);

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
      center: [75.503, 33.629], // starting position [lng, lat]
      zoom: 6, // starting zoom
    });

    const showDisputedBorders = (map, country_code) => {
      /*You can uncomment the following line to force a country code to see the map boundaries changes. Use the country code you want to test.*/
      //country_code = "IN"; 
      const claimed_by_countries = ["RU", "UA", "XN", "AM", "XK", "IN", "PK", "CN", "NP", "BT", "TR", "SY", "PS", "IL", "SY", "ET", "EH", "SD", "SS", "KE"];
      if (!claimed_by_countries.includes(country_code)){ //if the country code is not in the list of disputed ones, do nothing and return
        disputedLayers.forEach(layer => {
          const boundary_disputed = map.getLayer(layer);
          map.setFilter(layer, [...disputedLayersFilters[layer]]);
        });
        return;
      }
      if ( map.getLayer("Disputed border")) {
        disputedLayers.forEach(layer => {
          const boundary_disputed = map.getLayer(layer);
          map.setFilter(layer, [...disputedLayersFilters[layer], ["==", "claimed_by", country_code]]);
        });
      }
    }

    map.on('load', async () => {
      const geolocationIP = await maptilersdk.geolocation.info();
      const {country_code} = geolocationIP;
      showDisputedBorders(map, country_code);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display disputed borders based on visitor's view</title>
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
            center: [75.503, 33.629],
            zoom: 6
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [75.503, 33.629], // starting position [lng, lat]
              zoom: 6, // starting zoom
            });

            const showDisputedBorders = (map, country_code) => {
              /*You can uncomment the following line to force a country code to see the map boundaries changes. Use the country code you want to test.*/
              //country_code = "IN"; 
              const claimed_by_countries = ["RU", "UA", "XN", "AM", "XK", "IN", "PK", "CN", "NP", "BT", "TR", "SY", "PS", "IL", "SY", "ET", "EH", "SD", "SS", "KE"];
              if (!claimed_by_countries.includes(country_code)){ //if the country code is not in the list of disputed ones, do nothing and return
                disputedLayers.forEach(layer => {
                  const boundary_disputed = map.getLayer(layer);
                  map.setFilter(layer, [...disputedLayersFilters[layer]]);
                });
                return;
              }
              if ( map.getLayer("Disputed border")) {
                disputedLayers.forEach(layer => {
                  const boundary_disputed = map.getLayer(layer);
                  map.setFilter(layer, [...disputedLayersFilters[layer], ["==", "claimed_by", country_code]]);
                });
              }
            }

            map.on('load', async () => {
              const geolocationIP = await maptilersdk.geolocation.info();
              const {country_code} = geolocationIP;
              showDisputedBorders(map, country_code);
            });
    </script>
</body>
</html>
```
