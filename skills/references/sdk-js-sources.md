# Source: https://docs.maptiler.com/sdk-js/api/sources/

# 

  
    A **source** provides the data that is displayed on a map. Sources are defined by the [GL Style Specification](/gl-style-specification/sources/).
  

  
  ## [Vector Tile](#vector)

  [src/source/vector_tile_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/geojson_source.ts)
    A vector tile source. Tiles must be in [Vector Tile format](https://www.maptiler.com/news/2019/02/what-are-vector-tiles-and-why-you-should-care/). 
      All layers that use a vector source must specify a "source-layer" value.
      (See the [Style Specification](/gl-style-specification/sources/#vector)
      for detailed documentation of options.)
  
  Extends [Evented](/sdk-js/api/events/#evented).
  [Example](#vector-example)
  
    ```
``
```

  
  
    ```
``
```

  
  
    [Methods](#vector-instance-members)
  
  
  
    setTiles(tiles) 
              
            
    
      
          Sets the source `tiles` property and re-renders the map.
        
        [Parameters](#settiles-vector-parameters)
        
          tiles
          `([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)>)`
          An array of one or more tile source URLs, as in the TileJSON spec.
            
        [Returns](#settiles-vector-returns)
        
        
          
            [VectorTileSource](/sdk-js/api/sources/#vector)
          
        
        : 
        `this`
      
    
  
  
    setUrl(url) 
              
            
    
      
          Sets the source `url` property and re-renders the map.
        
        [Parameters](#seturl-vector-parameters)
        
          url
          `([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          A URL to a TileJSON resource. Supported protocols are http: and https:.
            
        [Returns](#seturl-vector-returns)
        
        
          
            [VectorTileSource](/sdk-js/api/sources/#vector)
          
        
        : 
        `this`
      
    
  
  [Related examples](#vector-related)
  
    [Add a vector tile source](/sdk-js/examples/vector-source/)
      
    [Add a third party vector tile source](/sdk-js/examples/third-party/)
      
  

  ## [Raster Tile](#raster)

  [src/source/raster_tile_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/raster_tile_source.ts)
    A raster tile source. Tiles must be in [ZXY](/guides/map-tiling-hosting/data-processing/tiling-scheme-in-folder-output#TilingschemeinFolderoutput-OpenGISWMTS/OpenStreetMap/GoogleXYZ/ZXY) or [TMS](/guides/map-tiling-hosting/data-processing/tiling-scheme-in-folder-output#TilingschemeinFolderoutput-OSGEOTMS) tile format.
      (See the [Style Specification](/gl-style-specification/sources/#raster)
      for detailed documentation of options.)
  
  Extends [Evented](/sdk-js/api/events/#evented).
  [Example](#raster-example)
  
    ```
``
```

  
  
    ```
``
```

  
  
    [Methods](#raster-instance-members)
  
  
  
    setTiles(tiles) 
              
            
    
      
          Sets the source `tiles` property and re-renders the map.
        
        [Parameters](#settiles-raster-parameters)
        
          tiles
          `([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)>)`
          An array of one or more tile source URLs, as in the raster tiles spec
            
        [Returns](#settiles-raster-returns)
        
        
          
            [RasterTileSource](/sdk-js/api/sources/#raster)
          
        
        : 
        `this`
      
    
  
  
    setUrl(url) 
              
            
    
      
          Sets the source `url` property and re-renders the map.
        
        [Parameters](#seturl-raster-parameters)
        
          url
          `([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          A URL to a TileJSON resource. Supported protocols are http: and https:.
            
        [Returns](#seturl-raster-returns)
        
        
          
            [RasterTileSource](/sdk-js/api/sources/#raster)
          
        
        : 
        `this`
      
    
  
  [Related examples](#raster-related)
  
    [Add a raster tile source](/sdk-js/examples/map-tiles/)
      
    [Add a WMS source](/sdk-js/examples/wms/)
      
  

  ## [GeoJSON](#geojsonsource)

  [src/source/geojson_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/geojson_source.ts#L68-L346)
    A source containing GeoJSON.
      (See the [Style Specification](/gl-style-specification/#sources-geojson)
      for detailed documentation of options.)
  
  Extends [Evented](/sdk-js/api/events/#evented).
  [Example](#geojsonsource-example)
  
    ```
``
```

  
  
    ```
``
```

  
  
    ```
``
```

  
  [Methods](#geojsonsource-instance-members)
  
    _updateWorkerData(diff?)
           
              
            
    
      
          Responsible for invoking WorkerSource's geojson.loadData target, which handles loading the geojson 
            data and preparing to serve it up as tiles, using geojson-vt or supercluster as appropriate.
        
        [Parameters](#updateworkerdata-parameters)
        diff`([GeoJSONSourceDiff](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/GeoJSONSourceDiff/))`
            The diff object
        
        callback`(Callback<[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<GeoJSON.Feature>>)`A
            callback to be called when the features are retrieved (
            `(error, features) => { ... }`
            ).
          
        [Returns](#updateworkerdata-returns)
        `Promise<void[]>`
      
    
  
  
    abortTile(tile)
           
              
            
    
      
          Allows to abort a tile loading.
        
        [Parameters](#abortTile-parameters)
        tile`([Tile](https://maplibre.org/maplibre-gl-js/docs/API/classes/Tile/))`
            The tile to abort
        
        [Returns](#abortTile-returns)
        `Promise<void[]>`
      
    
  
  
    getBounds() 
              
            
    
      
          Allows getting the source's boundaries. If there's a problem with the source's data, it will return an empty `LngLatBounds`.
        
        [Returns](#getBounds-returns)
        
          Promise<LngLatBounds>
        
        : 
        A promise which resolves to the source's boundaries.
      
    
  
  
    getClusterChildren(clusterId) 
              
            
    
      
          For clustered sources, fetches the children of the given cluster on the next zoom level (as an array of
            GeoJSON features).
        
        [Parameters](#getclusterchildren-parameters)
        clusterId`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
            The value of the cluster's `cluster_id` property.
        
        [Returns](#getclusterchildren-returns)
        
          Promise<Feature<Geometry,{ [name: string]: any; }>[]>
        
        : 
        A promise that is resolved when the features are retrieved.
      
    
  
  
    getClusterExpansionZoom(clusterId)
           
              
            
    
      
          For clustered sources, fetches the zoom at which the given cluster expands.
        
        [Parameters](#getclusterexpansionzoom-parameters)
        clusterId`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
            value of the cluster's
            `cluster_id`
            property.
          
        [Returns](#getclusterexpansionzoom-returns)
        
          Promise<number>
        
        : 
        A promise that is resolved with the zoom number.
      
    
  
  
    getClusterLeaves(clusterId, limit, offset) 
              
            
    
      
          For clustered sources, fetches the original points that belong to the cluster (as an array of GeoJSON
            features).
        
        [Parameters](#getclusterleaves-parameters)
        clusterId`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
            value of the cluster's
            `cluster_id`
            property.
          
        limit`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
            maximum number of features to return.
          
        offset`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
            number of features to skip (e.g. for pagination).
          
        [Returns](#getclusterleaves-returns)
        
          Promise<Feature<Geometry,{ [name: string]: any; }>[]>
        
        : 
        A promise that is resolved when the features are retrieved.
        [Example](#getclusterleaves-example)
        
          ```
``
```

        
      
    
  
  
    getData() 
              
            
    
      
          Allows to get the source's actual GeoJSON data.
        
        [Returns](#getData-returns) A promise which resolves to the source's actual GeoJSON data. 
            `Promise` <
        `GeoJSON` >
      
    
  
  
    hasTransition() 
              
            
    
      
          True if the source has transition, false otherwise.
        
        [Returns](#hasTransition-returns) 
            `boolean`
      
    
  
  
  
    loaded() 
              
            
    
      
          True if the source is loaded, false otherwise.
        
        [Returns](#loaded-returns) 
            `boolean`
      
    
  
  
    loadTile(tile)
           
              
            
    
      
          This method does the heavy lifting of loading a tile. In most cases it will defer the work to the relevant worker source.
        
        [Parameters](#loadTile-parameters)
        tile`([Tile](https://maplibre.org/maplibre-gl-js/docs/API/classes/Tile/))`
            The tile to load
        
        [Returns](#loadTile-returns)
        `Promise<void[]>`
      
    
  
  
    serialize()
           
              
            
    
      
          This method returns a plain (stringifiable) JS object representing the current state of the source. Creating a source using the returned object as the options should result in a Source that is equivalent to this one.
        
        [Returns](#serialize-returns)
        `GeoJSONSourceSpecification`
      
    
  
  
    setClusterOptions(options) 
              
            
    
      
          To disable/enable clustering on the source options.
        
        [Parameters](#setclusteroptions-parameters)
        options`([SetClusterOptions](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/SetClusterOptions/))`
            The options to set
        [Returns](#setclusteroptions-returns)
        `[GeoJSONSource](/sdk-js/api/sources/#geojsonsource)`:
          this
          
          [Example](#setclusteroptions-example)
        
          ```
``
```

        
      
    
  
  
    setData(data) 
              
            
    
      
          Sets the GeoJSON data and re-renders the map.
        
        [Parameters](#setdata-parameters)
        data`(([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object) | [string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)))`A
            GeoJSON data object or a URL to one. The latter is preferable in the case of large GeoJSON files.
          
        [Returns](#setdata-returns)
        `[GeoJSONSource](/sdk-js/api/sources/#geojsonsource)`:
          this
          
      
    
  
  
    unloadTile(tile)
           
              
            
    
      
          Allows to unload a tile.
        
        [Parameters](#unloadTile-parameters)
        tile`([Tile](https://maplibre.org/maplibre-gl-js/docs/API/classes/Tile/))`
            The tile to unload
        
        [Returns](#unloadTile-returns)
        `Promise<void[]>`
      
    
  
  
    updateData(diff) 
              
            
    
      
          Updates the source's GeoJSON, and re-renders the map.
          For sources with lots of features, this method can be used to make updates more quickly.
          This approach requires unique IDs for every feature in the source. 
            The IDs can either be specified on the feature, or by using the promoteId option to specify which property should be used as the ID.
          It is an error to call updateData on a source that did not have unique IDs for each of its features already.
          Updates are applied on a best-effort basis, updating an ID that does not exist will not result in an error.
        
        [Parameters](#updatedata-parameters)
        diff`([GeoJSONSourceDiff](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/GeoJSONSourceDiff/))`
            The changes that need to be applied.
        [Returns](#updatedata-returns)
        `[GeoJSONSource](/sdk-js/api/sources/#geojsonsource)`:
          this
          
      
    
  
  [Related examples](#geojsonsource-related)
  
    [Draw GeoJSON points](/sdk-js/examples/geojson-markers/)
      
    [Add a GeoJSON line](/sdk-js/examples/geojson-line/)
      
    [Create a heatmap from points](/sdk-js/examples/heatmap-layer/)
      
    [Create and style clusters](/sdk-js/examples/cluster/)
      
  

  ## [Raster DEM Tile](#raster-dem)

  [src/source/raster_dem_tile_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/raster_dem_tile_source.ts)
    A raster DEM source. Only supports [Terrain RGB format](/guides/map-tiling-hosting/data-hosting/rgb-terrain-by-maptiler).
      (See the [Style Specification](/gl-style-specification/sources/#raster-dem)
      for detailed documentation of options.)
  
  Extends [Evented](/sdk-js/api/events/#evented).
  [Example](#raster-dem-example)
  
    ```
``
```

  
  
    ```
``
```

  
  [Methods](#raster-dem-instance-members)
    
    
      setTiles(tiles) 
                
              
      
        
            Sets the source `tiles` property and re-renders the map.
          
          [Parameters](#settiles-dem-parameters)
          
            tiles
            `([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)>)`
            An array of one or more tile source URLs, as in the raster tiles spec
              
          [Returns](#settiles-dem-returns)
          
          
            
              [RasterDEMTileSource](/sdk-js/api/sources/#raster-dem)
            
          
          : 
          `this`
        
      
    
    
      setUrl(url) 
                
              
      
        
            Sets the source `url` property and re-renders the map.
          
          [Parameters](#seturl-raster-dem-parameters)
          
            url
            `([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
            A URL to a TileJSON resource. Supported protocols are http: and https:.
              
          [Returns](#seturl-raster-dem-returns)
          
          
            
              [RasterDEMTileSource](/sdk-js/api/sources/#raster-dem)
            
          
          : 
          `this`
        
      
    
  [Related examples](#raster-dem-related)
  
    [Add hillshading](/sdk-js/examples/hillshade/)
      
  

  ## [Image](#imagesource)

  [src/source/image_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/image_source.ts#L64-L274)
    A data source containing an image.
      (See the [Style Specification](/gl-style-specification/#sources-image)
      for detailed documentation of options.)
  
  Extends [Evented](/sdk-js/api/events/#evented).
  [Example](#imagesource-example)
  
    ```
``
```

  
  [Methods](#imagesource-instance-members)
      
  
    setCoordinates(coordinates) 
              
            
    
      
          Sets the image's coordinates and re-renders the map.
        
        [Parameters](#setcoordinates-image-parameters)
        coordinates`([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>>)`Four
            geographical coordinates,
            represented as arrays of longitude and latitude numbers, which define the corners of the image.
            The coordinates start at the top left corner of the image and proceed in clockwise order.
            They do not have to represent a rectangle.
          
        [Returns](#setcoordinates-image-returns)
        `[ImageSource](/sdk-js/api/sources/#imagesource)`:
          this
          
      
    
  
  
    updateImage(options) 
              
            
    
      
          Updates the image URL and, optionally, the coordinates. To avoid having the image flash after changing,
            set the `raster-fade-duration` paint property on the raster layer to 0.
        
        [Parameters](#updateimage-parameters)
        options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Options
            object.
          
          
            
| Required image URL. |
| Four geographical coordinates,                       represented as arrays of longitude and latitude numbers, which define the corners of the image.                       The coordinates start at the top left corner of the image and proceed in clockwise order.                       They do not have to represent a rectangle. |

          
        
        [Returns](#updateimage-returns)
        `[ImageSource](/sdk-js/api/sources/#imagesource)`:
          this
          
      
    
  

  ## [Video](#videosource)

  [src/source/video_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/video_source.ts#L47-L199)
    A data source containing video.
      (See the [Style Specification](/gl-style-specification/#sources-video)
      for detailed documentation of options.)
  
  Extends [ImageSource](/sdk-js/api/sources/#imagesource).
  
  [Example](#videosource-example)
  
  
    ```
``
```

  
  [Methods](#videosource-instance-members)
  
    getVideo() 
              
            
    
      
          Returns the HTML `video` element.
        
        [Returns](#getvideo-returns)
        
        `[HTMLVideoElement](https://developer.mozilla.org/docs/Web/API/HTMLVideoElement)`:
          The HTML
            `video`
            element.
          
      
    
  
  
  
    pause() 
              
            
    
      
          Pauses the video.
        
    
  
  
    play() 
              
            
    
      
          Plays the video.
        
    
  
  
    prepare() 
              
            
    
      
          Sets the video's coordinates and re-renders the map.
        
        ##### [Returns](#prepare-returns)

        
        
          [VideoSource](/sdk-js/api/sources/#videosource)
        
      
        : 
            `this`
      
    
  
  
    seek(seconds) 
              
            
    
      
          Sets playback to a timestamp, in seconds.
        
        [Parameters](#seek-parameters)
        
        seconds`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
          
        
      
    
  
  
    setCoordinates(coordinates) 
              
            
    
      
          Sets the video's coordinates and re-renders the map.
        
        [Parameters](#setcoordinates-video-parameters)
        coordinates`([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>>)`Four
            geographical coordinates,
            represented as arrays of longitude and latitude numbers, which define the corners of the image.
            The coordinates start at the top left corner of the image and proceed in clockwise order.
            They do not have to represent a rectangle.
          
        [Returns](#setcoordinates-video-returns)
        `[VideoSource](/sdk-js/api/sources/#videosource)`:
          this
          
      
    
  
  
    updateImage(options) 
              
            
    
      
          Updates the image URL and, optionally, the coordinates. To avoid having the image flash after changing,
            set the `raster-fade-duration` paint property on the raster layer
            to 0.
        
        [Parameters](#updateimage-video-parameters)
        options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Options
            object.
          
          
            
| Required image URL. |
| Four geographical coordinates,                       represented as arrays of longitude and latitude numbers, which define the corners of the                       image.                       The coordinates start at the top left corner of the image and proceed in clockwise order.                       They do not have to represent a rectangle. |

          
        
        [Returns](#updateimage-video-returns)
        `[VideoSource](/sdk-js/api/sources/#videosource)`:
          this
          
      
    
  
  Related
      examples
  
    [Add a video](/sdk-js/examples/video-on-a-map/)
      
  

  ## [Canvas](#canvassource)

  [src/source/canvas_source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/canvas_source.ts#L58-L235)
    A data source containing the contents of an HTML canvas. See [canvas source properties](#canvassource-properties) for detailed
      documentation of options.
  
  Extends [ImageSource](/sdk-js/api/sources/#imagesource).
  
  [Example](#canvassource-example)
  
    ```
``
```

  
  [Properties](#canvassource-properties)
  
| Source type. Must be `"canvas"`. |
| Canvas source from which to read pixels. Can be a string representing the ID of the canvas element, or the         `HTMLCanvasElement`         itself. |
| Four geographical coordinates denoting where to place the corners of the canvas, specified in         `[longitude, latitude]`         pairs. |
| Whether the canvas source is animated. If the canvas is static (i.e. pixels do not need to be re-read on         every frame),         `animate`         should be set to         `false`         to improve performance. |

  [Methods](#canvassource-instance-members)
  
    getCanvas() 
              
            
    
      
          Returns the HTML `canvas` element.
        
        [Returns](#getcanvas-returns)
        `[HTMLCanvasElement](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement)`:
          The HTML
            `canvas`
            element.
          
      
    
  
  
  
    pause() 
              
            
    
      
          Disables animation. The map will display a static copy of the canvas image.
        
    
  
  
    play() 
              
            
    
      
          Enables animation. The image will be copied from the canvas to the map on each frame.
        
    
  
  
    setCoordinates(coordinates) 
              
            
    
      
          Sets the video's coordinates and re-renders the map.
        
        [Parameters](#setcoordinates-parameters)
      coordinates`([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>>)`Four
          geographical coordinates,
          represented as arrays of longitude and latitude numbers, which define the corners of the image.
          The coordinates start at the top left corner of the image and proceed in clockwise order.
          They do not have to represent a rectangle.
        
        [Returns](#setcoordinates-returns)
        `[CanvasSource](/sdk-js/api/sources/#canvassource)`:
          this
          
      
    
  
  
    updateImage(options) 
              
            
    
      
          Updates the image URL and, optionally, the coordinates. To avoid having the image flash after changing,
            set the `raster-fade-duration` paint property on the raster layer to 0.
        
        [Parameters](#updateimage-image-parameters)
        options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Options
            object.
          
          
            
| Required image URL. |
| Four geographical coordinates,                       represented as arrays of longitude and latitude numbers, which define the corners of the image.                       The coordinates start at the top left corner of the image and proceed in clockwise order.                       They do not have to represent a rectangle. |

          
        
        [Returns](#updateimage-image-returns)
        `[CanvasSource](/sdk-js/api/sources/#canvassource)`:
          this
