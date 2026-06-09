# Source: https://docs.maptiler.com/sdk-js/api/map/

# 

  
    
    [ src/Map.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Map.ts)
  

  
      The `Map` object represents the map on your page. It exposes methods
        and properties that enable you to programmatically change the map,
        and fires events as users interact with it.
      You create a `Map` by specifying a `container` and other options.
        Then SDK JS initializes the map on the page and returns your `Map`
        object.
    
    Extends [Evented](/sdk-js/api/events/#evented).
    Example
    ```
``
```

    ## [Parameters](#map-parameters)

    
      options (MapOptions) 
                
              
      
        
          Options to provide to the Map constructor
          ([MapOptions](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Map.ts))

          [Properties](#map-options)
          
            
| Define the [MapTiler API key](https://cloud.maptiler.com/account/keys/) to be used.           This is equivalent to setting `config.apiKey` and will overwrite it. |
| The HTML element in which SDK JS will render the map, or           the element's string           `id`           . The specified element must have no children. |
| The map's style. This must be:                        ReferenceMapStyle (e.g. MapStyle.STREETS)             MapStyleVariant (e.g. MapStyle.STREETS.DARK)             MapTIler Style ID (e.g. “”)             uuid of custom style             an a JSON object               conforming to               the schema described in the               [GL Style Specification](/gl-style-specification/)                          a URL to               such JSON. |
| Define the language of the map. This can be done directly with a language ISO code (eg. "en")           or with a built-in [Languages](/sdk-js/api/languages/) shorthand (eg. Language.ENGLISH)           This applies only for the map instance, supersedes the `config.primaryLanguage`. |
| The initial geographical centerpoint of the map. If           `center`           is not specified in the constructor options, SDKJS will look for it in the map's style           object. If it is not specified in the style, either, it will default to           `[0, 0]`           Note: SDK JS uses longitude, latitude coordinate order (as opposed to latitude, longitude) to           match GeoJSON. |
| The initial zoom level of the map. If           `zoom`           is not specified in the constructor options, SDK JS will look for it in the map's style           object. If it is not specified in the style, either, it will default to           `0`           . |
| This will overwrite the projection property from the style (if any) and           will persist it later if the map style was to change.            Valid options are           `mercator`           ,           `globe`           . |
| The initial bearing (rotation) of the map, measured in degrees           counter-clockwise from north. If           `bearing`           is not specified in the constructor options, SDK JS will look for it in the map's style           object. If it is not specified in the style, either, it will default to           `0`           . |
| The initial pitch (tilt) of the map, measured in degrees away           from the plane of the screen (0-85). If           `pitch`           is not specified in the constructor options, SDK JS will look for it in the map's style           object. If it is not specified in the style, either, it will default to           `0`           . Values greater than 60 degrees are experimental and may result in rendering issues. If you encounter           any, please raise an issue with details in the MapLibre project. |
| If           `true`           , an           [AttributionControl](/sdk-js/api/controls/#attributioncontrol)           will be added to the map. |
| The threshold, measured in degrees, that determines when the           map's           bearing will snap to north. For example, with a           `bearingSnap`           of 7, if the user rotates           the map within 7 degrees of north, the map will automatically snap to exact north. |
| The initial bounds of the map. If           `bounds`           is specified, it overrides           `center`           and           `zoom`           constructor options. |
| If           `true`           , the "box zoom" interaction is enabled (see           [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler)           ). |
| Determines whether to cancel, or retain, tiles from the current viewport           which are still loading           but which belong to a farther (smaller) zoom level than the current one.           If `true`, when zooming in, tiles which didn't manage to load for           previous zoom levels will become canceled.           This might save some computing resources for slower devices, but the map details might appear more abruptly at           the end of the zoom.           If `false`, when zooming in, the previous zoom level(s) tiles will           progressively appear, giving a smoother map details experience.           However, more tiles will be rendered in a short period of time. |
| Set of WebGLContextAttributes that are applied to the WebGL context of           the map.           See [getContext](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext) for           more details.           `contextType`, can be set to           `webgl2` or `webgl` to force a           WebGL version.           Not setting it, MapTiler SDK will do it's best to get a suitable context. |
| If `true`, the elevation of the center point will           automatically be set to the terrain elevation (or zero if terrain is not enabled).           If `false`, the elevation of the center point will           default to sea level and will not automatically update.                        Needs to be set to false to keep the camera above ground when pitch > 90 degrees. |
| The max number of pixels a user can shift the mouse pointer           during a click for it to be considered a valid click (as opposed to a mouse drag). |
| If           `true`           , Resource Timing API information will be collected for requests made by GeoJSON and Vector Tile web           workers (this information is normally inaccessible from the main Javascript thread). Information will           be returned in a           `resourceTiming`           property of relevant           `data`           events. |
| If           `true`           or set to an options object, map is only accessible on desktop while holding Command/Ctrl and only           accessible on mobile with two fingers. Interacting with the map using normal gestures will trigger an           informational screen. With this option enabled, "drag to pitch" requires a three-finger gesture.           Cooperative gestures are disabled when a map enters fullscreen using [FullscreenControl](/sdk-js/api/controls/#fullscreencontrol).           A valid options object includes the following properties to customize the text on the informational           screen. The values below are the defaults.           ```javascript            {           windowsHelpText: "Use Ctrl + scroll to zoom the map",           macHelpText: "Use ⌘ + scroll to zoom the map",           mobileHelpText: "Use two fingers to move the map",           }            ``` |
| If           `true`           , symbols from multiple sources can collide with each other during collision detection. If           `false`           , collision detection is run separately for the symbols in each source. |
| Detect custom external controls.         Alternatively, customControls can be set to a **CSS selector string**, restricting autodetection to:                        Elements matching the selector directly             Or elements whose **ancestor** matches the selector                      ```javascript        const map = new maptilersdk.Map({         container: "map",         customControls: true, // or ".custom-ui"       });          ``` |
| If           `true`           , the "double click to zoom" interaction is enabled (see           [DoubleClickZoomHandler](/sdk-js/api/handlers/#doubleclickzoomhandler)           ). |
| If           `true`           , the "drag to pan" interaction is enabled. An           `Object`           value is passed as options to           [DragPanHandler#enable](/sdk-js/api/handlers/#dragpanhandler#enable)           . |
| If           `true`           , the "drag to rotate" interaction is enabled (see           [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler)           ). |
| The elevation of the initial geographical centerpoint of the map, in           meters above sea level.           If `elevation` is not specified in the constructor options,           it will default to `0`. |
| Controls the duration of the fade-in/fade-out animation for           label collisions, in milliseconds. This setting affects all symbol layers. This setting does not           affect the duration of runtime styling transitions or raster tile cross-fading. |
| A           [Map#fitBounds](/sdk-js/api/map/#map#fitbounds)           options object to use           *only*           when fitting the initial           `bounds`           provided above. |
| If           `true`           , an           [FullscreenControl](/sdk-js/api/controls/#fullscreencontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| Center map on the visitor's location by using the [IP geolocation API](https://docs.maptiler.com/cloud/api/geolocation/). There are two strategies:                                       `GeolocationType.POINT`:               centering the map on the actual visitor location, optionnaly using the zoom option               (zoom level 13 if none is provided). As a more precise option, if the user has previously granted access               to the browser location (more precise)               then this is going to be used.                                         `GeolocationType.COUNTRY`:               fitting the map view on the bounding box of the visitor's country. In this case, the zoom option, if               provided, will be ignored                                   The `geolocate` options will not be taken into consideration in the           following cases:                                       if the `center` options is provided, then it prevails                                         if the `hash` options is provided with the value `true` **AND** a location hash is already part of the URL.               If hash is true but there is not yet a location hash in the URL, then the geolocation will work. |
| If           `true`           , an           [MaptilerGeolocateControl](/sdk-js/api/controls/#maptilergeolocatecontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| If           `true`           , the map's position (zoom, center latitude, center longitude, bearing, and pitch) will be synced with           the hash fragment of the page's URL.           For example,           `http://path/to/my/page.html#2.59/39.26/53.07/-24.1/60`           .           An additional string may optionally be provided to indicate a parameter-styled hash,           e.g.           [http://path/to/my/page.html#map=2.59/39.26/53.07/-24.1/60&foo=bar](http://path/to/my/page.html#map=2.59/39.26/53.07/-24.1/60&foo=bar)           , where foo           is a custom parameter and bar is an arbitrary hash distinct from the map hash. |
| If           `false`           , no mouse, touch, or keyboard listeners will be attached to the map, so it will not respond to           interaction. |
| If           `true`           , keyboard shortcuts are enabled (see           [KeyboardHandler](/sdk-js/api/handlers/#keyboardhandler)           ). |
| A patch to apply to the default localization table for UI           strings, e.g. control tooltips. The           `locale`           object maps namespaced UI string IDs to translated strings in the target language; see           `src/ui/default_locale.js`           for an example with all supported string IDs. The object may specify all UI strings (thereby adding           support for a new translation) or only a subset of strings (thereby patching the default translation           table). |
| Defines a CSS           font-family for locally overriding generation of glyphs in the 'CJK Unified Ideographs', 'Hiragana',           'Katakana' and 'Hangul Syllables' ranges.           In these ranges, font settings from the map's style will be ignored, except for font-weight keywords           (light/regular/medium/bold).           Set to           `false`           , to enable font settings from the map's style for these glyph ranges.           The purpose of this option is to avoid bandwidth-intensive glyph server requests. (See           Use locally generated             ideographs           .) |
| A string representing the position of the MapTiler wordmark on           the map. Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| **This setting doesn't apply to free plans.** On paid plans,         the logo is hidden by default.         To show it, add this option and set it to `true`. |
| If set, the map will be constrained to the given bounds. |
| The canvas' `width`           and `height` max size.           The values are passed as an array where the first element is max width and the second element is max height.           You shouldn't set this above WebGl `MAX_TEXTURE_SIZE` |
| The maximum pitch of the map (0-180). |
| The maximum number of tiles stored in the tile cache for a given           source. If omitted, the cache will be dynamically sized based on the current viewport. |
| The maximum number of zoom levels for which to store tiles for a given           source.           Tile cache dynamic size is calculated by multiplying `maxTileCacheZoomLevels`           with the approximate number of tiles in the viewport for a given source. |
| The maximum zoom level of the map (0-24). |
| If           `true`           , an           [MaptilerMinimapControl](/sdk-js/api/controls/#maptilerminimapcontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           .            or [MinimapOptionsInput](/sdk-js/api/controls/#maptilerminimapcontrol-parameters) |
| The minimum pitch of the map (0-85). Values greater than 60           degrees are experimental and may result in rendering issues. If you encounter any, please raise an           issue with details in the MapLibre project. |
| The minimum zoom level of the map (0-24). |
| If           `true`           , an           [MaptilerNavigationControl](/sdk-js/api/controls/#maptilernavigationcontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| If           `false`           , the map's pitch (tilt) control with "drag to rotate" interaction will be disabled. |
| The pixel ratio. The canvas'           `width`           attribute will be           `container.clientWidth * pixelRatio`           and its           `height`           attribute will be           `container.clientHeight * pixelRatio`           . Defaults to           `devicePixelRatio`           if not specified. |
| If           `true`           , an           [MaptilerProjectionControl](/sdk-js/api/controls/#MaptilerProjectionControl)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| If           `false`           , the map won't attempt to re-request tiles once they expire per their HTTP           `cacheControl`           /           `expires`           headers. |
| If           `true`           , multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude. If           set to           `false`           :                        When the map is zoomed out far enough that a single representation of the world does not fill               the map's entire               container, there will be blank space beyond 180 and -180 degrees longitude.             Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on the               right edge of the               map and the other on the left edge of the map) at every zoom level. |
| The initial roll angle of the map, measured in degrees counter-clockwise           about the camera boresight.           If `roll` is not specified in the constructor options, MapTiler SDK           will look for it in the map's style object.           If it is not specified in the style, either, it will default to `0`. |
| If `false`, the map's roll control with "drag to rotate" interaction           will be disabled. |
| If           `true`           , an           [ScaleControl](/sdk-js/api/controls/#scalecontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| If           `true`           , the "scroll to zoom" interaction is enabled. An           `Object`           value is passed as options to           [ScrollZoomHandler#enable](/sdk-js/api/handlers/#scrollzoomhandler#enable)           . |
| The space option allows customizing the background environment of the globe, simulating deep space or skybox           effects.           You can enable a start space background by setting it to `true`.           For more customization, check [CubemapLayerConstructorOptions](/sdk-js/api/types/#CubemapLayerConstructorOptions)                  This option **only takes effect** when used in conjunction with the `projection: 'globe'` parameter. |
| If           `true`           , the map's loads a 3D terrain, based on a MapTiler "raster-dem"             source. |
| If           `true`           , an           [MaptilerTerrainControl](/sdk-js/api/controls/#maptilerterraincontrol)           will be added to the map.            Valid options are           `top-left`           ,           `top-right`           ,           `bottom-left`           ,           `bottom-right`           . |
| 3D terrain exaggeration factor. |
| If           `true`           , the "drag to pitch" interaction is enabled. An           `Object`           value is passed as options to           [TouchPitchHandler#enable](/sdk-js/api/handlers/#touchpitchhandler#enable)           . |
| If           `true`           , the "pinch to rotate and zoom" interaction is enabled. An           `Object`           value is passed as options to           [TouchZoomRotateHandler#enable](/sdk-js/api/handlers/#touchzoomrotatehandler#enable)           . |
| If           `true`           , the map will automatically resize when the browser window resizes. |
| A callback run before the map's           camera is moved due to user input or animation.           The callback can be used to modify the new center, zoom, pitch and bearing.           Expected to return an object containing center, zoom, pitch or bearing values to overwrite. |
| A callback run before the Map makes a request for an external           URL. The callback can be used to modify the url, set headers, or set the credentials property for           cross-origin requests.           Expected to return an object with a           `url`           property and optionally           `headers`           and           `credentials`           properties.                  Example                    ``` `` ``` |
| If `false`, style validation will be skipped.           Useful in production environment. |

          
        
      
    

    [Methods](#map-instance-members)

  addControl(control,
          position?) 
            
          
  
    
        Adds an [IControl](/sdk-js/api/controls/#icontrol) to the map, calling
          `control.onAdd(this)`.
        
      
      [Parameters](#addcontrol-parameters)
      
        control
        ([`IControl`](/sdk-js/api/controls/#icontrol))
        : The
          [IControl](/sdk-js/api/controls/#icontrol)
          to add.
        
      
      
        position
        (`string`?)
        : position
          on the map to which the control will be added.
          Valid values are
          `'top-left'`
          ,
          `'top-right'`
          ,
          `'bottom-left'`
          , and
          `'bottom-right'`
          . Defaults to
          `'top-right'`
          .
        
      
      [Returns](#addcontrol-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#addcontrol-example)
      
        ```
``
```

      
      [Related examples](#addcontrol-related)
      
        Display map navigation
              controls
          
      
    
  

  addImage(id, image, options) 
            
          
  
    
        Add an image to the style. This image can be displayed on the map like any other icon in the style's
          sprite using the image's ID with
          `icon-image`,
          `background-pattern`,
          `fill-pattern`,
          or `line-pattern`.
          A [Map.event:error](/sdk-js/api/map/#map.event:error) event will be fired if there
          is not enough space in the sprite to add this image.
        
      
      [Parameters](#addimage-parameters)
      
        id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        : The
          ID of the image.
        
      
      image
        ((`HTMLImageElement` |
          `ImageBitmap` |
          `ImageData` |
          {width: `number`,
          height: `number`,
          data: (`Uint8Array` |
          `Uint8ClampedArray`)} |
          `StyleImageInterface`))
        : The
          image as an
          `HTMLImageElement`
          ,
          `ImageData`
          ,
          `ImageBitmap`
          or object with
          `width`
          ,
          `height`
          , and
          `data`

          properties with the same format as
          `ImageData`
          .
        
      
      options
        `(Partial<StyleImageMetadata>)`
        : Options object. Defaults to `{}`
        
          
| The ratio of pixels in the image to physical pixels on the                     screen |
| Whether the image should be interpreted as an SDF image |
| `[[x1, x2], ...]`                     If                     `icon-text-fit`                     is used in a layer with this image, this option defines the part(s) of the image that can be                     stretched horizontally. |
| `[[y1, y2], ...]`                     If                     `icon-text-fit`                     is used in a layer with this image, this option defines the part(s) of the image that can be                     stretched vertically. |
| `[x1, y1, x2, y2]`                     If                     `icon-text-fit`                     is used in a layer with this image, this option defines the part of the image that can be                     covered by the content in                     `text-field`                     . |

        
      
      [Example](#addimage-example)
      
        ```
``
```

      
      [Related examples](#addimage-related)
      
        Use
            `HTMLImageElement`
            :
            [Add an icon to the map](/sdk-js/examples/add-image/)
          
        Use
            `ImageData`
            :
            Add a generated icon to
              the map
          
      
    
  

  addLayer(layer, beforeId?) 
            
          
  
    
        Adds a [GL style layer](/gl-style-specification/#layers)
          to the map's style.
        A layer defines how data from a specified source will be styled. Read more about layer types
          and available paint and layout properties in the GL Style
            Specification.
      
      [Parameters](#addlayer-parameters)
      
        layer
        (`Object`)
        : conforming
          to either the GL Style Specification's
          [layer definition](/gl-style-specification/#layers)
          or,
          less commonly, the
          [CustomLayerInterface](/sdk-js/api/properties/#customlayerinterface)
          specification.
          The GL Style Specification's layer definition is appropriate for most layers.
        
        
          
| A unique identifer that you define. |
| The type of layer (for example                     `fill`                     or                     `symbol`                     ).                     A list of layer types is available in the                     GL Style                       Specification                     .                     (This can also be `custom`. For more information, see                       [CustomLayerInterface](/sdk-js/api/properties/#customlayerinterface).) |
| The data source for the layer.                     Reference a source that has                     *already been defined*                     using the source's unique id.                     Reference a                     *new source*                     using a source object (as defined in the                     GL Style                       Specification                     ) directly.                     This is                     **required**                     for all                     `layer.type`                     options                     *except*                     for                     `custom`                     and                     `background`                     . |
| (optional) The name of the source layer within the                     specified                     `layer.source`                     to use for this style layer.                     This is only applicable for vector tile sources and is                     **required**                     when                     `layer.source`                     is of the type                     `vector`                     . |
| (optional) An expression specifying conditions on source                     features.                     Only features that match the filter are displayed.                     The GL Style Specification includes more information on the limitations of the                     [`filter`](/gl-style-specification/layers/#filter)                     parameter                     and a complete list of available                     [expressions](/gl-style-specification/expressions/)                     .                     If no filter is provided, all features in the source (or source layer for vector tilesets) will                     be displayed. |
| (optional) Paint properties for the layer.                     Available paint properties vary by                     `layer.type`                     .                     A full list of paint properties for each layer type is available in the                     GL Style                       Specification                     .                     If no paint properties are specified, default values will be used. |
| (optional) Layout properties for the layer.                     Available layout properties vary by                     `layer.type`                     .                     A full list of layout properties for each layer type is available in the                     GL Style                       Specification                     .                     If no layout properties are specified, default values will be used. |
| (optional) The maximum zoom level for the layer.                     At zoom levels equal to or greater than the maxzoom, the layer will be hidden.                     The value can be any number between                     `0`                     and                     `24`                     (inclusive).                     If no maxzoom is provided, the layer will be visible at all zoom levels for which there are                     tiles available. |
| (optional) The minimum zoom level for the layer.                     At zoom levels less than the minzoom, the layer will be hidden.                     The value can be any number between                     `0`                     and                     `24`                     (inclusive).                     If no minzoom is provided, the layer will be visible at all zoom levels for which there are                     tiles available. |
| (optional) Arbitrary properties useful to track with the                     layer, but do not influence rendering. |
| This is only applicable for layers with the type                     `custom`                     .                     See                     [CustomLayerInterface](/sdk-js/api/properties/#customlayerinterface)                     for more information. |

        
      
      beforeId
        (`string`?)
        : The
          ID of an existing layer to insert the new layer before,
          resulting in the new layer appearing visually beneath the existing layer.
          If this argument is not specified, the layer will be appended to the end of the layers array
          and appear visually above all other layers.
        
      
      [Returns](#addlayer-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#addlayer-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#addlayer-related)
      
      
        [Create and style clusters](/sdk-js/examples/cluster/)
          
        Add a vector tile
              source
          
        [Add a WMS source](/sdk-js/examples/wms/)
          
      
    
  

  addSource(id, source) 
            
          
  
    
        Adds a source to the map's style.
      
      [Parameters](#addsource-parameters)
      id
        (`string`)
        : The
          ID of the source to add. Must not conflict with existing sources.
        
      
      source
        (`Object`)
        : The
          source object, conforming to the
          GL Style Specification's
          [source definition](/gl-style-specification/#sources)
          or

          [CanvasSourceOptions](/sdk-js/api/sources/#canvassourceoptions)
          .
        
      
      [Returns](#addsource-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#addsource-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#addsource-related)
      
      
        GeoJSON source:
            [Add live realtime data](/sdk-js/examples/live-geojson/)
          
      
    
  

  addSprite(id, url, options?) 
            
          
  
    
        Adds a sprite to the map's style. Fires the `style` event.
      
      [Parameters](#addsprite-parameters)
      id
        (`string`)
        : The ID of the sprite to add. Must not conflict with existing sprites.
        
      
      url
        (`string`)
        : The URL to load the sprite from.
        
      
      options
        (`StyleSetterOptions`)
        : Options object.
        
      
      [Returns](#addsprite-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#addsprite-example)
      
      
        ```
``
```

      
    
  

  areTilesLoaded() 
            
          
  
    
        Returns a Boolean indicating whether all tiles in the viewport from all sources on
          the style are loaded.
      
      [Returns](#aretilesloaded-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether all tiles are loaded.
        
      [Example](#aretilesloaded-example)
      
        ```
``
```

      
    
  

  boxZoom 
            
          
  
    
        The map's [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler), which
          implements zooming using a drag gesture with the Shift key pressed.
          Find more details and examples using `boxZoom` in the [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler) section.
      
  

  calculateCameraOptionsFromCameraLngLatAltRotation(cameraLngLat, cameraAlt, bearing, pitch, roll) 
            
          
  
    
        Given a camera position and rotation, calculates zoom and center point and returns them as as Cameraoptions.
        
      
      [Parameters](#calculateCameraOptionsFromCameraLngLatAltRotation-parameters)
      cameraLngLat
        (`LngLatLike`)
        : The lng, lat of the camera to look from
        
      
      cameraAlt
        (`number`)
        : The altitude of the camera to look from, in meters above sea level
        
      
      bearing
        (`number`)
        : Bearing of the camera, in degrees
        
      
      pitch
        (`number`)
        : Pitch of the camera, in degrees
        
      
      roll
        (`number`?)
        : Roll of the camera, in degrees
        
      
      [Returns](#calculateCameraOptionsFromCameraLngLatAltRotation-returns)
      `[CameraOptions](/sdk-js/api/properties/#cameraoptions)`:
        the calculated camera options
        
    
  

  calculateCameraOptionsFromTo(from,
          altitudeFrom, to, altitudeTo) 
            
          
  
    
        Calculates pitch, zoom and bearing for looking at @param newCenter with the camera position being @param
          newCenter
          and returns them as Cameraoptions.
      
      [Parameters](#calculatecameraoptionsfromto-parameters)
      from
        ([`LngLat`](/sdk-js/api/geography/#lnglat))
        : The
          camera to look from
        
      
      altitudeFrom
        (`number`)
        : The
          altitude of the camera to look from
        
      
      to
        ([`LngLat`](/sdk-js/api/geography/#lnglat))
        : The
          center to look at
        
      
      altitudeTo
        (`number`)
        : Optional altitude of the center to look at. If none
          given the ground height
          will be used. Defaults to
          `0`
        
      
      [Returns](#calculatecameraoptionsfromto-returns)
      `[CameraOptions](/sdk-js/api/properties/#cameraoptions)`:
        the calculated camera options
        
    
  

  cameraForBounds(bounds,
          options?) 
            
          
  
    
      [Parameters](#cameraforbounds-parameters)
      bounds`([LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike))`Calculate
          the center for these bounds in the viewport and use
          the highest zoom level up to and including
          `Map#getMaxZoom()`
          that fits
          in the viewport. LngLatBounds represent a box that is always axis-aligned with bearing 0.
        
      options`(CameraForBoundsOptions?)`Options
          object
        
        
          
| The amount of padding in pixels to add to the given                     bounds. |
| Desired map bearing at end of animation, in degrees. |
| The center of the given bounds relative to the map's                     center, measured in pixels. |
| The maximum zoom level to allow when the camera would                     transition to the specified bounds. |

        
      
      [Returns](#cameraforbounds-returns)
      `CenterZoomBearing`:
        If map is able to fit to provided bounds, returns
          `center`
          ,
          `zoom`
          , and
          `bearing`
          .
          If map is unable to fit, method will warn and return undefined.
        
      [Example](#cameraforbounds-example)
      
      
        ```
``
```

      
    
  

  centerOnIpPoint(zoom)
        
          
        
         
            
          
  
    
        Centering the map on the actual visitor location. Used when geolocate is to POINT but could be triggered
          manually.
        
        As a more precise option, if the user has previously granted access to the browser location (more precise)
          then this is going to be used.
      
      [Parameters](#centeronippoint-parameters)
      zoom`([number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          zoom level to set.
        
      [Returns](#centeronippoint-returns)
      `[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`:
        `void`
        
      [Example](#centeronippoint-example)
      
      
        ```
``
```

      
    
  

  cooperativeGestures 
            
          
  
    
        The map's [CooperativeGesturesHandler](/sdk-js/api/handlers/#cooperativegestureshandler),
          which allows the user to see cooperative gesture info when user tries to zoom in/out.
          Find more details and examples using `cooperativeGestures` in the [CooperativeGesturesHandler](/sdk-js/api/handlers/#cooperativegestureshandler) section.
      
  

  disableTerrain()
        
          
        
         
            
          
  
    
        Disable the 3D terrain visualization.
        
      
      [Example](#disableterrain-example)
      
        ```
``
```

      
    
  

  disableHaloAnimations()
        
          
        
         
            
          
  
    
        Disable transitions between halo states, making it change instantly.
        
      
      [Example](#disablehaloanimations-example)
      
        ```
``
```

      
    
  

  disableSpaceAnimations()
        
          
        
         
            
          
  
    
        Disable transitions between space colors and backgrounds, making them change instantly (or as soon as the
          images have loaded)
        
      
      [Example](#disablespaceanimations-example)
      
        ```
``
```

      
    
  

  doubleClickZoom 
            
          
  
    
        The map's [DoubleClickZoomHandler](/sdk-js/api/handlers/#doubleclickzoomhandler),
          which allows the user to zoom by double clicking.
          Find more details and examples using `doubleClickZoom` in the [DoubleClickZoomHandler](/sdk-js/api/handlers/#doubleclickzoomhandler) section.
      
  

  dragPan 
            
          
  
    
        The map's [DragPanHandler](/sdk-js/api/handlers/#dragpanhandler), which
          implements dragging the map with a mouse or touch gesture.
          Find more details and examples using `dragPan` in the [DragPanHandler](/sdk-js/api/handlers/#dragpanhandler) section.
      
  

  dragRotate 
            
          
  
    
        The map's [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler), which
          implements rotating the map while dragging with the right
          mouse button or with the Control key pressed. Find more details and examples using `dragRotate`
          in the [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler) section.
      
  

  easeTo(options, eventData?) 
            
          
  
    
        Changes any combination of `center`, `zoom`, `bearing`,
          `pitch`, and `padding` with an
          animated transition
          between old and new values. The map will retain its current values for any
          details not specified in `options`.
        
        Note: The transition will happen instantly if the user has enabled
          the `reduced motion` accesibility feature enabled in their operating
          system,
          unless `options` includes `essential: true`.
      
      [Parameters](#easeto-parameters)
      options`(any)`Options
          describing the destination and animation of the transition.
          Accepts
          [CameraOptions](/sdk-js/api/properties/#cameraoptions)
          and
          [AnimationOptions](/sdk-js/api/properties/#animationoptions)
          .
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#easeto-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Related examples](#easeto-related)
      
      
        Navigate the map with
              game-like controls
          
      
    
  

  enableHaloAnimations()
        
          
        
         
            
          
  
    
        Enable transitions between halo states, making it transition between states (on by default).
        
      
      [Example](#enablehaloanimations-example)
      
        ```
``
```

      
    
  

  enableSpaceAnimations()
        
          
        
         
            
          
  
    
        Enable transitions between space colors and backgrounds, making them transition between colours and images.
        
      
      [Example](#enablespaceanimations-example)
      
        ```
``
```

      
    
  

  enableTerrain(exaggeration?)
        
          
        
         
            
          
  
    
        Enables the 3D terrain visualization.
        
      
      [Parameters](#enableterrain-parameters)
      exaggeration`([number?](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
        Enables the 3D terrain visualization and sets the terrain exaggeration factor
        
      
      [Example](#enableterrain-example)
      
        ```
``
```

      
    
  

  fitBounds(bounds, options?,
          eventData?) 
            
          
  
    
        Pans and zooms the map to contain its visible area within the specified geographical bounds.
          This function will also reset the map's bearing to 0 if bearing is nonzero.
      
      [Parameters](#fitbounds-parameters)
      bounds`([LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike))`Center
          these bounds in the viewport and use the highest
          zoom level up to and including
          `Map#getMaxZoom()`
          that fits them in the viewport.
        
      options`(FitBoundsOptions?)`Options supports
          all properties from
          [AnimationOptions](/sdk-js/api/properties/#animationoptions)
          and
          [CameraOptions](/sdk-js/api/properties/#cameraoptions)
          in addition to the fields below.
        
        
          
| The amount of padding in pixels to add to the given                     bounds. |
| If                     `true`                     , the map transitions using                      [Map#easeTo](/sdk-js/api/map/#map#easeto)                     . If                     `false`                     , the map transitions using                     [Map#flyTo](/sdk-js/api/map/#map#flyto)                     . See                     those functions and                     [AnimationOptions](/sdk-js/api/properties/#animationoptions)                     for information about options available. |
| An easing function for the animated transition. See                     [AnimationOptions](/sdk-js/api/properties/#animationoptions)                     . |
| The center of the given bounds relative to the map's                     center, measured in pixels. |
| The maximum zoom level to allow when the map view                     transitions to the specified bounds. |

        
      
      eventData`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Additional
          properties to be added to event objects of events triggered by this method.
        
      [Returns](#fitbounds-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#fitbounds-example)
      
      
        ```
``
```

      
      [Related examples](#fitbounds-related)
      
      
        Fit a map to a bounding
              box
          
      
    
  

  fitScreenCoordinates(p0, p1, bearing,
          options?, eventData?) 
            
          
  
    
        Pans, rotates and zooms the map to to fit the box made by points p0 and p1
          once the map is rotated to the specified bearing. To zoom without rotating,
          pass in the current map bearing.
      
      [Parameters](#fitscreencoordinates-parameters)
      p0`([PointLike](/sdk-js/api/geography/#pointlike))`First
          point on screen, in pixel coordinates
        
      p1`([PointLike](/sdk-js/api/geography/#pointlike))`Second
          point on screen, in pixel coordinates
        
      bearing`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`Desired
          map bearing at end of animation, in degrees
        
      options`(FitBoundsOptions?)`Options object
        
        
          
| The amount of padding in pixels to add to the given                     bounds. |
| If                     `true`                     , the map transitions using                      [Map#easeTo](/sdk-js/api/map/#map#easeto)                     . If                     `false`                     , the map transitions using                     [Map#flyTo](/sdk-js/api/map/#map#flyto)                     . See                     those functions and                     [AnimationOptions](/sdk-js/api/properties/#animationoptions)                     for information about options available. |
| An easing function for the animated transition. See                     [AnimationOptions](/sdk-js/api/properties/#animationoptions)                     . |
| The center of the given bounds relative to the map's                     center, measured in pixels. |
| The maximum zoom level to allow when the map view                     transitions to the specified bounds. |

        
      
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#fitscreencoordinates-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#fitscreencoordinates-example)
      
        ```
``
```

      
      [Related examples](#fitscreencoordinates-related)
      
        Used by
            [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler)
          
      
    
  

  fitToIpBounds()
        
          
        
         
            
          
  
    
        Fit the map view on the bounding box of the visitor's country. Used when geolocate is to COUNTRY but could be
          triggered manually.
        
      
      [Returns](#fittoipbounds-returns)
      `[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`:
        `void`
        
      [Example](#fittoipbounds-example)
      
        ```
``
```

      
    
  

  flyTo(options, eventData?) 
            
          
  
    
        Changes any combination of center, zoom, bearing, and pitch, animating the transition along a curve that
          evokes flight. The animation seamlessly incorporates zooming and panning to help
          the user maintain her bearings even after traversing a great distance.
        Note: The animation will be skipped, and this will behave equivalently to `jumpTo`
          if the user has the `reduced motion` accesibility feature enabled in
          their operating system,
          unless 'options' includes `essential: true`.
      
      [Parameters](#flyto-parameters)
      
      options`(FlyToOptions)`Options describing the
          destination and animation of the transition.
          Accepts
          [CameraOptions](/sdk-js/api/properties/#cameraoptions)
          ,
          [AnimationOptions](/sdk-js/api/properties/#animationoptions)
          ,
          and the following additional options.
        
        
          
| The zooming "curve" that will occur along the                     flight path. A high value maximizes zooming for an exaggerated animation, while a low                     value minimizes zooming for an effect closer to                     [Map#easeTo](/sdk-js/api/map/#map#easeto)                     . 1.42 is the average                     value selected by participants in the user study discussed in                      [van Wijk (2003)](https://www.win.tue.nl/~vanwijk/zoompan.pdf)                     . A value of                      `Math.pow(6, 0.25)`                     would be equivalent to the root mean squared average velocity. A                     value of 1 would produce a circular motion. |
| The zero-based zoom level at the peak of the flight path.                     If                      `options.curve`                     is specified, this option is ignored. |
| The average speed of the animation defined in relation to                      `options.curve`                     . A speed of 1.2 means that the map appears to move along the flight path                     by 1.2 times                     `options.curve`                     screenfuls every second. A                     *screenful*                     is the map's visible span.                     It does not correspond to a fixed physical distance, but varies by zoom level. |
| The average speed of the animation measured in screenfuls                     per second, assuming a linear timing curve. If                     `options.speed`                     is specified, this option is ignored. |
| The animation's maximum duration, measured in                     milliseconds.                     If duration exceeds maximum duration, it resets to 0. |

        
      
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#flyto-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#flyto-example)
      
      
        ```
``
```

      
      [Related examples](#flyto-related)
      
      
        [Fly to a location](/sdk-js/examples/flyto/)
          
        Slowly fly to a
              location
          
        Fly to a location based
              on scroll position
          
      
    
  

  getBearing() 
            
          
  
    
        Returns the map's current bearing. The bearing is the compass direction that is "up"; for example, a
          bearing
          of 90° orients the map so that east is up.
      
      [Returns](#getbearing-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The map's current bearing.
        
      [Related examples](#getbearing-related)
      
        Navigate the map with
              game-like controls
          
      
    
  

  getBounds() 
            
          
  
    
        Returns the map's geographical bounds. When the bearing or pitch is non-zero, the visible region is not
          an axis-aligned rectangle, and the result is the smallest bounds that encompasses the visible region.
      
      [Returns](#getbounds-returns)
      
      `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
        The geographical bounds of the map as
          [LngLatBounds](/sdk-js/api/geography/#lnglatbounds)
          .
        
      [Example](#getbounds-example)
      
      
        ```
``
```

      
    
  

  getCameraHash()
        
          
        
         
            
          
  
    
        Compute a base64 string hash that is unique for camera settings (to check if a user a moved in the process of
          geolocation)
        
      
      [Returns](#getcamerahash-returns)
      `[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)`:
      The camera hash base64 string.
      
      [Example](#getcamerahash-example)
      
        ```
``
```

      
    
  

  getCameraTargetElevation()
        
          
        
         
            
          
  
    
        Returns the elevation for the point where the camera is looking. This value corresponds to: "meters above sea
          level" * "exaggeration"
        
      
      [Returns](#getcameratargetelevation-returns)
      `[number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
      The elevation.
      
      [Example](#getcameratargetelevation-example)
      
        ```
``
```

      
    
  

  getCanvas() 
            
          
  
    
        Returns the map's `<canvas>` element.
      
      [Returns](#getcanvas-returns)
      
      `[HTMLCanvasElement](https://developer.mozilla.org/docs/Web/API/HTMLCanvasElement)`:
        The map's
          `<canvas>`
          element.
        
      [Related examples](#getcanvas-related)
      
      
        [Measure distances](/sdk-js/examples/measure/)
          
        Display a popup on
              hover
          
        Center the map on a
              clicked symbol
          
      
    
  

  getCanvasContainer() 
            
          
  
    
        Returns the HTML element containing the map's `<canvas>`
          element.
        If you want to add non-GL overlays to the map, you should append them to this element.
        This is the element to which event bindings for map interactivity (such as panning and zooming) are
          attached. It will receive bubbled events from child elements such as the `<canvas>`, but
          not from
          map controls.
      
      [Returns](#getcanvascontainer-returns)
      `[HTMLElement](https://developer.mozilla.org/docs/Web/HTML/Element)`:
        The container of the map's
          `<canvas>`
          .
        
      Related
          examples
      
        Create a draggable
              point
          
      
    
  

  getCenter() 
            
          
  
    
        Returns the map's geographical centerpoint.
      
      [Returns](#getcenter-returns)
      
      `[LngLat](/sdk-js/api/geography/#lnglat)`:
        The
          map's geographical centerpoint.
        
      [Example](#getcenter-example)
      
      
        ```
``
```

      
    
  

  getCenterClampedToGround() 
            
          
  
    
        Returns the value of `centerClampedToGround`.
        If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if
          terrain is not enabled). If false, the elevation of the center point will default to sea level and will not
          automatically update. Defaults to true. Needs to be set to false to keep the camera above ground when pitch >
          90 degrees.
      
      [Returns](#getCenterClampedToGround-returns)
      
      `boolean`
    
  

  getCenterElevation() 
            
          
  
    
        Returns the elevation of the map's center point.
      
      [Returns](#getCenterElevation-returns)
      
      `number`: The elevation of the map's center point, in meters above sea
        level.

      
    
  

  getContainer() 
            
          
  
    
        Returns the map's containing HTML element.
      
      [Returns](#getcontainer-returns)
      `[HTMLElement](https://developer.mozilla.org/docs/Web/HTML/Element)`:
        The map's container.
        
    
  

  getFeatureState(feature) 
            
          
  
    
        Gets the `state` of a feature.
          A feature's `state` is a set of user-defined key-value pairs that
          are assigned to a feature at
          runtime.
          Features are identified by their `feature.id` attribute, which can
          be any number or string.
        Note: To access the values in a feature's state object for the purposes of styling the feature, use
            the `feature-state`
              expression.
      
      [Parameters](#getfeaturestate-parameters)
      feature`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Feature
          identifier. Feature objects returned from

          [Map#queryRenderedFeatures](/sdk-js/api/map/#map#queryrenderedfeatures)
          or event handlers can be used as feature identifiers.
        
        
          
| Unique id of the feature. |
| The id of the vector or GeoJSON source for the feature. |
| (optional)                     For vector tile sources, `sourceLayer` is                       required. |

        
      
      [Returns](#getfeaturestate-returns)
      
      `[Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)`:
        The state of the feature: a set of key-value pairs that was assigned to the feature at runtime.
        
      [Example](#getfeaturestate-example)
      
      
        ```
``
```

      
    
  

  getFilter(layerId) 
            
          
  
    
        Returns the filter applied to the specified style layer.
      
      [Parameters](#getfilter-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the style layer whose filter to get.
        
      [Returns](#getfilter-returns)
      
      `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)`:
        The layer's filter.
        
    
  

  getGlobalState() 
            
          
  
    
        Returns the global map state.
      
      [Returns](#getGlobalState-returns)
      
      `Record<string, any>`:
      The map state object.
    
  

  getGlyphs(layerId) 
            
          
  
    
        Returns the filter applied to the specified style layer.
      
      [Returns](#getglyphs-returns)
      
      `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`:
        The glyphs Style's glyphs url.
        
    
  

  getHalo()
        
          
        
         
            
          
  
    
        Returns the map's halo (atmospheric glow) of the globe.
      
      [Returns](#gethalo-returns)
      
      `([RadialGradientLayer](/sdk-js/api/types/#RadialGradientLayer) | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined))`:
        Halo (atmospheric glow) of the globe or `undefined` if the halo was
          not set in the map.
        
      
      [Example](#gethalo-example)
      
      
        ```
``
```

      
    
  

  getImage(id) 
            
          
  
    
        Returns an image, specified by ID, currently available in the map.
          This includes both images from the style's original sprite and any
          images that have been added at runtime using addImage.
      
      [Parameters](#getimage-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          The ID of the image.
        
      [Returns](#getimage-returns)
      `StyleImage`: An image in the map with the
          specified ID.
        
      [Example](#getimage-example)
      
      
        ```
``
```

      
    
  

  getLayer(id) 
            
          
  
    
        Returns the layer with the specified ID in the map's style.
      
      [Parameters](#getlayer-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to get.
        
      [Returns](#getlayer-returns)
      `StyleLayer`: The layer with
          the specified ID, or
          `undefined`

          if the ID corresponds to no existing layers.
        
      [Example](#getlayer-example)
      
      
        ```
``
```

      
      [Related examples](#getlayer-related)
      
      
        Filter symbols by
              toggling a list
          
        Filter symbols
              by text input
          
      
    
  

  getLayersOrder() 
            
          
  
    
        Return the ids of all layers currently in the style, including custom layers, in order.
      
      [Returns](#getLayersOrder-returns)
      `string[]`: ids of layers, in
          order.
      [Example](#getLayersOrder-example)
      
      
        ```
``
```

      
    
  

  getLayoutProperty(layerId,
          name) 
            
          
  
    
        Returns the value of a layout property in the specified style layer.
      
      [Parameters](#getlayoutproperty-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to get the layout property from.
        
      name`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          name of the layout property to get.
        
      [Returns](#getlayoutproperty-returns)`any`: The value of
          the specified layout property.
        
    
  

  getLight() 
            
          
  
    
        Returns the value of the light object.
      
      [Returns](#getlight-returns)
      
      `[Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)`:
        light Light properties of the style.
        
    
  

  getMaptilerSessionId()
        
          
        
         
            
          
  
    
        Get the MapTiler session ID. Convenient to dispatch to externaly built component that
          do not directly have access to the SDK configuration but do have access to a Map instance.
      
      [Returns](#getmaptilersessionid-returns)`string`: the
          MapTiler session ID
        
      [Example](#getmaptilersessionid-example)
      
        ```
``
```

      
    
  

  getMaxBounds() 
            
          
  
    
        Returns the maximum geographical bounds the map is constrained to, or `null` if none set.
      
      [Returns](#getmaxbounds-returns)
      `([LngLatBounds](/sdk-js/api/geography/#lnglatbounds) | null)`:
        The map object.
        
      [Example](#getmaxbounds-example)
      
        ```
``
```

      
    
  

  getMaxPitch() 
            
          
  
    
        Returns the map's maximum allowable pitch.
      
      [Returns](#getmaxpitch-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        maxPitch
        
    
  

  getMaxZoom() 
            
          
  
    
        Returns the map's maximum allowable zoom level.
      
      [Returns](#getmaxzoom-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        maxZoom
        
      [Example](#getmaxzoom-example)
      
        ```
``
```

      
    
  

  getMinPitch() 
            
          
  
    
        Returns the map's minimum allowable pitch.
      
      [Returns](#getminpitch-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        minPitch
        
    
  

  getMinZoom() 
            
          
  
    
        Returns the map's minimum allowable zoom level.
      
      [Returns](#getminzoom-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        minZoom
        
      [Example](#getminzoom-example)
      
        ```
``
```

      
    
  

  getPadding() 
            
          
  
    
        Returns the current padding applied around the map viewport.
      
      [Returns](#getpadding-returns)
      `[PaddingOptions](/sdk-js/api/properties/#paddingoptions)`:
        The current padding around the map viewport.
        
    
  

  getPaintProperty(layerId,
          name) 
            
          
  
    
        Returns the value of a paint property in the specified style layer.
      
      [Parameters](#getpaintproperty-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to get the paint property from.
        
      name`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          name of a paint property to get.
        
      [Returns](#getpaintproperty-returns)
      `any`: The value of
          the specified paint property.
        
    
  

  getPitch() 
            
          
  
    
        Returns the map's current pitch (tilt).
      
      [Returns](#getpitch-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The map's current pitch, measured in degrees away from the plane of the screen.
        
    
  

  getPixelRatio() 
            
          
  
    
        Returns the map's pixel ratio.
      
      [Returns](#getpixelratio-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The pixel ratio.
        
    
  

  getProjection() 
            
          
  
    
        Gets the [ProjectionSpecification](/gl-style-specification/projection)
      
      [Returns](#getProjection-returns)
      `[ProjectionSpecification](/gl-style-specification/projection)`:
        the projection specification.
      [Example](#getProjection-example)
      
      
        ```
``
```

      
    
  

  getRenderWorldCopies() 
            
          
  
    
        Returns the state of `renderWorldCopies`. If `true`, multiple copies of the world
          will be rendered side by side beyond -180 and 180 degrees longitude. If set to `false`:
        
          When the map is zoomed out far enough that a single representation of the world does not fill the
            map's entire
            container, there will be blank space beyond 180 and -180 degrees longitude.
          Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on the right
            edge of the
            map and the other on the left edge of the map) at every zoom level.
        
      
      [Returns](#getrenderworldcopies-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        renderWorldCopies
        
      [Example](#getrenderworldcopies-example)
      
        ```
``
```

      
      [Related examples](#getrenderworldcopies-related)
      
        Render world
              copies
          
      
    
  

  getRoll() 
            
          
  
    
        Returns the map's current roll angle.
      
      [Returns](#getRoll-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The map's current roll, measured in degrees about the camera boresight.
        
      [Example](#getRoll-example)
      
        ```
``
```

      
    
  

  getSdkConfig()
        
          
        
         
            
          
  
    
        Get the SDK config object. This is convenient to dispatch the SDK configuration to externally built layers
          that
          do not directly have access to the SDK configuration but do have access to a Map instance.
      
      [Returns](#getsdkconfig-returns)`config`: the
          [SDK config object](/sdk-js/api/config/)
        
      [Example](#getsdkconfig-example)
      
        ```
``
```

      
    
  

  getSky() 
            
          
  
    
        Returns the value of the style's sky.
      
      [Returns](#getSky-returns)
      `SkySpecification`:
        the sky properties of the style.
        
      [Example](#getSky-example)
      
        ```
``
```

      
    
  

  getSource(id) 
            
          
  
    
        Returns the source with the specified ID in the map's style.
        This method is often used to update a source using the instance members for the relevant
          source type as defined in [Sources](#sources).
          For example, setting the `data` for a GeoJSON source or updating the
          `url` and
          `coordinates`
          of an image source.
        
      
      [Parameters](#getsource-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the source to get.
        
      [Returns](#getsource-returns)
      
      `(Source | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined))`:
        The style source with the specified ID or
          `undefined`
          if the ID
          corresponds to no existing sources.
          The shape of the object varies by source type.
          A list of options for each source type is available on the GL Style Specification's

          [Sources](/gl-style-specification/sources/)
          page.
        
      [Example](#getsource-example)
      
      
        ```
``
```

      
      [Related examples](#getsource-related)
      
      
        Create a draggable
              point
          
        Animate a
              point
          
        Add live realtime
              data
          
      
    
  

  getSpace()
        
          
        
         
            
          
  
    
        Returns the map's space (background environment) of the globe.
      
      [Returns](#getspace-returns)
      
      `([CubemapLayer](/sdk-js/api/types/#CubemapLayer) | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined))`:
        Space (background environment) of the globe or `undefined` if the
          space was not set in the map.
        
      
      [Example](#getspace-example)
      
      
        ```
``
```

      
    
  

  getSprite() 
            
          
  
    
        Returns the map's GL style object, a JSON object which can be used to recreate the map's style.
      
      [Returns](#getsprite-returns)
      
      `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)`:
        Style's sprite list of id-url pairs.
        
        ``
      
      [Example](#getsprite-example)
      
      
        ```
``
```

      
    
  

  getStyle() 
            
          
  
    
        Returns the map's GL style object, a JSON object which can be used to recreate the map's style.
      
      [Returns](#getstyle-returns)
      
      `[Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)`:
        The map's style JSON object.
        
      [Example](#getstyle-example)
      
      
        ```
``
```

      
    
  

  getTerrain() 
            
          
  
    
        Get the terrain-options if terrain is loaded
      
      [Returns](#getterrain-returns)`TerrainSpecification`: the
          TerrainSpecification passed to setTerrain
        
      [Example](#getterrain-example)
      
        ```
``
```

      
    
  

  getTerrainExaggeration()
        
          
        
         
            
          
  
    
        Get the terrain exaggeration factor if terrain is loaded
      
      [Returns](#getterrainexaggeration-returns)`number`: the
          terrain exaggeration factor
        
      [Example](#getterrainexaggeration-example)
      
        ```
``
```

      
    
  

  getVerticalFieldOfView()
         
            
          
  
    
        Returns the map's current vertical field of view, in degrees.
      
      [Returns](#getVerticalFieldOfView-returns)`number`: The map's current vertical field of view.
         Default Value: `36.87`
      [Example](#getVerticalFieldOfView-example)
      
        ```
``
```

      
    
  

  getZoom() 
            
          
  
    
        Returns the map's current zoom level.
      
      [Returns](#getzoom-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The map's current zoom level.
        
      [Example](#getzoom-example)
      
        ```
``
```

      
    
  

  hasControl(control) 
            
          
  
    
        Checks if a control exists on the map.
      
      [Parameters](#hascontrol-parameters)
      control`([IControl](/sdk-js/api/controls/#icontrol))`The
          [IControl](/sdk-js/api/controls/#icontrol)
          to check.
        
      [Returns](#hascontrol-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True if map contains control.
        
      [Example](#hascontrol-example)
      
        ```
``
```

      
    
  

  hasImage(id) 
            
          
  
    
        Check whether or not an image with a specific ID exists in the style. This checks both images
          in the style's original sprite and any images
          that have been added at runtime using [Map#addImage](/sdk-js/api/map/#map#addimage).
      
      [Parameters](#hasimage-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the image.
        
      [Returns](#hasimage-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether the image exists.
        
      [Example](#hasimage-example)
      
      
        ```
``
```

      
    
  

  hasTerrain()
        
          
        
         
            
          
  
    
        Check whether or not the terrian is enabled.
      
      [Returns](#hasterrain-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether the terrain exists.
        
      [Example](#hasterrain-example)
      
      
        ```
``
```

      
    
  

  isGlobeProjection()
        
          
        
         
            
          
  
    
        Returns whether a globe projection is currently being used.
      
      [Returns](#isGlobeProjection-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True if the map projection is globe.
        
      [Example](#isGlobeProjection-example)
      
      
        ```
``
```

      
    
  

  isLanguageUpdated()
        
          
        
         
            
          
  
    
        Returns `true` is the language was ever updated, meaning changed from
          what is delivered in the style.
          Returns `false` if language in use is the language from the style and
          has never been changed.
        
      
      [Returns](#isLanguageUpdated-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True is the language was ever updated.
        
      [Example](#isLanguageUpdated-example)
      
      
        ```
``
```

      
    
  

  isMoving() 
            
          
  
    
        Returns true if the map is panning, zooming, rotating, or pitching due to a camera animation or user
          gesture.
      
      [Returns](#ismoving-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True if the map is moving.
        
      [Example](#ismoving-example)
      
      
        ```
``
```

      
    
  

  isRotating() 
            
          
  
    
        Returns true if the map is rotating due to a camera animation or user gesture.
      
      [Returns](#isrotating-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True if the map is rotating.
        
      [Example](#isrotating-example)
      
        ```
``
```

      
    
  

  isSourceLoaded(id) 
            
          
  
    
        Returns a Boolean indicating whether the source is loaded. Returns `true` if the source with
          the given ID in the map's style has no outstanding network requests, otherwise `false`.
      
      [Parameters](#issourceloaded-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the source to be checked.
        
      [Returns](#issourceloaded-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether the source is loaded.
        
      [Example](#issourceloaded-example)
      
        ```
``
```

      
    
  

  isStyleLoaded() 
            
          
  
    
        Returns a Boolean indicating whether the map's style is fully loaded.
      
      [Returns](#isstyleloaded-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether the style is fully loaded.
        
      [Example](#isstyleloaded-example)
      
        ```
``
```

      
    
  

  isZooming() 
            
          
  
    
        Returns true if the map is zooming due to a camera animation or user gesture.
      
      [Returns](#iszooming-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        True if the map is zooming.
        
      [Example](#iszooming-example)
      
      
        ```
``
```

      
    
  

  jumpTo(options, eventData?) 
            
          
  
    
        Changes any combination of center, zoom, bearing, and pitch, without
          an animated transition. The map will retain its current values for any
          details not specified in `options`.
      
      [Parameters](#jumpto-parameters)
      options`(JumpToOptions)`Options object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#jumpto-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#jumpto-example)
      
      
        ```
``
```

      
      [Related examples](#jumpto-related)
      
      
        Jump to a series of
              locations
          
        Update a feature
              in realtime
          
      
    
  

  keyboard 
            
          
  
    
        The map's [KeyboardHandler](/sdk-js/api/handlers/#keyboardhandler), which allows
          the user to zoom, rotate, and pan the map using keyboard
          shortcuts. Find more details and examples using `keyboard` in the [KeyboardHandler](/sdk-js/api/handlers/#keyboardhandler) section.
      
  

  listens(type) 
            
          
  
    
        Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the
          specified type.
      
      [Parameters](#listens-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          The event type.
        
      [Returns](#listens-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        `true` if there is at least one registered listener
          for specified event type, `false` otherwise
        
    
  

  listImages() 
            
          
  
    
        Returns an Array of strings containing the IDs of all images currently available in the map.
          This includes both images from the style's original sprite
          and any images that have been added at runtime using [Map#addImage](/sdk-js/api/map/#map#addimage).
        
      
      [Returns](#listimages-returns)
      `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)>`:
        An Array of strings containing the names of all sprites/images currently available in the map.
        
      [Example](#listimages-example)
      
        ```
``
```

      
    
  

  loaded() 
            
          
  
    
        Returns a Boolean indicating whether the map is fully loaded.
        Returns `false` if the style is not yet fully loaded,
          or if there has been a change to the sources or style that
          has not yet fully loaded.
      
      [Returns](#loaded-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        A Boolean indicating whether the map is fully loaded.
        
    
  

  loadImage(url) 
            
          
  
    
        Load an image from an external URL to be used with [Map#addImage](/sdk-js/api/map/#map#addimage).
          External
          domains must support [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).
        
      
      [Parameters](#loadimage-parameters)
      url`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          URL of the image file. Image file must be in png, webp, or jpg format.
        
      [Returns](#loadimage-returns)
      
      `Promise<GetResourceResponse<ImageBitmap | HTMLImageElement>>`:
        A promise that is resolved when the image is loaded.
        
      [Example](#loadimage-example)
      
      
        ```
``
```

      
      [Related examples](#loadimage-related)
      
      
        [Add an icon to the map](/sdk-js/examples/add-image/)
          
      
    
  

  moveLayer(id, beforeId?) 
            
          
  
    
        Moves a layer to a different z-position.
      
      [Parameters](#movelayer-parameters)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to move.
        
      beforeId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)?)`The
          ID of an existing layer to insert the new layer before. When viewing the map, the
          `id`
          layer will appear beneath the
          `beforeId`
          layer. If
          `beforeId`
          is omitted, the layer will be appended to the end of the layers array and appear above all other layers on
          the map.
        
      [Returns](#movelayer-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#movelayer-example)
      
      
        ```
``
```

      
    
  

  off(type, layer, listener) 
            
          
  
    
        Removes an event listener for layer-specific events previously added with `Map#on`. See [Map Events](#map-events) for a full list of events
          and their description.
      
      [Parameters](#off-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          event type previously used to install the listener.
        
      layer`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          layer ID or listener previously used to install the listener.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function previously installed as a listener.
        
      [Returns](#off-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  off(type, layerIds,
          listener) 
            
          
  
    
        Overload of the `off` method that allows to listen to events specifying
          multiple layers.
      
      [Parameters](#off3-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          event type previously used to install the listener.
        
      layerIds`([string[]](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        The array of style layer IDs or listener previously used to install the listener.
        
      
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function previously installed as a listener.
        
      [Returns](#off3-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  off(type, listener) 
            
          
  
    
        Overload of the `off` method that allows to listen to events without
          specifying a layer.
      
      See [Map off method](#map#off) for parameters, returns, and other descriptions.
    
  

  on(type, layer, listener) 
            
          
  
    
        Adds a listener for events of a specified type, optionally limited to features in a specified style
          layer. See [Map Events](#map-events) for a full list of events and their description.
      
      [Parameters](#on-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        The
          event type to listen for. Events compatible with the optional
          `layerIds`
          parameter are triggered
          when the cursor enters a visible portion of the specified layer from outside that layer or outside the map
          canvas.
        
      
      layerIds`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of a style layer. Event will only be triggered if its location
          is within a visible feature in this layer. The event will have a
          `features`
          property containing
          an array of the matching features. If
          `layer`
          is not supplied, the event will not have a
          `features`
          property.
          Please note that many event types are not compatible with the optional
          `layer`
          parameter.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function to be called when the event is fired.
        
      [Returns](#on-returns)
      [`Subscription`](/sdk-js/api/types/#Subscription)
      [Example](#on-example)
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#on-related)
      
        Display popup on
              click
          
        Center the map on a
              clicked symbol
          
        [Create a hover effect](/sdk-js/examples/hover-styles/)
          
        Create a draggable
              marker
          
      
    
  

  on(type, layerIds, listener) 
            
          
  
    
        Overload of the `on` method that allows to listen to events specifying
          multiple layers.
      
      [Parameters](#on3-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        The
          event type to listen for. Events compatible with the optional
          `layerIds`
          parameter are triggered
          when the cursor enters a visible portion of the specified layer from outside that layer or outside the map
          canvas.
        
      
      layerIds`([string[]](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        The array of style layer IDs. Event will only be triggered if its location
          is within a visible feature in this layer. The event will have a
          `features`
          property containing
          an array of the matching features. If
          `layer`
          is not supplied, the event will not have a
          `features`
          property.
          Please note that many event types are not compatible with the optional
          `layer`
          parameter.
        
      
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function to be called when the event is fired.
        
      [Returns](#on3-returns)
      [`Subscription`](/sdk-js/api/types/#Subscription)
      [Example](#on3-example)
      
        ```
``
```

      
    
  

  on(type, listener) 
            
          
  
    
        Overload of the `on` method that allows to listen to events without
          specifying a layer.
      
      See [Map on method](#map#on) for parameters, returns, and other descriptions.
    
  

  once(type, layer, listener) 
            
          
  
    
        Adds a listener that will be called only once to a specified event type occurring on features in a
          specified style layer. See [Map Events](#map-events) for a full list of events and their
          description.
      
      [Parameters](#once-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          event type to listen for; one of
          `'mousedown'`
          ,
          `'mouseup'`
          ,
          `'click'`
          ,
          `'dblclick'`
          ,

          `'mousemove'`
          ,
          `'mouseenter'`
          ,
          `'mouseleave'`
          ,
          `'mouseover'`
          ,
          `'mouseout'`
          ,
          `'contextmenu'`
          ,
          `'touchstart'`
          ,

          `'touchend'`
          , or
          `'touchcancel'`
          .
          `mouseenter`
          and
          `mouseover`
          events are triggered when the cursor enters
          a visible portion of the specified layer from outside that layer or outside the map canvas.
          `mouseleave`

          and
          `mouseout`
          events are triggered when the cursor leaves a visible portion of the specified layer, or leaves
          the map canvas.
        
      layer`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of a style layer. Only events whose location is within a visible
          feature in this layer will trigger the listener. The event will have a
          `features`
          property containing
          an array of the matching features.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function to be called when the event is fired.
        
      [Returns](#once-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
    
  

  once(type, layerIds,
          listener) 
            
          
  
    
        Overload of the `once` method that allows to listen to events
          specifying multiple layers.
      
      [Parameters](#once3-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          event type to listen for; one of
          `'mousedown'`
          ,
          `'mouseup'`
          ,
          `'click'`
          ,
          `'dblclick'`
          ,

          `'mousemove'`
          ,
          `'mouseenter'`
          ,
          `'mouseleave'`
          ,
          `'mouseover'`
          ,
          `'mouseout'`
          ,
          `'contextmenu'`
          ,
          `'touchstart'`
          ,

          `'touchend'`
          , or
          `'touchcancel'`
          .
          `mouseenter`
          and
          `mouseover`
          events are triggered when the cursor enters
          a visible portion of the specified layer from outside that layer or outside the map canvas.
          `mouseleave`

          and
          `mouseout`
          events are triggered when the cursor leaves a visible portion of the specified layer, or leaves
          the map canvas.
        
      layerIds`([string[]](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
        The array of style layer IDs. Only events whose location is within a visible
          feature in this layer will trigger the listener. The event will have a
          `features`
          property containing
          an array of the matching features.
        
      
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function to be called when the event is fired.
        
      [Returns](#once3-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
    
  

  once(type, listener) 
            
          
  
    
        Overload of the `once` method that allows to listen to events without
          specifying a layer.
      
      See [Map once method](#map#once) for parameters, returns, and other descriptions.
    
  

  onLoadAsync()
        
          
        
         
            
          
  
    
        Awaits for the Map instance to be "loaded" and returns a Promise to the Map.
        If the Map instance is already loaded, the Promise is resolved directly, otherwise, it is resolved as a
          result of the "load" event.
      
      [Returns](#onLoadAsync-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#onLoadAsync-example)
      
      
        ```
``
```

      
    
  

  onLoadWithTerrainAsync()
        
          
        
         
            
          
  
    
        Awaits for the Map instance to be "loaded" as well as with terrain being non-null for the first time and
          returns a Promise to the Map.
        If the Map instance is already loaded with terrain, the Promise is resolved directly, otherwise, it is
          resolved as a result of the "loadWithTerrain" event.
      
      [Returns](#onLoadWithTerrainAsync-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#onLoadWithTerrainAsync-example)
      
      
        ```
``
```

      
    
  

  onReadyAsync()
        
          
        
         
            
          
  
    
        Awaits for the Map instance to be "ready" and returns a Promise to the Map.
        If the Map instance is already loaded, the Promise is resolved directly, otherwise, it is resolved as a
          result of the "ready" event.
      
      [Returns](#onReadyAsync-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#onReadyAsync-example)
      
      
        ```
``
```

      
    
  

  panBy(offset, options?,
          eventData?) 
            
          
  
    
        Pans the map by the specified offset.
      
      [Parameters](#panby-parameters)
      
      offset`([PointLike](/sdk-js/api/geography/#pointlike))``x`
          and
          `y`
          coordinates by which to pan the map.
        
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#panby-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Related examples](#panby-related)
      
      
        Navigate the map with
              game-like controls
          
      
    
  

  panTo(lnglat, options?,
          eventData?) 
            
          
  
    
        Pans the map to the specified location with an animated transition.
      
      [Parameters](#panto-parameters)
      
      lnglat`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`The
          location to pan the map to.
        
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          describing the destination and animation of the transition.
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#panto-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#panto-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#panto-related)
      
      
        Update a feature
              in realtime
          
      
    
  

  project(lnglat) 
            
          
  
    
        Returns a [Point](https://github.com/mapbox/point-geometry) representing pixel coordinates,
          relative to the map's `container`,
          that correspond to the specified geographical location.
      
      [Parameters](#project-parameters)
      lnglat`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`The
          geographical location to project.
        
      [Returns](#project-returns)
      `Point`:
        The
          [Point](https://github.com/mapbox/point-geometry)
          corresponding to
          `lnglat`
          , relative to the map's
          `container`
          .
        
      [Example](#project-example)
      
        ```
``
```

      
    
  

  queryRenderedFeatures(geometry?,
          options?) 
            
          
  
    
        Returns an array of MapGeoJSONFeature objects
          representing visible features that satisfy the query parameters.
      
      [Parameters](#queryrenderedfeatures-parameters)
      geometry`(([PointLike](/sdk-js/api/geography/#pointlike) | [Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[PointLike](/sdk-js/api/geography/#pointlike)>)?)`The
          geometry of the query region:
          either a single point or southwest and northeast points describing a bounding box.
          Omitting this parameter (i.e. calling
          [Map#queryRenderedFeatures](/sdk-js/api/map/#map#queryrenderedfeatures)
          with zero arguments,
          or with only a
          `options`
          argument) is equivalent to passing a bounding box encompassing the entire
          map viewport.
        
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
          object.
        
        
          
| An array of                     [style layer IDs](/gl-style-specification/#layer-id)                     for the query to inspect.                     Only features within these layers will be returned. If this parameter is undefined, all layers                     will be checked. |
| A                     [filter](/gl-style-specification/layers/#filter)                      to limit query results. |
| Whether to check if the [options.filter] conforms to the                     MapLibre GL Style Specification. Disabling validation is a performance optimization that should                     only be used if you have previously validated the values you will be passing to this function. |

        
      
      [Returns](#queryrenderedfeatures-returns)
      `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<MapGeoJSONFeature>`:
        An array of MapGeoJSONFeature objects.
          The `properties` value of each returned feature object contains
            the properties of its source
            feature. For GeoJSON sources, only
            string and numeric property values are supported (i.e. `null`,
            `Array`, and
            `Object` values are not supported).
          
          Each feature includes top-level `layer`, `source`, and `sourceLayer`
            properties. The `layer` property is an object
            representing the style layer to which the feature belongs. Layout and paint properties in this object
            contain values
            which are fully evaluated for the given zoom level and feature.
          Only features that are currently rendered are included. Some features will **not** be
            included, like:
          
            Features from layers whose `visibility` property is `"none"`.
            Features from layers whose zoom range excludes the current zoom level.
            Symbol features that have been hidden due to text or icon collision.
          
          Features from all other layers are included, including features that may have no visible
            contribution to the rendered result; for example, because the layer's opacity or color alpha component
            is set to
          
            
          
          The topmost rendered feature appears first in the returned array, and subsequent features are sorted by
            descending z-order. Features that are rendered multiple times (due to wrapping across the antimeridian
            at low
            zoom levels) are returned only once (though subject to the following caveat).
          Because features come from tiled vector data or GeoJSON data that is converted to tiles internally,
            feature
            geometries may be split or duplicated across tile boundaries and, as a result, features may appear
            multiple
            times in query results. For example, suppose there is a highway running through the bounding rectangle
            of a query.
            The results of the query will be those parts of the highway that lie within the map tiles covering the
            bounding
            rectangle, even if the highway extends into other tiles, and the portion of the highway within each map
            tile
            will be returned as a separate feature. Similarly, a point feature near a tile boundary may appear in
            multiple
            tiles due to tile buffering.
        
      [Example](#queryrenderedfeatures-example)
      
        ```
``
```

      
      
        ```
``
```

      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#queryrenderedfeatures-related)
      
        Get features
              under the mouse pointer
          
      
    
  

  querySourceFeatures(sourceId,
          parameters?) 
            
          
  
    
        Returns an array of MapGeoJSONFeature objects
          representing features within the specified vector tile or GeoJSON source that satisfy the query
          parameters.
      
      [Parameters](#querysourcefeatures-parameters)
      sourceId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the vector tile or GeoJSON source to query.
        
      parameters`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
          object.
        
        
          
| The name of the source layer                     to query.                     *For vector tile sources, this parameter is required.*                     For GeoJSON sources, it is ignored. |
| A                     [filter](/gl-style-specification/layers/#filter)                      to limit query results. |
| Whether to check if the [parameters.filter] conforms to                     the MapLibre GL Style Specification. Disabling validation is a performance optimization that                     should only be used if you have previously validated the values you will be passing to this                     function. |

        
      
      [Returns](#querysourcefeatures-returns)
      `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<MapGeoJSONFeature>`:
        An array of MapGeoJSONFeature objects.
          In contrast to [Map#queryRenderedFeatures](/sdk-js/api/map/#map#queryrenderedfeatures), this
            function returns all features matching the query parameters,
            whether or not they are rendered by the current style (i.e. visible). The domain of the query includes
            all currently-loaded
            vector tiles and GeoJSON source tiles: this function does not check tiles outside the currently
            visible viewport.
          Because features come from tiled vector data or GeoJSON data that is converted to tiles internally,
            feature
            geometries may be split or duplicated across tile boundaries and, as a result, features may appear
            multiple
            times in query results. For example, suppose there is a highway running through the bounding rectangle
            of a query.
            The results of the query will be those parts of the highway that lie within the map tiles covering the
            bounding
            rectangle, even if the highway extends into other tiles, and the portion of the highway within each map
            tile
            will be returned as a separate feature. Similarly, a point feature near a tile boundary may appear in
            multiple
            tiles due to tile buffering.
        
      [Example](#querysourcefeatures-example)
      
        ```
``
```

      
    
  

  queryTerrainElevation(lngLatLike) 
            
          
  
    
        Get the elevation difference between a given point and a point that is currently in the
          middle of the screen.
          This method should be used for proper positioning of custom 3d objects.
          Returns null if terrain is not enabled.
          This method is subject to change in Maplibre GL JS v5.
      
      [Parameters](#queryterrainelevation-parameters)
      lngLatLike`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`
        [x,y] or LngLat coordinates of the location.
        
      
      [Returns](#queryterrainelevation-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`
      elevation offset in meters
      [Example](#queryterrainelevation-example)
      
        ```
``
```

      
    
  

  redraw() 
            
          
  
    
        Force a synchronous redraw of the map.
      
      [Returns](#redraw-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#redraw-example)
      
      
        ```
``
```

      
    
  

  refreshTiles(sourceId,
          tileIds?) 
            
          
  
    
        Triggers a reload of the selected tiles.
      
      [Parameters](#refreshTiles-parameters)
      
      sourceId
        `(string)`
        The ID of the source.
      
      tileIds?
        `(object[])`
        An array of tile IDs to be reloaded. If not defined, all tiles will be reloaded.
      
      [Returns](#refreshTiles-returns)
      
      `void`
      [Example](#refreshTiles-example)
      
      
        ```
``
```

      
    
  

  remove() 
            
          
  
    
        Clean up and release all internal resources associated with this map.
        This includes DOM elements, event bindings, web workers, and WebGL resources.
        Use this method when you are done using the map and wish to ensure that it no
          longer consumes browser resources. Afterwards, you must not call any other
          methods on the map.
      
  

  removeControl(control) 
            
          
  
    
        Removes the control from the map.
      
      [Parameters](#removecontrol-parameters)
      control`([IControl](/sdk-js/api/controls/#icontrol))`The
          [IControl](/sdk-js/api/controls/#icontrol)
          to remove.
        
      [Returns](#removecontrol-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#removecontrol-example)
      
        ```
``
```

      
    
  

  removeFeatureState(target,
          key) 
            
          
  
    
        Removes the `state` of a feature, setting it back to the default
          behavior.
          If only a `target.source` is specified, it will remove the state for
          all features from that
          source.
          If `target.id` is also specified, it will remove all keys for that
          feature's state.
          If `key` is also specified, it removes only that key from that
          feature's state.
          Features are identified by their `feature.id` attribute, which can
          be any number or string.
      
      [Parameters](#removefeaturestate-parameters)
      target`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Identifier
          of where to remove state. It can be a source, a feature, or a specific key of feature.
          Feature objects returned from
          [Map#queryRenderedFeatures](/sdk-js/api/map/#map#queryrenderedfeatures)
          or event handlers can be used as feature identifiers.
        
        
          
| (optional) Unique id of the feature. Optional if key is                     not specified. |
| The id of the vector or GeoJSON source for the feature. |
| (optional)                     For vector tile sources, `sourceLayer` is                       required. |

        
      
      key`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`(optional)
          The key in the feature state to reset.
        
      [Example](#removefeaturestate-example)
      
        ```
``
```

      
      
        ```
``
```

      
      
        ```
``
```

      
    
  

  removeImage(id) 
            
          
  
    
        Remove an image from a style. This can be an image from the style's original
          sprite or any images
          that have been added at runtime using [Map#addImage](/sdk-js/api/map/#map#addimage).
      
      [Parameters](#removeimage-parameters)
      
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the image.
        
      [Example](#removeimage-example)
      
        ```
``
```

      
    
  

  removeLayer(id) 
            
          
  
    
        Removes the layer with the given ID from the map's style.
        If no such layer exists, an `error` event is fired.
      
      [Parameters](#removelayer-parameters)
      
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`id
          of the layer to remove
        
      [Example](#removelayer-example)
      
        ```
``
```

      
    
  

  removeSource(id) 
            
          
  
    
        Removes a source from the map's style.
      
      [Parameters](#removesource-parameters)
      
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the source to remove.
        
      [Returns](#removesource-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#removesource-example)
      
        ```
``
```

      
    
  

  removeSprite(id) 
            
          
  
    
        Removes the sprite from the map's style. Fires the `style` event.
      
      [Parameters](#removesprite-parameters)
      
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          The ID of the sprite to remove. If the sprite is declared as a single URL, the ID must be "default".
        
      [Returns](#removesprite-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#removesprite-example)
      
        ```
``
```

      
    
  

  repaint 
            
          
  
    
        Gets and sets a Boolean indicating whether the map will
          continuously repaint. This information is useful for analyzing performance.
      
  

  resetNorth(options?,
          eventData?) 
            
          
  
    
        Rotates the map so that north is up (0° bearing), with an animated transition.
      
      [Parameters](#resetnorth-parameters)
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#resetnorth-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  resetNorthPitch(options?,
          eventData?) 
            
          
  
    
        Rotates and pitches the map so that north is up (0° bearing) and pitch is 0°, with an animated
          transition.
      
      [Parameters](#resetnorthpitch-parameters)
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#resetnorthpitch-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  resize(eventData?) 
            
          
  
    
        Resizes the map according to the dimensions of its
          `container` element.
        
        Checks if the map container size changed and updates the map if it has changed.
          This method must be called after the map's `container` is resized
          programmatically
          or when the map is shown after being initially hidden with CSS.
      
      [Parameters](#resize-parameters)
      eventData`(any?)`Additional properties to be
          passed to
          `movestart`
          ,
          `move`
          ,
          `resize`
          , and
          `moveend`

          events that get triggered as a result of resize. This can be useful for differentiating the
          source of an event (for example, user-initiated or programmatically-triggered events).
        
      [Returns](#resize-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#resize-example)
      
      
        ```
``
```

      
    
  

  rotateTo(bearing, options?,
          eventData?) 
            
          
  
    
        Rotates the map to the specified bearing, with an animated transition. The bearing is the compass
          direction
          that is "up"; for example, a bearing of 90° orients the map so that east is up.
      
      [Parameters](#rotateto-parameters)
      bearing`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          desired bearing.
        
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#rotateto-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  scrollZoom 
            
          
  
    
        The map's [ScrollZoomHandler](/sdk-js/api/handlers/#scrollzoomhandler), which
          implements zooming in and out with a scroll wheel or trackpad.
          Find more details and examples using `scrollZoom` in the [ScrollZoomHandler](/sdk-js/api/handlers/#scrollzoomhandler) section.
      
  

  setBearing(bearing,
          eventData?) 
            
          
  
    
        Sets the map's bearing (rotation). The bearing is the compass direction that is "up"; for example, a
          bearing
          of 90° orients the map so that east is up.
        Equivalent to `jumpTo({bearing: bearing})`.
      
      [Parameters](#setbearing-parameters)
      bearing`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          desired bearing.
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setbearing-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setbearing-example)
      
        ```
``
```

      
    
  

  setCenter(center,
          eventData?) 
            
          
  
    
        Sets the map's geographical centerpoint. Equivalent to `jumpTo({center: center})`.
      
      [Parameters](#setcenter-parameters)
      center`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`The
          centerpoint to set.
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setcenter-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setcenter-example)
      
      
        ```
``
```

      
    
  

  setCenterClampedToGround(centerClampedToGround) 
            
          
  
    
        Sets the value of `centerClampedToGround`.
        If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if
          terrain is not enabled). If false, the elevation of the center point will default to sea level and will not
          automatically update. Defaults to true. Needs to be set to false to keep the camera above ground when pitch >
          90 degrees.
      
      [Parameters](#setCenterClampedToGround-parameters)
      centerClampedToGround`(boolean)`
      [Returns](#setCenterClampedToGround-returns)
      
      `void`
    
  

  setCenterElevation(elevation,
          eventData?) 
            
          
  
    
        Sets the elevation of the map's center point, in meters above sea level.
          Equivalent to `jumpTo({elevation: elevation})`.
        Triggers the following events: `movestart` and `moveend`.
      
      [Parameters](#setCenterElevation-parameters)
      elevation`(number)`The elevation to set, in meters above sea level.
        
      eventData`(any?)`Additional properties to be added to event objects of events
          triggered by this method.
        
      [Returns](#setCenterElevation-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setEventedParent(parent,
          data?) 
            
          
  
    
        Bubble all events fired by this instance of Evented to this parent instance of Evented.
      
      [Parameters](#setEventedParent-parameters)
      parent`(Evented?)`
      data`(any?)`
      [Returns](#setEventedParent-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setFeatureState(feature,
          state) 
            
          
  
    
        Sets the `state` of a feature.
          A feature's `state` is a set of user-defined key-value pairs that
          are assigned to a feature at
          runtime.
          When using this method, the `state` object is merged with any
          existing key-value pairs in the
          feature's state.
          Features are identified by their `feature.id` attribute, which can
          be any number or string.
        This method can only be used with sources that have a `feature.id`
          attribute. The
          `feature.id` attribute can be defined in three ways:
        
        
          For vector or GeoJSON sources, including an `id` attribute in
            the original data file.
          For vector or GeoJSON sources, using the `promoteId`
            option at the time the source is defined.
          For GeoJSON sources, using the `generateId`
            option to auto-assign an `id` based on the feature's index in the
            source data. If you change
            feature data using `map.getSource('some id').setData(..)`, you may
            need to re-apply state
            taking into account updated `id` values.
        
        Note: You can use the `feature-state`
              expression to access the values in a feature's state object for the purposes of styling.
      
      [Parameters](#setfeaturestate-parameters)
      feature`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`Feature
          identifier. Feature objects returned from

          [Map#queryRenderedFeatures](/sdk-js/api/map/#map#queryrenderedfeatures)
          or event handlers can be used as feature identifiers.
        
        
          
| Unique id of the feature. |
| The id of the vector or GeoJSON source for the feature. |
| (optional)                     For vector tile sources, `sourceLayer` is                       required. |

        
      
      state`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`A
          set of key-value pairs. The values should be valid JSON types.
        
      [Example](#setfeaturestate-example)
      
      
        ```
``
```

      
      Related
          examples
      
        [Create a hover effect](/sdk-js/examples/hover-styles/)
          
      
    
  

  setFilter(layerId, filter, options =
          {}) 
            
          
  
    
        Sets the filter for the specified style layer.
        Filters control which features a style layer renders from its source.
          Any feature for which the filter expression evaluates to `true` will
          be
          rendered on the map. Those that are false will be hidden.
        Use `setFilter` to show a subset of your source data.
        To clear the filter, pass `null` or `undefined` as the second parameter.
      
      [Parameters](#setfilter-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to which the filter will be applied.
        
      filter`(([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          filter, conforming to the GL Style Specification's

          [filter definition](/gl-style-specification/layers/#filter)
          . If
          `null`
          or
          `undefined`
          is provided, the function removes any existing filter from the layer.
        
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`(default
          `{}`)Options object.
        
        
          
| Whether to check if the filter conforms to the MapLibre GL                     Style Specification. Disabling validation is a performance optimization that should only be used                     if you have previously validated the values you will be passing to this function. |

        
      
      [Returns](#setfilter-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setfilter-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#setfilter-related)
      
      
        Create a timeline
              animation
          
      
    
  

  setGlobalStateProperty(propertyName,
          value) 
            
          
  
    
        Sets a global state property that can be retrieved with the `global-state` expression.
          If the value is null, it resets the property to its default value defined in the state style property.
        Note that changing `global-state` values defined in layout properties
          is not supported, and will be ignored.
      
      [Parameters](#setGlobalStateProperty-parameters)
      
        propertyName
        `(string)`
        The name of the state property to set.
      
      value
        `(any)`
        The value of the state property to set.
      
      [Returns](#setGlobalStateProperty-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setGlyphs(glyphsUrl,
          options?) 
            
          
  
    
        Sets the value of the style's glyphs property.
      
      [Parameters](#setglyphs-parameters)
      glyphsUrl`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          The Glyph URL to set. Must conform to the [GL Style Specification](/gl-style-specification).
        
      options`([StyleSetterOptions](/sdk-js/api/types/#StyleSetterOptions)?)`
        The Options object.
        
      
      [Returns](#setglyphs-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setglyphs-example)
      
      
        ```
``
```

      
    
  

  setHalo(halo)
          
        
         
            
          
  
  
    
        Sets the halo (atmospheric glow) for the map.
      
      [Parameters](#sethalo-parameters)
      halo`([RadialGradientLayerConstructorOptions](/sdk-js/api/types/#RadialGradientLayerConstructorOptions))`
      
      [Example](#sethalo-example)
      
      
        ```
``
```

      
    
  

  setLanguage(language)
        
          
        
         
            
          
  
    
        Sets the map labels language.
        Note: not all the languages shorthands provided are available.
      
      [Parameters](#setlanguage-parameters)
      
      language([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | 
            [Language](/sdk-js/api/languages/))The
          language to be applied. The language generally depends on the style. Whenever a label is not supported in the
          defined language, it falls back to `maptilersdk.Language.LATIN`.
          Languages that are written right-to-left such as arabic and hebrew are fully supported by default. No need
            to install any plugin!
        
      [Returns](#setlanguage-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setlanguage-example)
      
        ```
``
```

        [Related examples](#setlanguage-related)
        
        
          [How to change the default map labels language](/sdk-js/examples/language-map/)
          
          How to change the map labels language based on visitor's
                location
          [Change a map's language](/sdk-js/examples/language-switch/)
        
      
    
  

  setLayerZoomRange(layerId, minzoom,
          maxzoom) 
            
          
  
    
        Sets the zoom extent for the specified style layer. The zoom extent includes the
          [minimum zoom level](/gl-style-specification/#layer-minzoom)
          and [maximum zoom level](/gl-style-specification/#layer-maxzoom))
          at which the layer will be rendered.
        
        Note: For style layers using vector sources, style layers cannot be rendered at zoom levels lower than
          the
          minimum zoom level of the *source layer* because the data does not exist at those zoom levels. If
          the minimum
          zoom level of the source layer is higher than the minimum zoom level defined in the style layer, the style
          layer will not be rendered at all zoom levels in the zoom range.
      
      [Parameters](#setlayerzoomrange-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to which the zoom extent will be applied.
        
      minzoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          minimum zoom to set (0-24).
        
      maxzoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          maximum zoom to set (0-24).
        
      [Returns](#setlayerzoomrange-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setlayerzoomrange-example)
      
        ```
``
```

      
    
  

  setLayoutProperty(layerId, name, value,
          options = {}) 
            
          
  
    
        Sets the value of a layout property in the specified style layer.
      
      [Parameters](#setlayoutproperty-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to set the layout property in.
        
      name`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          name of the layout property to set.
        
      value`(any)`The value of
          the layout property. Must be of a type appropriate for the property, as defined in the
          [GL Style Specification](/gl-style-specification/)
          .
        
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`(default
          `{}`)Options object.
        
        
          
| Whether to check if                     `value`                     conforms to the MapLibre GL Style Specification. Disabling validation is a performance                     optimization that should only be used if you have previously validated the values you will be                     passing to this function. |

        
      
      [Returns](#setlayoutproperty-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setlayoutproperty-example)
      
        ```
``
```

      
    
  

  setLight(light, options =
          {}) 
            
          
  
    
        Sets the any combination of light values.
      
      [Parameters](#setlight-parameters)
      light`(LightSpecification)`Light properties to
          set. Must conform to the
          [GL Style Specification](/gl-style-specification/#light)
          .
        
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`(default
          `{}`)Options object.
        
        
          
| Whether to check if the filter conforms to the GL                     Style Specification. Disabling validation is a performance optimization that should only be used                     if you have previously validated the values you will be passing to this function. |

        
      
      [Returns](#setlight-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setMaxBounds(bounds) 
            
          
  
    
        Sets or clears the map's geographical bounds.
        Pan and zoom operations are constrained within these bounds.
          If a pan or zoom is performed that would
          display regions outside these bounds, the map will
          instead display a position and zoom level
          as close as possible to the operation's request while still
          remaining within the bounds.
      
      [Parameters](#setmaxbounds-parameters)
      
      bounds`(([LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          maximum bounds to set. If
          `null`
          or
          `undefined`
          is provided, the function removes the map's maximum bounds.
        
      [Returns](#setmaxbounds-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setmaxbounds-example)
      
        ```
``
```

      
    
  

  setMaxPitch(maxPitch) 
            
          
  
    
        Sets or clears the map's maximum pitch.
          If the map's current pitch is higher than the new maximum,
          the map will pitch to the new maximum.
      
      [Parameters](#setmaxpitch-parameters)
      
      maxPitch`(([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          maximum pitch to set (0-85). Values greater than 60 degrees are experimental and may result in rendering
          issues. If you encounter any, please raise an issue with details in the MapLibre project.
          If
          `null`
          or
          `undefined`
          is provided, the function removes the current maximum pitch (sets it to 60).
        
      [Returns](#setmaxpitch-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setMaxZoom(maxZoom) 
            
          
  
    
        Sets or clears the map's maximum zoom level.
          If the map's current zoom level is higher than the new maximum,
          the map will zoom to the new maximum.
      
      [Parameters](#setmaxzoom-parameters)
      maxZoom`(([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          maximum zoom level to set.
          If
          `null`
          or
          `undefined`
          is provided, the function removes the current maximum zoom (sets it to 22).
        
      [Returns](#setmaxzoom-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setmaxzoom-example)
      
        ```
``
```

      
    
  

  setMinPitch(minPitch) 
            
          
  
    
        Sets or clears the map's minimum pitch.
          If the map's current pitch is lower than the new minimum,
          the map will pitch to the new minimum.
      
      [Parameters](#setminpitch-parameters)
      
      minPitch`(([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          minimum pitch to set (0-85). Values greater than 60 degrees are experimental and may result in rendering
          issues. If you encounter any, please raise an issue with details in the MapLibre project.
          If
          `null`
          or
          `undefined`
          is provided, the function removes the current minimum pitch (i.e. sets it to 0).
        
      [Returns](#setminpitch-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setMinZoom(minZoom) 
            
          
  
    
        Sets or clears the map's minimum zoom level.
          If the map's current zoom level is lower than the new minimum,
          the map will zoom to the new minimum.
        It is not always possible to zoom out and reach the set `minZoom`.
          Other factors such as map height may restrict zooming. For example,
          if the map is 512px tall it will not be possible to zoom below zoom 0
          no matter what the `minZoom` is set to.
      
      [Parameters](#setminzoom-parameters)
      minZoom`(([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | null | [undefined](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/undefined)))`The
          minimum zoom level to set (-2 - 24).
          If
          `null`
          or
          `undefined`
          is provided, the function removes the current minimum zoom (i.e. sets it to -2).
        
      [Returns](#setminzoom-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setminzoom-example)
      
        ```
``
```

      
    
  

  setPadding(padding,
          eventData?) 
            
          
  
    
        Sets the padding in pixels around the viewport.
        Equivalent to `jumpTo({padding: padding})`.
      
      [Parameters](#setpadding-parameters)
      padding`([PaddingOptions](/sdk-js/api/properties/#paddingoptions))`The
          desired padding. Format: { left: number, right: number, top: number, bottom: number }
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setpadding-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setpadding-example)
      
        ```
``
```

      
    
  

  setPaintProperty(layerId, name, value,
          options = {}) 
            
          
  
    
        Sets the value of a paint property in the specified style layer.
      
      [Parameters](#setpaintproperty-parameters)
      layerId`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the layer to set the paint property in.
        
      name`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          name of the paint property to set.
        
      value`(any)`The value of
          the paint property to set.
          Must be of a type appropriate for the property, as defined in the
          [GL Style Specification](/gl-style-specification/)
          .
        
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`(default
          `{}`)Options object.
        
        
          
| Whether to check if                     `value`                     conforms to the MapLibre GL Style Specification. Disabling validation is a performance                     optimization that should only be used if you have previously validated the values you will be                     passing to this function. |

        
      
      [Returns](#setpaintproperty-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setpaintproperty-example)
      
      
        ```
``
```

      
      Related
          examples
      
        Change a layer's color
              with buttons
          
        Create a draggable
              point
          
      
    
  

  setPitch(pitch, eventData?) 
            
          
  
    
        Sets the map's pitch (tilt). Equivalent to `jumpTo({pitch: pitch})`.
        
      
      [Parameters](#setpitch-parameters)
      pitch`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          pitch to set, measured in degrees away from the plane of the screen (0-60).
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setpitch-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setPixelRatio(pixelRatio) 
            
          
  
    
        Sets the map's pixel ratio. This allows to override `devicePixelRatio`.
          After this call, the canvas' `width` attribute will be
          `container.clientWidth * pixelRatio`
          and its height attribute will be `container.clientHeight * pixelRatio`.
        
      
      [Parameters](#setpixelratio-parameters)
      pixelRatio`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          pixel ratio.
        
    
  

  setProjection(projection?,
          options?) 
            
          
  
    
        Sets the [ProjectionSpecification](/gl-style-specification/projection)
        Accepts types:
        
          `"mercator"` for [Web Mercator Projection](https://en.wikipedia.org/wiki/Web_Mercator_projection)
          `"vertical-perspective"` for [General Perspective projection](https://en.wikipedia.org/wiki/General_Perspective_projection)
          
          And preset `"globe"` for adaptive globe (interpolates from
            vertical-perspective to mercator projection between zoom levels 10 and 12.) 

        
        
      
      
        **ProjectionChangeOptions**
        Whether the new projection should be persisted for any future style changes.
        
          If `true`, the new projection is persisted and is applied after all
          future style changes.
          If `false` or not specified, the new projection will be used only until
          the next style change, when it will
          get replaced with the first applicable value from this list:
          
            a previously persisted projection
            a projection specified in `Map` constructor options
            a projection specified in `projection` property of the style
              itself
            the Mercator projection
          
        
      

      projection`(ProjectionSpecification?)`
      options`(ProjectionChangeOptions?)`
      This will set the map projection
      [Example](#setProjection-example)
      
        ```
``
```

      
      [Returns](#setProjection-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setRenderWorldCopies(renderWorldCopies) 
            
          
  
    
        Sets the state of `renderWorldCopies`.
      
      [Parameters](#setrenderworldcopies-parameters)
      renderWorldCopies`([boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean))`If
          `true`
          , multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude. If set
          to
          `false`
          :
          
            When the map is zoomed out far enough that a single representation of the world does not fill the
              map's entire
              container, there will be blank space beyond 180 and -180 degrees longitude.
            Features that cross 180 and -180 degrees longitude will be cut in two (with one portion on the right
              edge of the
              map and the other on the left edge of the map) at every zoom level.
          
          `undefined` is treated as `true`, `null` is treated as
            `false`.
          
        
      [Returns](#setrenderworldcopies-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setrenderworldcopies-example)
      
        ```
``
```

      
      [Related examples](#setrenderworldcopies-related)
      
        Render world
              copies
          
      
    
  

  setRoll(roll, eventData?) 
            
          
  
    
        Sets the map's roll angle. Equivalent to `jumpTo({roll: roll})`.
        
        Triggers the following events: `movestart`, `moveend`,
          `rollstart`, and `rollend`.
        
      
      [Parameters](#setRoll-parameters)
      roll`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
        The roll to set, measured in degrees about the camera boresight
      
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setRoll-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  setSecondaryLanguage(language)
        
          
        
         
            
          
  
    
        Sets the map labels secondary language.
        
      
      [Parameters](#setsecondarylanguage-parameters)
      language([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | 
            [Language](/sdk-js/api/languages/))The
          language to be applied. The language generally depends on the style. Whenever a label is not supported in the
          defined language, it falls back to `maptilersdk.Language.LATIN`.
          Languages that are written right-to-left such as arabic and hebrew are fully supported by default. No need
            to install any plugin!
        
      [Returns](#setsecondarylanguage-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setsecondarylanguage-example)
      
        ```
``
```

      
    
  

  setSky(sky, options?) 
            
          
  
    
        Sets the value of style's sky properties.
      
      [Parameters](#setSky-parameters)
      sky
          [`(SkySpecification)`](/gl-style-specification/sky/)
        
        Sky properties to set. Must conform to the GL Style
            Specification.
      
      options`(StyleSetterOptions?)`Options object.
        
      [Returns](#setSky-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setSky-example)
      
        ```
``
```

      
    
  

  setSourceTileLodParams(maxZoomLevelsOnScreen, tileCountMaxMinRatio, sourceId?) 
            
          
  
    
        Change the tile Level of Detail behavior of the specified source.
          These parameters have no effect when pitch == 0, and the largest effect when the horizon is visible on screen.
        
      
      [Parameters](#setSourceTileLodParams-parameters)
      
        maxZoomLevelsOnScreen
        `(number)`
        The maximum number of distinct zoom levels allowed on screen at a time.
          There will generally be fewer zoom levels on the screen,
          the maximum can only be reached when the horizon is at the top of the screen.
          Increasing the maximum number of zoom levels causes the zoom level to decay faster toward the horizon.
      
      tileCountMaxMinRatio
        `(number)`
        The ratio of the maximum number of tiles loaded (at high pitch) to the minimum number of tiles loaded.
          Increasing this ratio allows more tiles to be loaded at high pitch angles.
          If the ratio would otherwise be exceeded,
          the zoom level is reduced uniformly to keep the number of tiles within the limit.
      
      sourceId?
        `(string)`
        The ID of the source to set tile LOD parameters for.
          All sources will be updated if unspecified.
          If sourceId is specified but a corresponding source does not exist, an error is thrown.
      
      [Returns](#setSourceTileLodParams-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setSourceTileLodParams-example)
      
      
        ```
``
```

      
    
  

  setSpace(space)
          
        
         
            
          
  
  
    
        Sets the space for the map.
        This method, at present, **overwrites** the current config.
          If an option is not set it will internally revert to the default option unless explicitly set when calling.
        
      
      [Parameters](#setspace-parameters)
      space`([CubemapLayerConstructorOptions](/sdk-js/api/types/#CubemapLayerConstructorOptions))`
      
      [Example](#setspace-example)
      
      
        ```
``
```

      
    
  

  setSprite(spriteUrl,
          options?) 
            
          
  
    
        Sets the value of style's sky properties.
      
      [Parameters](#setSprite-parameters)
      spriteUrl
          `(string)`
        
        Sprite URL to set.
      
      options`(StyleSetterOptions?)`Options object.
        
      [Returns](#setSprite-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setSprite-example)
      
        ```
``
```

      
    
  

  setStyle(style, options?)
          
        
         
            
          
  
  
    
        Updates the map's style object with a new value.
        If a style is already set when this is used and options.diff is set to true, the map renderer will
          attempt to compare the given style
          against the map's current state and perform only the changes necessary to make the map style match the
          desired state. Changes in sprites
          (images used for icons and patterns) and glyphs (fonts for label text) **cannot** be diffed.
          If the sprites or fonts used in the current
          style and the given style are different in any way, the map renderer will force a full update, removing
          the current style and building
          the given one from scratch.
      
      [Parameters](#setstyle-parameters)
      style(([ReferenceMapStyle](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | 
            [MapStyleVariant](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) |
            [string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) |
            [StyleSpecification](/gl-style-specification/) | null))
        The map's style. This must be:
          
            ReferenceMapStyle (e.g. MapStyle.STREETS)
            MapStyleVariant (e.g. MapStyle.STREETS.DARK)
            MapTIler Style ID (e.g. “”)
            uuid of custom style
            an a JSON object
              conforming to
              the schema described in the
              [GL Style Specification](/gl-style-specification/)
            
            a URL to
              such JSON
            null
          
        
      
      options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
          object.
        
        
          
| If false, force a 'full' update, removing the current                     style                     and building the given one instead of attempting a diff-based update. |
| TransformStyleFunction is a convenience function that allows                     to modify a style after it is fetched but before it is committed to the map state. |
| Defines a CSS                     font-family for locally overriding generation of glyphs in the 'CJK Unified Ideographs',                     'Hiragana', 'Katakana' and 'Hangul Syllables' ranges.                     In these ranges, font settings from the map's style will be ignored, except for font-weight                     keywords (light/regular/medium/bold).                     Set to                     `false`                     , to enable font settings from the map's style for these glyph ranges.                     Forces a full update. |
| If false, style validation will be skipped. Useful in                     production environment. |

        
      
      [Returns](#setstyle-returns)
      
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setstyle-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#setstyle-related)
      
      
        [Built-in map styles](/sdk-js/examples/built-in-styles/)
        [How to display a style switcher control](/sdk-js/examples/control-style-switcher/)
        
      
    
  

  setTerrain(options?) 
            
          
  
    
        Loads a 3D terrain mesh, based on a "raster-dem" source.
      
      [Parameters](#setterrain-parameters)
      options`(TerrainSpecification?)`Options
          object.
        
      [Returns](#setterrain-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setterrain-example)
      
        ```
``
```

      
    
  

  setTerrainAnimationDuration(duration)
        
          
        
         
            
          
  
    
        Set the duration (millisec) of the terrain animation for growing or flattening.
        
      
      [Parameters](#setTerrainAnimationDuration-parameters)
      duration`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
        Sets the terrain animation duration in milliseconds
        
      
      [Example](#setTerrainAnimationDuration-example)
      
        ```
``
```

      
    
  

  setTerrainExaggeration(exaggeration)
        
          
        
         
            
          
  
    
        Sets the 3D terrain exageration factor. This method is just a shortcut to .enableTerrain
        
      
      [Parameters](#setterrainexaggeration-parameters)
      exaggeration`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
        Sets the terrain exaggeration factor
        
      
      [Example](#setterrainexaggeration-example)
      
        ```
``
```

      
    
  

  setTransformRequest(transformRequest) 
            
          
  
    
        Updates the requestManager's transform request with a new function
      
      [Parameters](#settransformrequest-parameters)
      transformRequest`(RequestTransformFunction)`A
          callback run before the Map makes a request for an external URL. The callback can be used to modify the
          url, set headers, or set the credentials property for cross-origin requests.
          Expected to return an object with a
          `url`
          property and optionally
          `headers`
          and
          `credentials`
          properties
        
      [Returns](#settransformrequest-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#settransformrequest-example)
      
        ```
``
```

      
    
  

  setVerticalFieldOfView(fov,
          eventData?) 
            
          
  
    
        Sets the map's vertical field of view, in degrees. Default `36.87`.
        Triggers the following events: `movestart`, `move`,
          and `moveend`.
        The internal camera has a default vertical field of view (*[wikipedia](https://en.wikipedia.org/wiki/Field_of_view)*)
          of a wide `~36.86` degrees.
          In globe mode, such a large *FOV* reduces the amount of the Earth that can be seen at once
          and exaggerates the central part, comparably to a fisheye lens.
          In many cases, a narrower *FOV* is preferable.
      
      FOV comparison:
      
| 01° | 50° |
| --- | --- |
|  |  |

      [Parameters](#setVerticalFieldOfView-parameters)
      fov`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
        The vertical field of view to set, in degrees (0-180).
      
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setVerticalFieldOfView-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setVerticalFieldOfView-example)
      
        ```
``
```

      
    
  

  setZoom(zoom, eventData?) 
            
          
  
    
        Sets the map's zoom level. Equivalent to `jumpTo({zoom: zoom})`.
        
      
      [Parameters](#setzoom-parameters)
      zoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          zoom level to set (0-20).
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#setzoom-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#setzoom-example)
      
        ```
``
```

      
    
  

  showCollisionBoxes 
            
          
  
    
        Gets and sets a Boolean indicating whether the map will render boxes
          around all symbols in the data source, revealing which symbols
          were rendered or which were hidden due to collisions.
          This information is useful for debugging.
      
  

  showOverdrawInspector
          
            
          
  
    
        Gets and sets a Boolean indicating whether the map should color-code each fragment
          to show how many times it has been shaded.
          White fragments have been shaded 8 or more times.
          Black fragments have been shaded 0 times. This information is useful for debugging.
      
  

  showPadding 
            
          
  
    
        Gets and sets a Boolean indicating whether the map will visualize
          the padding offsets.
      
  

  showTileBoundaries 
            
          
  
    
        Gets and sets a Boolean indicating whether the map will render an outline
          around each tile and the tile ID. These tile boundaries are useful for
          debugging.
        The uncompressed file size of the first vector source is drawn in the top left
          corner of each tile, next to the tile ID.
      
      [Example](#showtileboundaries-example)
      
        ```
``
```

      
    
  

  snapToNorth(options?,
          eventData?) 
            
          
  
    
        Snaps the map so that north is up (0° bearing), if the current bearing is close enough to it (i.e. within
          the
          `bearingSnap` threshold).
        
      
      [Parameters](#snaptonorth-parameters)
      
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#snaptonorth-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
    
  

  stop() 
            
          
  
    
        Stops any animated transition underway.
      
      [Returns](#stop-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
    
  

  touchPitch 
            
          
  
    
        The map's [TouchPitchHandler](/sdk-js/api/handlers/#touchpitchhandler), which
          allows the user to pitch the map with touch gestures.
          Find more details and examples using `touchPitch` in the [TouchPitchHandler](/sdk-js/api/handlers/#touchpitchhandler) section.
      
  

  touchZoomRotate 
            
          
  
    
        The map's [TouchZoomRotateHandler](/sdk-js/api/handlers/#touchzoomrotatehandler),
          which allows the user to zoom or rotate the map with touch gestures.
          Find more details and examples using `touchZoomRotate` in the [TouchZoomRotateHandler](/sdk-js/api/handlers/#touchzoomrotatehandler) section.
      
  

  transformCameraUpdate
          
            
          
  
    
        A callback ([CameraUpdateTransformFunction](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/CameraUpdateTransformFunction/))
          used to defer camera updates or apply arbitrary constraints.
          If specified, this Camera instance can be used as a stateless component in React etc.
      
  

  triggerRepaint() 
            
          
  
    
        Trigger the rendering of a single frame. Use this method with custom layers to
          repaint the map when the layer changes. Calling this multiple times before the
          next frame is rendered will still result in only a single frame being rendered.
      
      [Example](#triggerrepaint-example)
      
        ```
``
```

      
      Related
          examples
      
        [Add a 3D model](/sdk-js/examples/add-3d-model/)
          
        Add an animated
              icon to the map
          
      
    
  

  unproject(point) 
            
          
  
    
        Returns a [LngLat](/sdk-js/api/geography/#lnglat) representing geographical
          coordinates that correspond
          to the specified pixel coordinates.
      
      [Parameters](#unproject-parameters)
      point`([PointLike](/sdk-js/api/geography/#pointlike))`The
          pixel coordinates to unproject.
        
      [Returns](#unproject-returns)
      
      `[LngLat](/sdk-js/api/geography/#lnglat)`:
        The
          [LngLat](/sdk-js/api/geography/#lnglat)
          corresponding to
          `point`
          .
        
      [Example](#unproject-example)
      
      
        ```
``
```

      
    
  

  updateImage(id, image) 
            
          
  
    
        Update an existing image in a style. This image can be displayed on the map like any other icon in the
          style's
          sprite using the image's ID with
          `icon-image`,
          `background-pattern`,
          `fill-pattern`,
          or `line-pattern`.
        
      
      [Parameters](#updateimage-parameters)
      
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
          ID of the image.
        
      image`(([HTMLImageElement](https://developer.mozilla.org/docs/Web/API/HTMLImageElement) | ImageBitmap | ImageData | {width: [number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number), height: [number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number), data: ([Uint8Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | [Uint8ClampedArray](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray))} | [StyleImageInterface](/sdk-js/api/properties/#styleimageinterface)))`The
          image as an
          `HTMLImageElement`
          ,
          `ImageData`
          ,
          `ImageBitmap`
          or object with
          `width`
          ,
          `height`
          , and
          `data`

          properties with the same format as
          `ImageData`
          .
        
      [Example](#updateimage-example)
      
        ```
``
```

      
    
  

  version 
            
          
  
    
        Returns the package version of the library
      
      [Returns](#version-returns)
      `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`:
        Package version of the library
        
    
  

  zoomIn(options?, eventData?) 
            
          
  
    
        Increases the map's zoom level by 1.
      
      [Parameters](#zoomin-parameters)
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#zoomin-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#zoomin-example)
      
      
        ```
``
```

      
    
  

  zoomOut(options?,
          eventData?) 
            
          
  
    
        Decreases the map's zoom level by 1.
      
      [Parameters](#zoomout-parameters)
      options`([AnimationOptions](/sdk-js/api/properties/#animationoptions)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#zoomout-returns)
      `[Map](/sdk-js/api/map/#map)`: `this`
        
      [Example](#zoomout-example)
      
        ```
``
```

      
    
  

  zoomTo(zoom, options?,
          eventData?) 
            
          
  
    
        Zooms the map to the specified zoom level, with an animated transition.
      
      [Parameters](#zoomto-parameters)
      zoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          zoom level to transition to.
        
      options`(([AnimationOptions](/sdk-js/api/properties/#animationoptions) | null)?)`Options
          object
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#zoomto-returns)
      `[Map](/sdk-js/api/map/#map)`:
        `this`
        
      [Example](#zoomto-example)
      
      
        ```
``
```

      
    
  

    ## [Events](#map-events)

  boxzoomcancel 
            
          
  
    
        Fired when the user cancels a "box zoom" interaction, or when the bounding box does not meet the minimum
          size threshold.
          See [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler).
      
      [Properties](#boxzoomcancel-properties)
      data`([MapLibreZoomEvent](/sdk-js/api/events/#maplibrezoomevent))`
      
      [Example](#boxzoomcancel-example)
      
        ```
``
```

      
    
  

  boxzoomend 
            
          
  
    
        Fired when a "box zoom" interaction ends. See [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler).
      
      [Properties](#boxzoomend-properties)
      data`([MapLibreZoomEvent](/sdk-js/api/events/#maplibrezoomevent))`
      
      [Example](#boxzoomend-example)
      
        ```
``
```

      
    
  

  boxzoomstart 
            
          
  
    
        Fired when a "box zoom" interaction starts. See [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler).
      
      [Properties](#boxzoomstart-properties)
      data`([MapLibreZoomEvent](/sdk-js/api/events/#maplibrezoomevent))`
      
      [Example](#boxzoomstart-example)
      
        ```
``
```

      
    
  

  click 
            
          
  
    
        Fired when a pointing device (usually a mouse) is pressed and released at the same point on the map.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only when the
          point that is pressed and released contains a visible portion of the specifed layer.
      
      [Properties](#click-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#click-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#click-related)
      
      
        [Measure distances](/sdk-js/examples/measure/)
          
        Center the map on a
              clicked symbol
          
      
    
  

  contextmenu 
            
          
  
    
        Fired when the right button of the mouse is clicked or the context menu key is pressed within the map.
        
      
      [Properties](#contextmenu-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#contextmenu-example)
      
        ```
``
```

      
    
  

  cooperativegestureprevented 
            
          
  
    
        Fired whenever the cooperativeGestures option prevents a gesture from being handled by the map. 
          This is useful for showing your own UI when this happens.
        
      
      [Properties](#cooperativegestureprevented-properties)
      data(`[WheelEvent](/sdk-js/api/events/#mapwheelevent)`
          | `[TouchEvent](/sdk-js/api/events/#maptouchevent)`) &
          `object` 
      
      Type declaration
      
      gestureType(`"wheel_zoom"`
        | `"touch_pan"`)
    
      [Example](#cooperativegestureprevented-example)
      
        ```
``
```

      
    
  

  data 
            
          
  
    
        Fired when any map data loads or changes. See [MapDataEvent](/sdk-js/api/events/#mapdataevent)
          for more information.
      
      [Properties](#data-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#data-example)
      
      
        ```
``
```

      
      [Related examples](#data-related)
      
      
        Display HTML clusters
              with custom properties
          
      
    
  

  dataabort 
            
          
  
    
        Fired when a request for one of the map's sources' tiles is aborted.
          Fired when a request for one of the map's sources' data is aborted.
          See [MapDataEvent](/sdk-js/api/events/#mapdataevent) for more information.
      
      [Properties](#dataabort-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#dataabort-example)
      
        ```
``
```

      
    
  

  dataloading 
            
          
  
    
        Fired when any map data (style, source, tile, etc) begins loading or
          changing asyncronously. All `dataloading` events are followed by a
          `data`,
          `dataabort` or `error` event.
          See [MapDataEvent](/sdk-js/api/events/#mapdataevent) for more information.
        
      
      [Properties](#dataloading-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#dataloading-example)
      
        ```
``
```

      
    
  

  dblclick 
            
          
  
    
        Fired when a pointing device (usually a mouse) is pressed and released twice at the same point on
          the map in rapid succession.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only
          when the point that is clicked twice contains a visible portion of the specifed layer.
      
      [Properties](#dblclick-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#dblclick-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
    
  

  drag 
            
          
  
    
        Fired repeatedly during a "drag to pan" interaction. See [DragPanHandler](/sdk-js/api/handlers/#dragpanhandler).
      
      [Properties](#drag-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#drag-example)
      
      
        ```
``
```

      
    
  

  dragend 
            
          
  
    
        Fired when a "drag to pan" interaction ends. See [DragPanHandler](/sdk-js/api/handlers/#dragpanhandler).
      
      [Properties](#dragend-properties)
      data`({originalEvent: [DragEvent](https://developer.mozilla.org/docs/Web/API/DragEvent)})`
      
      [Example](#dragend-example)
      
      
        ```
``
```

      
      [Related examples](#dragend-related)
      
      
        Create a draggable
              marker
          
      
    
  

  dragstart 
            
          
  
    
        Fired when a "drag to pan" interaction starts. See [DragPanHandler](/sdk-js/api/handlers/#dragpanhandler).
      
      [Properties](#dragstart-properties)
      data`({originalEvent: [DragEvent](https://developer.mozilla.org/docs/Web/API/DragEvent)})`
      
      [Example](#dragstart-example)
      
        ```
``
```

      
    
  

  error 
            
          
  
    
        Fired when an error occurs. This is GL JS's primary error reporting
          mechanism. We use an event instead of `throw` to better accommodate
          asyncronous operations. If no listeners are bound to the `error`
          event, the
          error will be printed to the console.
      
      [Properties](#error-properties)
      data`({error: {message: [string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)}})`
      
      [Example](#error-example)
      
      
        ```
``
```

      
    
  

  idle 
            
          
  
    
        Fired after the last frame rendered before the map enters an
          "idle" state:
        
          No camera transitions are in progress
          All currently requested tiles have loaded
          All fade/transition animations have completed
        
      
      [Example](#idle-example)
      
      
        ```
``
```

      
    
  

  load 
            
          
  
    
        Fired immediately after all necessary resources have been downloaded
          and the first visually complete rendering of the map has occurred.
      
      [Example](#load-example)
      
      
        ```
``
```

      
      [Related examples](#load-related)
      
      
        Draw GeoJSON
              points
          
        Add live realtime
              data
          
        Animate a
              point
          
      
    
  

  loadWithTerrain
        
          
        
         
            
          
  
    
        Fired only once in a `Map` instance lifecycle, when both the `load`
           event and the `terrain` event with **non-null terrain** are fired.
      
      [Example](#loadWithTerrain-example)
      
      
        ```
``
```

      
    
  

  mousedown 
            
          
  
    
        Fired when a pointing device (usually a mouse) is pressed within the map.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only when the
          the cursor is pressed while inside a visible portion of the specifed layer.
      
      [Properties](#mousedown-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mousedown-example)
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#mousedown-related)
      
        Create a draggable
              point
          
      
    
  

  mouseenter 
            
          
  
    
        Fired when a pointing device (usually a mouse) enters a visible portion of a specified layer from
          outside that layer or outside the map canvas.
        **Important:** This event can only be listened for when [Map#on](/sdk-js/api/map/#map#on) includes three arguments,
          where the second argument specifies the desired layer.
      
      [Properties](#mouseenter-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mouseenter-example)
      
        ```
``
```

      
      [Related examples](#mouseenter-related)
      
        Center the map on a
              clicked symbol
          
        Display a popup on
              click
          
      
    
  

  mouseleave 
            
          
  
    
        Fired when a pointing device (usually a mouse) leaves a visible portion of a specified layer, or leaves
          the map canvas.
        **Important:** This event can only be listened for when [Map#on](/sdk-js/api/map/#map#on) includes three arguements,
          where the second argument specifies the desired layer.
      
      [Properties](#mouseleave-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mouseleave-example)
      
        ```
``
```

      
      [Related examples](#mouseleave-related)
      
        Highlight features under
              the mouse pointer
          
        Display a popup on
              click
          
      
    
  

  mousemove 
            
          
  
    
        Fired when a pointing device (usually a mouse) is moved while the cursor is inside the map.
          As you move the cursor across the map, the event will fire every time the cursor changes position within
          the map.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only when the
          the cursor is inside a visible portion of the specified layer.
      
      [Properties](#mousemove-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mousemove-example)
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#mousemove-related)
      
        Get coordinates of the
              mouse pointer
          
        Highlight features under
              the mouse pointer
          
        Display a popup on
              over
          
      
    
  

  mouseout 
            
          
  
    
        Fired when a point device (usually a mouse) leaves the map's canvas.
      
      [Properties](#mouseout-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mouseout-example)
      
      
        ```
``
```

      
    
  

  mouseover 
            
          
  
    
        Fired when a pointing device (usually a mouse) is moved within the map.
          As you move the cursor across a web page containing a map,
          the event will fire each time it enters the map or any child elements.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only when the
          the cursor is moved inside a visible portion of the specifed layer.
      
      [Properties](#mouseover-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mouseover-example)
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#mouseover-related)
      
        Get coordinates of the
              mouse pointer
          
        Highlight features under
              the mouse pointer
          
        Display a popup on
              hover
          
      
    
  

  mouseup 
            
          
  
    
        Fired when a pointing device (usually a mouse) is released within the map.
        **Note:** This event is compatible with the optional `layerId` parameter.
          If `layerId` is included as the second argument in [Map#on](/sdk-js/api/map/#map#on), the event listener will fire only when the
          the cursor is released while inside a visible portion of the specifed layer.
      
      [Properties](#mouseup-properties)
      data`([MapMouseEvent](/sdk-js/api/events/#mapmouseevent))`
      
      [Example](#mouseup-example)
      
      
        ```
``
```

      
      
        ```
``
```

      
      [Related examples](#mouseup-related)
      
      
        Create a draggable
              point
          
      
    
  

  move 
            
          
  
    
        Fired repeatedly during an animated transition from one view to
          another, as the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
      
      [Properties](#move-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#move-example)
      
      
        ```
``
```

      
      [Related examples](#move-related)
      
      
        Display HTML clusters
              with custom properties
          
      
    
  

  moveend 
            
          
  
    
        Fired just after the map completes a transition from one
          view to another, as the result of either user interaction or methods such as [Map#jumpTo](/sdk-js/api/map/#map#jumpto).
      
      [Properties](#moveend-properties)
      data`({originalEvent: [DragEvent](https://developer.mozilla.org/docs/Web/API/DragEvent)})`
      
      [Example](#moveend-example)
      
      
        ```
``
```

      
      [Related examples](#moveend-related)
      
      
        Display HTML clusters
              with custom properties
          
      
    
  

  movestart 
            
          
  
    
        Fired just before the map begins a transition from one
          view to another, as the result of either user interaction or methods such as [Map#jumpTo](/sdk-js/api/map/#map#jumpto).
      
      [Properties](#movestart-properties)
      data`({originalEvent: [DragEvent](https://developer.mozilla.org/docs/Web/API/DragEvent)})`
      
      [Example](#movestart-example)
      
        ```
``
```

      
    
  

  pitch 
            
          
  
    
        Fired repeatedly during the map's pitch (tilt) animation between
          one state and another as the result of either user interaction
          or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
      
      [Properties](#pitch-properties)
      data`(MapEventData)`
      [Example](#pitch-example)
      
      
        ```
``
```

      
    
  

  pitchend 
            
          
  
    
        Fired immediately after the map's pitch (tilt) finishes changing as
          the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
        
      
      [Properties](#pitchend-properties)
      data`(MapEventData)`
      [Example](#pitchend-example)
      
      
        ```
``
```

      
    
  

  pitchstart 
            
          
  
    
        Fired whenever the map's pitch (tilt) begins a change as
          the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto) .
        
      
      [Properties](#pitchstart-properties)
      data`(MapEventData)`
      [Example](#pitchstart-example)
      
        ```
``
```

      
    
  

  projectiontransition 
            
          
  
    
        Fired when map's projection is modified in other ways than by map being moved.
        
      
      [Properties](#projectiontransition-properties)
      data`(MapProjectionEvent)`
      [Example](#projectiontransition-example)
      
        ```
``
```

      
    
  

  ready
        
          
        
         
            
          
  
    
        Called only once after `load` and wait for all the controls managed by 
          the Map constructor to be dealt with (as one relies on async logic).
          
            Since the `ready` event waits that all the basic controls 
            are nicely positioned, it is **safer** to use `ready` than
            `load` if you plan to add other custom comtrols with
             the `.addControl()` method.
          
      
      [Example](#ready-example)
      
      
        ```
``
```

      
      [Related examples](#ready-related)
      
      
        Draw GeoJSON
              points
          
        Add live realtime
              data
          
        Animate a
              point
          
      
    
  

  remove 
            
          
  
    
        Fired immediately after the map has been removed with [Map.event:remove](/sdk-js/api/map/#map.event:remove).
      
      [Example](#evt-remove-example)
      
      
        ```
``
```

      
    
  

  render 
            
          
  
    
        Fired whenever the map is drawn to the screen, as the result of
        
          a change to the map's position, zoom, pitch, or bearing
          a change to the map's style
          a change to a GeoJSON source
          the loading of a vector tile, GeoJSON file, glyph, or sprite
        
      
      [Example](#render-example)
      
      
        ```
``
```

      
    
  

  resize 
            
          
  
    
        Fired immediately after the map has been resized.
      
      [Example](#evt-resize-example)
      
      
        ```
``
```

      
    
  

  rotate 
            
          
  
    
        Fired repeatedly during a "drag to rotate" interaction. See [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler).
      
      [Properties](#rotate-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#rotate-example)
      
      
        ```
``
```

      
    
  

  rotateend 
            
          
  
    
        Fired when a "drag to rotate" interaction ends. See [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler).
      
      [Properties](#rotateend-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#rotateend-example)
      
        ```
``
```

      
    
  

  rotatestart 
            
          
  
    
        Fired when a "drag to rotate" interaction starts. See [DragRotateHandler](/sdk-js/api/handlers/#dragrotatehandler).
      
      [Properties](#rotatestart-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#rotatestart-example)
      
        ```
``
```

      
    
  

  sourcedata 
            
          
  
    
        Fired when one of the map's sources loads or changes, including if a tile belonging
          to a source loads or changes. See [MapDataEvent](/sdk-js/api/events/#mapdataevent)
          for more information.
      
      [Properties](#sourcedata-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#sourcedata-example)
      
        ```
``
```

      
    
  

  sourcedataabort 
            
          
  
    
        Fired when a request for one of the map's sources' data is aborted.
          See [MapDataEvent](/sdk-js/api/events/#mapdataevent) for more information.
      
      [Properties](#sourcedataabort-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#sourcedataabort-example)
      
        ```
``
```

      
    
  

  sourcedataloading 
            
          
  
    
        Fired when one of the map's sources begins loading or changing asyncronously.
          All `sourcedataloading` events are followed by a `sourcedata`,
          `sourcedataabort` or `error`
          event.
          See [MapDataEvent](/sdk-js/api/events/#mapdataevent) for more information.
        
      
      [Properties](#sourcedataloading-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#sourcedataloading-example)
      
        ```
``
```

      
    
  

  styledata 
            
          
  
    
        Fired when the map's style loads or changes. See
          [MapDataEvent](/sdk-js/api/events/#mapdataevent) for more information.
        
      
      [Properties](#styledata-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#styledata-example)
      
        ```
``
```

      
    
  

  styledataloading 
            
          
  
    
        Fired when the map's style begins loading or changing asyncronously.
          All `styledataloading` events are followed by a `styledata`
          or `error` event. See [MapDataEvent](/sdk-js/api/events/#mapdataevent)
          for more information.
      
      [Properties](#styledataloading-properties)
      data`([MapDataEvent](/sdk-js/api/events/#mapdataevent))`
      
      [Example](#styledataloading-example)
      
        ```
``
```

      
    
  

  styleimagemissing 
            
          
  
    
        Fired when an icon or pattern needed by the style is missing. The missing image can
          be added with [Map#addImage](/sdk-js/api/map/#map#addimage) within this event
          listener callback to prevent the image from
          being skipped. This event can be used to dynamically generate icons and patterns.
      
      [Properties](#styleimagemissing-properties)
      id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
          The id of the missing image.
          
      [Example](#styleimagemissing-example)
      
        ```
``
```

      
      [Related examples](#styleimagemissing-related)
      
        Generate
              and add a missing icon to the map
          
      
    
  

  terrain 
            
          
  
    
        Fired when a `terrain`
          event occurs within the map.
      
      [Example](#terrain-example)
      
        ```
``
```

      
    
  

  terrainAnimationStart
        
          
        
         
            
          
  
    
        The `terrainAnimationStart` event is fired 
          when the animation begins transitioning between terrain and non-terrain states. 
        
      
      [Example](#terrainAnimationStart-example)
      
        ```
``
```

      
    
  

  terrainAnimationStop
        
          
        
         
            
          
  
    
        The `terrainAnimationStop` event is fired 
          when the animation between terrain and non-terrain states ends. 
        
      
      [Example](#terrainAnimationStop-example)
      
        ```
``
```

      
    
  

  touchcancel 
            
          
  
    
        Fired when a `touchcancel`
          event occurs within the map.
      
      [Properties](#touchcancel-properties)
      data`([MapTouchEvent](/sdk-js/api/events/#maptouchevent))`
      
      [Example](#touchcancel-example)
      
        ```
``
```

      
    
  

  touchend 
            
          
  
    
        Fired when a `touchend` event
          occurs within the map.
      
      [Properties](#touchend-properties)
      data`([MapTouchEvent](/sdk-js/api/events/#maptouchevent))`
      
      [Example](#touchend-example)
      
      
        ```
``
```

      
      [Related examples](#touchend-related)
      
      
        Create a draggable
              point
          
      
    
  

  touchmove 
            
          
  
    
        Fired when a `touchmove` event
          occurs within the map.
      
      [Properties](#touchmove-properties)
      data`([MapTouchEvent](/sdk-js/api/events/#maptouchevent))`
      
      [Example](#touchmove-example)
      
        ```
``
```

      
      [Related examples](#touchmove-related)
      
        Create a draggable
              point
          
      
    
  

  touchstart 
            
          
  
    
        Fired when a `touchstart` event
          occurs within the map.
      
      [Properties](#touchstart-properties)
      data`([MapTouchEvent](/sdk-js/api/events/#maptouchevent))`
      
      [Example](#touchstart-example)
    
      ```
``
```

    
      [Related examples](#touchstart-related)
      
        Create a draggable
              point
          
      
    
  

  webglcontextlost 
            
          
  
    
        Fired when the WebGL context is lost.
        The maps is rendered with WebGL, that leverages the GPU to provide high-performance graphics. In some cases, the host machine, operating system or the graphics driver, can decide that continuing to run such high performance graphics is unsustainable, and will abort the process. This is called a "WebGL context loss". Such situation happens when the ressources are running low or when multiple browser tabs are competing to access graphics memory.
      
      [Example](#webglcontextlost-example)
      
        ```
``
```

      
    
  

  webglcontextrestored 
            
          
  
    
        Fired when the WebGL context is restored.
      
      [Example](#webglcontextrestored-example)
      
        ```
``
```

      
    
  

  wheel 
            
          
  
    
        Fired when a `wheel`
          event occurs within the map.
      
      [Properties](#wheel-properties)
      data`([MapWheelEvent](/sdk-js/api/events/#mapwheelevent))`
      
      [Example](#wheel-example)
      
      
        ```
``
```

      
    
  

  zoom 
            
          
  
    
        Fired repeatedly during an animated transition from one zoom level to another,
          as the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
      
      [Properties](#zoom-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#zoom-example)
      
      
        ```
``
```

      
    
  

  zoomend 
            
          
  
    
        Fired just after the map completes a transition from one zoom level to another,
          as the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
      
      [Properties](#zoomend-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#zoomend-example)
      
      
        ```
``
```

      
    
  

  zoomstart 
            
          
  
    
        Fired just before the map begins a transition from one zoom level to another,
          as the result of either user interaction or methods such as [Map#flyTo](/sdk-js/api/map/#map#flyto).
      
      [Properties](#zoomstart-properties)
      data`(([MapMouseEvent](/sdk-js/api/events/#mapmouseevent) | [MapTouchEvent](/sdk-js/api/events/#maptouchevent)))`
      
      [Example](#zoomstart-example)
      
        ```
``
```

      
    
  

    ## [Related examples](#map-related)

    
      [Display a map](/sdk-js/examples/add-map/)
