# Source: https://docs.maptiler.com/sdk-js/examples/interactive-false/

# Display a non-interactive map

The [MapTiler SDK JS](/sdk-js/) is a mapping library designed for creating *interactive maps*, but you can also disable the interactivity and simulate a *static map*.

To get a simple non-interactive map, it's typically much easier and more lightweight to [generate a&nbsp;static map image](/guides/maps-apis/static-maps/static-maps-for-your-web/) via our [Static maps API](/cloud/api/static-maps/). However, you may prefer to use the SDK JS in these cases:

- You already have a complex interactive map implemented and just want a simple way to switch it to non-interactive.

- You need to add special features and custom data to your map, so the [markers](/guides/maps-apis/static-maps/static-map-with-markers/) and [lines](/guides/maps-apis/static-maps/static-map-with-lines/) that a static map allows aren't sufficient.

To make your map non-interactive with MapTiler SDK JS, build your map as usual and then add the parameter `interactive: false`. See the result and code below.

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
    <title>Display a non-interactive map</title>
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
            center: [-74.5, 40],
            zoom: 9
        });


    </script>
</body>
</html>
```
