# Source: https://docs.maptiler.com/sdk-js/examples/language-switch/

# Change a map's language

You can utilize the [`setLanguage`](/sdk-js/api/map/#map#setLanguage) function to dynamically switch between languages. This function allows you to modify the language setting for the labels that appear on maps. By following these guidelines, users can customize the language of map labels based on their personal preferences.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
document
      .getElementById('buttons')
      .addEventListener('click', function (event) {
        const language = event.target.id;
        map.setLanguage(maptilersdk.Language[language]);
      });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Change a map's language</title>
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
            center: [16.05, 48],
            zoom: 2.9
        });

        document
              .getElementById('buttons')
              .addEventListener('click', function (event) {
                const language = event.target.id;
                map.setLanguage(maptilersdk.Language[language]);
              });
    </script>
</body>
</html>
```
