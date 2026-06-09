# Source: https://docs.maptiler.com/sdk-js/examples/language-map/

# Change the map labels language

This tutorial shows how to change the default map labels language.

It explains the steps to change the language setting for the labels displayed on maps. By following these instructions, users can customize the language of map labels according to their preferences. This tutorial aims to assist users in personalizing their map experience by adjusting the language used for map labels.

<div class="tab-common-content" markdown="1">

1. Change the map language to Japanese. By default, if nothing is specified, the SDK uses the language defined in the browser. This corresponds to `maptilersdk.Language.AUTO`. If we want to change the default language of the map we must indicate the language in the sdk `config`.

<pre class="line-numbers" data-start="17" data-line-offset="16" data-line="18"><code class="language-js"><!--

maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

maptilersdk.config.primaryLanguage = maptilersdk.Language.JAPANESE;

const map = new maptilersdk.Map({

container: 'map', // container's id or the HTML element in which MapLibre GL JS will render the map

style: maptilersdk.MapStyle.STREETS,

center: [, ], // starting position [lng, lat]

zoom: , // starting zoom

});

--></code></pre>

1. Reload the page. Now you should see the map with the Japanese labels.

1. Add event handler for map load event. You will add code to change the map language in this handler.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="25-27"><code class="language-js"><!--

map.on('load', async function() {

});

--></code></pre>

1. Change the map language to French. The language generally depends on the style but we made it possible to easily update it with a single function and from a built-in list of languages.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="26"><code class="language-js"><!--

map.on('load', async function() {

map.setLanguage(maptilersdk.Language.FRENCH);

});

--></code></pre>

1. Reload the page. Now you should see the map with the Frech labels.

1. Change the map language to Arabic. Languages that are written right-to-left such as arabic and hebrew are fully supported by default. No need to install any plugin!.

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="26"><code class="language-js"><!--

map.on('load', async function() {

map.setLanguage(maptilersdk.Language.ARABIC);

});

--></code></pre>

1. Reload the page. Now you should see the map with the Arabic labels.

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
maptilersdk.config.primaryLanguage = maptilersdk.Language.JAPANESE;
      container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [11.78, 43.35], // starting position [lng, lat]
      zoom: 3.51, // starting zoom
    });
    map.on('load', async function() {
      map.setLanguage(maptilersdk.Language.ARABIC);   
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change the map labels language</title>
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
            center: [11.78, 43.35],
            zoom: 3.51
        });

        maptilersdk.config.primaryLanguage = maptilersdk.Language.JAPANESE;
              container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [11.78, 43.35], // starting position [lng, lat]
              zoom: 3.51, // starting zoom
            });
            map.on('load', async function() {
              map.setLanguage(maptilersdk.Language.ARABIC);   
            });
    </script>
</body>
</html>
```
