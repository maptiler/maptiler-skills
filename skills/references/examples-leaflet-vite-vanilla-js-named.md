# Source: https://docs.maptiler.com/leaflet/examples/vite-vanilla-js-named/

# 

In this tutorial, you’ll learn how to add a map using Leaflet to your Vite app. Together we will make a simple fullscreen map application as an example of how to use MapTiler maps together with Vite for your own app.

In this example, we will use named imports to import only the specific elements we use in our application.

By the end of this tutorial, you will be able to create a full-screen map.

<iframe style="height: 400px; width: 100%" src="?key=&position=16/33.747305/-84.389774&mapId="></iframe>

## Getting started

_Minimal requirements for completing this tutorial._

- **Basic Vite knowledge.** You don’t need a lot of experience using [Vite](https://vitejs.dev/){:target="\_blank" rel="noopener"} for this tutorial, but you should be familiar with basic concepts and workflow.

- **MapTiler API key.** Your MapTiler account access key is on your MapTiler [Cloud](https://cloud.maptiler.com/account/keys){:target="\_blank" rel="noopener"} account page or [Get API key for FREE](https://cloud.maptiler.com/account/keys){:target="\_blank" rel="noopener"}.

- **Leaflet.** JavaScript library for building web maps. In this tutorial, you will learn how to install it.

- **Maptiler SDK layer.** The [L.maptiler.maptilerLayer()](https://github.com/maptiler/leaflet-maptilersdk) plugin is how you display vector tiles in Leaflet JS..

- **Node.js and npm.** Necessary to run your Vite app locally. [Node.js](https://nodejs.org/en/){:target="\_blank" rel="noopener"}

## Create an app

In this step, we are going to learn how to create a Vite app.

To create a new Vite project, run in your command-line:

```bash
npm create vite@latest my-vite-map -- --template vanilla
```

Navigate to the newly created project folder `my-vite-map`

```bash
cd my-vite-map
```

Inside the newly created project folder, run `npm install` to install the dependencies.

To start your local environment, run `npm run dev`. You will find your app running on address `http://localhost:5173/`.

Now you should see the app in your browser.



### Installation and setting up

To install Leaflet and Maptiler SDK layer, navigate to your project folder and run the command:

```bash
npm i leaflet @maptiler/leaflet-maptilersdk
```

Navigate to the `src` folder and replace all the contents of the `style.css` file with the following lines:

```css
html,
body {
  margin: 0;
}

#app {
  width: 100vw;
  height: 100vh;
}
```

Replace all the contents of the `main.js` file with the following lines:

```js
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "./style.css";
import { MaptilerLayer } from "@maptiler/leaflet-maptilersdk";
import { MapStyle } from "@maptiler/sdk";

function init() {
  const container = document.getElementById("app");

  if (!container) throw new Error('There is no div with the id: "app" ');

  const map = L.map(container, {
    center: L.latLng(33.747305, -84.389774),
    zoom: 16,
  });

  // Create a MapTiler Layer inside Leaflet
  const mtLayer = new MaptilerLayer({
    // Get your free API key at https://cloud.maptiler.com
    apiKey: "YOUR_MAPTILER_API_KEY_HERE",
    style: MapStyle.BASIC.DARK,
  }).addTo(map);
}

init();
```



With everything done up until now, you should be able see your beautiful map in your browser.



Once the application is finished, you can export the project for production.

```bash
npm run build
```

## Conclusion

Congratulations! You have finished your simple fullscreen map app using Vite + Leaflet.

## Useful links

[MapTiler SDK JS API](https://docs.maptiler.com/sdk-js/){:target="\_blank" rel="noopener"}

[Leaflet - MapTiler SDK layer](https://github.com/maptiler/leaflet-maptilersdk){:target="\_blank" rel="noopener"}

[Vite - Getting Started](https://vitejs.dev/guide/){:target="\_blank" rel="noopener"}

[MapTiler - ](https://www.maptiler.com/cloud/customize/){:target="\_blank" rel="noopener"}

