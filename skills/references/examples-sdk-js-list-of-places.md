# Source: https://docs.maptiler.com/sdk-js/examples/list-of-places/

# List of places

This tutorial shows how to sync the map with a list of places.

This tutorial will guide you through the process of creating a compilation of locations and synchronizing it with a map. The map will display markers for each of these locations. By following these steps, you will be able to generate a list of places where selecting an item from the list will automatically select the pin on the map. Similarly, when making changes to the map view, the list of places will be updated to only show the locations that are currently visible on the map. Additionally, selecting a place on the map will highlight and select the corresponding item on the list.

Download the [shoe sample icon](./shoes.png) and the [selected shoe sample icon](./shoes_selected.png), The icon is from the [Maps Icons Collection](https://mapicons.mapsmarker.com).

Download the [shoe shops GeoJSON sample data](/sdk-js/assets/shops_shoe.geojson)

<div class="tab-common-content" markdown="1">

1. We are going to modify the structure of the web page to have two main elements: a sidebar (`aside`) where we will show the list of shoe stores and the main area (`main`) where we will display the map.

<pre class="line-numbers" data-start="15" data-line-offset="14" data-line="15-22"><code class="language-html"><!--

<aside class="sidebar">

<div class="sidebar-content-info"></div>

</aside>

<main class="main">

<div id="map">

<button class="btn hidden">Search in this area</button>

</div>

</main>

--></code></pre>

1. Add the CSS classes to create the simple Flexbox Layout for the Sidebar + Main Content Area

<pre class="line-numbers" data-start="10" data-line-offset="9" data-line="10-61"><code class="language-css"><!--

body {

margin: 0;

padding: 0;

min-height: 100vh;

display: flex;

}

.sidebar {

min-width: 450px;

max-width: 450px;

display: flex;

}

.main {

flex-grow: 1;

display: flex;

}

position: relative;

width: 100%;

height: 100%;

}

.btn {

display: block;

position: relative;

margin: 8px auto;

height: 40px;

padding: 10px;

border: none;

border-radius: 3px;

font-size: 12px;

text-align: center;

color: #fff;

background:#3174FF;

z-index: 2;

}

.hidden {

display: none;

}

.sidebar-content-info {

display: flex;

flex-direction: column;

font-size: 1rem;

width: 100%;

word-break: break-word;

overflow-y: auto;

max-height: 100vh;

}

--></code></pre>

1. Reload the page. Now you should see the app in your browser.

1. Add an event handler for the map load event. You will add code to create a GeoJSON source and a vector layer in this handler. We will also add other map event handlers.

<pre class="line-numbers" data-start="82" data-line-offset="81" data-line="82-86"><code class="language-js"><!--

map.on('load', async function() {

//your code here

//end load function code

});

--></code></pre>

1. Add a custom images to the map. You can use any image or download the [shoe image](./shoes.png) and the [selected shoe image](./shoes_selected.png) we used in the tutorial. In the example, these images are in the same folder as the index.html file

<pre class="line-numbers" data-start="83" data-line-offset="82" data-line="84-89"><code class="language-js"><!--

//your code here

const image = await map.loadImage('./shoes.png');

map.addImage('pinShoe', image.data);

const imageSelected = await map.loadImage('./shoes_selected.png');

map.addImage('pinShoeSelected', imageSelected.data);

//end load function code

--></code></pre>

1. Create GeoJSON source. The following snippet creates GeoJSON source hosted on MapTiler (check out the [How to Upload GeoJSON to MapTiler](/guides/maps-apis/maps-platform/prepare-geojson-with-attributes-for-choropleth-map-and-upload-geojson-to-maptiler-cloud#PrepareGeoJSONwithattributesforchoroplethmapanduploadGeoJSONtoMapTilerCloud-UploadGeoJSONtoMapTilerCloud){:target="_blank" rel="noopener"} tutorial). Publish the dataset and copy the link to the GeoJSON. Download the [shoe shop GeoJSON sample data](/sdk-js/assets/shops_shoe.geojson). In this example we will add a random image (in the photo property) to each of the map elements.

<pre class="line-numbers" data-start="90" data-line-offset="89" data-line="90-106"><code class="language-js"><!--

const shops = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

function randomIntFromInterval(min = 1, max = 5) { // min and max included

return Math.floor(Math.random() * (max - min + 1) + min);

}

//add a random image to the GeoJSON features

shops.features.forEach(item => {

item.properties.photo = `./shoe_shop_${randomIntFromInterval()}.jpeg`;

})

map.addSource('shops', {

type: 'geojson',

generateId: true,

data: shops

});

//end load function code

--></code></pre>

1. Add the vector layer. In this example, we will use the shoe image to display a point layer using a custom PNG icon as a pin.

<pre class="line-numbers" data-start="107" data-line-offset="106" data-line="107-116"><code class="language-js"><!--

map.addLayer({

'id': 'points',

'type': 'symbol',

'source': 'shops',

'layout': {

'icon-image': 'pinShoe',

},

'paint': {}

});

//end load function code

--></code></pre>

1. Now you should see the map with pins.

1. Change the cursor to a pointer when the mouse is over the points layer.

<pre class="line-numbers" data-start="117" data-line-offset="116" data-line="117-124"><code class="language-js"><!--

map.on('mouseenter', 'points', (e) => {

map.getCanvas().style.cursor = 'pointer';

});

map.on('mouseleave', 'points', (e) => {

map.getCanvas().style.cursor = '';

});

//end load function code

--></code></pre>

1. Create the list with the elements that are displayed on the map.

<pre class="line-numbers" data-start="125" data-line-offset="124" data-line="125-126"><code class="language-js"><!--

map.on('render', createListFromSource);

//end load function code

--></code></pre>

1. Update the list when the map view is changed. With this event, we will have the map view and the list synchronized. Every time the view is updated (zoomed, panned) the *"Search in this area"* button is displayed. This will allow us to refresh the list and only show the elements that appear on the map.

<pre class="line-numbers" data-start="127" data-line-offset="126" data-line="127-128"><code class="language-js"><!--

map.on('moveend', showRefreshListButton);

//end load function code

--></code></pre>

1. Get the point layer elements when the user clicks on the map. With the `click` event, the user will be able to select an element on the map. This will allow us to select the same item in the list.

<pre class="line-numbers" data-start="129" data-line-offset="128" data-line="129-130"><code class="language-js"><!--

map.on('click', getPoint);

//end load function code

--></code></pre>

1. We are done with the functions that are executed when the map is loaded. Now we will create the functions outside of the `load` event handler.

<pre class="line-numbers" data-start="131" data-line-offset="130" data-line="134-144"><code class="language-js"><!--

//end load function code

});

function createListFromSource() {

}

function showRefreshListButton() {

}

function getPoint(e) {

}

--></code></pre>

1. Get the elements that are visible in the map view.

<pre class="line-numbers" data-start="134" data-line-offset="133" data-line="135-140,143-150"><code class="language-js"><!--

function createListFromSource() {

const features = getRenderedFeatures();

if (features.length) {

//stop listening to the map render event

map.off('render', createListFromSource);

updateList();

}

}

function getRenderedFeatures(point) {

//if the point is null, it is searched within the bounding box of the map view

const features = map.queryRenderedFeatures(point, {

layers: ['points']

});

return features;

}

--></code></pre>

1. Select a map element when the user clicks on it.

<pre class="line-numbers" data-start="155" data-line-offset="154" data-line="156-171,174-181"><code class="language-js"><!--

function getPoint(e) {

const features = getRenderedFeatures(e.point);

if (features.length) {

const element = features[0];

selectedItem = element.id;

map.setLayoutProperty('points', 'icon-image',

[

'match',

['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources

element.id, 'pinShoeSelected', //image when id is the clicked feature id

'pinShoe' // default

]

);

selectMapToList(element);

} else {

cleanSelection();

}

}

function cleanSelection() {

}

function selectMapToList(element) {

}

--></code></pre>

1. Create a list of places.

<pre class="line-numbers" data-start="182" data-line-offset="181" data-line="182-222"><code class="language-js"><!--

let selectedItem;

function updateList() {

const features = getRenderedFeatures();

const listItems = features.map(item => {

return `<div class='list-item ${item.id === selectedItem ? "selected" : ""}'

data-id="${item.id}" data-lnglat="${item.geometry.coordinates.join()}">

${createListItemContent(item)}

</div>`;

});

const listContainer = document.querySelector('.sidebar-content-info');

listContainer.scrollTop = 0;

listContainer.innerHTML = listItems.join('');

}

function createListItemContent(item) {

const html = [``];

if (item.properties.name) {

html.push(`<h2>${item.properties.name}</h2>`);

}

if (item.properties.operator) {

html.push(`<h4>${item.properties.operator}</h4>`);

}

if (item.properties["addr:street"]) {

html.push(`<div class="addr">${item.properties["addr:street"]}, ${item.properties["addr:housenumber"]}</div>`);

}

if (item.properties.opening_hours) {

html.push(`<h5>Opening hours</h5>`);

item.properties.opening_hours.split(",").forEach(element => {

html.push(`<div>${element.trim()}</div>`);

});

}

if (item.properties.phone) {

html.push(`<div><a href="tel:${item.properties.phone}" target="_blank" rel="noopener noreferrer">${item.properties.phone}</a></div>`);

}

if (item.properties.website) {

html.push(`<div><a href="${item.properties.website}" target="_blank" rel="noopener noreferrer">${item.properties.website}</a></div>`);

}

return html.join('');

}

--></code></pre>

1. Create the list style. Add the list style to your stylesheet.

<pre class="line-numbers" data-start="63" data-line-offset="62" data-line="63-83"><code class="language-css"><!--

.list-item {

border-bottom: 1px solid #333333;

padding: 16px;

}

.list-item:hover {

cursor: pointer;

background-color: #E4ECFF;

}

.list-item h2 {

margin: 0.23em 0;

}

.list-item.selected {

background-color: #05D0DF;

}

.list-item img {

width: 100%;

}

--></code></pre>

1. With everything done up until now, you should be able to see your map and the list of places in your browser.

1. Next, we are going to add some events to link the list with the map. These events will ensure that when a list item is clicked on, the corresponding marker on the map is selected and centered on the map view.

<pre class="line-numbers" data-start="245" data-line-offset="244" data-line="245-268"><code class="language-js"><!--

let listContainer = document.querySelector('.sidebar-content-info');

listContainer.addEventListener('click', (e) => {

cleanSelection();

const li = e.target.closest('.list-item');

li.classList.toggle('selected');

if (li.classList.contains('selected')) {

selectedItem = parseInt(li.dataset.id);

selectListToMap(li);

}

});

function selectListToMap(item) {

map.setLayoutProperty('points', 'icon-image',

[

'match',

['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources

parseInt(item.dataset.id), 'pinShoeSelected', //image when id is the clicked feature id

'pinShoe' // default

]

);

map.setCenter(item.dataset.lnglat.split(','));

}

--></code></pre>

1. We have already made it so that selecting an item from the list selects it on the map. Now we will do the other way, when selecting an element on the map it is selected in the list.

<pre class="line-numbers" data-start="200" data-line-offset="199" data-line="201-204"><code class="language-js"><!--

function selectMapToList(element) {

cleanListSelection();

const listSelected = document.querySelector(`.list-item[data-id="${element.id}"]`);

listSelected.classList.add('selected');

listSelected.scrollIntoView({behavior: 'smooth', block: 'nearest'});

}

--></code></pre>

1. At this point we already have the list linked and synchronized with the map. Now we will create some functions to toggle the selected elements so that we have only one element selected in both the list and the map.

<pre class="line-numbers" data-start="196" data-line-offset="195" data-line="197-199, 202-208"><code class="language-js"><!--

function cleanSelection() {

selectedItem = null;

map.setLayoutProperty('points', 'icon-image', 'pinShoe');

cleanListSelection();

}

function cleanListSelection() {

const listSelected = document.querySelector(`.list-item.selected`);

if (listSelected) {

listSelected.classList.remove('selected');

}

}

--></code></pre>

1. Finally, we need to show the *"Search in this area"* button when the map view is updated and update the list when the user clicks the button.

<pre class="line-numbers" data-start="173" data-line-offset="172" data-line="174,177-182"><code class="language-js"><!--

function showRefreshListButton() {

document.querySelector('.btn').classList.remove('hidden');

}

document.querySelector('.btn').addEventListener('click', (e) => {

e.target.classList.add('hidden');

cleanSelection();

updateList();

});

--></code></pre>

1. Congratulations! You have your map with place markers synchronized with the list of places.

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [-0.0921, 51.5108], // starting position [lng, lat]
      zoom: 11, // starting zoom
    });

    map.on('load', async function() {
      //your code here
      const image = await map.loadImage('./shoes.png');
      map.addImage('pinShoe', image.data);

      const imageSelected = await map.loadImage('./shoes_selected.png');
      map.addImage('pinShoeSelected', imageSelected.data);

      const shops = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

      function randomIntFromInterval(min = 1, max = 5) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min);
      }

      //add a random image to the GeoJSON features
      shops.features.forEach(item => {
        item.properties.photo = `./shoe_shop_${randomIntFromInterval()}.jpeg`;
      });

      map.addSource('shops', {
        type: 'geojson',
        generateId: true,
        data: shops
      });

      map.addLayer({
        'id': 'points',
        'type': 'symbol',
        'source': 'shops',
        'layout': {
          'icon-image': 'pinShoe',
        },
        'paint': {}
      });

      map.on('mouseenter', 'points', (e) => {
        map.getCanvas().style.cursor = 'pointer';
      });

      map.on('mouseleave', 'points', (e) => {
        map.getCanvas().style.cursor = '';
      });

      map.on('render', createListFromSource);

      map.on('moveend', showRefreshListButton);

      map.on('click', getPoint);

      //end load function code
    });

    function createListFromSource() {
      const features = getRenderedFeatures();
      if (features.length) {
        //stop listening to the map render event
        map.off('render', createListFromSource);
        updateList();
      }
    }

    function getRenderedFeatures(point) {
      //if the point is null, it is searched within the bounding box of the map view
      const features = map.queryRenderedFeatures(point, {
        layers: ['points']
      });
      return features;
    }

    function showRefreshListButton() {
      document.querySelector('.btn').classList.remove('hidden');
    }

    document.querySelector('.btn').addEventListener('click', (e) => {
      e.target.classList.add('hidden');
      cleanSelection();
      updateList();
    });

    function getPoint(e) {
      const features = getRenderedFeatures(e.point);
      if (features.length) {
        const element = features[0];
        selectedItem = element.id;
        map.setLayoutProperty('points', 'icon-image',
          [
            'match',
            ['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources
            element.id, 'pinShoeSelected', //image when id is the clicked feature id
            'pinShoe' // default
          ]
        );
        selectMapToList(element);
      } else {
        cleanSelection();
      }
    }

    function cleanSelection() {
      selectedItem = null;
      map.setLayoutProperty('points', 'icon-image', 'pinShoe');
      cleanListSelection();
    }

    function cleanListSelection() {
      const listSelected = document.querySelector(`.list-item.selected`);
      if (listSelected) {
        listSelected.classList.remove('selected');
      }
    }

    function selectMapToList(element) {
      cleanListSelection();
      const listSelected = document.querySelector(`.list-item[data-id="${element.id}"]`);
      listSelected.classList.add('selected');
      listSelected.scrollIntoView({behavior: 'smooth', block: 'nearest'});
    }

    let selectedItem;

    function updateList() {
      const features = getRenderedFeatures();
      const listItems = features.map(item => {
        return `<div class='list-item ${item.id === selectedItem ? "selected" : ""}' 
          data-id="${item.id}" data-lnglat="${item.geometry.coordinates.join()}">
            ${createListItemContent(item)}
          </div>`;
      });
      const listContainer = document.querySelector('.sidebar-content-info');
      listContainer.scrollTop = 0;
      listContainer.innerHTML = listItems.join('');
    }

    function createListItemContent(item) {
      const html = [`<img src="${item.properties.photo}" alt="shoe shop">`];
      if (item.properties.name) {
        html.push(`<h2>${item.properties.name}</h2>`);  
      }
      if (item.properties.operator) {
        html.push(`<h4>${item.properties.operator}</h4>`);  
      }
      if (item.properties["addr:street"]) {
        html.push(`<div class="addr">${item.properties["addr:street"]}, ${item.properties["addr:housenumber"]}</div>`);
      }
      if (item.properties.opening_hours) {
          html.push(`<h5>Opening hours</h5>`);
          item.properties.opening_hours.split(",").forEach(element => {
            html.push(`<div>${element.trim()}</div>`);
          });
      }
      if (item.properties.phone) {
        html.push(`<div><a href="tel:${item.properties.phone}" target="_blank" rel="noopener noreferrer">${item.properties.phone}</a></div>`);
      }
      if (item.properties.website) {
        html.push(`<div><a href="${item.properties.website}" target="_blank" rel="noopener noreferrer">${item.properties.website}</a></div>`);
      }
      return html.join('');
    }

    let listContainer = document.querySelector('.sidebar-content-info');

    listContainer.addEventListener('click', (e) => {
      cleanSelection();
      const li = e.target.closest('.list-item');
      li.classList.toggle('selected');
      if (li.classList.contains('selected')) {
        selectedItem = parseInt(li.dataset.id);
        selectListToMap(li);
      }
    });

    function selectListToMap(item) {
      map.setLayoutProperty('points', 'icon-image',
        [
          'match',
          ['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources
          parseInt(item.dataset.id), 'pinShoeSelected', //image when id is the clicked feature id
          'pinShoe' // default
        ]
      );
      map.setCenter(item.dataset.lnglat.split(','));
    }
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of places</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: maptilersdk.MapStyle.STREETS,
            center: [-0.0921, 51.5108],
            zoom: 11
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [-0.0921, 51.5108], // starting position [lng, lat]
              zoom: 11, // starting zoom
            });

            map.on('load', async function() {
              //your code here
              const image = await map.loadImage('./shoes.png');
              map.addImage('pinShoe', image.data);

              const imageSelected = await map.loadImage('./shoes_selected.png');
              map.addImage('pinShoeSelected', imageSelected.data);

              const shops = await maptilersdk.data.get('YOUR_MAPTILER_DATASET_ID_HERE');

              function randomIntFromInterval(min = 1, max = 5) { // min and max included 
                return Math.floor(Math.random() * (max - min + 1) + min);
              }

              //add a random image to the GeoJSON features
              shops.features.forEach(item => {
                item.properties.photo = `./shoe_shop_${randomIntFromInterval()}.jpeg`;
              });

              map.addSource('shops', {
                type: 'geojson',
                generateId: true,
                data: shops
              });

              map.addLayer({
                'id': 'points',
                'type': 'symbol',
                'source': 'shops',
                'layout': {
                  'icon-image': 'pinShoe',
                },
                'paint': {}
              });

              map.on('mouseenter', 'points', (e) => {
                map.getCanvas().style.cursor = 'pointer';
              });

              map.on('mouseleave', 'points', (e) => {
                map.getCanvas().style.cursor = '';
              });

              map.on('render', createListFromSource);

              map.on('moveend', showRefreshListButton);

              map.on('click', getPoint);

              //end load function code
            });

            function createListFromSource() {
              const features = getRenderedFeatures();
              if (features.length) {
                //stop listening to the map render event
                map.off('render', createListFromSource);
                updateList();
              }
            }

            function getRenderedFeatures(point) {
              //if the point is null, it is searched within the bounding box of the map view
              const features = map.queryRenderedFeatures(point, {
                layers: ['points']
              });
              return features;
            }

            function showRefreshListButton() {
              document.querySelector('.btn').classList.remove('hidden');
            }

            document.querySelector('.btn').addEventListener('click', (e) => {
              e.target.classList.add('hidden');
              cleanSelection();
              updateList();
            });

            function getPoint(e) {
              const features = getRenderedFeatures(e.point);
              if (features.length) {
                const element = features[0];
                selectedItem = element.id;
                map.setLayoutProperty('points', 'icon-image',
                  [
                    'match',
                    ['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources
                    element.id, 'pinShoeSelected', //image when id is the clicked feature id
                    'pinShoe' // default
                  ]
                );
                selectMapToList(element);
              } else {
                cleanSelection();
              }
            }

            function cleanSelection() {
              selectedItem = null;
              map.setLayoutProperty('points', 'icon-image', 'pinShoe');
              cleanListSelection();
            }

            function cleanListSelection() {
              const listSelected = document.querySelector(`.list-item.selected`);
              if (listSelected) {
                listSelected.classList.remove('selected');
              }
            }

            function selectMapToList(element) {
              cleanListSelection();
              const listSelected = document.querySelector(`.list-item[data-id="${element.id}"]`);
              listSelected.classList.add('selected');
              listSelected.scrollIntoView({behavior: 'smooth', block: 'nearest'});
            }

            let selectedItem;

            function updateList() {
              const features = getRenderedFeatures();
              const listItems = features.map(item => {
                return `<div class='list-item ${item.id === selectedItem ? "selected" : ""}' 
                  data-id="${item.id}" data-lnglat="${item.geometry.coordinates.join()}">
                    ${createListItemContent(item)}
                  </div>`;
              });
              const listContainer = document.querySelector('.sidebar-content-info');
              listContainer.scrollTop = 0;
              listContainer.innerHTML = listItems.join('');
            }

            function createListItemContent(item) {
              const html = [`<img src="${item.properties.photo}" alt="shoe shop">`];
              if (item.properties.name) {
                html.push(`<h2>${item.properties.name}</h2>`);  
              }
              if (item.properties.operator) {
                html.push(`<h4>${item.properties.operator}</h4>`);  
              }
              if (item.properties["addr:street"]) {
                html.push(`<div class="addr">${item.properties["addr:street"]}, ${item.properties["addr:housenumber"]}</div>`);
              }
              if (item.properties.opening_hours) {
                  html.push(`<h5>Opening hours</h5>`);
                  item.properties.opening_hours.split(",").forEach(element => {
                    html.push(`<div>${element.trim()}</div>`);
                  });
              }
              if (item.properties.phone) {
                html.push(`<div><a href="tel:${item.properties.phone}" target="_blank" rel="noopener noreferrer">${item.properties.phone}</a></div>`);
              }
              if (item.properties.website) {
                html.push(`<div><a href="${item.properties.website}" target="_blank" rel="noopener noreferrer">${item.properties.website}</a></div>`);
              }
              return html.join('');
            }

            let listContainer = document.querySelector('.sidebar-content-info');

            listContainer.addEventListener('click', (e) => {
              cleanSelection();
              const li = e.target.closest('.list-item');
              li.classList.toggle('selected');
              if (li.classList.contains('selected')) {
                selectedItem = parseInt(li.dataset.id);
                selectListToMap(li);
              }
            });

            function selectListToMap(item) {
              map.setLayoutProperty('points', 'icon-image',
                [
                  'match',
                  ['id'], // get the feature id (make sure your data has an id set or use generateIds for GeoJSON sources
                  parseInt(item.dataset.id), 'pinShoeSelected', //image when id is the clicked feature id
                  'pinShoe' // default
                ]
              );
              map.setCenter(item.dataset.lnglat.split(','));
            }
    </script>
</body>
</html>
```
