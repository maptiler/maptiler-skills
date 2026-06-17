# Source: https://docs.maptiler.com/sdk-js/examples/custom-map/

# Display a custom map

This tutorial shows the process of displaying a customized map on a webpage by utilizing MapTiler.

With [MapTiler's customization tool](https://www.maptiler.com/cloud/customize/), you can craft fully customized interactive web maps. Stand out from your competitors and enhance the quality of your web mapping applications. Take your mapping experience to the next level.

To create your first customized map, check out the [How to create a custom map](/guides/general/how-to-create-custom-map/) tutorial.

<div class="tab-common-content" markdown="1">

1. Replace the style with your custom map style. Check the [Publish the map](/guides/general/how-to-create-custom-map/#publish-the-map) section to get the URL of your custom style.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="20"><code class="language-js">

const map = new maptilersdk.Map({

container: 'map', // container id

style: `YOUR_CUSTOM_MAP_ID`,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

</code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
        style: 'YOUR_CUSTOM_MAP_ID',
        center: [10.989249486220501, 46.948652944430734], // starting position [lng, lat]
        zoom: 11, // starting zoom
        });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a custom map</title>
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
            style: 'YOUR_CUSTOM_MAP_ID',
            center: [10.989249486220501, 46.948652944430734],
            zoom: 11
        });

        container: 'map', // container's id or the HTML element to render the map
                style: 'YOUR_CUSTOM_MAP_ID',
                center: [10.989249486220501, 46.948652944430734], // starting position [lng, lat]
                zoom: 11, // starting zoom
                });
    </script>
</body>
</html>
```
