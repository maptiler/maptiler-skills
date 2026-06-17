# Source: https://docs.maptiler.com/leaflet/examples/react/

# 

In this tutorial, you’ll learn how to use Leaflet with React and MapTiler Vector Tiles: this tutorial shows how to install Leaflet from NPM and create a map and display it on a React application.

By the end of this tutorial, you will be able to create a full-screen map.

<iframe style="height: 400px; width: 100%" src="?key=&position=12/52.507932/13.338414"></iframe>

## Getting started

*Minimal requirements for completing this tutorial.*

* **Basic React JS knowledge.** You don’t need a lot of experience using [React](https://reactjs.org/){:target="_blank" rel="noopener"} for this tutorial, but you should be familiar with basic concepts and workflow.

* **MapTiler API key.** Your MapTiler account access key is on your MapTiler [Cloud](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"} account page or [Get API key for FREE](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"}.

* **Leaflet.** JavaScript library for building web maps. In this tutorial, you will learn how to install it.

* **Maptiler SDK layer.** The [L.maptiler.maptilerLayer()](https://github.com/maptiler/leaflet-maptilersdk) plugin is how you display vector tiles in Leaflet JS..

* **Node.js and npm.** Necessary to run your Next.js app locally. [Node.js](https://nodejs.org/en/){:target="_blank" rel="noopener"}

## Create an app

In this step, we are going to learn how to create a React app.

To create a new react project run in your command-line:

``` bash
npm create vite my-react-map -- --template react
```

`create vite` will create a simple one-page application in React. For more information follow [Scaffolding Your First Vite Project](https://vitejs.dev/guide/#scaffolding-your-first-vite-project){:target="_blank" rel="noopener"}.

Navigate to the newly created project folder `my-react-map`

``` bash
cd my-react-map
```

Inside the newly created project, run `npm install` to install the dependencies.

To start your local environment, run `npm run dev`. You will find your app running on address `http://localhost:5173/`.

Now you should see the app in your browser.



### Installation and setting up

To install Leaflet and Maptiler SDK layer, navigate to your project folder and run the command:

``` bash
npm i leaflet @maptiler/leaflet-maptilersdk
```

Navigate to the `src` folder and delete all the contents of the `index.css` file.

Navigate to the `src` folder and replace all the contents of the `App.css` file with the following lines:

``` css
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
  'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
  sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
  monospace;
}
```

Replace all the contents of the `App.jsx` file with the following lines:

``` jsx
import './App.css';

function App() {
  return (
    <div className="App">
    This is my map App
    </div>
  );
}

export default App;
```

Now you should see “This is my map App“ in your browser.

### Create a map component

In this step, we will create a simple map component.

Create a new folder called `components` inside the `src` folder.

Create a new file called `map.jsx` inside the `components` folder.

First, we’ll import Leaflet, MapTiler SDK JS and the required React functions. Add these lines on top of `map.jsx` file.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1-10"><code class="language-jsx"><!--
import React, { useRef, useEffect, useState } from 'react';
import "leaflet/dist/leaflet.css";

import L from "leaflet";

import './map.css';

import { MaptilerLayer } from "@maptiler/leaflet-maptilersdk";
--></code></pre>

Now we will create a function as our map component.

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="12-16"><code class="language-jsx"><!--
const Map = () => {

}

export default Map;
--></code></pre>

And set up your map's default state.

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="13-16"><code class="language-jsx"><!--
const Map = () => {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const center = { lng: 13.338414, lat: 52.507932 };
  const [zoom] = useState(12);
}
--></code></pre>

The state stores the map object, its container, longitude, latitude, and zoom for the map.

In the next step, we will initialize the map in the `Map()` function.

<pre class="line-numbers" data-start="18" data-line-offset="17" data-line="18-32"><code class="language-jsx"><!--
useEffect(() => {
  if (map.current) return; // stops map from intializing more than once

  map.current = new L.Map(mapContainer.current, {
    center: L.latLng(center.lat, center.lng),
    zoom: zoom
  });

  // Create a MapTiler Layer inside Leaflet
  const mtLayer = new MaptilerLayer({
    // Get your free API key at https://cloud.maptiler.com
    apiKey: "YOUR_MAPTILER_API_KEY_HERE",
  }).addTo(map.current);

}, [center.lng, center.lat, zoom]);
--></code></pre>



This code will be right after the component is inserted into the DOM tree. We initialize the map using React effect hook and we also set up some basic options of the map:

1. The `mapContainer` option sets the DOM element in which will the map be rendered. We will assign the `ref` our component expects to an HTML element, which will act as a container, later in this tutorial.

1. The `center` and `zoom` options set the starting position of the map.

Now, we will add the `return` statement to your `Map()` function. Add the following code to your component above the closing curly brace of `Map()`:

<pre class="line-numbers" data-start="34" data-line-offset="33" data-line="34-38"><code class="language-jsx"><!--
return (
  <div className="map-wrap">
    <div ref={mapContainer} className="map" />
  </div>
);
--></code></pre>

The `ref={mapContainer}` specifies that App should be drawn to the HTML page in the `<div>` element.

We are finished with our basic map component, your `map.jsx` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-jsx"><!--
import React, { useRef, useEffect, useState } from 'react';
import "leaflet/dist/leaflet.css";

import L from "leaflet";

import './map.css';

import { MaptilerLayer } from "@maptiler/leaflet-maptilersdk";

const Map = () => {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const center = { lng: 13.338414, lat: 52.507932 };
  const [zoom] = useState(12);

  useEffect(() => {
    if (map.current) return; // stops map from intializing more than once
  
    map.current = new L.Map(mapContainer.current, {
      center: L.latLng(center.lat, center.lng),
      zoom: zoom
    });
  
    // Create a MapTiler Layer inside Leaflet
    const mtLayer = new MaptilerLayer({
      // Get your free API key at https://cloud.maptiler.com
      apiKey: "YOUR_MAPTILER_API_KEY_HERE",
    }).addTo(map.current);
  
  }, [center.lng, center.lat, zoom]);

  return (
    <div className="map-wrap">
      <div ref={mapContainer} className="map"/>
    </div>
  )
}

export default Map;
--></code></pre>

Now we will need simple styling to render the map correctly. Create a file named `map.css` in `components` folder for the map component style and write the following code to your `map.css` file:

``` css
.map-wrap {
  position: relative;
  width: 100%;
  height: 100vh;
}

.map {
  position: absolute;
  width: 100%;
  height: 100%;
}
```

We use `position: absolute` on the map itself and `position: relative` on the wrap around the map for more possibilities in future styling.

### Render a map

Now we will import the map component into your app, add the following line to the top of the `App.jsx`.

``` jsx
import Map from './components/map.jsx';
```

And then, replace the text *This is my map App* with `<Map />` component in your `App()` function. Your `App.jsx` file should then look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1,8"><code class="language-jsx"><!--
import Map from './components/map.jsx';

import './App.css';

function App() {
  return (
    <div className="App">
      <Map />
    </div>
  );
}

export default App;
--></code></pre>

With everything done up until now, you should be able see your beautiful map in your browser.



