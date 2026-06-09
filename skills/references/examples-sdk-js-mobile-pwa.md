# Source: https://docs.maptiler.com/sdk-js/examples/mobile-pwa/

# Display a map

This example shows how to use MapTiler SDK to create a native mobile app that can be pushed to the Apple App Store and Google Play.

<div class="mobile-viewer">

<div class="mobile-case"></div>

</div>

With this project as a starter (or any Capacitor app) and with a single codebase, you can create:

* A web app hosted online, which people visit with a regular web browser.

* A PWA that people can turn into a semi-app (under certain conditions: Android, EU-iPhone, etc.).

* A Capacitor-powered native web app wrapped to be distributed on Apple AppStore and Google Play.

> [!NOTE]

> PWAs or [Progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) are web apps hosted online, like any website, but they are shipped with a few extra settings in a manifest file. We are not going to cover this here, but it's worth mentioning that your web app does **not** need to comply to the PWA set of rules to be wrapped inside a native mobile app with Capacitor. Those are two very different things, both with their pros and cons.

>

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
            center: [0, 0],
            zoom: 0
        });


    </script>
</body>
</html>
```
