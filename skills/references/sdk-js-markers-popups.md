# Source: https://docs.maptiler.com/sdk-js/api/markers/

# 

  
    
      Elements that can be added to the map. The items in this section exist
      outside of the map's
      `canvas` element.
    
  

  
  
    [Marker](#marker)
  
  
    [src/ui/marker.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/marker.ts#L56-L685)
  
  
    Creates a marker component
  
  
    Extends [Evented](/sdk-js/api/events/#evented).
  
  
    [Example](#marker-example)
  
  
    ```
``
```

  
  
    ```
``
```

  
  
    [Parameters](#marker-parameters)
  
  
    options(Object?)
    
      
| A string indicating the part of the Marker that should be                 positioned closest to the coordinate set via                 [Marker#setLngLat](/sdk-js/api/markers/#marker#setlnglat)                 . Options are                 `'center'`                 ,                 `'top'`                 ,                 `'bottom'`                 ,                 `'left'`                 ,                 `'right'`                 ,                 `'top-left'`                 ,                 `'top-right'`                 ,                 `'bottom-left'`                 , and                 `'bottom-right'`                 . |
| Space-separated CSS class names to add to marker element. |
| The max number of pixels a user can shift the mouse pointer                 during a click on the marker for it to be considered a valid                 click (as opposed to a marker drag). The default is to inherit                 map's clickTolerance. |
| The color to use for the default marker if options.element is                 not provided. The default is light blue. |
| A boolean indicating whether or not a marker is able to be                 dragged to a new position on the map. |
| DOM element to use as a marker. The default is a light blue,                 droplet-shaped SVG marker. |
| The offset in pixels as a                 [PointLike](/sdk-js/api/geography/#pointlike)                 object to apply relative to the element's center. Negatives                 indicate left and up. |
| Marker's opacity when it's in clear view (not behind 3d terrain).                  The default is `1` |
| Marker's opacity when it's behind 3d terrain.                  The default is `0.2` |
| `map`                 aligns the                 `Marker`                 to the plane of the map.                 `viewport`                 aligns the                 `Marker`                 to the plane of the viewport.                 `auto`                 automatically matches the value of                 `rotationAlignment`                 . |
| The rotation angle of the marker in degrees, relative to its                 respective                 `rotationAlignment`                 setting. A positive value will rotate the marker clockwise. |
| `map`                 aligns the                 `Marker`                 's rotation relative to the map, maintaining a bearing as the                 map rotates.                 `viewport`                 aligns the                 `Marker`                 's rotation relative to the viewport, agnostic to map                 rotations.                 `auto`                 is equivalent to                 `viewport`                 . |
| The scale to use for the default marker if options.element is                 not provided. The default scale corresponds to a height of                 `41px`                 and a width of                 `27px`                 . |

    
  
  
    legacyOptions`(MarkerOptions?)`
  
  
    [Methods](#marker-instance-members)
  
  
    
      addClassName(className)
            
              
            
    
    
      
        
          Adds a CSS class to the marker element.
        
        
          [Parameters](#addclassname-marker-parameters)
        
        
          className(string)
          Non-empty string with CSS class name to add to marker element.
          
        
        
          [Example](#addclassname-marker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      addTo(map)
            
              
            
    
    
      
        
          
            Attaches the `Marker` to a
            `Map` object.
          
        
        
          [Parameters](#addto-marker-parameters)
        
        
          map([Map](/sdk-js/api/map/#map))The SDK JS map to add the marker to. 
        
        
          [Returns](#addto-marker-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
        
          [Example](#addto-marker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      getElement()
            
              
            
    
    
      
        
          
            Returns the `Marker`'s HTML
            element.
          
        
        
          [Returns](#getelement-marker-returns)
        
        HTMLElement: element 
      
    
  
  
    
      getLngLat()
            
              
            
    
    
      
        
          Get the marker's geographical location.
          
            The longitude of the result may differ by a multiple of 360
            degrees from the longitude previously set by
            `setLngLat` because
            `Marker` wraps the anchor
            longitude across copies of the world to keep the marker on screen.
          
        
        
          [Returns](#getlnglat-marker-returns)
        
        [LngLat](/sdk-js/api/geography/#lnglat):
          A
            [LngLat](/sdk-js/api/geography/#lnglat)
            describing the marker's location.
          
        
          [Example](#getlnglat-marker-example)
        
        
          ```
``
```

        
        
          [Related examples](#getlnglat-marker-related)
        
        
          
            [Create a draggable Marker](/sdk-js/examples/drag-a-marker/)
            
          
        
      
    
  
  
    
      getOffset()
            
              
            
    
    
      
        
          Get the marker's offset.
        
        
          [Returns](#getoffset-returns)
        
        `Point`: The marker's screen coordinates in
            pixels. 
      
    
  
  
    
      getPitchAlignment()
            
              
            
    
    
      
        
          
            Returns the current
            `pitchAlignment` property of
            the marker.
          
        
        
          [Returns](#getpitchalignment-returns)
        
        string:
          The current pitch alignment of the marker in degrees.
          
      
    
  
  
    
      getPopup()
            
              
            
    
    
      
        
          
            Returns the
            [Popup](/sdk-js/api/markers/#popup) instance that is
            bound to the [Marker](/sdk-js/api/markers/#marker).
          
        
        
          [Returns](#getpopup-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          popup 
        
          [Example](#getpopup-example)
        
        
          ```
``
```

        
      
    
  
  
    
      getRotation()
            
              
            
    
    
      
        
          
            Returns the current rotation angle of the marker (in degrees).
          
        
        
          [Returns](#getrotation-returns)
        
        number: The current rotation angle of the marker. 
      
    
  
  
    
      getRotationAlignment()
            
              
            
    
    
      
        
          
            Returns the current
            `rotationAlignment` property
            of the marker.
          
        
        
          [Returns](#getrotationalignment-returns)
        
        string:
          The current rotational alignment of the marker. 
      
    
  
  
    
      isDraggable()
            
              
            
    
    
      
        
          Returns true if the marker can be dragged
        
        
          [Returns](#isdraggable-returns)
        
        boolean: True if the marker is draggable. 
      
    
  
  
    listens(type) 
              
            
    
      
          Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the specified type.
        
        [Parameters](#listens-marker-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
            The event type.
        
        [Returns](#listens-marker-returns)
        
        `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
          `true` if there is at least one registered listener 
            for specified event type, `false` otherwise
          
      
    
  
  
    off(type, listener) 
              
            
    
      
          Removes a previously registered event listener.
        
        [Parameters](#off-marker-parameters)
        
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
            event type previously used to install the listener.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
            function previously installed as a listener.
          
        [Returns](#off-marker-returns)
        `[Marker](/sdk-js/api/markers/#marker)`: `this`
          
      
    
  
  
    on(type, layer, listener) 
              
            
    
      
          Adds a listener for events of a specified type, optionally limited to features in a specified style
            layer.
        
        [Parameters](#on-marker-parameters)
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
            The event type to add a listen for.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`
            The function to be called when the event is fired. 
              The listener function is called with the data object passed to `fire`, 
              extended with `target` and `type` properties
          
          [Returns](#on-marker-returns)
          `[Marker](/sdk-js/api/markers/#marker)`: `this`
            
      
    
  
  
    once(type, listener?) 
              
            
    
      
          Adds a listener that will be called only once to a specified event type.
          The listener will be called first time the event fires after the listener is registered.
        
        [Parameters](#once-marker-parameters)
        
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)?)`The
            event type to listen for.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`
            The function to be called when the event is fired the first time.
          
          [Returns](#once-marker-returns)
          `([Marker](/sdk-js/api/markers/#marker) | Promise	<any> )`: `this` or a promise if a listener is not provided
            
      
    
  
  
    
      remove()
            
              
            
    
    
      
        
          Removes the marker from a map
        
        
          [Returns](#remove-marker-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
        
          [Example](#remove-marker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      removeClassName(className)
            
              
            
    
    
      
        
          Removes a CSS class from the marker element.
        
        
          [Parameters](#removeclassname-marker-parameters)
        
        
          className(string)
          Non-empty string with CSS class name to remove from marker element.
          
        
        
          [Example](#removeclassname-marker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      setDraggable(shouldBeDraggable)
            
              
            
    
    
      
        
          
            Sets the
            `draggable` property and
            functionality of the marker
          
        
        
          [Parameters](#setdraggable-parameters)
        
        
          shouldBeDraggable(boolean)(default `false`)Turns drag
            functionality on/off 
        
        
          [Returns](#setdraggable-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
      
    
  
  
    
      setLngLat(lnglat)
            
              
            
    
    
      
        
          Set the marker's geographical position and move it.
        
        
          [Parameters](#setlnglat-marker-parameters)
        
        
          lnglat([LngLat](/sdk-js/api/geography/#lnglat))A
            [LngLat](/sdk-js/api/geography/#lnglat)
            describing where the marker should be located.
          
        
        
          [Returns](#setlnglat-marker-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
        
          [Example](#setlnglat-marker-example)
        
        
          ```
``
```

        
        
          [Related examples](#setlnglat-marker-related)
        
        
          
            [Add custom icons with Markers](/sdk-js/examples/custom-marker-icons/)
            
          
          
            [Create a draggable Marker](/sdk-js/examples/drag-a-marker/)
            
          
        
      
    
  
  
    
      setOffset(offset)
            
              
            
    
    
      
        
          Sets the offset of the marker
        
        
          [Parameters](#setoffset-marker-parameters)
        
        
          offset([PointLike](/sdk-js/api/geography/#pointlike))The offset in pixels as a
            [PointLike](/sdk-js/api/geography/#pointlike)
            object to apply relative to the element's center. Negatives
            indicate left and up.
          
        
        
          [Returns](#setoffset-marker-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
      
    
  
  
    
      setPitchAlignment(alignment?)
            
              
            
    
    
      
        
          
            Sets the
            `pitchAlignment` property of
            the marker.
          
        
        
          [Parameters](#setpitchalignment-parameters)
        
        
          alignment(string?)Sets the
            `pitchAlignment`
            property of the marker. If alignment is 'auto', it will
            automatically match
            `rotationAlignment`
            .
          
        
        
          [Returns](#setpitchalignment-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
      
    
  
  
    
      setPopup(popup?)
            
              
            
    
    
      
        
          
            Binds a [Popup](/sdk-js/api/markers/#popup) to the
            [Marker](/sdk-js/api/markers/#marker).
          
        
        
          [Parameters](#setpopup-parameters)
        
        
          popup(([Popup](/sdk-js/api/markers/#popup) | null)?)An instance of the
            [Popup](/sdk-js/api/markers/#popup)
            class. If undefined or null, any popup set on this
            [Marker](/sdk-js/api/markers/#marker)
            instance is unset.
          
        
        
          [Returns](#setpopup-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
        
          [Example](#setpopup-example)
        
        
          ```
``
```

        
        
          [Related examples](#setpopup-related)
        
        
          
            [Attach a popup to a marker instance](/sdk-js/examples/set-popup/)
            
          
        
      
    
  
  
    
      setRotation(rotation)
            
              
            
    
    
      
        
          
            Sets the `rotation` property
            of the marker.
          
        
        
          [Parameters](#setrotation-parameters)
        
        
          rotation(number)(default `0`)The rotation angle of the
            marker (clockwise, in degrees),
            relative to its respective
            [Marker#setRotationAlignment](/sdk-js/api/markers/#marker#setrotationalignment)
            setting.
          
        
        
          [Returns](#setrotation-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
      
    
  
  
    
      setRotationAlignment(alignment)
            
              
            
    
    
      
        
          
            Sets the
            `rotationAlignment` property
            of the marker.
          
        
        
          [Parameters](#setrotationalignment-parameters)
        
        
          alignment(string)(default `'auto'`)Sets the
            `rotationAlignment`
            property of the marker.
          
        
        
          [Returns](#setrotationalignment-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
      
    
  
  
    
      toggleClassName(className)
            
              
            
    
    
      
        
          Add or remove the given CSS class on the marker element, depending on whether the element currently has that class.
        
        
          [Parameters](#toggleclassName-marker-parameters)
        
        
          className(string)
          Non-empty string with CSS class name to add/remove.
          
        
        
          [Returns](#toggleclassName-marker-returns)
        
        `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
          if the class was removed return `false`, 
            if class was added, then return `true`
        
          [Example](#toggleclassName-marker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      togglePopup()
            
              
            
    
    
      
        
          
            Opens or closes the
            [Popup](/sdk-js/api/markers/#popup) instance that is
            bound to the [Marker](/sdk-js/api/markers/#marker),
            depending on the current state of the
            [Popup](/sdk-js/api/markers/#popup).
          
        
        
          [Returns](#togglepopup-returns)
        
        `[Marker](/sdk-js/api/markers/#marker)`:
          `this` 
        
          [Example](#togglepopup-example)
        
        
          ```
``
```

        
      
    
  
  
    [Events](#marker-events)
  
  
    
      drag
            
              
            
    
    
      
        
          Fired while dragging
        
        
          [Properties](#drag-properties)
        
        
          marker([Marker](/sdk-js/api/markers/#marker)): object that is being dragged 
        
      
    
  
  
    
      dragend
            
              
            
    
    
      
        
          Fired when the marker is finished being dragged
        
        
          [Properties](#dragend-properties)
        
        
          marker([Marker](/sdk-js/api/markers/#marker)): object that was dragged 
        
      
    
  
  
    
      dragstart
            
              
            
    
    
      
        
          Fired when dragging starts
        
        
          [Properties](#dragstart-properties)
        
        
          marker([Marker](/sdk-js/api/markers/#marker)): object that is being dragged 
        
      
    
  
  
    [Related examples](#marker-related)
  
  
    
      [Add custom icons with Markers](/sdk-js/examples/custom-marker-icons/)
      
    
    
      [Create a draggable Marker](/sdk-js/examples/drag-a-marker/)
      
    
  

  
  
    [ImageViewerMarker](#imageViewerMarker)
  
  
    [src/ImageViewer/ImageViewerMarker.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ImageViewer/ImageViewerMarker.ts)
  
  
    Creates a ImageViewerMarker component. 
      This is, for all intents and purposes, the same as `Marker` 
      with the exception of **working in image pixels**, not *lat/lon*. 
      It composes the the internal logic of the Marker class so the behaviour should be exactly the same.
  
  
    Extends [Evented](/sdk-js/api/events/#evented).
  
  
    [Example](#imageViewerMarker-example)
  
  
    ```
``
```

  
  
    ```
``
```

  
  
  
    [Methods](#imageViewerMarker-instance-members)
  
  
    Lists the methods that are different or exclusive to the `ImageViewerMarker` class. 
    For the complete list of methods, check out [Marker.Methods](/sdk-js/api/markers/#marker-instance-members) 
  
  
    
      addTo(viewer)
            
              
            
    
    
      
        
          
            Attaches the `ImageViewerMarker` to a
            `ImageViewer` instance.
          
        
        
          [Parameters](#addTo-imageViewerMarker-parameters)
        
        
          viewer([ImageViewer](/sdk-js/api/image-viewer))The SDK JS imageViewer to add the marker to. 
        
        
          [Returns](#addTo-imageViewerMarker-returns)
        
        `[ ImageViewerMarker](/sdk-js/api/markers/#imageViewerMarker)`:
          `this` 
        
          [Example](#addTo-imageViewerMarker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      getPosition()
            
              
            
    
    
      
        
          Gets the position of the ImageViewerMarker. 
            This is the equivalent of the `getLngLat` function 
            of the markers on the map
        
        
          [Returns](#getPosition-imageViewerMarker-returns)
        
        [PointLike](/sdk-js/api/geography/#pointlike):
          A Point or an array [number, number] of two numbers representing x and y screen coordinates in pixels.
          
        
          [Example](#getPosition-imageViewerMarker-example)
        
        
          ```
``
```

        
      
    
  
  
    
      setPosition(px)
            
              
            
    
    
      
        
          Sets the position of the ImageViewerMarker.
            This is the equivalent of the `setLngLat` function 
            of the markers on the map
          
        
        
          [Parameters](#setPosition-imageViewerMarker-parameters)
        
        
          px`([number, number])`
          The position of the ImageViewerMarker in image pixels.
          
        
        
          [Returns](#setPosition-imageViewerMarker-returns)
        
        `[ImageViewerMarker](/sdk-js/api/markers/#imageViewerMarker)`:
          `this` 
        
          [Example](#setPosition-imageViewerMarker-example)
        
        
          ```
``
```

        
      
    
  
  
    [Related examples](#imageViewerMarker-related)
  
  
    
      [Add markers to a non-georeferenced image](/sdk-js/examples/image-viewer-marker/)
      
    
  

  
  
    [Popup](#popup)
  
  
    [src/ui/popup.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/popup.ts#L99-L590)
  
  
    A popup component.
  
  
    Extends [Evented](/sdk-js/api/events/#evented).
  
  
    [Example](#popup-example)
  
  
    ```
``
```

  
  
    [Parameters](#popup-parameters)
  
  
    options(Object?)
    
      
| If                 `true`                 , a close button will appear in the top right corner of the                 popup. |
| If                 `true`                 , the popup will closed when the map is clicked. |
| If                 `true`                 , the popup will closed when the map moves. |
| If                 `true`                 , the popup will try to focus the first focusable element                 inside the popup. |
| A string indicating the part of the Popup that should be                 positioned closest to the coordinate set via                 [Popup#setLngLat](/sdk-js/api/markers/#popup#setlnglat)                 . Options are                 `'center'`                 ,                 `'top'`                 ,                 `'bottom'`                 ,                 `'left'`                 ,                 `'right'`                 ,                 `'top-left'`                 ,                  `'top-right'`                 ,                 `'bottom-left'`                 , and                 `'bottom-right'`                 . If unset the anchor will be dynamically set to ensure the                 popup falls within the map container with a preference for                 `'bottom'`                 . |
| A pixel offset applied to the popup's location specified as:                                                         a single number specifying a distance from the popup's                     location                                                           a                     [PointLike](/sdk-js/api/geography/#pointlike)                     specifying a constant offset                                                           an object of                     [Point](/sdk-js/api/geography/#point)s                     specifing an offset for each anchor position Negative                     offsets indicate left and up. |
| Space-separated CSS class names to add to popup container |
| A string that sets the CSS property of the popup's maximum                 width, eg                 `'300px'`                 . To ensure the popup resizes to fit its content, set this                 property to                 `'none'`                 . Available values can be found here:                 [https://developer.mozilla.org/en-US/docs/Web/CSS/max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) |

    
  
  
    [Methods](#popup-instance-members)
  
  
    
      addClassName(className)
            
              
            
    
    
      
        
          Adds a CSS class to the popup container element.
        
        
          [Parameters](#addclassname-parameters)
        
        
          className(string)Non-empty string with CSS class name to add to popup container
          
        
        
          [Returns](#addclassname-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#addclassname-example)
        
        
          ```
``
```

        
      
    
  
  
    
      addTo(map)
            
              
            
    
    
      
        
          Adds the popup to a map.
        
        
          [Parameters](#addto-parameters)
        
        
          map([Map](/sdk-js/api/map/#map))The SDK JS map to add the popup to. 
        
        
          [Returns](#addto-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#addto-example)
        
        
          ```
``
```

        
        
          [Related examples](#addto-related)
        
        
          
            [Display a popup](/sdk-js/examples/popup/)
            
          
          
            [Display a popup on hover](/sdk-js/examples/popup-on-hover/)
            
          
          
            [Display a popup on click](/sdk-js/examples/popup-on-click/)
            
          
          
            [Show polygon information on click](/sdk-js/examples/polygon-popup-on-click/)
            
          
        
      
    
  
  
    
      getElement()
            
              
            
    
    
      
        
          
            Returns the `Popup`'s HTML
            element.
          
        
        
          [Returns](#getelement-returns)
        
        HTMLElement: element 
        
          [Example](#getelement-example)
        
        
          ```
``
```

        
      
    
  
  
    
      getLngLat()
            
              
            
    
    
      
        
          Returns the geographical location of the popup's anchor.
          
            The longitude of the result may differ by a multiple of 360
            degrees from the longitude previously set by
            `setLngLat` because
            `Popup` wraps the anchor
            longitude across copies of the world to keep the popup on screen.
          
        
        
          [Returns](#getlnglat-returns)
        
        [LngLat](/sdk-js/api/geography/#lnglat):
          The geographical location of the popup's anchor. 
      
    
  
  
    
      getMaxWidth()
            
              
            
    
    
      
        
          Returns the popup's maximum width.
        
        
          [Returns](#getmaxwidth-returns)
        
        string: The maximum width of the popup. 
      
    
  
  
    
      isOpen()
            
              
            
    
    
      
        
        
          [Returns](#isopen-returns)
        
        boolean:
          `true`
            if the popup is open,
            `false`
            if it is closed.
          
      
    
  
  
    listens(type) 
              
            
    
      
          Returns a true if this instance of Evented or any forwardeed instances of Evented have a listener for the specified type.
        
        [Parameters](#listens-parameters)
      type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
            The event type.
        
        [Returns](#listens-returns)
        
        `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
          `true` if there is at least one registered listener 
            for specified event type, `false` otherwise
          
      
    
  
  
    off(type, listener) 
              
            
    
      
          Removes a previously registered event listener.
        
        [Parameters](#off-parameters)
        
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`The
            event type previously used to install the listener.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`The
            function previously installed as a listener.
          
        [Returns](#off-returns)
        `[Popup](/sdk-js/api/markers/#popup)`: `this`
          
      
    
  
  
    on(type, layer, listener) 
              
            
    
      
          Adds a listener for events of a specified type, optionally limited to features in a specified style
            layer.
        
        [Parameters](#on-parameters)
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String))`
            The event type to add a listen for.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`
            The function to be called when the event is fired. 
              The listener function is called with the data object passed to `fire`, 
              extended with `target` and `type` properties
          
          [Returns](#on-returns)
        `[Popup](/sdk-js/api/markers/#popup)`: `this`
          
      
    
  
  
    once(type, listener?) 
              
            
    
      
          Adds a listener that will be called only once to a specified event type.
          The listener will be called first time the event fires after the listener is registered.
        
        [Parameters](#once-parameters)
        
        type`([string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)?)`The
            event type to listen for.
          
        listener`([Function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/function))`
            The function to be called when the event is fired the first time.
          
          [Returns](#once-returns)
          `([Popup](/sdk-js/api/markers/#popup) | Promise	<any> )`: `this` or a promise if a listener is not provided
            
      
    
  
  
    
      remove()
            
              
            
    
    
      
        
          Removes the popup from the map it has been added to.
        
        
          [Returns](#remove-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#remove-example)
        
        
          ```
``
```

        
      
    
  
  
    
      removeClassName(className)
            
              
            
    
    
      
        
          Removes a CSS class from the popup container element.
        
        
          [Parameters](#removeclassname-parameters)
        
        
          className(string)Non-empty string with CSS class name to remove from popup
            container
          
        
        
          [Returns](#removeclassname-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#removeclassname-example)
        
        
          ```
``
```

        
      
    
  
  
    
      setDOMContent(htmlNode)
            
              
            
    
    
      
        
          
            Sets the popup's content to the element provided as a DOM node.
          
        
        
          [Parameters](#setdomcontent-parameters)
        
        
          htmlNode(Node)A DOM node to be used as content for the popup. 
        
        
          [Returns](#setdomcontent-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#setdomcontent-example)
        
        
          ```
``
```

        
      
    
  
  
    
      setHTML(html)
            
              
            
    
    
      
        
          Sets the popup's content to the HTML provided as a string.
          
            This method does not perform HTML filtering or sanitization, and
            must be used only with trusted content. Consider
            [Popup#setText](/sdk-js/api/markers/#popup#settext) if
            the content is an untrusted text string.
          
        
        
          [Parameters](#sethtml-parameters)
        
        
          html(string)A string representing HTML content for the popup. 
        
        
          [Returns](#sethtml-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#sethtml-example)
        
        
          ```
``
```

        
        
          [Related examples](#sethtml-related)
        
        
          
            [Display a popup](/sdk-js/examples/popup/)
            
          
          
            [Display a popup on hover](/sdk-js/examples/popup-on-hover/)
            
          
          
            [Display a popup on click](/sdk-js/examples/popup-on-click/)
            
          
          
            [Attach a popup to a marker instance](/sdk-js/examples/set-popup/)
            
          
        
      
    
  
  
    
      setLngLat(lnglat)
            
              
            
    
    
      
        
          
            Sets the geographical location of the popup's anchor, and moves
            the popup to it. Replaces trackPointer() behavior.
          
        
        
          [Parameters](#setlnglat-parameters)
        
        
          lnglat(LngLatLike)The geographical location to set as the popup's anchor.
          
        
        
          [Returns](#setlnglat-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
      
    
  
  
    
      setMaxWidth(maxWidth)
            
              
            
    
    
      
        
          
            Sets the popup's maximum width. This is setting the CSS property
            `max-width`. Available
            values can be found here:
            [https://developer.mozilla.org/en-US/docs/Web/CSS/max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width)
          
        
        
          [Parameters](#setmaxwidth-parameters)
        
        
          maxWidth(string)A string representing the value for the maximum width.
          
        
        
          [Returns](#setmaxwidth-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
      
    
  
  
    
      setOffset(offset?)
            
              
            
    
    
      
        
          Sets the popup's offset.
        
        
          [Parameters](#setoffset-parameters)
        
        
          offset`(Offset?)`Sets the popup's offset. 
        
        
          [Returns](#setoffset-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
      
    
  
  
    
      setSubpixelPositioning(value)
            
              
            
    
    
      
        
          Set the option to allow subpixel positioning of the popup by passing a boolean
          
        
        
          [Parameters](#setsubpixelpositioning-parameters)
        
        
          value(boolean)When boolean is true, subpixel positioning is enabled for the popup.
        
        
          [Example](#setsubpixelpositioning-example)
        
        
          ```
``
```

        
      
    
  
  
    
      setText(text)
            
              
            
    
    
      
        
          Sets the popup's content to a string of text.
          
            This function creates a
            [Text](https://developer.mozilla.org/en-US/docs/Web/API/Text)
            node in the DOM, so it cannot insert raw HTML. Use this method for
            security against XSS if the popup content is user-provided.
          
        
        
          [Parameters](#settext-parameters)
        
        
          text(string)Textual content for the popup. 
        
        
          [Returns](#settext-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#settext-example)
        
        
          ```
``
```

        
      
    
  
  
    
      toggleClassName(className)
            
              
            
    
    
      
        
          
            Add or remove the given CSS class on the popup container,
            depending on whether the container currently has that class.
          
        
        
          [Parameters](#toggleclassname-parameters)
        
        
          className(string)Non-empty string with CSS class name to add/remove 
        
        
          [Returns](#toggleclassname-returns)
        
        boolean:
          if the class was removed return false, if class was added, then
            return true
          
        
          [Example](#toggleclassname-example)
        
        
          ```
``
```

        
      
    
  
  
    
      trackPointer()
            
              
            
    
    
      
        
          
            Tracks the popup anchor to the cursor position on screens with a
            pointer device (it will be hidden on touchscreens). Replaces the
            `setLngLat` behavior. For
            most use cases, set
            `closeOnClick` and
            `closeButton` to
            `false`.
          
        
        
          [Returns](#trackpointer-returns)
        
        `[Popup](/sdk-js/api/markers/#popup)`:
          `this` 
        
          [Example](#trackpointer-example)
        
        
          ```
``
```

        
      
    
  
  
    [Events](#popup-events)
  
  
    
      close
            
              
            
    
    
      
        
          Fired when the popup is closed manually or programatically.
        
        
          [Properties](#close-properties)
        
        
          popup([Popup](/sdk-js/api/markers/#popup)): object that was closed 
        
        
          [Example](#close-example)
        
        
          ```
``
```

        
      
    
  
  
    
      open
            
              
            
    
    
      
        
          Fired when the popup is opened manually or programatically.
        
        
          [Properties](#open-properties)
        
        
          popup([Popup](/sdk-js/api/markers/#popup)): object that was opened 
        
        
          [Example](#open-example)
        
        
          ```
``
```

        
      
    
  
  
    [Related examples](#popup-related)
  
  
    
      [Display a popup](/sdk-js/examples/popup/) 
    
    
      [Display a popup on hover](/sdk-js/examples/popup-on-hover/)
      
    
    
      [Display a popup on click](/sdk-js/examples/popup-on-click/)
      
    
    
      [Attach a popup to a marker instance](/sdk-js/examples/set-popup/)
