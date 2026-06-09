# Source: https://docs.maptiler.com/sdk-js/examples/scroll-fly-to/

# Fly to a location based on scroll position

Create a story map. As you scroll down the page, the map will automatically move to the specific location of each chapter in the story.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const chapters = {
      'baker': {
        bearing: 27,
        center: [-0.15591514, 51.51830379],
        zoom: 15.5,
        pitch: 20
      },
      'aldgate': {
        duration: 6000,
        center: [-0.07571203, 51.51424049],
        bearing: 150,
        zoom: 15,
        pitch: 0
      },
      'london-bridge': {
        bearing: 90,
        center: [-0.08533793, 51.50438536],
        zoom: 13,
        speed: 0.6,
        pitch: 40
      },
      'woolwich': {
        bearing: 90,
        center: [0.05991101, 51.48752939],
        zoom: 12.3
      },
      'gloucester': {
        bearing: 45,
        center: [-0.18335806, 51.49439521],
        zoom: 15.3,
        pitch: 20,
        speed: 0.5
      },
      'caulfield-gardens': {
        bearing: 180,
        center: [-0.19684993, 51.5033856],
        zoom: 12.3
      },
      'telegraph': {
        bearing: 90,
        center: [-0.10669358, 51.51433123],
        zoom: 17.3,
        pitch: 40
      },
      'charing-cross': {
        bearing: 90,
        center: [-0.12416858, 51.50779757],
        zoom: 14.3,
        pitch: 20
      }
    };

    // On every scroll event, check which element is on screen
    window.onscroll = function () {
      const chapterNames = Object.keys(chapters);
      for (let i = 0; i < chapterNames.length; i++) {
        const chapterName = chapterNames[i];
        if (isElementOnScreen(chapterName)) {
          setActiveChapter(chapterName);
          break;
        }
      }
    };

    let activeChapterName = 'baker';
    function setActiveChapter(chapterName) {
      if (chapterName === activeChapterName) return;

      map.flyTo(chapters[chapterName]);

      document.getElementById(chapterName).setAttribute('class', 'active');
      document.getElementById(activeChapterName).setAttribute('class', '');

      activeChapterName = chapterName;
    }

    function isElementOnScreen(id) {
      const element = document.getElementById(id);
      const bounds = element.getBoundingClientRect();
      return bounds.top < window.innerHeight && bounds.bottom > 0;
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fly to a location based on scroll position</title>
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
            center: [-0.15591514, 51.51830379],
            zoom: 15.5,
            pitch: 45,
            bearing: 27
        });

        const chapters = {
              'baker': {
                bearing: 27,
                center: [-0.15591514, 51.51830379],
                zoom: 15.5,
                pitch: 20
              },
              'aldgate': {
                duration: 6000,
                center: [-0.07571203, 51.51424049],
                bearing: 150,
                zoom: 15,
                pitch: 0
              },
              'london-bridge': {
                bearing: 90,
                center: [-0.08533793, 51.50438536],
                zoom: 13,
                speed: 0.6,
                pitch: 40
              },
              'woolwich': {
                bearing: 90,
                center: [0.05991101, 51.48752939],
                zoom: 12.3
              },
              'gloucester': {
                bearing: 45,
                center: [-0.18335806, 51.49439521],
                zoom: 15.3,
                pitch: 20,
                speed: 0.5
              },
              'caulfield-gardens': {
                bearing: 180,
                center: [-0.19684993, 51.5033856],
                zoom: 12.3
              },
              'telegraph': {
                bearing: 90,
                center: [-0.10669358, 51.51433123],
                zoom: 17.3,
                pitch: 40
              },
              'charing-cross': {
                bearing: 90,
                center: [-0.12416858, 51.50779757],
                zoom: 14.3,
                pitch: 20
              }
            };

            // On every scroll event, check which element is on screen
            window.onscroll = function () {
              const chapterNames = Object.keys(chapters);
              for (let i = 0; i < chapterNames.length; i++) {
                const chapterName = chapterNames[i];
                if (isElementOnScreen(chapterName)) {
                  setActiveChapter(chapterName);
                  break;
                }
              }
            };

            let activeChapterName = 'baker';
            function setActiveChapter(chapterName) {
              if (chapterName === activeChapterName) return;

              map.flyTo(chapters[chapterName]);

              document.getElementById(chapterName).setAttribute('class', 'active');
              document.getElementById(activeChapterName).setAttribute('class', '');

              activeChapterName = chapterName;
            }

            function isElementOnScreen(id) {
              const element = document.getElementById(id);
              const bounds = element.getBoundingClientRect();
              return bounds.top < window.innerHeight && bounds.bottom > 0;
            }
    </script>
</body>
</html>
```
