# Source: https://docs.maptiler.com/sdk-js/api/image-viewer/

# 

  
  
  [ src/ImageViewer/ImageViewer.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ImageViewer/ImageViewer.ts)
   

  
      MapTiler's `ImageViewer` component allows you 
        to display tiled, non-georeferenced images but interact with them in almost the same 
        way you would if you were displaying map. 
        These can be handy for zoomable non-georeferenced, 
        geographically "inaccurate" maps such as hotel maps, golf courses, theme parks etc. 
        Think pixels instead of lattitudes and longtidues.
      You create a `ImageViewer` by specifying a `container` and other options.
        Then SDK JS initializes the viewer on the page and returns your `ImageViewer`
        object.
    
    Extends [Evented](/sdk-js/api/events/#evented).
    Example
    ```
``
```

    ## [Parameters](#imageViewer-parameters)

    
      options (ImageViewerConstructorOptions) 
                
              
      
        
            Options to provide to the ImageViewer constructor
            ([ImageViewerConstructorOptions](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ImageViewer/ImageViewer.ts))
          
          [Properties](#imageViewer-options)
          
            
| Define the [MapTiler API key](https://cloud.maptiler.com/account/keys/) to be used.          This is equivalent to setting [`config.apiKey`](/sdk-js/api/config/) and will overwrite it. |
| The HTML element in which SDK JS will render the viewer, or           the element's string           `id`. |
| The unique UUID of the image object you are displaying. |
| The initial centerpoint in pixels of the viewer. |
| The initial zoom level of the viewer. |
| The initial bearing (rotation) of the viewer, measured in degrees           counter-clockwise from north. |
| Whether to show tiles debug information. |
| Whether to show a control to fit the image to the viewport. |
| Whether to show a navigation control. |
| The maximum zoom level of the viewer. |
| The minimum zoom level of the viewer. |

          
        
      
    

    ## [Methods](#imageViewer-instance-members)

  `ImageViewer` provides a subset of methods for interaction with the map. 
  A major caveat is that the `ImageViewer` component works in pixels and not in LngLat. 
  Thus, when using methods such as `setCenter` or 
  `flyTo` the pixel values provided refer to 
  the **absolute pixel position** on the image, not screen pixel position.

  Imagine your image is 10,000px x 10,000px, if regardless if your zoom is 2 or 4, 
  calling `.setCenter(500,500)` will always position the viewer over the same part of the image.

  fitImageBounds(bounds) 
            
          
  
    
        Set the bounds of the image.
        
      
      [Parameters](#fitImageBounds-parameters)
      bounds`([[number, number],[number, number]])`The bounds of the image. The bounds are defined by topLeft and bottomRight corner.
        
      [Returns](#fitImageBounds-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
    
  

  fitImageToViewport(options?) 
            
          
  
    
        Fits the image to the viewport.
        
      
      [Parameters](#fitImageToViewport-parameters)
      options`(object?)`
           Options describing the destination.
        
        
          
| Whether to ease to the viewport bounds.                   Default `false` |

        
      
      [Returns](#fitImageToViewport-returns)
      `void`
      [Example](#fitImageToViewport-example)
      
        ```
``
```

      
    
  

  flyTo(options, eventData?) 
            
          
  
    
        Fly to a given center.
      
      [Parameters](#flyto-parameters)
      
      options`(ImageViewerFlyToOptions)`Options describing the
          destination.
        
        
          
| The given center. |

        
      
      eventData`(MapDataEvent?)`The event data.
        
      [Returns](#flyto-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#flyto-example)
      
      
        ```
``
```

      
    
  

  getBearing() 
            
          
  
    
        Get the bearing of the ImageViewer in degrees.
      
      [Returns](#getbearing-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The viewer's current bearing.
        
    
  

  getCanvas() 
            
          
  
    
        Get the canvas of the internal SDK instance.
      
      [Returns](#getCanvas-returns)
      
      `HTMLCanvasElement`:
        The canvas of the internal SDK instance.
      
    
  

  getCenter() 
            
          
  
    
        Get the center of the ImageViewer in pixels.
      
      [Returns](#getcenter-returns)
      
      `[number, number]`:
        The center of the ImageViewer.
      
      [Example](#getcenter-example)
      
      
        ```
``
```

      
    
  

  getImageBounds() 
            
          
  
    
        Get the visible bounds of the image in the viewport in imagePixels. [topLeft, bottomRight]
      
      [Returns](#getImageBounds-returns)
      
      `[[number, number], [number, number]]`:
        The visible bounds of the image.
      
      [Example](#getImageBounds-example)
      
      
        ```
``
```

      
    
  

  getImageMetadata() 
            
          
  
    
        Get the image metadata.
      
      [Returns](#getImageMetadata-returns)
      
      `ImageMetadata`:
        The [image metadata](/sdk-js/api/types/#ImageMetadata).
      
      [Example](#getImageMetadata-example)
      
      
        ```
``
```

      
    
  

  getZoom() 
            
          
  
    
        Returns the viewer's current zoom level.
      
      [Returns](#getzoom-returns)
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The viewer's current zoom level.
        
      [Example](#getzoom-example)
      
        ```
``
```

      
    
  

  jumpTo(options, eventData?) 
            
          
  
    
        Jump to a given center.
      
      [Parameters](#jumpTo-parameters)
      
      options`(ImageViewerJumpToOptions)`Options describing the
          destination.
        
        
          
| The given center. |

        
      
      eventData`(MapDataEvent?)`The event data.
        
      [Returns](#jumpTo-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#jumpTo-example)
      
      
        ```
``
```

      
    
  

  onReadyAsync() 
            
          
  
    
        Waits for the ImageViewer to be ready.
      
      [Returns](#onReadyAsync-returns)
      `Promise<void>`
      [Example](#onReadyAsync-example)
      
        ```
``
```

      
    
  

  panBy(delta, options?,
          eventData?) 
            
          
  
    
        Pan by a given delta in pixels.
      
      [Parameters](#panby-parameters)
      
      delta`([PointLike](/sdk-js/api/geography/#pointlike))`
          The delta to pan by.
        
      options`(ImageViewerEaseToOptions?)`Options
          object for the pan.
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#panby-returns)
      
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
    
  

  panTo(center, options?,
          eventData?) 
            
          
  
    
        Pan to a given center in pixels.
      
      [Parameters](#panto-parameters)
      
      center`([number, number])`The
          location to pan the map to.
        
      options`(ImageViewerEaseToOptions?)`The options for the pan.
        
      eventData`(any?)`Additional properties to be
          added to event objects of events triggered by this method.
        
      [Returns](#panto-returns)
      
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#panto-example)
      
      
        ```
``
```

      
    
  

  pointIsWithinImageBounds(px)
         
            
          
  
    
        Check if a given point is within the bounds of the image.
      
      [Parameters](#pointIsWithinImageBounds-parameters)
      
      px`([number, number])`The point to be evaluated.
        
      [Returns](#pointIsWithinImageBounds-returns)
      
      `boolean`
      [Example](#pointIsWithinImageBounds-example)
      
      
        ```
``
```

      
    
  

  remove() 
            
          
  
    
        Destroys the ImageViewer, removes the map instance and all event listeners. Useful for cleanup.
      
      [Returns](#remove-returns)
      
      `void`
    
  

  setBearing(bearing) 
            
          
  
    
        Set the bearing of the ImageViewer in degrees..
      
      [Parameters](#setbearing-parameters)
      bearing`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          desired bearing.
        
      [Returns](#setbearing-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#setbearing-example)
      
        ```
``
```

      
    
  

  setCenter(center) 
            
          
  
    
        Set the center of the ImageViewer in pixels.
      
      [Parameters](#setcenter-parameters)
      center`([number, number])`The
          centerpoint to set.
        
      [Returns](#setcenter-returns)
      
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#setcenter-example)
      
      
        ```
``
```

      
    
  

  setZoom(zoom) 
            
          
  
    
        Sets the viewer's zoom level.
        
      
      [Parameters](#setzoom-parameters)
      zoom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
          zoom level to set.
        
      [Returns](#setzoom-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/)`:
        `this`
        
      [Example](#setzoom-example)
      
        ```
``
```

      
    
  

  on(type, listener) 
            
          
  
    
        Adds a listener for events of a specified type.
      
      [Parameters](#on-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          The
          event type to listen for.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`
          The function to be called when the event is `fired`. 
            The listener function is called with the data object passed to fire, 
            extended with `target` and 
            `type` properties.
        
      [Returns](#on-returns)
      [`Subscription`](/sdk-js/api/types/#Subscription)
      [Example](#on-example)
      
        ```
``
```

      
    
  

  off(type, listener) 
            
          
  
    
        Removes a previously registered event listener.
      
      [Parameters](#off-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          The event type to remove listeners for.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
          function previously installed as a listener.
        
      [Returns](#off-returns)
      `[ImageViewer](/sdk-js/api/image-viewer/#imageViewer)`: `this`
        
    
  

  once(type, listener?) 
            
          
  
    
        Adds a listener that will be called only once to a specified event type.
        The listener will be called first time the event fires after the listener is registered.
      
      [Parameters](#once-parameters)
      
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
          The event type to listen for.
        
      listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function)?)`
          The function to be called when the event is fired the first time.
        
      [Returns](#once-returns)
      
      `[ImageViewer](/sdk-js/api/image-viewer/#imageViewer)` | 
      `Promise<any>`
      :
        `this` or a promise if a listener is not provided
        
    
  

    ## [Events](#imageViewer-events)

In a similar manner, a subset of map events are fired by the image viewer. 
  All UI interaction events that would normally include a `LngLat` in the 
  event data instead receive an `imageX` 
  and `imageY` field, representing an absolute pixel position of the image. 
  This is same for `flyTo`, `jumpTo`, 
  `panTo` etc.

A full list of supported events can be found in the exported type declaration 
  [`ImageViewerEventTypes`](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ImageViewer/events.ts)

  imageviewerinit
         
            
          
  
    
        Called only once after the viewer is initialized.
      
      [Example](#imageviewerinit-example)
      
      
        ```
``
```

      
    
  

  imageviewerready
         
            
          
  
    
        Called only once after the viewer is ready.
      
      [Example](#imageviewerready-example)
      
      
        ```
``
```

      
    
  

  imagevieweriniterror 
            
          
  
    
        Fired when an error occurs.
      
      [Properties](#error-properties)
      data`({error: {message: [string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)}})`
      
    
  

    ## [Related examples](#imageViewer-related)

    
      [Display a tiled, non-georeferenced image](/sdk-js/examples/image-viewer/)
        
      
      
        [Add markers to a non-georeferenced image](/sdk-js/examples/image-viewer-marker/)
