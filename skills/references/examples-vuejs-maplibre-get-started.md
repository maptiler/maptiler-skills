# Source: https://docs.maptiler.com/vuejs/maplibre-gl-js/get-started/

# 

In this tutorial, you’ll learn how to display a map in Vue.js using MapLibre GL JS. Together we will make a simple full-screen map application as an example of how to use MapTiler maps together with Vue.js and MapLibre GL JS for your own Vue.js app.

## Installation and setting up

1. Clone the [Get started with Vue.js and MapLibre GL JS](https://github.com/maptiler/get-started-vuejs-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

```sh
  git clone https://github.com/maptiler/get-started-vuejs-maplibre-gl-js.git my-vuejs-map
```

1. Navigate to the newly created project folder **my-vuejs-map**

```sh
  cd my-vuejs-map
```

1. Install dependencies

```sh
  npm install
```

1. Now navigate to the `src` folder and open the `App.vue` file. 
<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3"><code class="language-html"><!--
  <template>
    <mgl-map
      mapStyle="https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_MAPTILER_API_KEY_HERE"
      :zoom=14
      :center="[16.62662018, 49.2125578]"
    >
      <mgl-navigation-control position="top-left"/>
    </mgl-map>
  </template>
--></code></pre>

1. Start your local environment

```sh
  npm run serve
```

1. You will find your app on the address `http://localhost:8080/`. Now you should see the map in your browser.

## Learn more

If you want to learn how to create a Vue.js component to render a map using MapLibre GL JS see the [How to display a map in Vue.js using MapLibre GL JS](/vuejs/maplibre-gl-js/how-to-use-maplibre-gl-js/) tutorial.

### Vue.js with MapTiler maps

If you're looking to develop Vue.js applications with MapTiler SDK JS, check out our tutorial titled [Vue.js with MapTiler maps](/vuejs/). This step-by-step tutorial will provide you with the necessary guidance and examples to create a Vue.js component that leverages the power of MapTiler SDK JS mapping library to render maps.
