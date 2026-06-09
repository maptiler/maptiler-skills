# Source: https://docs.maptiler.com/angular/sdk-js/how-to-use-sdk-js/

# 

In this step-by-step tutorial, you’ll learn how to create an Angular component that leverages the power of MapTiler SDK JS mapping library to render maps. Together we will build a simple full-screen map application, serving as a practical example of how to seamlessly integrate MapTiler maps into your Angular app.

By the end of this tutorial, you will be able to create a full-screen map with a marker placed at a specified location. With your newfound knowledge, you will be able to create visually stunning maps within your Angular projects. Take a look at the final output of this tutorial below:



## Getting started

*Minimal requirements for completing this tutorial.*

* **Some experience with Angular** You don’t need a lot of experience using [Angular](https://angular.io/){:target="_blank" rel="noopener"} for this tutorial, but you should be familiar with basic concepts and workflow.

* **MapTiler API key.** Your MapTiler account access key is on your MapTiler [Cloud](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"} account page or [Get the API key for FREE](https://cloud.maptiler.com/account/keys){:target="_blank" rel="noopener"}.

* **MapTiler SDK JS.** JavaScript library for building web maps. In this tutorial, you will learn how to install it.

* **Node.js and npm.** Necessary to run your Angular app locally. [Node.js](https://nodejs.org/en/){:target="_blank" rel="noopener"}

* **Angular CLI.** You need to have the [Angular CLI](https://angular.io/cli){:target="_blank" rel="noopener"} installed. To install the Angular CLI, open a terminal window and run the following command:

``` bash
npm install -g @angular/cli
```

## Create an app

In this step, we are going to learn how to create an Angular app.

To create a new Angular project, run in your command-line:

``` bash
ng new my-angular-map
```

The `ng new` command prompts you for information about features to include in the initial app. Accept the defaults by pressing the Enter or Return key. This installs the necessary Angular npm packages and other dependencies and creates a new workspace and a simple Welcome app, ready to run. For more information, follow [Create a workspace and initial application](https://angular.dev/tools/cli/setup-local#create-a-workspace-and-initial-application){:target="_blank" rel="noopener"}.

Navigate to the newly created project folder `my-angular-map`

``` bash
cd my-angular-map
```

Inside the newly created project folder, run `ng serve --open` to start your local environment. You will find your app running on the address `http://localhost:4200/`.

Now you should see the app in your browser.



### Installation and setting up

To install MapTiler SDK JS library, navigate to your project folder and run the command:

``` bash
npm i @maptiler/sdk
```

Open the `tsconfig.json` file and add the `allowSyntheticDefaultImports: true` and `noImplicitAny: false` options to the `compilerOptions` list:

<pre class="line-numbers" data-start="7" data-line-offset="6" data-line="8,9"><code class="language-json"><!--
"forceConsistentCasingInFileNames": true,
"allowSyntheticDefaultImports": true,
"noImplicitAny": false,
"strict": true,
--></code></pre>

Also the `tsconfig.json` file and add the `strictTemplates: true` and `strictNullChecks: false` options to the `angularCompilerOptions` list:

<pre class="line-numbers" data-start="29" data-line-offset="28" data-line="33,34"><code class="language-json"><!--
"angularCompilerOptions": {
  "enableI18nLegacyMessageIdFormat": false,
  "strictInjectionParameters": true,
  "strictInputAccessModifiers": true,
  "strictTemplates": true,
  "strictNullChecks": false
}
--></code></pre>

Navigate to the `src` folder and replace all the contents of the `styles.css` file with the following lines:

``` css
body {
  margin: 0;
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

Now navigate to the `src/app` folder and delete all the content of the `app.component.html` file

Write the following lines in the `app.component.html` file

``` html
<div class="App">
  This is my map App
</div>
```

Now you should see “This is my map App“ in your browser.

Open the `app.component.css` file and add these lines to center the content:

``` css
.App {
  text-align: center;
}
```

### Create a navbar component

In this step, we will create a simple heading navbar component.

To create a new Angular component run in your command-line:

``` bash
ng generate component navbar
```

Navigate to the newly created component folder `src/app/navbar`

Remove all the content in the template file created by the Angular CLI (called `navbar.component.html`) and write the following lines: 

``` html
<div class="heading">
  <h1>This is my map App</h1>
</div>
```

Next, we are going to stylize our component to make a black navbar. Open the `navbar.component.css` file and write these lines:

``` css
.heading {
  margin: 0;
  padding: 0px;
  background-color: black;
  color: white;
}

.heading > h1 {
  padding: 20px;
  margin: 0;
}
```

The generator automatically added the `NavbarComponent` to the `AppModule` to make it available to other components in the application.

Finally, to display the `NavbarComponent` as a child of the element of `AppComponent`, add the `<app-navbar>` element to `app.component.html`. Replace the text *This is my map App* with `<app-navbar></app-navbar>`. Your `app.component.html` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2"><code class="language-html"><!--
<div class="App">
  <app-navbar></app-navbar>
</div>
--></code></pre>

Now you should see the black navbar at the top of your browser.



### Create a map component

In this step, we will create a simple map component. To create the map component run in your command-line:

``` bash
ng generate component map
```

Navigate to the newly created component folder `src/app/map`

Remove all the content in the template file created by the Angular CLI (called `map.component.html`) and write the following lines: 

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-html"><!--
<div class="map-wrap">
  <div class="map" #map></div>
</div>
--></code></pre>

Next, we are going to stylize our component to make a full-screen map. Open the `map.component.css` file and write these lines:

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

Now we are going to modify the logic of our component to create a map using MapTiler SDK JS. Open the `map.component.ts` file and update the top of the file to import `ViewChild, ElementRef, AfterViewInit, OnDestroy` from `@angular/core`.

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="1"><code class="language-ts"><!--
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
--></code></pre>

Add the `AfterViewInit, OnDestroy` lifecycle hooks to the `MapComponent`

<pre class="line-numbers" data-start="8" data-line-offset="7" data-line="8"><code class="language-ts"><!--
export class MapComponent implements OnInit, AfterViewInit, OnDestroy {
--></code></pre>

Right after the @angular/core imports, import the necessary objects from MapTiler SDK JS include the MapTiler SDK CSS file

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2, 4"><code class="language-ts"><!--
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
import { Map, MapStyle, config } from '@maptiler/sdk';

import '@maptiler/sdk/dist/maptiler-sdk.css';
--></code></pre>

Create the map property where we are going to save the Map object. Write the following line just before the constructor function:

<pre class="line-numbers" data-start="11" data-line-offset="10" data-line="12"><code class="language-ts"><!--
export class MapComponent implements OnInit, AfterViewInit, OnDestroy {
  map: Map | undefined;
}
--></code></pre>

Add the reference to the element where the map will be displayed. On the line next to the map property, add these lines:

<pre class="line-numbers" data-start="12" data-line-offset="11" data-line="14,15"><code class="language-ts"><!--
map: Map | undefined;

@ViewChild('map')
private mapContainer!: ElementRef<HTMLElement>;
--></code></pre>

We use `@ViewChild` to get an instance of the native element `<div class = "map" #map></div>` declared in the component template `map.component.html`

Define the `ngOnInit` function to create the apiKey in the SDK `config` object, add these lines:

<pre class="line-numbers" data-start="14" data-line-offset="13" data-line="17-19"><code class="language-ts"><!--
@ViewChild('map')
private mapContainer!: ElementRef<HTMLElement>;

ngOnInit(): void {
  config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
}
--></code></pre>



Define the `ngAfterViewInit` function to create our map. After the `ngOnInit` function, add these lines:

<pre class="line-numbers" data-start="21" data-line-offset="20" data-line="21-30"><code class="language-ts"><!--
ngAfterViewInit() {
  const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

  this.map = new Map({
    container: this.mapContainer.nativeElement,
    style: MapStyle.STREETS,
    center: [initialState.lng, initialState.lat],
    zoom: initialState.zoom
  });
}
--></code></pre>


1. The `container` option sets the DOM element in which the map will be rendered. We will assign the `ElementRef` (obtained thanks to the` @ViewChild`) expected by our component to an HTML element, which will act as a container. Keep in mind that it can only be used after the execution of the `ngAfterViewInit` hook.

1. The `style` option defines what style is the map going to use.

1. The `center` and `zoom` options set the starting position of the map.

Define the `ngOnDestroy` function for cleanup that needs to occur when the instance is destroyed. After the `ngAfterViewInit` function write:

<pre class="line-numbers" data-start="32" data-line-offset="31" data-line="32-34"><code class="language-ts"><!--
ngOnDestroy() {
  this.map?.remove();
}
--></code></pre>

Your `map.component.ts` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0"><code class="language-ts"><!--
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
import { Map, MapStyle, config } from '@maptiler/sdk';

import '@maptiler/sdk/dist/maptiler-sdk.css';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, AfterViewInit, OnDestroy {
  map: Map | undefined;

  @ViewChild('map')
  private mapContainer!: ElementRef<HTMLElement>;

  ngOnInit(): void {
    config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
  }

  ngAfterViewInit() {
    const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

    this.map = new Map({
      container: this.mapContainer.nativeElement,
      style: MapStyle.STREETS,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom
    });
  }

  ngOnDestroy() {
    this.map?.remove();
  }
}
--></code></pre>

### Render a map

Finally, to display the `MapComponent` as a child of the element of `AppComponent`, add the `<app-map>` element to `app.component.html`. Your `app.component.html` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="3"><code class="language-html"><!--
<div class="App">
  <app-navbar></app-navbar>
  <app-map></app-map>
</div>
--></code></pre>

With everything done up until now, you should be able to see your beautiful map in your browser.



### Map marker

Another basic thing to add to your map could be a [marker](/sdk-js/api/markers/#marker){:target="_blank" rel="noopener"} of some location.

Add the `Marker` next to the Map object import from MapTiler SDK in the `map.components.ts` file.

<pre class="line-numbers" data-start="2" data-line-offset="1" data-line="2"><code class="language-ts"><!--
import { Map, MapStyle, Marker, config } from '@maptiler/sdk';
--></code></pre>

In the following line where we declare the navigation control, we add these lines:

<pre class="line-numbers" data-start="30" data-line-offset="29" data-line="30-32"><code class="language-ts"><!--
new Marker({color: "#FF0000"})
  .setLngLat([139.7525,35.6846])
  .addTo(this.map);
--></code></pre>

We create a new marker using the `Marker` function. We added the color option to make it red, then set Lng/Lat of the marker using `.setLngLat()` function, and finally added it to the current map using `.addTo()` function.

We are finished with our basic map objects, your `map.component.ts` file should look like this:

<pre class="line-numbers" data-start="1" data-line-offset="0" data-line="2, 29-32"><code class="language-ts"><!--
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
import { Map, MapStyle, Marker, config } from '@maptiler/sdk';

import '@maptiler/sdk/dist/maptiler-sdk.css';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit, AfterViewInit, OnDestroy {
  map: Map | undefined;

  @ViewChild('map')
  private mapContainer!: ElementRef<HTMLElement>;

  ngOnInit(): void {
    config.apiKey = 'YOUR_MAPTILER_API_KEY_HERE';
  }

  ngAfterViewInit() {
    const initialState = { lng: 139.753, lat: 35.6844, zoom: 14 };

    this.map = new Map({
      container: this.mapContainer.nativeElement,
      style: MapStyle.STREETS,
      center: [initialState.lng, initialState.lat],
      zoom: initialState.zoom
    });
    new Marker({color: "#FF0000"})
      .setLngLat([139.7525,35.6846])
      .addTo(this.map);
  }

  ngOnDestroy() {
    this.map?.remove();
  }
}
--></code></pre>



Once the application is finished, you can export the project for production.

``` bash
ng build
```

## Conclusion

Congratulations! You have finished your simple full-screen map app using Angular, showing Tokyo with a marker on Tokyo Imperial Palace. You can explore more about MapTiler SDK JS for your map in the [MapTiler SDK JS API reference](https://docs.maptiler.com/sdk-js){:target="_blank" rel="noopener"}.

With MapTiler SDK JS, Angular developers can create stunning visualizations and data-driven maps that are responsive and efficient. It also provides support for advanced features like WebGL rendering, 3D maps, and animations.

## Useful links

[MapTiler SDK JS API](https://docs.maptiler.com/sdk-js/){:target="_blank" rel="noopener"}

[NPM - MapTiler SDK JS](https://www.npmjs.com/package/@maptiler/sdk){:target="_blank" rel="noopener"}

[Angular - Getting started](https://angular.io/start){:target="_blank" rel="noopener"}

[MapTiler - ](https://www.maptiler.com/cloud/customize/){:target="_blank" rel="noopener"}

## Learn more

Check the more than [100 MapTiler SDK JS examples](/sdk-js/examples/) that we have prepared so that you can see the limitless possibilities of MapTiler SDK JS and unlock the full potential of your Angular applications. It offers easy terrain, built-in styles, language switching, geocoding, TypeScript power, optional IP geolocation, etc.

### Get started with Angular and MapLibre GL JS

If you're looking to develop Angular applications with MapLibre GL JS, you have two options. First, you can make use of the ngx-maplibre-gl library, which provides an easy and convenient way to integrate MapLibre GL JS into your Angular projects. Alternatively, you can choose to develop your custom component from scratch. To get started, be sure to check out our tutorial titled [Get Started with Angular and MapLibre GL JS](/angular/maplibre-gl-js/get-started/). This tutorial will provide you with the necessary guidance and examples to kickstart your Angular and MapLibre GL JS development journey.
