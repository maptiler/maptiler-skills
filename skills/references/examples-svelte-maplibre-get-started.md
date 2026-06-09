# Source: https://docs.maptiler.com/svelte/maplibre-gl-js/get-started/

# 

In this tutorial, you’ll learn how to display a map in Svelte using MapLibre GL JS. Together we will make a simple full-screen map application as an example of how to use MapTiler maps together with Svelte and MapLibre GL JS for your own Svelte app.

## Installation and setting up

1. Clone the [Get Started with Svelte and MapLibre GL JS](https://github.com/maptiler/get-started-svelte-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

```sh
  git clone https://github.com/maptiler/get-started-svelte-maplibre-gl-js.git my-svelte-map
```

1. Navigate to the newly created project folder **my-svelte-map**

```sh
  cd my-svelte-map
```

1. Install dependencies

```sh
  npm install
```

1. Now navigate to the `src` folder and open the `App.svelte` file. 
   
   <pre class="line-numbers" data-start="16" data-line-offset="15" data-line="18"><code class="language-html"><!--
     <main>
       <Map id="map"
         style="https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_MAPTILER_API_KEY_HERE"
         location=
         bind:map={map} bind:zoom={zoom} bind:center={center} />
     </main>
   --></code></pre>

   

1. Start your local environment

```sh
  npm run dev
```

1. You will find your app on the address `http://localhost:8080/`. Now you should see the map in your browser.

## Learn more

If you want to learn how to create a Svelte component to render a map using MapLibre GL JS see the [How to display a map in Svelte using MapLibre GL JS](/svelte/maplibre-gl-js/how-to-use-maplibre-gl-js/) tutorial.

### Svelte with MapTiler maps

If you're looking to develop Svelte applications with MapTiler SDK JS, check out our tutorial titled [Svelte with MapTiler maps](/svelte/). This step-by-step tutorial will provide you with the necessary guidance and examples to create a Svelte component that leverages the power of MapTiler SDK JS mapping library to render maps.
