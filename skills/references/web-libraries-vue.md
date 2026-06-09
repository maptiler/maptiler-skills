# Source: https://docs.maptiler.com/vuejs/maplibre-gl-js/how-to-use-maplibre-gl-js/

# 

In this step-by-step tutorial, you’ll learn how to create a Vue.js component to render a map using MapLibre GL JS. Together we will make a simple full-screen map application, serving as a practical example of how to seamlessly integrate MapTiler maps with MapLibre GL JS into your Vue.js app.

By the end of this tutorial, you will be able to create a full-screen map with a marker placed at a specified location. Your final map will look like this:



## Getting started

_Minimal requirements for completing this tutorial._

- **Some experience with Vue.js** You don’t need a lot of experience using [Vue.js](https://vuejs.org/){:target="\_blank" rel="noopener"} for this tutorial, but you should be familiar with basic concepts and workflow.

- **MapTiler API key.** Your MapTiler account access key is on your MapTiler [Cloud](https://cloud.maptiler.com/account/keys){:target="\_blank" rel="noopener"} account page or [Get API key for FREE](https://cloud.maptiler.com/account/keys){:target="\_blank" rel="noopener"}.

- **MapLibre GL JS.** JavaScript library for building web maps. In this tutorial, you will learn how to install it.

- **Node.js and npm.** Necessary to run your Vue.js app locally. [Node.js](https://nodejs.org/en/){:target="\_blank" rel="noopener"}

- **Vue CLI.** You need to have the [Vue CLI](https://cli.vuejs.org/){:target="\_blank" rel="noopener"} installed. To install the Vue CLI, open a terminal window and run the following command:

```bash
npm install -g @vue/cli
```

## Create an app

In this step, we are going to learn how to create a Vue.js app.

To create a new Vue.js project, run in your command-line:

```bash
vue create my-vue-map
```

The `vue create` command prompts you for information about features to include in the initial app. Select the `Default (Vue 3) ([Vue 3] babel, eslint)` option.



Use the arrow keys and press the Enter or Return key to select an option. The Vue CLI installs the necessary Vue.js npm packages and other dependencies and creates a new workspace and a simple Welcome app, ready to run. For more information, follow [Creating a Project](https://cli.vuejs.org/guide/creating-a-project.html#vue-create){:target="\_blank" rel="noopener"}.

Navigate to the newly created project folder `my-vue-map`

```bash
cd my-vue-map
```

Inside the newly created project folder, run `npm run serve` to start your local environment. You will find your app running on the address `http://localhost:8080/`.

Now you should see the app in your browser.



### Installation and setting up

To install MapLibre GL library, navigate to your project folder and run the command:

```bash
npm i maplibre-gl
```

Navigate to the `src` folder and delete all the content of the `App.vue` file. Write the following lines in the `App.vue` file

```html
<template>
  <div class="app">This is my map App</div>
</template>




```

Now you should see “This is my map App“ in your browser.

Navigate to the `src/components` folder and delete de `HelloWorld.vue` file

### Create a navbar component

In this step, we will create a simple heading navbar component.

Create a new file called `Navbar.vue` inside the `components` folder and write these lines:

```html
<template>
  <div class="heading">
    <h1>This is my map App</h1>
  </div>
</template>




```

Finally, to display the `Navbar` we need to import the Navbar component and add it to our main component template section `App.vue`.

Import the navbar component into `App.vue` script block

<pre class="line-numbers" data-start="7" data-line-offset="6" data-line="2, 6"><code class="language-html"><!--


--></code></pre>

Replace the text _This is my map App_ with `<Navbar />`. Your `App.vue` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3,8,13"><code class="language-html"><!--
<template>
  <div class="app">
    <Navbar />
  </div>
</template>





--></code></pre>

Now you should see the black navbar at the top of your browser.



### Create a map component

In this step, we will create a simple map component.

Create a new file called `Map.vue` inside the `components` folder and write these lines:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-html"><!--
<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"></a>
    <div class="map" ref="mapContainer"></div>
  </div>
</template>





--></code></pre>

We use `position: absolute` on the map itself and `position: relative` on the wrap around the map for more possibilities in future styling.



1. The `container` option sets the DOM element in which the map will be rendered. We will assign the `mapContainer` ref expected by our component to an HTML element, which will act as a container. Keep in mind that the reference to `mapContainer` can only be used after the execution of the `onMounted` hook.

1. The `style` option defines what style is the map going to use.

1. The `center` and `zoom` options set the starting position of the map.

1. The `onUnmounted` function does the cleanup that should occur when the instance is destroyed.

### Render a map

Finally, to display the `Map` we need to import the Map component and add it to our main component `App.vue`.

Import the map component into `App.vue` script block

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="10, 16"><code class="language-html"><!--


--></code></pre>

Add the `<Map />` just below the Navbar in the template section. The template block should look like this

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="4"><code class="language-html"><!--
<template>
  <div class="app">
    <Navbar />
    <Map />
  </div>
</template>
--></code></pre>

With everything done up until now, you should be able to see your beautiful map in your browser.



Your `App.vue` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="4, 10, 16"><code class="language-html"><!--
<template>
  <div class="app">
    <Navbar />
    <Map />
  </div>
</template>





--></code></pre>

### Basic additional options

The last topic of this tutorial will be adding basic objects to your map. For more detailed information you can visit the [MapLibre documentation](https://maplibre.org/maplibre-gl-js/docs/API/#markers-and-controls){:target="\_blank" rel="noopener"}.

### Map Controls

We will navigate back to our `Map.vue` file and add map [navigation controls](https://maplibre.org/maplibre-gl-js/docs/API/classes/NavigationControl/){:target="\_blank" rel="noopener"} to our map.

Add the `NavigationControl` next to the Map object import from MapLibre GL.

<pre class="line-numbers" data-start="10" data-line-offset="9" data-line="10"><code class="language-js"><!--
import { Map, NavigationControl } from 'maplibre-gl';
--></code></pre>

On line 30 (just after the initialization of the map) of the `Map.vue` file, add the following line:

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30"><code class="language-js"><!--
map.value.addControl(new NavigationControl(), 'top-right');
--></code></pre>

`new NavigationControl()` will create a new controls object which we add to the current map using the `addControl()` function in the `'top-right'` position.



### Map marker

Another basic thing to add to your map could be a [marker](https://maplibre.org/maplibre-gl-js/docs/API/classes/Marker/){:target="\_blank" rel="noopener"} of some location.

Add the `Marker` next to the Map object import from MapLibre GL.

<pre class="line-numbers" data-start="10" data-line-offset="9" data-line="10"><code class="language-js"><!--
import { Map, NavigationControl, Marker } from 'maplibre-gl';
--></code></pre>

In the following line where we declare the navigation control, we add these lines:

<pre class="line-numbers" data-start="31" data-line-offset="30" data-line="31-33"><code class="language-js"><!--
new Marker({color: "#FF0000"})
  .setLngLat([139.7525,35.6846])
  .addTo(map);
--></code></pre>

We create a new marker using the `Marker` function. We added the color option to make it red, then set Lng/Lat of the marker using `.setLngLat()` function, and finally added it to the current map using `.addTo()` function.

We are finished with our basic map objects, your `Map.vue` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="10, 30-33"><code class="language-html"><!--
<template>
  <div class="map-wrap">
    <a href="https://www.maptiler.com" class="watermark"></a>
    <div class="map" ref="mapContainer"></div>
  </div>
</template>





--></code></pre>



### Full code to download

We have created a template with the result of this tutorial that will serve as a basis to build future applications. You can access the template repository at [Vue.js template for MapLibre](https://github.com/maptiler/vue-template-maplibre-gl-js){:target="\_blank" rel="noopener"}.

### Online demo:

You can see an online demo at [https://labs.maptiler.com/vue-template-maplibre-gl-js/](https://labs.maptiler.com/vue-template-maplibre-gl-js/){:target="\_blank" rel="noopener"}

## Conclusion

Congratulations! You have finished your simple full-screen map app using Vue.js, showing Tokyo with a marker on Tokyo Imperial Palace. You can explore more about MapLibre GL JS for your map in the [MapLibre API reference](https://maplibre.org/maplibre-gl-js/docs/API/){:target="\_blank" rel="noopener"}.

## Useful links

[MapTiler - JavaScript Maps API](https://docs.maptiler.com/sdk-js/){:target="\_blank" rel="noopener"}

[Vue.js](https://vuejs.org/){:target="\_blank" rel="noopener"}

[NPM - MapLibre GL](https://www.npmjs.com/package/maplibre-gl){:target="\_blank" rel="noopener"}

[MapLibre official web](https://maplibre.org/){:target="\_blank" rel="noopener"}

[MapTiler - ](https://www.maptiler.com/cloud/customize/){:target="\_blank" rel="noopener"}

## Learn more

### Vue.js with MapTiler maps

If you're looking to develop Vue.js applications with MapTiler SDK JS, check out our tutorial titled [Vue.js with MapTiler maps](/vuejs/). This step-by-step tutorial will provide you with the necessary guidance and examples to create a Vue.js component that leverages the power of MapTiler SDK JS mapping library to render maps.
