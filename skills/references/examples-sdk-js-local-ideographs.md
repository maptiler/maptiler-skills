# Source: https://docs.maptiler.com/sdk-js/examples/local-ideographs/

# Use locally generated ideographs

Rendering Chinese/Japanese/Korean (CJK) ideographs and precomposed Hangul Syllables requires downloading large amounts of font data, which can significantly slow map load times. Use the `localIdeographFontFamily` setting to speed up map load times by using locally available fonts instead of font data fetched from the server. This setting defines a CSS 'font-family' for locally overriding generation of glyphs in the 'CJK Unified Ideographs' and 'Hangul Syllables' Unicode ranges. In these ranges, font settings from the map's style will be ignored in favor of the locally available font. Keywords in the fontstack defined in the map's style (light/regular/medium/bold) will be translated into a CSS 'font-weight'.

This setting is enabled by default to use the system 'sans-serif' font. When overriding this setting, the fonts you select may not be available on all users' devices. Specify at least one broadly available fallback font class such as 'sans-serif'.

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
    <title>Use locally generated ideographs</title>
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
            center: [120.3049, 31.4751],
            zoom: 12
        });


    </script>
</body>
</html>
```
