# Source: https://docs.maptiler.com/react/sdk-js/how-to-use-sdk-js/

# 

In this step-by-step tutorial, you’ll learn how to create a React JS component that leverages the power of MapTiler SDK JS mapping library to render maps. Together we will build a simple full-screen map application, serving as a practical example of how to seamlessly integrate MapTiler maps into your own React app.

By the end of this tutorial, you will be able to create a full-screen map with a marker placed at a specified location. With your newfound knowledge, you will be able to create visually stunning maps within your React projects. Take a sneak peek at the final output of this tutorial below:

{: width="3200" height="1800" data-aspect-ratio="1.78" }

## Getting started

*Minimal requirements for completing this tutorial.*

* **Basic React JS knowledge.** You don’t need a lot of experience using [React](https://reactjs.org/){:target="_blank" rel="noopener"} for this tutorial, but you should be familiar with basic concepts and workflow.

* **MapTiler API key.** Your MapTiler account access key is on your MapTiler [Cloud](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"} account page or [Get API key for FREE](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"}.

* **MapTiler SDK JS.** JavaScript library for building web maps. In this tutorial, you will learn how to install it.

* **Node.js and npm.** Necessary to run your React app locally. [Node.js](https://nodejs.org/en/){:target="_blank" rel="noopener"}

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

To start your local environment, run `npm run dev`. You will find your app running on the address `http://localhost:5173/`.

Now you should see the app in your browser.



### Installation and setting up

To install MapTiler SDK JS library, navigate to your project folder and run the command:

``` bash
npm i @maptiler/sdk
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

### Create a navbar component

In this step, we will create a simple heading navbar component.

Create a new folder called `components` inside the `src` folder.

Create a new file called `navbar.jsx` inside the `components` folder and write these lines:

``` jsx
import React from 'react';
import './navbar.css';

export default function Navbar(){
  return (
    <div className="heading">
    <h1>This is my map App</h1>
    </div>
  );
}
```

Create a new file called `navbar.css` inside the `components` folder and write these lines:

``` css
.heading {
  margin: 0;
  padding: 0px;
  background-color: black;
  color: white;
  text-align: center;
}

.heading > h1 {
  padding: 20px;
  margin: 0;
}
```

Finally, to display the `Navbar` we need to import the Navbar component and add it to our main component `App.jsx`.

Import the navbar component into `App.jsx` write the following line at the beginning of the file

``` jsx
import Navbar from './components/navbar.jsx';
```

Replace the text *This is my map App* with `<Navbar />`. Your `App.jsx` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1, 7"><code class="language-jsx"><!--
import Navbar from './components/navbar.jsx';
import './App.css';

function App() {
  return (
    <div className="App">
    <Navbar/>
    </div>
  );
}

export default App;
--></code></pre>

Now you should see the black navbar at the top of your browser.



### Create a map component

In this step, we will create a simple map component.

Create a new file called `map.jsx` inside the `components` folder.

First, we’ll import MapTiler SDK JS and the required React functions. Add these lines on top of `map.jsx` file.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1-4"><code class="language-jsx"><!--
import React, { useRef, useEffect } from 'react'; 
import * as maptilersdk from '@maptiler/sdk';
import "@maptiler/sdk/dist/maptiler-sdk.css";
import './map.css';
--></code></pre>

Now we will create a function as our map component.

<pre class="line-numbers" data-start="6" data-line-offset="5" data-line="6-7"><code class="language-jsx"><!--
export default function Map() {
}
--></code></pre>

And set up your map's default state.

<pre class="line-numbers" data-start="6" data-line-offset="5" data-line="7-11"><code class="language-jsx"><!--
export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const tokyo = { lng: 139.753, lat: 35.6844 };
  const zoom = 14;
  maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
}
--></code></pre>

The state stores the map object, its container. Longitude, latitude, and zoom for the map will all change as your user interacts with the map.



In the next step, we will initialize the map in the `Map()` function.

<pre class="line-numbers" data-start="13" data-line-offset="12" data-line="13-23"><code class="language-jsx"><!--
useEffect(() => {
  if (map.current) return; // stops map from intializing more than once
  
  map.current = new maptilersdk.Map({
    container: mapContainer.current,
    style: maptilersdk.MapStyle.STREETS,
    center: [tokyo.lng, tokyo.lat],
    zoom: zoom
  });
  
}, [tokyo.lng, tokyo.lat, zoom]);
--></code></pre>

This code will be right after the component is inserted into the DOM tree. We initialize the map using React effect hook and we also set up some basic options of the map:

1. The `container` option sets the DOM element in which will the map be rendered. We will assign the `ref` our component expects to an HTML element, which will act as a container, later in this tutorial.

1. The `style` option defines what style is the map going to use.

1. The `center` and `zoom` options set the starting position of the map.

Now, we will add the `return` statement to your `Map()` function. Add the following code to your component above the closing curly brace of `Map()`:

<pre class="line-numbers" data-start="25" data-line-offset="24" data-line="25-29"><code class="language-jsx"><!--
return (
  <div className="map-wrap">
    <div ref={mapContainer} className="map" />
  </div>
);
--></code></pre>

The `ref={mapContainer}` specifies that App should be drawn to the HTML page in the `<div>` element.

We are finished with our basic map component, your `map.jsx` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-jsx"><!--
import React, { useRef, useEffect } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import "@maptiler/sdk/dist/maptiler-sdk.css";
import './map.css';

export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const tokyo = { lng: 139.753, lat: 35.6844 };
  const zoom = 14;
  maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

  useEffect(() => {
    if (map.current) return; // stops map from intializing more than once

    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: maptilersdk.MapStyle.STREETS,
      center: [tokyo.lng, tokyo.lat],
      zoom: zoom
    });
    
  }, [tokyo.lng, tokyo.lat, zoom]);
  
  return (
    <div className="map-wrap">
      <div ref={mapContainer} className="map" />
    </div>
  );
}
--></code></pre>

Now we will need simple styling to render the map correctly. Create a file named `map.css` in `components` folder for the map component style and write the following code to your `map.css` file:

``` css
.map-wrap {
  position: relative;
  width: 100%;
  height: calc(100vh - 77px); /* calculate height of the screen minus the heading */
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

And then, add the imported `<Map/>` component in your `App()` function. Your `App.jsx` file should then look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2, 10"><code class="language-jsx"><!--
import React from 'react';
import Map from './components/map.jsx';
import Navbar from './components/navbar.jsx';
import './App.css';

function App() {
  return(
    <div className="App">
      <Navbar/>
      <Map/>
    </div>
  )
}

export default App;
--></code></pre>

With everything done up until now, you should be able see your beautiful map in your browser.



### Map marker

Another basic thing to add to your map could be a [marker](/sdk-js/api/markers/#marker){:target="_blank" rel="noopener"} of some location.

In the next line where we declare the navigation control we add these lines:

<pre class="line-numbers" data-start="23" data-line-offset="22" data-line="23-25"><code class="language-jsx"><!--
new maptilersdk.Marker({color: "#FF0000"})
  .setLngLat([139.7525,35.6846])
  .addTo(map.current);
--></code></pre>

We create a new marker using the `.marker` function. We added the color option to make it red, then set Lng/Lat of the marker using `.setLngLat()` function , and finally added it to the current map using `.addTo()` function.

We are finished with our basic map objects, your `map.js` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="23-25"><code class="language-jsx"><!--
import React, { useRef, useEffect } from 'react';
import * as maptilersdk from '@maptiler/sdk';
import "@maptiler/sdk/dist/maptiler-sdk.css";
import './map.css';

export default function Map() {
  const mapContainer = useRef(null);
  const map = useRef(null);
  const tokyo = { lng: 139.753, lat: 35.6844 };
  const zoom = 14;
  maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
 
  useEffect(() => {
    if (map.current) return; // stops map from intializing more than once
  
    map.current = new maptilersdk.Map({
      container: mapContainer.current,
      style: maptilersdk.MapStyle.STREETS,
      center: [tokyo.lng, tokyo.lat],
      zoom: zoom
    });
  
    new maptilersdk.Marker({color: "#FF0000"})
      .setLngLat([139.7525,35.6846])
      .addTo(map.current);
  }, [tokyo.lng, tokyo.lat, zoom]);

  return (
    <div className="map-wrap">
      <div ref={mapContainer} className="map" />
    </div>
  );
}
--></code></pre>



## What's next

To enhance your map app, check out our **series on maps in React**. In the episodes, you'll learn how to add popups, a visualization switcher, geocoding control, 3D terrain, and a sidebar:

1. [Build a map app with Material UI](/react/sdk-js/get-started-material-ui/)
2. [Add points from GeoJSON](/react/sdk-js/geojson-points/)
3. [Create a heatmap](/react/sdk-js/heatmap/)
4. [Add popups and sidebar](/react/sdk-js/popup-sidebar/)
5. [Add place search (geocoding control) to a map](/react/sdk-js/geocoding-control/)
6. [Create a 3D terrain map with place search](/react/sdk-js/geocoding-control/)

Also, you can check [more than 200 SDK JS examples](/sdk-js/examples/) to see the limitless possibilities of MapTiler SDK JS and unlock the full potential of your React applications. It offers easy terrain, built-in styles, language switching, geocoding, TypeScript power, optional IP geolocation, etc.

## Useful links

- [MapTiler SDK JS API](https://docs.maptiler.com/sdk-js/){:target="_blank" rel="noopener"}
- [NPM - MapTiler SDK JS](https://www.npmjs.com/package/@maptiler/sdk){:target="_blank" rel="noopener"}
- [Vite - Getting Started](https://vitejs.dev/guide/){:target="_blank" rel="noopener"}
- [MapTiler - ](https://www.maptiler.com/cloud/customize/){:target="_blank" rel="noopener"}
