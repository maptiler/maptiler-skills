# Source: https://docs.maptiler.com/sdk-js/examples/display-and-style-rich-text-labels/

# Display and style rich text labels

Use the [`format` expression](/gl-style-specification/expressions/#types-format) to display country labels in both English and in the local language.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
map.on('load', function () {
        map.setLayoutProperty('Country labels', 'text-field', [
            'format',
            ['get', 'name_en'],
            { 'font-scale': 1.2 },
            '\n',
            {},
            ['get', 'name_de'],
            {
                'font-scale': 0.8,
                'text-font': [
                    'literal',
                    ['DIN Offc Pro Italic', 'Arial Unicode MS Regular']
                ]
            }
        ]);
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display and style rich text labels</title>
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
            style: maptilersdk.MapStyle.BASE,
            center: [9.49, 49.01],
            zoom: 4 // starting zoom
        });

        map.on('load', function () {
                map.setLayoutProperty('Country labels', 'text-field', [
                    'format',
                    ['get', 'name_en'],
                    { 'font-scale': 1.2 },
                    '\n',
                    {},
                    ['get', 'name_de'],
                    {
                        'font-scale': 0.8,
                        'text-font': [
                            'literal',
                            ['DIN Offc Pro Italic', 'Arial Unicode MS Regular']
                        ]
                    }
                ]);
            });
    </script>
</body>
</html>
```
