# Source: https://docs.maptiler.com/react/maplibre-gl-js/get-started/

# 

In this tutorial, you’ll learn how to display a map in React JS using MapLibre GL JS. Together we will make a simple full-screen map application as an example of how to use MapTiler maps together with React and MapLibre GL JS for your own React app.

## Installation and setting up

1. Clone the [Get Started with React JS and MapLibre GL JS](https://github.com/maptiler/get-started-react-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

```sh
  git clone https://github.com/maptiler/get-started-react-maplibre-gl-js.git my-react-map
```

1. Navigate to the newly created project folder **my-react-map**

```sh
  cd my-react-map
```

1. Install dependencies

```sh
  npm install
```

1. Now navigate to the `src` folder and open the `App.js` file. 
   
   <pre class="line-numbers" data-start="10" data-line-offset="9" data-line="17"><code class="language-html"><!--
     <Map mapLib={maplibregl}
       initialViewState=
       style=
       mapStyle="https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_MAPTILER_API_KEY_HERE"
     >
   --></code></pre>

   

1. Start your local environment

```sh
  npm start
```

1. You will find your app on the address `http://localhost:3000`. Now you should see the map in your browser.

## Learn more

If you want to learn how to create a React component to render a map using MapLibre GL JS see the [How to display a map in React using MapLibre GL JS](/react/maplibre-gl-js/how-to-use-maplibre-gl-js/) tutorial.

### React JS with MapTiler maps

If you're looking to develop React applications with MapTiler SDK JS, check out our tutorial titled [React JS with MapTiler maps](/react/). This step-by-step tutorial will provide you with the necessary guidance and examples to create a React JS component that leverages the power of MapTiler SDK JS mapping library to render maps.

### Get Started With MapLibre GL JS for React Native

You can also develop your applications using React Native. Check out the tutorial [Get started with React Native and MapLibre GL JS](/react-native/)
