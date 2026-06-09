# Source: https://docs.maptiler.com/guides/self-hosting/map-server/how-to-work-with-map-styles-in-maptiler-server/

# How to work with map styles in MapTiler Server

Map Style is a style.JSON document that defines the visual appearance of a map. Style includes information about data sources, such as OpenMapTiles or MapTiler Planet, and the specific styling of the selected layers. All this information can be modified based on the needed purpose of the map.






We prepared **ready\-to\-use map styles** that cover most of the use cases and fit perfectly with the MapTiler data. Alternatively, you can download a third\-party map style and adjust it or create your own from scratch.


### MapTiler sample data package

To get the sample data package and learn more about it, go to [MapTiler Server sample package](/guides/self-hosting/self-hosted-maps/maptiler-data-sample-package/).

### Preview the sample data with map styles


Once you load your **map styles zip file** into the software, you will be able to preview the content of the sample data. In the **Tiles** tab, you can preview the raw osm dataset of the Zurich area. In **Maps,** you can preview that particular dataset, together with beautiful **map styles** on top of it.


The Map Styles package contains **Basic**, **Dataviz, Outdoor**, **Satellite Hybrid,** and **Streets** styles.





Bear in mind that you will be able to fully zoom ([zoom level](https://maptiler.com/google-maps-coordinates-tile-bounds-projection/#resolution-and-scales) 0 to 14 and 18\+ over zoom) only to the Zurich area, as this is the default dataset we included in the sample package. The exception here is **Satellite\-Hybrid** Map Style where the zoom levels for the whole planet are 0 to 6, with over zoom available.


### Preview other data with the map styles


If you haven't added your data to MapTiler Server yet, you can do it, by navigating to the **Tiles** tab in MapTiler Server and selecting "NEW TILES". Now drag and drop the MBtiles or Geopackage file into the software. Read more here: [How to add and host data in MapTiler Server](/guides/self-hosting/map-server/how-to-add-and-host-data-in-maptiler-server)


If you need guidance on how to download other free data we offer, read this article:   
[How to try MapTiler Server using free MapTiler data](/guides/self-hosting/map-server/getting-started)


 


Map Styles by default are attached to the Zurich dataset that is part of MapTiler sample data. If you want to connect your style.json to other datasets you can do it by using one of the following methods:


 *Change the name of Zurich Dataset to any different name \[e.g zurich\-osm] or delete it.)*  
Rename the downloaded file to "maptiler\-osm". You can do it by hitting on the "DETAIL" button of the downloaded dataset in the **Tiles** tab and then pressing "CHANGE ID".  
 *The path to finding the map styles is at the top of the "MAPS" tab in MapTiler Server).*  
Edit your favorite map style (e.g. maps → streets → style.json) and at the very bottom of the file, replace the URL of the source with the filename of the data you downloaded  
*(e.g replace `"url": "#maptiler-osm"` with  `"url": "#osm-2020-07-03-v3.6.1_europe_germany.mbtiles"` if you want this map style to serve the OSM dataset of Germany)  
*


You can now preview the dataset with your favorite map style.   
  
You might not be able to see the full value of the Map Style design as it consists of various datasets and the ones included in the free Map Style Package include data for **Zurich Area only**. To be able to download datasets in other regions, you need to [purchase the map data](https://www.maptiler.com/data/pricing/).


 





Customizing your own Map Style
------------------------------


If the Map Styles that are part of the package are not enough for you, there is a way to customize your own map style and use it in MapTiler Server. To be able to do so you need to go through the process of [customizing and exporting the map style](/guides/self-hosting/map-server/how-to-use-custom-map-styles-in-maptiler-server-export-from-cloud).
