# Source: https://docs.maptiler.com/sdk-js/api/properties/

# 

    SDK JS's global properties and options that you can access while initializing your map or accessing
      information about its status.
  
  
    ## [addProtocol](#addprotocol)

    [src/source/protocol_crud.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/protocol_crud.ts)
      Adds a custom load resource function that will be called when using a URL that starts with a custom url schema.
        This will happen in the main thread, and workers might call it if they don't know how to handle the protocol.
        The example below will be triggered for custom:// urls defined in the sources list in the style definitions.
        The function passed will receive the request parameters and should return with the resulting resource,
        for example a pbf vector tile, non-compressed, represented as ArrayBuffer.
    
    [Example](#addprotocol-example)
    
    
      ```
``
```

    
    [Parameters](#addprotocol-parameters)
    customProtocol`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`the
        protocol to hook, for example 'custom'
      
    loadFn`([AddProtocolAction](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/AddProtocolAction/))`the
        function to use when trying to fetch a tile specified by the customProtocol
      
  
  
    ## [addSourceType](#addsurcetype)

    [src/source/source.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/source.ts)
      Adds a custom source type, making it available for use with Map.addSource.
    
    [Parameters](#addsurcetype-parameters)
    name`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
      The name of the source type; source definition objects use this name in the `{type: ...}` field.
      
    
    SourceType`([SourceClass](https://maplibre.org/maplibre-gl-js/docs/API/type-aliases/SourceClass/))`
      
      
    
  
  
    [clearPrewarmedResources](#clearprewarmedresources)
    [src/util/global_worker_pool.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/global_worker_pool.ts)
      Clears up resources that have previously been created by `maptilersdk.prewarm()`.
        Note that this is typically not necessary. You should only call this function
        if you expect the user of your app to not return to a Map view at any point
        in your application.
    
    [Example](#clearprewarmedresources-example)
    
      ```
``
```

    
  
  
    [getMaxParallelImageRequests](#getmaxparallelimagerequests)
    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Gets the maximum number of images (raster tiles, sprites, icons) to load in parallel,
        which affects performance in raster-heavy maps. 16 by default.
    
    [Example](#getmaxparallelimagerequests-example)
    
      ```
``
```

    
    [Returns](#getmaxparallelimagerequests-returns)
    `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
      Number of parallel requests currently configured.
      
  
  
    [getRTLTextPluginStatus](#getrtltextpluginstatus)
    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts#L263-L263)
      Gets the map's RTL text
          plugin
        status.
        The status can be `unavailable` (i.e. not requested or removed), `loading`,
        `loaded` or `error`.
        If the status is `loaded` and the plugin is requested again, an error will
        be thrown.
      
    
    [Example](#getrtltextpluginstatus-example)
    
      ```
``
```

    
  
  
    ## [getVersion](#getversion)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Returns the package version of the library.
    
    [Example](#getversion-example)
    
    
      ```
``
```

    
  
  
    ## [getWorkerCount](#getworkercount)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Gets the number of web workers instantiated on a page with GL JS maps.
        By default, workerCount is 1 except for Safari browser where it is set to half the number of CPU cores (capped
        at 3).
        Make sure to set this property before creating any map instances for it to have effect.
      
    
    [Example](#getworkercount-example)
    
      ```
``
```

    
    [Returns](#getworkercount-returns)
    `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
      Number of workers currently configured.
      
  
  
    ## [getWorkerUrl](#getworkerurl)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Gets the worker url
      
    
    [Returns](#getworkerurl-returns)
    `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`:
      The worker url.
      
  
  
    [getWebGLSupportError](#getWebGLSupportError)
    [src/index.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/index.ts)
      Detect WebGL compatibility
      
    
    [Returns](#getWebGLSupportError-returns)
    `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`
    |
    `[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null)`:
      Return `null` if there is no error (WebGL is supported), or returns a
        string with the error message if WebGL2 is not supported.
      
  
  
    [importScriptInWorkers](#importscriptinworkers)
    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Allows loading javascript code in the worker thread.
        Note that since this is using some very internal classes and flows it is considered experimental and can break
        at any point.
      
      It can be useful for the following examples:
        
          Using `self.addProtocol` in the worker thread -
            note that you might need to also register the protocol on the main thread.
          Using `self.registerWorkerSource(workerSource: WorkerSource)` to
            register a worker source,
            which sould come with `addSourceType` usually
          Using `self.actor.registerMessageHandler` to override some internal
            worker operations
        
      
    
    [Example](#importscriptinworkers-example)
    
      ```
``
```

    
    [Parameters](#importscriptinworkers-parameters)
    workerUrl`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
      The worker url e.g. a url of a javascript file to load in the worker
      
    
    [Returns](#importscriptinworkers-returns)
    `Promise<void[]>`
  
  
    ## [prewarm](#prewarm)

    [src/util/global_worker_pool.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/global_worker_pool.ts)
      Initializes resources like WebWorkers that can be shared across maps to lower load
        times in some situations. `maptilersdk.workerUrl` and `maptilersdk.workerCount`, if being
        used, must be set before `prewarm()` is called to have an effect.
      By default, the lifecycle of these resources is managed automatically, and they are
        lazily initialized when a Map is first created. By invoking `prewarm()`,
        these
        resources will be created ahead of time, and will not be cleared when the last Map
        is removed from the page. This allows them to be re-used by new Map instances that
        are created later. They can be manually cleared by calling
        `maptilersdk.clearPrewarmedResources()`. This is only necessary if your
        web page remains
        active but stops using maps altogether.
      
      This is primarily useful when using GL-JS maps in a single page app, wherein a user
        would navigate between various views that can cause Map instances to constantly be
        created and destroyed.
    
    [Example](#prewarm-example)
    
    
      ```
``
```

    
  
  
    ## [removeProtocol](#removeprotocol)

    [src/source/protocol_crud.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/source/protocol_crud.ts)
      Removes a previously added protocol
    
    [Example](#removeprotocol-example)
    
      ```
``
```

    
    [Parameters](#removeprotocol-parameters)
    customProtocol`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`the
        custom protocol to remove registration for
      
  
  
    [setMaxParallelImageRequests](#getmaxparallelimagerequests)
    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Sets the maximum number of images (raster tiles, sprites, icons) to load in parallel, which affects performance
        in raster-heavy maps. 16 by default.
    
    [Example](#setmaxparallelimagerequests-example)
    
      ```
``
```

    
    [Parameters](#setmaxparallelimagerequests-parameters)
    numRequests`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
      The maximum number of images to load in parallel.
      
    
  
  
    [setRTLTextPlugin](#setrtltextplugin)
    
    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts#L263-L263)
      Sets the map's RTL text
          plugin.
        Necessary for supporting the Arabic and Hebrew languages, which are written right-to-left.
    
    [Example](#setrtltextplugin-example)
    
      ```
``
```

    
    [Parameters](#setrtltextplugin-parameters)
    pluginURL`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`URL
        pointing to the MapLibre RTL text plugin source.
      
    callback`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`Called
        with an error argument if there is an error.
      
    lazy`([boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean))`If
        set to
        `true`
        , maplibregl will defer loading the plugin until rtl text is encountered,
        rtl text will then be rendered only after the plugin finishes loading.
      
  
  
    ## [setWorkerCount](#setworkercount)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Sets the number of web workers instantiated on a page with GL JS maps.
        By default, workerCount is 1 except for Safari browser where it is set to half the number of CPU cores (capped
        at 3).
        Make sure to set this property before creating any map instances for it to have effect.
      
    
    [Example](#setworkercount-example)
    
      ```
``
```

    
    [Parameters](#setworkercount-parameters)
    count`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
      The number of workers.
      
    
  
  
    ## [setWorkerUrl](#setworkerurl)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts)
      Sets the worker url
      
    
    [Parameters](#setworkerurl-parameters)
    value`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
      The worker url.
      
    
  
  
    ## [clearStorage](#clearstorage)

    [src/index.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/index.ts#L163-L165)
      Clears browser storage used by this library. Using this method flushes the SDK JS tile
        cache that is managed by this library. Tiles may still be cached by the browser
        in some cases.
      This API is supported on browsers where the `Cache`
          API
        is supported and enabled. This includes all major browsers when pages are served over
        `https://`, except Internet Explorer and Edge Mobile.
      
      When called in unsupported browsers or environments (private or incognito mode), the
        callback will be called with an error argument.
    
    [Example](#clearstorage-example)
    
      ```
``
```

    
    [Parameters](#clearstorage-parameters)
    callback`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`Called
        with an error argument if there is an error.
      
  
  
    [AnimationOptions](#animationoptions)
    
    [src/ui/camera.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/camera.ts#L103-L116)
      Options common to map movement methods that involve animation, such as [Map#panBy](/sdk-js/api/map/#map#panby) and
        [Map#easeTo](/sdk-js/api/map/#map#easeto), controlling the duration and easing function
        of the animation. All properties
        are optional.
      
    
    [Properties](#animationoptions-properties)
    duration`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
        The animation's duration, measured in milliseconds.
        
    easing`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`:
        A function taking a time in the range 0..1 and returning a number where 0 is
          the initial state and 1 is the final state. Default is a `bezier-curve`
          function with
          control points (0.25, 0.1) and (0.25, 1). Example:
          ```
``
```

        
    offset`([PointLike](/sdk-js/api/geography/#pointlike))`:
        of the target center relative to real map container center at the end of animation.
        
    animate`([boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean))`:
        If
          `false`
          , no animation will occur.
        
    essential`([boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean))`:
        If
          `true`
          , then the animation is considered essential and will not be affected by

          `prefers-reduced-motion`
          .
        
  
  
    ## [CameraOptions](#cameraoptions)

    [src/ui/camera.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/camera.ts#L29-L59)
      Options common to [Map#jumpTo](/sdk-js/api/map/#map#jumpto), [Map#easeTo](/sdk-js/api/map/#map#easeto), and [Map#flyTo](/sdk-js/api/map/#map#flyto),
        controlling the desired location,
        zoom, bearing, and pitch of the camera. All properties are optional, and when a property is omitted, the current
        camera value for that property will remain unchanged.
    
    [Example](#cameraoptions-example)
    
      ```
``
```

    
    [Properties](#cameraoptions-properties)
    center`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`:
        The desired center.
        
    zoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
        The desired zoom level.
        
    bearing`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
        The desired bearing in degrees. The bearing is the compass direction that
          is "up". For example,
          `bearing: 90`
          orients the map so that east is up.
        
    pitch`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
        The desired pitch in degrees. The pitch is the angle towards the horizon
          measured in degrees with a range between 0 and 60 degrees. For example, pitch: 0 provides the appearance
          of looking straight down at the map, while pitch: 60 tilts the user's perspective towards the horizon.
          Increasing the pitch value is often used to display 3D objects.
        
    around`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`:
        If
          `zoom`
          is specified,
          `around`
          determines the point around which the zoom is centered.
        
    padding`([PaddingOptions](/sdk-js/api/properties/#paddingoptions))`:
        Dimensions in pixels applied on each side of the viewport for shifting the vanishing point.
        
    Related
        examples
    
      [Set pitch and bearing](/sdk-js/examples/set-perspective/)
        
      [Jump to a series of locations](/sdk-js/examples/jump-to/)
        
      [Fly to a location](/sdk-js/examples/flyto/)
        
      [Display buildings in 3D](/sdk-js/examples/3d-buildings/)
        
    
  
  
    ## [PaddingOptions](#paddingoptions)

    [src/geo/edge_insets.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/edge_insets.ts#L99-L116)
      Options for setting padding on calls to methods such as [Map#fitBounds](/sdk-js/api/map/#map#fitbounds), [Map#fitScreenCoordinates](/sdk-js/api/map/#map#fitscreencoordinates), and [Map#setPadding](/sdk-js/api/map/#map#setpadding). Adjust these options to set the amount
        of padding in pixels added to the edges of the canvas. Set a uniform padding on all edges or individual values
        for each edge. All properties of this object must be
        non-negative integers.
    
    [Example](#paddingoptions-example)
    
      ```
``
```

    
    
      ```
``
```

    
    [Properties](#paddingoptions-properties)
    top`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
    
    bottom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
    
    right`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
    
    left`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
    
    [Static Members](#paddingoptions-static-members)
    
      bottom 
                
              
      
        
          [Properties](#bottom-properties)
          bottom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
              Padding in pixels from the bottom of the map canvas.
              
        
      
    
    
      left 
                
              
      
        
          [Properties](#left-properties)
          
          right`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
              Padding in pixels from the right of the map canvas.
              
        
      
    
    
      right 
                
              
      
        
          [Properties](#right-properties)
          left`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
              Padding in pixels from the left of the map canvas.
              
        
      
    
    
      top 
                
              
      
        
          [Properties](#top-properties)
          
          top`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`:
              Padding in pixels from the top of the map canvas.
              
        
      
    
    [Related examples](#paddingoptions-related)
    
      Fit to the bounds of a
            LineString
        
      [Fit a map to a bounding box](/sdk-js/examples/fitbounds/)
        
    
  
  
    [RequestParameters](#requestparameters)
    [src/util/ajax.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/ajax.ts#L42-L64)
      A `RequestParameters` object to be returned from
        Map.options.transformRequest callbacks.
    
    [Example](#requestparameters-example)
    
      ```
``
```

    
    [Properties](#requestparameters-properties)
    url`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
        The URL to be requested.
        
    headers`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object))`:
        The headers to be sent with the request.
        
    method`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
        Request method
          `'GET' | 'POST' | 'PUT'`
          .
        
    body`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
        Request body.
        
    type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
        Response body type to be returned
          `'string' | 'json' | 'arrayBuffer'`
          .
        
    credentials`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
        `'same-origin'|'include'`
          Use 'include' to send cookies with cross-origin requests.
        
    collectResourceTiming`([boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean))`:
        If true, Resource Timing API information will be collected for these transformed requests and returned in
          a resourceTiming property of relevant data events.
        
  
  
    [StyleImageInterface](#styleimageinterface)
    [src/style/style_image.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/style/style_image.ts#L75-L125)
      Interface for dynamically generated style images. This is a specification for
        implementers to model: it is not an exported method or class.
      Images implementing this interface can be redrawn for every frame. They can be used to animate
        icons and patterns or make them respond to user input. Style images can implement a
        [StyleImageInterface#render](/sdk-js/api/properties/#styleimageinterface#render) method.
        The method is called every frame and
        can be used to update the image.
      
    
    [Example](#styleimageinterface-example)
    
      ```
``
```

    
    [Methods](#styleimageinterface-instance-members)
    
      data 
                
              
      
        
          [Properties](#data-properties)
          
          data`(([Uint8Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | [Uint8ClampedArray](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)))`
          
        
      
    
    
      height 
                
              
      
        
          [Properties](#height-properties)
          height`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
          
        
      
    
    
      onAdd(map) 
                
              
      
        
            Optional method called when the layer has been added to the Map with [Map#addImage](/sdk-js/api/map/#map#addimage).
          
          [Parameters](#onadd-styleimageinterface-parameters)
          map`([Map](/sdk-js/api/map/#map))`The
              Map this custom layer was just added to.
            
        
      
    
    
      onRemove() 
                
              
      
        
            Optional method called when the icon is removed from the map with [Map#removeImage](/sdk-js/api/map/#map#removeimage).
              This gives the image a chance to clean up resources and event listeners.
          
      
    
    
      render() 
                
              
      
        
            This method is called once before every frame where the icon will be used.
              The method can optionally update the image's `data` member with a
              new image.
            If the method updates the image it must return `true` to commit the
              change.
              If the method returns `false` or nothing the image is assumed to not
              have changed.
            If updates are infrequent it maybe easier to use [Map#updateImage](/sdk-js/api/map/#map#updateimage) to update
              the image instead of implementing this method.
          
          [Returns](#render-styleimageinterface-returns)
          
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if this method updated the image.
              `false`
              if the image was not changed.
            
        
      
    
    
      width 
                
              
      
        
          [Properties](#width-properties)
          width`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`
          
        
      
    
    [Related examples](#styleimageinterface-related)
    
      Add an animated icon to
            the map.
        
    
  
  
    [CustomLayerInterface](#customlayerinterface)
    [src/style/style_layer/custom_style_layer.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/style/style_layer/custom_style_layer.ts#L73-L157)
      Interface for custom style layers. This is a specification for
        implementers to model: it is not an exported method or class.
      Custom layers allow a user to render directly into the map's GL context using the map's camera.
        These layers can be added between any regular layers using [Map#addLayer](/sdk-js/api/map/#map#addlayer).
      Custom layers must have a unique `id` and must have the `type` of `"custom"`.
        They must implement `render` and may implement `prerender`, `onAdd` and
        `onRemove`.
        They can trigger rendering using [Map#triggerRepaint](/sdk-js/api/map/#map#triggerrepaint)
        and they should appropriately handle [Map.event:webglcontextlost](/sdk-js/api/map/#map.event:webglcontextlost) and
        [Map.event:webglcontextrestored](/sdk-js/api/map/#map.event:webglcontextrestored).
      
      The `renderingMode` property controls whether the layer is treated as a
        `"2d"` or
        `"3d"` map layer. Use:
      
      
        `"renderingMode": "3d"` to use the depth buffer and share it with
          other layers
        `"renderingMode": "2d"` to add a layer with no depth. If you need to
          use the depth buffer for a
          `"2d"` layer you must use an offscreen
          framebuffer and [CustomLayerInterface#prerender](/sdk-js/api/properties/#customlayerinterface#prerender)
        
      
    
    [Example](#customlayerinterface-example)
    
      ```
``
```

    
    [Methods](#customlayerinterface-instance-members)
    
      id 
                
              
      
        
          [Properties](#id-properties)
          
          id`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
              A unique layer id.
              
        
      
    
    
      onAdd(map,
              gl) 
                
              
      
        
            Optional method called when the layer has been added to the Map with [Map#addLayer](/sdk-js/api/map/#map#addlayer). This
              gives the layer a chance to initialize gl resources and register event listeners.
          
          [Parameters](#onadd-customlayerinterface-parameters)
          map`([Map](/sdk-js/api/map/#map))`The
              Map this custom layer was just added to.
            
          gl`([WebGLRenderingContext](https://developer.mozilla.org/docs/Web/API/WebGLRenderingContext))`The
              gl context for the map.
            
        
      
    
    
      onRemove(map,
              gl) 
                
              
      
        
            Optional method called when the layer has been removed from the Map with [Map#removeLayer](/sdk-js/api/map/#map#removelayer). This
              gives the layer a chance to clean up gl resources and event listeners.
          
          [Parameters](#onremove-customlayerinterface-parameters)
          map`([Map](/sdk-js/api/map/#map))`The
              Map this custom layer was just added to.
            
          gl`([WebGLRenderingContext](https://developer.mozilla.org/docs/Web/API/WebGLRenderingContext))`The
              gl context for the map.
            
        
      
    
    
      prerender(gl, matrix) 
                
              
      
        
            Optional method called during a render frame to allow a layer to prepare resources or render into a
              texture.
            The layer cannot make any assumptions about the current GL state and must bind a framebuffer before
              rendering.
          
          [Parameters](#prerender-parameters)
          gl`([WebGLRenderingContext](https://developer.mozilla.org/docs/Web/API/WebGLRenderingContext))`The
              map's gl context.
            
          matrix`(mat4)`The map's
              camera matrix. It projects spherical mercator
              coordinates to gl coordinates. The mercator coordinate
              `[0, 0]`
              represents the
              top left corner of the mercator world and
              `[1, 1]`
              represents the bottom right corner. When
              the
              `renderingMode`
              is
              `"3d"`
              , the z coordinate is conformal. A box with identical x, y, and z
              lengths in mercator units would be rendered as a cube.
              [MercatorCoordinate](/sdk-js/api/geography/#mercatorcoordinate)
              .fromLngLat
              can be used to project a
              `LngLat`
              to a mercator coordinate.
            
        
      
    
    
      render(gl,
              matrix) 
                
              
      
        
            Called during a render frame allowing the layer to draw into the GL context.
            The layer can assume blending and depth state is set to allow the layer to properly
              blend and clip other layers. The layer cannot make any other assumptions about the
              current GL state.
            If the layer needs to render to a texture, it should implement the `prerender` method
              to do this and only use the `render` method for drawing directly
              into the main framebuffer.
            The blend function is set to `gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA)`. This expects
              colors to be provided in premultiplied alpha form where the `r`,
              `g` and
              `b` values are already
              multiplied by the `a` value. If you are unable to provide colors in
              premultiplied form you
              may want to change the blend function to
              `gl.blendFuncSeparate(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA, gl.ONE, gl.ONE_MINUS_SRC_ALPHA)`.
            
          
          [Parameters](#render-customlayerinterface-parameters)
          gl`([WebGLRenderingContext](https://developer.mozilla.org/docs/Web/API/WebGLRenderingContext))`The
              map's gl context.
            
          matrix`([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>)`The
              map's camera matrix. It projects spherical mercator
              coordinates to gl coordinates. The spherical mercator coordinate
              `[0, 0]`
              represents the
              top left corner of the mercator world and
              `[1, 1]`
              represents the bottom right corner. When
              the
              `renderingMode`
              is
              `"3d"`
              , the z coordinate is conformal. A box with identical x, y, and z
              lengths in mercator units would be rendered as a cube.
              [MercatorCoordinate](/sdk-js/api/geography/#mercatorcoordinate)
              .fromLngLat
              can be used to project a
              `LngLat`
              to a mercator coordinate.
            
        
      
    
    
      renderingMode 
                
              
      
        
          [Properties](#renderingmode-properties)
          renderingMode`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
              Either
                `"2d"`
                or
                `"3d"`
                . Defaults to
                `"2d"`
                .
              
        
      
    
    
      type 
                
              
      
        
          [Properties](#type-properties)
          
          type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`:
              The layer's type. Must be
                `"custom"`
                .
