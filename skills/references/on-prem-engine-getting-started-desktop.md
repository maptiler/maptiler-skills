# Source: https://docs.maptiler.com/guides/map-tiling-hosting/data-processing/getting-started/

# Get started with MapTiler Engine

This friendly beginner guide helps you install MapTiler Engine and create your first map tileset from a sample drone image. We'll explain briefly what's happening at every step, so that you understand how MapTiler Engine works.

At the end of the tutorial, you'll have the sample drone image tiled, georeferenced, and saved on your local drive (optionally also in MapTiler) in a special map-ready format. You'll get a preview of the result and learn what to do next. 

Here are the steps we'll go through:

1. [Install MapTiler Engine](#install)
2. [Download a sample image](#sample-image)
3. [Georeference the image](#georeference)
4. [Set tiling parameters](#parameters)
5. [Preview the result](#result)
6. [Next steps](#next-steps)

-----

<a name="install"></a>
## Install MapTiler Engine

1. Go to the [Engine download page](https://www.maptiler.com/engine/download/){:target="_blank" rel="noopener"} and select the installation package for your operating system. 

2. Install and run MapTiler Engine. Note that MapTiler Engine will be a new and unknown application to your system, so you may need to handle some security pop-ups in the process. Get more information in the detailed installation guides: 

     - [Windows](/guides/map-tiling-hosting/data-processing/installation-on-windows/)
     - [Linux (via Docker)](/guides/map-tiling-hosting/data-processing/maptiler-engine-in-docker/)

<a name="sample-image"></a>
## Download a sample image

We’ll show you the tiling process using a drone image of the Moturiki Island in New Zealand. It’s a regular JPG, without any geospatial metadata attached to it. 

> [!NOTE]
> Processing an image with MapTiler Engine is called **raster tiling**. MapTiler Engine can also process other types of data, but images are the easiest type to start with.

1. <a href="./moturiki_island.jpg" download>Download the sample image here.</a> <!-- Image by Look Up Look Down Photography under the Unsplash license. -->

2. Run MapTiler Engine and open the sample image in it. You can either drag and drop the file in the dashed line area, or use the button.

     

<a name="georeference"></a>
## Georeference the image

Georeferencing is the process of assigning coordinates to an object (in this case a drone image). Geospatial coordinates determine the object's position on Earth, and so make it possible to display the object on a map.

1. When you upload the image, you’re asked to specify its geographical location. There are multiple options to provide this information, but most require that you already know the coordinates or have them ready in a file. We don't have that, so we’ll **assign location visually** using the georeferencer tool.

     

     To use the visual georeferencer, you’ll need to log in to MapTiler. If you don’t have an account, you get a sign-up screen to create one instantly—it’s free and with no obligations.

    > [!NOTE]
    > You need to log in just once. MapTiler Engine will remember your details and keep you logged in for next time. 

2. Visual georeferencer opens. First, let's switch the basemap to a more suitable one. Use the little **globe button** to open the basemap selector.

     

3. Select the satellite map to use it as the georeferencer basemap. This will help you identify the drone image location more easily.

     

4. Now, use the **search button** to find the right area on the map. For our sample image, look up "Mount Maunganui" in the Bay of Plenty, New Zealand. 

     

5. Moturiki is a small island located at the end of the city beach. Zoom in until you see the narrow pathway connecting the island with the beach—this is the area captured on our sample drone image.

     

6. You're now ready to georeference the image. How to do it: Click on a spot in the image and then on the same spot on the map (or vice versa). This creates a point with the corresponding location in the image and on the map. You can position the point precisely thanks to the optical sight which appears on click.

    > [!IDEA]
    > To make the task easier, place the point in a visually distinctive spot, such as a path crossing or a prominent rock formation.

     

8. Repeat the previous step in different parts of the image to get at least three points (more is better). Place them as accurately as possible. If you make a mistake, just click on a point to reposition or remove it.

     With the third point placed, the image rotates to match the orientation of the map. Add a few more points for accuracy and continue to the next step. 

     

<a name="parameters"></a>
## Set tiling parameters

1. When you close the visual georeferencer, you'll see an overview of the image setup. Keep the default values and continue. 

     

2. On the next screen, select the output format **GeoPackage**. This will be the format of the whole tileset container (which is different from the format of the individual tiles inside). 

     You can learn more about the [output formats](/guides/map-tiling-hosting/data-processing/folder-vs-mbtiles-vs-geopackage/){:target="_blank" rel="noopener"} but it's not necessary for this tutorial.

     

3. The output settings let you set up the format of the tiles (images within the tileset) and related details. MapTiler Engine pre-fills this screen based on an analysis of the input data, so you should always get good results if you keep the recommended values. The only change you need to do here: Select the **Non-commercial use** checkbox (unless you're already using a paid MapTiler Engine license).

     

4. Select where to save the tiling output on your local machine.

5. Select where to upload the tiling output. (This doesn't affect the local output set in the previous step. You always get local output, no matter if you decide to also upload to cloud or not.) We recommend uploading to MapTiler where your tileset will be conveniently ready for further work and testing. 

     

6. In the last configuration step, you can edit the filename for the cloud upload. When the processing is done, you'll find your new tileset under that name in your MapTiler account.

     

<a name="result"></a>
## Preview the result

1. After MapTiler Engine guides you through all the settings, it automatically starts processing the file. You can watch the progress on screen. The sample image shouldn't take more than a few minutes to process.

     

2. When the processing is complete, go to the **Options** menu and select **Output preview**. 

     

3. In the preview, MapTiler Engine shows your new tileset on top of a basemap. This gives you an idea of what your image might look like when integrated into an actual map. Try zooming and panning to see how the map will behave. You can also adjust transparency with the slider to see how accurately you’ve positioned the image and how well it blends with the basemap. 

     
 
Closing the preview takes you back to the finished task. All key functions are accessible from the **Options** menu, so be sure to explore it. From there, you can view a simple task report, open the location where your tileset is stored (on the local drive and in MapTiler), save the task settings for backup, or edit the task and run it again. 

<a name="next-steps"></a>
## Next steps

**Proceed to adding your new tiles to a map:** Now that you have your tileset ready [in MapTiler](https://cloud.maptiler.com/tiles/){:target="_blank" rel="noopener"}, you can easily integrate it into a real map. 👉 Learn [how to use your image as part of a map](/guides/map-tiling-hosting/data-hosting/how-to-host-your-own-geodata/#use-your-image-as-part-of-the-map). 

If you prefer to self-host your tiles and maps, you'll want to check out [MapTiler Server](/guides/self-hosting/map-server/).

**Keep exploring Engine:** MapTiler Engine can process more than just images. 👉 Find out [what is vector data](/guides/map-tiling-hosting/data-processing/vector-feature/) and [how to tile it](/guides/map-tiling-hosting/data-processing/how-to-create-tiles-from-vector-data/).

> [!IDEA]
> Ready for full speed? See what features and benefits you can unlock with a MapTiler Engine [commercial license](https://www.maptiler.com/engine/pricing/).
