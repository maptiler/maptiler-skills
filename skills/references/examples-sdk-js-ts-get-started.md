# Source: https://docs.maptiler.com/sdk-js/examples/ts-get-started/

# 

Create a map using the SDK based on TypeScript. Benefit from features like code completion, type safety, accurate documentation, and backward compatibility. Save time on your project by reducing typos and mistakes. No need to worry about changes to API endpoints and how they may affect your code.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>

Choose from a wide range of bundlers to find the best solution for your project. Whether you prefer [Parcel](https://parceljs.org/), [Webpack](https://webpack.js.org/), [Rollup](https://rollupjs.org/), [Turbopack](https://turbo.build/pack), or any other bundler, you have plenty of options to choose from.

1. Install the npm package.

<pre><code class="language-bash"><!--
npm install --save @maptiler/sdk
--></code></pre>

1. Create a `<div>` element with a certain id where you want your map to be.

   Add `<div>` tag into your page. This div will be the container where the map will be loaded.

    <pre><code class="language-html"><!--
      <div id="map"></div>
    --></code></pre>

1. Include the following code in your TypeScript `main.ts` file.

<pre><code class="language-js"><!--
  import { config, Map, MapOptions } from '@maptiler/sdk';

  import "@maptiler/sdk/dist/maptiler-sdk.css";

  config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

  const options: MapOptions = {
    container: document.getElementById("map") as HTMLElement, // container's id or the HTML element in which SDK will render the map
  }

  // Instanciating a map
  const map: Map = new Map(options);
--></code></pre>

1. 

1. Create the map containter style. Add the map containter style to you stylesheet `style.css`. The div must have non-zero height. In this case we are going to make a fullscreen map.

<pre><code class="language-css"><!--
body { margin: 0; padding: 0; }

#map { position: absolute; top: 0; bottom: 0; width: 100%; }
--></code></pre>

Check out the tutorial <a href="#" class="show-parcel">How to create a map with TypeScript and Parcel</a>.

<div id="parcel-tutorial" class="hidden">
<ol>
<li>
Install bundler and build tools. This tutorial will use Parcel because it supports TypeScript out of the box without any additional configuration.

    <pre><code class="language-bash"><!--
    npm i -D parcel-bundler typescript
    --></code></pre>

</li>
<li>
Create the TypeScript config file.

    <pre><code class="language-bash"><!--
    npx tsc --init
    --></code></pre>

</li>
<li>
Update the package.json scripts. Create the <code class="language-plaintext">dev</code> and <code class="language-plaintext">build</code> scripts.

    <pre><code class="language-json"><!--
    "scripts": {
      "dev": "parcel src/index.html",
      "build": "parcel build src/index.html"
    },
    --></code></pre>

</li>
<li>
Create a <code class="language-plaintext">src</code> folder and inside this forder create 3 files: 
<code class="language-plaintext">index.html</code>, <code class="language-plaintext">main.ts</code>, and <code class="language-plaintext">style.css</code>.
</li>
<li>
Copy the following code, paste it into <code class="language-plaintext">index.html</code> file. The <code class="language-plaintext">&lt;div id="map"&gt;</code> will be the container where the map will be loaded.

    <pre><code class="language-html"><!--
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>MapTiler SDK JS with TS</title>
      <link rel="stylesheet" href="./style.css">
      <script src="./main.ts" defer></script>
    </head>
    <body>
      <div id="map"></div>
    </body>
    </html>
    --></code></pre>

</li>
<li>
Create the map container style. Add the map container style to you stylesheet <code class="language-plaintext">style.css</code>. The div must have non-zero height. In this case we are going to make a fullscreen map.

    <pre><code class="language-css"><!--
    body { margin: 0; padding: 0; }

    #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    --></code></pre>

</li>
<li>
Include the following code in your <code class="language-plaintext">main.ts</code> file.

    <pre><code class="language-js"><!--
      import { config, Map, MapOptions } from '@maptiler/sdk';

      import "@maptiler/sdk/dist/maptiler-sdk.css";

      config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';

      const options: MapOptions = {
        container: document.getElementById("map") as HTMLElement, // container's id or the HTML element in which SDK will render the map
      }

      // Instanciating a map
      const map: Map = new Map(options);
    --></code></pre>

</li>
<li markdown="1">

</li>
<li>
Running the dev server. To see the map run the local server. Open a terminal and write.

    <pre><code class="language-bash"><!--
    npm run dev
    --></code></pre>

</li>
<li>
Now you can see your application opening <code class="language-plain">http://localhost:1234</code> in your browser. By default, the map will be initialized with the style <a href="https://www.maptiler.com/maps/#style=">maptilersdk.MapStyle.STREETS</a> and centered on the actual visitor location using the <a href="https://github.com/maptiler/maptiler-sdk-js#%EF%B8%8F%EF%B8%8F-geolocation">IP geolocation</a> API provided by <a href="https://docs.maptiler.com/cloud/api/geolocation/">MapTiler</a>.
</li>
</ol>
</div>



<script>
  document.querySelectorAll("#parcel-tutorial > ol > li").forEach((elem) => {
    elem.classList.add("my-2");
  });

  document.querySelector(".show-parcel").addEventListener('click', (evt) => {
    evt.preventDefault();
    evt.stopPropagation()
    document.getElementById("parcel-tutorial").classList.toggle("hidden");

    const parcel_codes = Array.from(document.querySelectorAll("#parcel-tutorial > ol > li .code-toolbar"));
    parcel_codes.forEach((elem) => {
      elem.classList.add("my-2", "ms-0");
    });
  });
</script>

