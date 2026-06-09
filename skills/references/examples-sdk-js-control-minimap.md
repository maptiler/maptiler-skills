# Source: https://docs.maptiler.com/sdk-js/examples/control-minimap/

# Display a minimap control to aid the map navigation

This tutorial shows how to display a minimap or overview map control in MapTiler SDK JS to aid map navigation.

By following this guide, users will learn how to integrate and display a minimap within their map interface using MapTiler SDK JS. The minimap provides users with a compact overview of the entire map, allowing them to easily navigate and explore different areas. With the help of MapTiler SDK JS, developers can effortlessly incorporate a minimap control into their web-based mapping applications, making it easier for users to interact with and navigate through their maps.

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
    <title>Display a minimap control to aid the map navigation</title>
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
            zoom: 10
        });


    </script>
</body>
</html>
```
