# Source: https://docs.maptiler.com/angular/maplibre-gl-js/get-started/

# 

In this tutorial, you’ll learn how to display a map in Angular using MapLibre GL JS. Together we will make a simple full-screen map application as an example of how to use MapTiler maps together with Angular and MapLibre GL JS for your own Angular app.

## Installation and setting up

1. Clone the [Get started with Angular and MapLibre GL JS](https://github.com/maptiler/get-started-angular-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

   ```shell
   git clone https://github.com/maptiler/get-started-angular-maplibre-gl-js.git my-angular-map
   ```

1. Navigate to the newly created project folder **my-angular-map**

   ```shell
   cd my-angular-map
   ```

1. Install dependencies

   ```shell
   npm install
   ```

1. Now navigate to the `src/app` folder and open the `app.component.html` file. 
   <pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2"><code class="language-html"><!--
     <mgl-map
       [style]="'https://api.maptiler.com/maps/streets-v4/style.json?key=YOUR_MAPTILER_API_KEY_HERE'"
       [zoom]="[14]"
       [center]="[16.62662018, 49.2125578]"
     >
       <mgl-control mglNavigation position="top-left"></mgl-control>
     </mgl-map>
   --></code></pre>

1. Start your local environment

   ```sh
   npm start
   ```

1. You will find your app on the address `http://localhost:4200/`. Now you should see the map in your browser.

## Learn more

If you want to learn how to create an Angular component to render a map using MapLibre GL JS see the [How to display a map in Angular using MapLibre GL JS](/angular/maplibre-gl-js/how-to-use-maplibre-gl-js/) tutorial.

### Angular with MapTiler maps

If you're looking to develop Angular applications with MapTiler SDK JS, check out our tutorial titled [Angular with MapTiler maps](/angular/). This step-by-step tutorial will provide you with the necessary guidance and examples to create an Angular component that leverages the power of MapTiler SDK JS mapping library to render maps.
