# Source: https://docs.maptiler.com/sdk-js/examples/built-in-styles/

# Display a map

Our built-in styles are designed to make it easier for you to create beautiful maps, without the need for extra coding or worrying about outdated versions. To explore the full range of available built-in styles and their variants, please refer to the [list of built-in styles](/sdk-js/api/map-styles/#mapstylelist)

This tutorial provides an overview of the built-in styles available and their implementation in map customization. To illustrate this, we have developed a selector tool that allows effortless modification of the map's style.

By utilizing the pre-existing styles available in our SDK (`maptilersdk.MapStyle`), you can benefit from numerous advantages:

- Updates to styles: With our built-in styles, any updates made to a particular style will not require you to modify your existing codebase. This ensures that you always have access to the latest version of styles without any hassle.

- Simplified usage: Our built-in styles are designed to be easily memorable, eliminating the need for manually typing style URLs. Additionally, you no longer have to include the API key in every URL, streamlining the process even further.

- Enhanced code completion: By utilizing the built-in styles, you can leverage code completion features that significantly reduce typos and other common mistakes. This ensures a smoother and more efficient mapping experience.

Each of our built-in styles is specifically tailored for a particular purpose, such as **street navigation, outdoor adventure, minimalist dashboards**, etc. Furthermore, each style offers a variety of **variants\*** that maintain the same level of information and purpose but differ in terms of color schemes. This allows you to choose the variant that best suits your needs, whether it be a **dark** or **light** color scheme, among others.

<div class="tab-common-content" markdown="1">

1. Change the map style to a hybrid satellite images.

<pre class="line-numbers" data-start="23" data-line-offset="22" data-line="23"><code class="language-js"><!--

map.setStyle(maptilersdk.MapStyle.HYBRID);

--></code></pre>

1. Create a selector to change the map style. In this example we will use some of the build-in styles. See the full <a href="/sdk-js/api/map-styles/#mapstylelist">list of styles</a>. Copy the following code into your HTML file.

<pre><code class="language-html"><!--

<select class="mapstyles-select">

<optgroup label="Navigation and city exploration">

<option value="STREETS">STREETS</option>

<option value="STREETS.DARK">STREETS.DARK</option>

<option value="STREETS.LIGHT">STREETS.LIGHT</option>

<option value="STREETS.PASTEL">STREETS.PASTEL</option>

</optgroup>

<option value="OUTDOOR">OUTDOOR</option>

<option value="WINTER">WINTER</option>

<option value="SATELLITE">SATELLITE</option>

<option value="HYBRID" selected>HYBRID</option>

<optgroup label="Data visualization">

<option value="DATAVIZ">DATAVIZ</option>

<option value="DATAVIZ.DARK">DATAVIZ.DARK</option>

<option value="DATAVIZ.LIGHT">DATAVIZ.LIGHT</option>

</optgroup>

</select>

--></code></pre>

1. Change the style when the user select one style.

<pre><code class="language-js"><!--

document.querySelector('.mapstyles-select').addEventListener('change', (e) => {

const style_code = e.target.value.split(".");

style_code.length === 2 ? map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) : map.setStyle(maptilersdk.MapStyle[style_code[0]]);

});

--></code></pre>

1. Create the layer selector style. Add the selector style to your stylesheet.

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
document.getElementById('mapstyles').addEventListener('change', (e) => {
      const style_code = e.target.value.split(".");
      style_code.length === 2 ? map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) : map.setStyle(maptilersdk.MapStyle[style_code[0]]); 
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
            style: maptilersdk.MapStyle.HYBRID,
            center: [2.33174, 48.86245],
            zoom: 15
        });

        document.getElementById('mapstyles').addEventListener('change', (e) => {
              const style_code = e.target.value.split(".");
              style_code.length === 2 ? map.setStyle(maptilersdk.MapStyle[style_code[0]][style_code[1]]) : map.setStyle(maptilersdk.MapStyle[style_code[0]]); 
            });
    </script>
</body>
</html>
```
