# Source: https://docs.maptiler.com/sdk-js/examples/how-to-use/

# Display a map

Learn how to generate and showcase an interactive map on a web page using MapTiler with this comprehensive tutorial. The step-by-step guide will walk you through the entire process.

By following these steps, you will be able to harness the power of MapTiler SDK JS to effortlessly develop web mapping applications. Experiment with different map styles, customizations, and functionalities to create an exceptional mapping experience for your web application users.

<Tabs groupId="methods">

<TabItem value="npm" default>

1. Install the npm package.

<pre><code class="language-bash"><!--

npm install --save @maptiler/sdk

--></code></pre>

1.  Create the map style. Add the map style to your stylesheet. The div must have non-zero height.

<pre><code class="language-css">

body {

margin: 0;

padding: 0;

}

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

</code></pre>

1.  Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre><code class="language-html"><!--

<div id="map"></div>

--></code></pre>

1.  Include the CSS file.

If you have a bundler that can handle CSS, you can import the CSS from @maptiler/sdk/dist/maptiler-sdk.css.

<pre><code class="language-js"><!--

import '@maptiler/sdk/dist/maptiler-sdk.css';

--></code></pre>

> [!INFO]

> Including the CSS file using a `<link>` in the head of the document via the CDN is the easiest way.

>

> ``` html

> <link href='https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css' rel='stylesheet' />

> ```

>

1.  Finally, load the map with the style. Include the following code in your JavaScript.

<pre><code class="language-js">

import { Map, MapStyle, config } from '@maptiler/sdk';

config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new Map({

container: 'map', // container's id or the HTML element in which SDK will render the map

style: MapStyle.STREETS,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

</code></pre>

1.

</TabItem>

<TabItem value="cdn">

1. Create a basic HTML file.

<pre class="line-numbers"><code class="language-html"><!--

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title></title>

<style>

body {

margin: 0;

padding: 0;

}

</style>

</head>

<body>

</body>

<script>

</script>

</html>

--></code></pre>

1.  Include the MapTiler SDK JS JavaScript and CSS files in the `<head>` of your HTML file.

<pre class="line-numbers" data-start="6" data-line-offset="5" data-line="7,8"><code class="language-html"><!--

<title></title>

<script src="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.umd.min.js"></script>

<link href="https://cdn.maptiler.com/maptiler-sdk-js//maptiler-sdk.css" rel="stylesheet" />

<style>

--></code></pre>

1.  Create a `<div>` element with a certain id where you want your map to be.

Add `<div>` tag into your page. This div will be the container where the map will be loaded.

<pre class="line-numbers" data-start="14" data-line-offset="13" data-line="15"><code class="language-html"><!--

<body>

<div id="map"></div>

</body>

--></code></pre>

1.  Create the map style. Add the map style to your stylesheet. The div must have non-zero height.

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="12-17"><code class="language-css">

position: absolute;

top: 0;

bottom: 0;

width: 100%;

}

</code></pre>

1.  Finally, load the map with the style. Include the following code in your JavaScript.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="25-33"><code class="language-js">

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element in which the SDK will render the map

style: maptilersdk.MapStyle.STREETS,

center: [, ], // starting position [lng, lat]

zoom:  // starting zoom

});

</code></pre>

1.

</TabItem>

</Tabs>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

const map = new maptilersdk.Map({
    container: 'map',
    style: maptilersdk.MapStyle.STREETS,
    center: [16.62662018, 49.2125578], // starting position [lng, lat]
    zoom: 14 // starting zoom
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
            style: maptilersdk.MapStyle.STREETS,
            center: [16.62662018, 49.2125578],
            zoom: 14 // starting zoom
        });
    </script>
</body>
</html>
```
```
