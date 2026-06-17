# Source: https://docs.maptiler.com/sdk-js/examples/geocoding-vanilla-js/

---

# 

This tutorial demonstrates how to search places usign the standalone [MapTiler Geocoding Control](/sdk-js/modules/geocoding/), and shows both the JSON response from the Geocoding API and the selected list item.

This example doesn't use a map. To use the control on a map, you can see code examples of [how to use the Geocoding control with different map libraries and Javascript frameworks](/sdk-js/modules/geocoding/examples/).

<iframe style="height: 400px; width: 100%" src="?key=&focus=true"></iframe>

## Vanilla JavaScript / HTML

### `code.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geocoding how to search places</title>
  <script
    src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/index.umd.js"></script>

  <style>
    #results {
      position: absolute;
      top: 48px;
      bottom: 0;
      left: 8px;
      right: 8px;
      overflow: auto;
      background: #E4ECFF;
      font-size: 0.85em;
      border-radius: 6px;
      box-shadow: 0px 15px 68px rgba(51, 51, 89, 0.15);
      padding: 8px;
    }

    #search-container {
      position: absolute;
      right: 48px;
    }
  </style>
</head>

<body>
  <div id="search-container">
    <maptiler-geocoder apiKey="YOUR_MAPTILER_API_KEY_HERE"></maptiler-geocoder>
  </div>

  <pre id="results"></pre>
  <script src="/sdk-js/assets/js/readParams.js"></script>
  <script type="module">
    //Change the apikey attribute of the web component to load your API key from an environment variable or similar.
    const geocodingControl = document.querySelector("maptiler-geocoder");
    geocodingControl.apiKey = key;

    geocodingControl.addEventListener("pick", (e) => {
      document.getElementById("results").innerHTML =
        e.detail ? JSON.stringify(e.detail, null, 2) : "";
    });

    geocodingControl.addEventListener("response", (e) => {
      document.getElementById("results").innerHTML =
        e.detail ? JSON.stringify(e.detail, null, 2) : "";
    });

    geocodingControl.setQuery("London");

    setTimeout(() => {
      if (urlParams.get('focus')) {
        geocodingControl.focus();
      }
    }, 500);
  </script>
</body>

</html>
```

### `code1.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geocoding how to search places</title>
  <script
    src="https://cdn.maptiler.com/maptiler-geocoding-control/v3.0.0/index.umd.js"></script>
  <style>
    #results {
      position: absolute;
      top: 48px;
      bottom: 0;
      left: 8px;
      right: 8px;
      overflow: auto;
      background: #E4ECFF;
      font-size: 0.85em;
      border-radius: 6px;
      box-shadow: 0px 15px 68px rgba(51, 51, 89, 0.15);
      padding: 8px;
    }

    #search-container {
      position: absolute;
      right: 48px;
    }
  </style>
</head>

<body>
  <div id="search-container">
    <maptiler-geocoder apiKey="YOUR_MAPTILER_API_KEY_HERE"></maptiler-geocoder>
  </div>
  <pre id="results"></pre>
  <script type="module">
    const geocodingControl = document.querySelector("maptiler-geocoder");
    //Change the apikey attribute of the web component to load your API key from an environment variable or similar.
    //const apiKey = "YOUR_MAPTILER_API_KEY_HERE";
    //geocodingControl.apiKey = apiKey;

    geocodingControl.addEventListener("response", (e) => {
      document.getElementById("results").innerHTML =
        e.detail ? JSON.stringify(e.detail, null, 2) : "";
    });

    geocodingControl.addEventListener("pick", (e) => {
      document.getElementById("results").innerHTML =
        e.detail ? JSON.stringify(e.detail, null, 2) : "";
    });
  </script>
</body>

</html>
```

## NPM / Modules / Framework Implementation

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="robots" content="noindex">
  <title>Geocoding how to search places</title>
  <link rel="stylesheet" href="./style.css">
</head>
<body>
  <div id="search-container">
    <maptiler-geocoder apiKey="YOUR_MAPTILER_API_KEY_HERE"></maptiler-geocoder>
  </div>
  <pre id="results"></pre>
  <script type="module" src="./main.js"></script>
</body>
</html>
```

### `main.js`
```javascript
---
layout: none
---
import '@maptiler/geocoding-control/';

const geocodingControl = document.querySelector("maptiler-geocoder");
//Change the apikey attribute of the web component to load your API key from an environment variable or similar.
//const apiKey = "YOUR_MAPTILER_API_KEY_HERE";
//geocodingControl.apiKey = apiKey;

geocodingControl.addEventListener("response", (e) => {
  document.getElementById("results").innerHTML =
    e.detail ? JSON.stringify(e.detail, null, 2) : "";
});

geocodingControl.addEventListener("pick", (e) => {
  document.getElementById("results").innerHTML =
    e.detail ? JSON.stringify(e.detail, null, 2) : "";
});
```

### `package.json`
```json
{
  "name": "maptiler-geocoding-vanilla-js",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@maptiler/geocoding-control": "^latest"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```

### `style.css`
```css
#results {
  position: absolute;
  top: 48px;
  bottom: 0;
  left: 8px;
  right: 8px;
  overflow: auto;
  background: #E4ECFF;
  font-size: 0.85em;
  border-radius: 6px;
  box-shadow: 0px 15px 68px rgba(51, 51, 89, 0.15);
  padding: 8px;
}

#search-container {
  position: absolute;
  right: 48px;
}
```

