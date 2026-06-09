# Source: https://docs.maptiler.com/sdk-js/api/events/

# 

  
    The different types of events that SDK JS can raise.
    
      You can also find additional event documentation for:
      `Map`,
      `Marker`,
      `Popup`, and
      `GeolocationControl`.
    
  
  
    
      [Evented](#evented)
    
    
      src/util/evented.ts
    
    
      Methods mixed in to other classes for event capabilities.
    
    
      Methods
    
    
  
  
    
      [MapMouseEvent](#mapmouseevent)
    
    
      src/ui/events.ts
    
    
      
        `MapMouseEvent` is the event type
        for mouse-related map events.
      
    
    
      Extends
      Event.
    
    
      Example
    
    
      ```
``
```

    
    
      Methods
    
    
      
        lngLat
              
                
      
      
        
          
            The geographic location on the map of the mouse cursor.
          
        
      
    
    
      
        originalEvent
              
                
      
      
        
          
            The DOM event which caused the map event.
          
        
      
    
    
      
        point
              
                
      
      
        
          
            
              The pixel coordinates of the mouse cursor, relative to the map and
              measured from the top left corner.
            
          
        
      
    
    
      
        preventDefault()
              
                
      
      
        
          
            
              Prevents subsequent default processing of the event by the map.
            
            
              Calling this method will prevent the following default map
              behaviors:
            
            
              
                On `mousedown` events, the
                behavior of
                DragPanHandler
              
              
                On `mousedown` events, the
                behavior of
                DragRotateHandler
              
              
                On `mousedown` events, the
                behavior of
                BoxZoomHandler
              
              
                On `dblclick` events, the
                behavior of
                DoubleClickZoomHandler
              
            
          
        
      
    
    
      
        target
              
                
      
      
        
          
            
              The `Map` object that fired
              the event.
            
          
        
      
    
    
      
        type
              
                
      
      
        
          
            
              The event type (one of
              Map.event:mousedown,
              Map.event:mouseup, [Map.event:click](/sdk-js/api/map/#map.event:click),
              Map.event:dblclick,
              Map.event:mousemove,
              Map.event:mouseover,
              Map.event:mouseenter,
              Map.event:mouseleave,
              Map.event:mouseout,
              Map.event:contextmenu).
            
          
        
      
    
  
  
    
      [MapTouchEvent](#maptouchevent)
    
    
      src/ui/events.ts
    
    
      
        `MapTouchEvent` is the event type
        for touch-related map events.
      
    
    
      Extends
      Event.
    
    
      Methods
    
    
      
        lngLat
              
                
      
      
        
          
            
              The geographic location on the map of the center of the touch
              event points.
            
          
        
      
    
    
      
        lngLats
              
                
      
      
        
          
            
              The geographical locations on the map corresponding to a
              touch event's
                `touches`
              property.
            
          
        
      
    
    
      
        originalEvent
              
                
      
      
        
          
            The DOM event which caused the map event.
          
        
      
    
    
      
        point
              
                
      
      
        
          
            
              The pixel coordinates of the center of the touch event points,
              relative to the map and measured from the top left corner.
            
          
        
      
    
    
      
        points
              
                
      
      
        
          
            
              The array of pixel coordinates corresponding to a
              touch event's
                `touches`
              property.
            
          
        
      
    
    
      
        preventDefault()
              
                
      
      
        
          
            
              Prevents subsequent default processing of the event by the map.
            
            
              Calling this method will prevent the following default map
              behaviors:
            
            
              
                On `touchstart` events,
                the behavior of
                DragPanHandler
              
              
                On `touchstart` events,
                the behavior of
                TouchZoomRotateHandler
              
            
          
        
      
    
    
      
        target
              
                
      
      
        
          
            
              The `Map` object that fired
              the event.
            
          
        
      
    
    
      
        type
              
                
      
      
        
          
            The event type.
          
        
      
    
  
  
    
      MapLibreZoomEvent
    
    
      src/ui/events.ts
    
    
      
        A `MapLibreZoomEvent` is the event
        type for the boxzoom-related map events emitted by the
        [BoxZoomHandler](/sdk-js/api/handlers/#boxzoomhandler).
      
    
    
      Properties
    
    
      originalEvent(MouseEvent):
        The DOM event that triggered the boxzoom event. Can be a
          `MouseEvent`
          or
          `KeyboardEvent`
        
    
    
      type(string):
        The type of boxzoom event. One of
          `boxzoomstart`
          ,
          `boxzoomend`
          or
          `boxzoomcancel`
        
    
    
      target([Map](/sdk-js/api/map/#map)):
        The
          `Map`
          instance that triggerred the event
        
    
  
  
    
      [MapDataEvent](#mapdataevent)
    
    
      src/ui/events.ts
    
    
      
        A `MapDataEvent` object is emitted
        with the
        [Map.event:data](/sdk-js/api/map/#map.event:data) and
        Map.event:dataloading
        events. Possible values for
        `dataType`s are:
      
      
        
          `'source'`: The non-tile data
          associated with any source
        
        
          `'style'`: The
          [style](/gl-style-specification/) used by the map
        
      
    
    
      [Example](#mapdataevent-example)
    
    
      ```
``
```

    
    
      Properties
    
    
      type(string): The event type. 
    
    
      dataType(string):
        The type of data that has changed. One of
          `'source'`
          ,
          `'style'`
          .
        
    
    
      isSourceLoaded(boolean?):
        True if the event has a
          `dataType`
          of
          `source`
          and the source has no outstanding network requests.
        
    
    
      source(Object?):
        The
          style spec representation of the source
          if the event has a
          `dataType`
          of
          `source`
          .
        
    
    
      sourceDataType(string?):
        Included if the event has a
          `dataType`
          of
          `source`
          and the event signals that internal data has been received or changed.
          Possible values are
          `metadata`
          ,
          `content`
          and
          `visibility`
          .
        
    
    
      tile(Object?):
        The tile being loaded or changed, if the event has a
          `dataType`
          of
          `source`
          and the event is related to loading of a tile.
        
    
    
      coord(Coordinates?):
        The coordinate of the tile if the event has a
          `dataType`
          of
          `source`
          and the event is related to loading of a tile.
        
    
  
  
    
      [MapWheelEvent](#mapwheelevent)
    
    
      src/ui/events.ts
    
    
      
        `MapWheelEvent` is the event type
        for the `wheel` map event.
      
    
    
      Extends
      Object.
    
    
      Methods
    
    
      
        originalEvent
              
                
      
      
        
          
            The DOM event which caused the map event.
          
        
      
    
    
      
        preventDefault()
              
                
      
      
        
          
            
              Prevents subsequent default processing of the event by the map.
            
            
              Calling this method will prevent the the behavior of
              ScrollZoomHandler.
            
          
        
      
    
    
      
        target
              
                
      
      
        
          
            
              The `Map` object that fired
              the event.
            
          
        
      
    
    
      
        type
              
                
      
      
        
          
            The event type.
          
        
      
    
  
  
    ## [MapProjectionEvent](#MapProjectionEvent)

    [src/ui/events.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/events.ts)
      Supporting type to add validation to another style related type.
    
    [Type declaration](#MapProjectionEvent-types)
    
      newProjection?
      `ProjectionSpecification`
      Specifies the name of the new projection. 
        Additionally includes 'globe-mercator' to describe globe that has internally switched to mercator.
