# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-language/

# MapTiler Geocoding control language

Indicate the language(s) utilized for the response text and the prioritization of query results in geocoding control. Include the `language` options within the control constructor. For a complete list of geocoding control options, please refer to the [Geocoding control's reference documentation](/sdk-js/modules/geocoding/api/api-reference/#options). In the given example, we initialize the control to incorporate French and English languages.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
//set geocoding control language. Example Canada, Quebec province that is primarily Francophone
    const gc = new maptilerGeocoder.GeocodingControl({
      language: ['fr', 'en']
    });
    map.addControl(gc, 'top-right');
    document.getElementById('buttons').addEventListener('click', function (event) {
      // Retrieve language based on button id
      gc.setOptions({
        language: event.target.id,
        placeholder: setPlaceHolder(event.target.id)
      });
    });
    function setPlaceHolder(language) {
      switch (language) {
        case 'en':
          return 'Search';
          break;
        case 'fr':
          return 'Recherche';
          break;
        case 'de':
          return 'Suchen';
          break;
        case 'ja':
          return '検索';
          break;
        case 'es':
          return 'Buscar';
          break;
        default:
          return 'Search';
          break;
      }
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MapTiler Geocoding control language</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/maptilersdk.umd.js"></script>
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
            center: [-72.745, 46.081],
            zoom: 6
        });

        //set geocoding control language. Example Canada, Quebec province that is primarily Francophone
            const gc = new maptilerGeocoder.GeocodingControl({
              language: ['fr', 'en']
            });
            map.addControl(gc, 'top-right');
            document.getElementById('buttons').addEventListener('click', function (event) {
              // Retrieve language based on button id
              gc.setOptions({
                language: event.target.id,
                placeholder: setPlaceHolder(event.target.id)
              });
            });
            function setPlaceHolder(language) {
              switch (language) {
                case 'en':
                  return 'Search';
                  break;
                case 'fr':
                  return 'Recherche';
                  break;
                case 'de':
                  return 'Suchen';
                  break;
                case 'ja':
                  return '検索';
                  break;
                case 'es':
                  return 'Buscar';
                  break;
                default:
                  return 'Search';
                  break;
              }
            }
    </script>
</body>
</html>
```
