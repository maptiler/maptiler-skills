# Source: https://docs.maptiler.com/sdk-js/examples/change-map-styles/

# Display a map

This tutorial demonstrates the process of altering map styles, allowing users to seamlessly transition between the built-in maps and their customized maps. Explore the selection of pre-designed styles available in MapTiler's library by referring to the [list of built-in styles](/sdk-js/api/map-styles/#mapstylelist).

MapTiler provides a wide range of predefined styles, enabling users to customize their maps to suit their specific preferences. Additionally, you have the option to create a completely 100% customized map using [MapTiler's  tool](https://www.maptiler.com/cloud/customize/).

Using the built-in styles and their variants defined in the SDK (`maptilersdk.MapStyle`) has several advantages such as:

- If we make an update to a style, you won't have to modify your codebase. Always use the latest version of styles.

- They are easier to remember, no need to type along the style URL. No more putting the API key in every URL.

- Code completion: reducing typos and other common mistakes.

The built-in styles generally define a purpose for which this style is the most relevant: **street navigation, outdoor adventure, minimalist dashboard**, etc. Then, each style offers a range of **variants** that contain the same level of information and have the same purpose but use different color schemes like **dark, light**, etc.

<div class="tab-common-content" markdown="1">

1. Change the map style to a hybrid satellite images.

<pre class="line-numbers" data-start="23" data-line-offset="22" data-line="23"><code class="language-js"><!--

map.setStyle(MapStyle.STREETS.DARK);

--></code></pre>

1.  Create a selector to change the map style. In this example we will use some of the build-in styles. See the full <a href="/sdk-js/api/map-styles/#mapstylelist">list of styles</a>. Copy the following code into your HTML file.

<pre><code class="language-html"><!--

<select class="mapstyles-select">

<optgroup label="Navigation and city exploration">

<option value="STREETS">STREETS</option>

<option value="STREETS.DARK" selected>STREETS.DARK</option>

<option value="STREETS.LIGHT">STREETS.LIGHT</option>

<option value="STREETS.PASTEL">STREETS.PASTEL</option>

</optgroup>

<option value="OUTDOOR">OUTDOOR</option>

<option value="WINTER">WINTER</option>

<option value="SATELLITE">SATELLITE</option>

<option value="HYBRID">HYBRID</option>

<optgroup label="Data visualization">

<option value="DATAVIZ">DATAVIZ</option>

<option value="DATAVIZ.DARK">DATAVIZ.DARK</option>

<option value="DATAVIZ.LIGHT">DATAVIZ.LIGHT</option>

</optgroup>

<option value="YOUR_CUSTOM_MAP_ID_1">Custom map name 1</option>

<option value="YOUR_CUSTOM_MAP_ID_2">Custom map name 2</option>

</select>

--></code></pre>

1.  Change the style when the user select one style.

<pre><code class="language-js"><!--

document.querySelector('.mapstyles-select').addEventListener('change', (e) => {

const style_code = e.target.value.split(".");

style_code.length === 2 ?

map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) :

map.setStyle(maptilersdk.MapStyle[style_code[0]] || style_code[0]);

});

--></code></pre>

1.  Create the layer selector style. Add the selector style to your stylesheet.

<pre><code class="language-css"><!--

.mapstyles-select {

position: relative;

top: 5px;

left: 5px;

z-index: 1000;

}

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document.querySelector('.mapstyles-select').addEventListener('change', (e) => {
      const style_code = e.target.value.split(".");
      style_code.length === 2 ? 
        map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) : 
        map.setStyle(maptilersdk.MapStyle[style_code[0]] || style_code[0]); 
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display a map</title>
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
            style: maptilersdk.MapStyle.STREETS.DARK,
            center: [11.5786, 48.0968],
            zoom: 10
        });

        document.querySelector('.mapstyles-select').addEventListener('change', (e) => {
              const style_code = e.target.value.split(".");
              style_code.length === 2 ? 
                map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) : 
                map.setStyle(maptilersdk.MapStyle[style_code[0]] || style_code[0]); 
            });
    </script>
</body>
</html>
```
