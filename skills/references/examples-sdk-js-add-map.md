# Source: https://docs.maptiler.com/sdk-js/examples/add-map/

# Add a map to a webpage

Create a map within an HTML element using MapTiler SDK JS. Additionally, it is possible to [insert maps into websites with a simple iframe](/guides/maps-apis/maps-platform/insert-maps-in-websites-with-a-simple-iframe) directly from MapTiler.

This is the most basic demonstration of utilizing the MapTiler SDK JS to effortlessly build a web mapping application. Feel free to explore various map styles, customizations, and functionalities to provide an exceptional mapping experience for your users. Take a look at the other [examples](/sdk-js/examples/) available to discover the full potential of the SDK.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript

```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a map to a webpage</title>
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
            zoom: 10 // starting zoom
        });


    </script>
</body>
</html>
```
