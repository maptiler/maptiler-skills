# Source: https://docs.maptiler.com/sdk-js/examples/control-legend/

# Display a map legend control to toggle layers visualization

This tutorial demonstrates the process of presenting a map legend control that allows for the toggling of layer visualization.

By following this guide, users will learn how to display a control panel that showcases the various layers of a map and enables them to easily turn on or off specific layers as needed. This functionality provides a convenient way for users to customize their map viewing experience, allowing them to focus on specific layers of interest while hiding others.

<div class="tab-common-content" markdown="1">

1. Include the `maplibre-gl-legend` JavaScript and CSS files in the `<head>` of your HTML file. To create the legend we will use the [maplibre-gl-legend](https://github.com/watergis/maplibre-gl-legend){:target="_blank" rel="noopener"} plugin.

<pre><code class="language-html"><!--

<link href='https://www.unpkg.com/@watergis/maplibre-gl-legend@latest/dist/maplibre-gl-legend.css' rel='stylesheet' />

<script src="https://www.unpkg.com/@watergis/maplibre-gl-legend@latest/dist/maplibre-gl-legend.umd.js"></script>

--></code></pre>

1. Add event handler for map `load` event. You will add code to create a vector source and a vector layer in this handler.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-28"><code class="language-js"><!--

map.on('load', function() {

});

--></code></pre>

1. Create the list of layers that we want to show in the legend. For each layer we must create a key:value pair where the key is the ID of the layer in the map style and the value is text that is displayed in the legend.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="25-31"><code class="language-js"><!--

map.on('load', function() {

const targets = {

Residential: "Residential",

Water: "Water",

Building: "Building",

Airport: "Airport",

"Other POI": "Pois",

};

});

--></code></pre>

1. Add the `maplibre-gl-legend` control to the map.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="32-38"><code class="language-js"><!--

map.on('load', function() {

const targets = {

Residential: "Residential",

Water: "Water",

Building: "Building",

Airport: "Airport",

"Other POI": "Pois",

};

const options = {

showDefault: true,

showCheckbox: true,

onlyRendered: true,

reverseOrder: true

};

map.addControl(new MaplibreLegendControl.MaplibreLegendControl(targets, options), "bottom-left");

});

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', () => {
        const targets = {
          Residential: "Residential",
          Water: "Water",
          Building: "Building",
          Airport: "Airport",
          "Other POI": "Pois",
        };
        const options = {
          showDefault: true,
          showCheckbox: true,
          onlyRendered: false,
          reverseOrder: true
        };
        map.addControl(new MaplibreLegendControl.MaplibreLegendControl(targets, options), "bottom-left");
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a map legend control to toggle layers visualization</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <link href="https://www.unpkg.com/@watergis/maplibre-gl-legend@latest/dist/maplibre-gl-legend.css" rel="stylesheet" />
    <script src="https://www.unpkg.com/@watergis/maplibre-gl-legend@latest/dist/maplibre-gl-legend.umd.js"></script>
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
            center: [16.62662018, 49.2125578],
            zoom: 10
        });

        map.on('load', () => {
                const targets = {
                  Residential: "Residential",
                  Water: "Water",
                  Building: "Building",
                  Airport: "Airport",
                  "Other POI": "Pois",
                };
                const options = {
                  showDefault: true,
                  showCheckbox: true,
                  onlyRendered: false,
                  reverseOrder: true
                };
                map.addControl(new MaplibreLegendControl.MaplibreLegendControl(targets, options), "bottom-left");
              });
    </script>
</body>
</html>
```
