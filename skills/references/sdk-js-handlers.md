# Source: https://docs.maptiler.com/sdk-js/api/handlers/

# 

    Items related to the ways in which the map responds to user input.
  
  
    ## [BoxZoomHandler](#boxzoomhandler)

    [src/ui/handler/box_zoom.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/box_zoom.ts)
      The `BoxZoomHandler` allows the user to zoom the map to fit within a bounding box.
        The bounding box is defined by clicking and holding `shift` while dragging the cursor.
    
    [Methods](#boxzoomhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "box zoom" interaction.
          
          [Example](#disable-boxzoomhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable() 
                
              
      
        
            Enables the "box zoom" interaction.
          
          [Example](#enable-boxzoomhandler-example)
          
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns a Boolean indicating whether the "box zoom" interaction is active, i.e. currently being used.
          
          [Returns](#isactive-boxzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "box zoom" interaction is active.
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "box zoom" interaction is enabled.
          
          [Returns](#isenabled-boxzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "box zoom" interaction is enabled.
            
        
      
    
  
  
    [CooperativeGesturesHandler](#cooperativegestureshandler)
    [src/ui/handler/cooperative_gestures.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/cooperative_gestures.ts)
        
      A `CooperativeGesturesHandler` is a control that adds 
        cooperative gesture info when user tries to zoom in/out.
    
    
      When the CooperativeGestureHandler blocks a gesture, it will emit a `cooperativegestureprevented` event.
    
    [Example](#cooperativegestureshandler-example)
    
      ```
``
```

    
    [Properties](#cooperativegestureshandler-properties)
    
      _bypassKey 
                
              
      
        
            This is the key (`"ctrlKey"` | `"metaKey"`)
               that will allow to bypass the cooperative gesture protection.
          
        
      
    
    [Methods](#cooperativegestureshandler-instance-members)
  
    isActive() 
              
            
    
      
          This is used to indicate if the handler is currently active or not. 
            In case a handler is active, it will block other handlers from getting the relevant events. 
            There is an allow list of handlers that can be active at the same time, 
            which is configured when adding a handler.
        
        [Returns](#isActive-cooperativegestureshandler-returns)
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        `true`
          if the cooperative gestures interaction is enabled.
        
      
    
  
  
    reset() 
              
            
    
      
          Can be called by the manager at any time and must reset everything to it's original state.
        
      
    
  
  
  
    [ScrollZoomHandler](#scrollzoomhandler)
    [src/ui/handler/scroll_zoom.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/scroll_zoom.ts)
      The `ScrollZoomHandler` allows the user to zoom the map by scrolling.
    
    [Methods](#scrollzoomhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "scroll to zoom" interaction.
          
          [Example](#disable-scrollzoomhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "scroll to zoom" interaction.
          
          [Parameters](#enable-scrollzoomhandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object.
            
            
              
| If "center" is passed, map will zoom around center of map |

            
          
          [Example](#enable-scrollzoomhandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "scroll to zoom" interaction is enabled.
          
          [Returns](#isenabled-scrollzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "scroll to zoom" interaction is enabled.
            
        
      
    
    
      setWheelZoomRate(wheelZoomRate) 
                
              
      
        
            Set the zoom rate of a mouse wheel
          
          [Parameters](#setwheelzoomrate-parameters)
          wheelZoomRate`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
              `1/450`)The rate used to scale mouse wheel movement to a zoom value.
            
          [Example](#setwheelzoomrate-example)
          
            ```
``
```

          
        
      
    
    
      setZoomRate(zoomRate) 
                
              
      
        
            Set the zoom rate of a trackpad
          
          [Parameters](#setzoomrate-parameters)
          zoomRate`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
              `1/100`)The rate used to scale trackpad movement to a zoom value.
            
          [Example](#setzoomrate-example)
          
            ```
``
```

          
        
      
    
  
  
    ## [DragPanHandler](#dragpanhandler)

    [src/ui/handler/shim/drag_pan.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/shim/drag_pan.ts)
      The `DragPanHandler` allows the user to pan the map by clicking and dragging
        the cursor.
    
    [Methods](#dragpanhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "drag to pan" interaction.
          
          [Example](#disable-dragpanhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "drag to pan" interaction.
          
          [Parameters](#enable-dragpanhandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object
            
            
              
| factor used to scale the drag velocity |
| easing function applled to                         `map.panTo`                         when applying the drag. |
| the maximum value of the drag velocity. |
| the rate at which the speed reduces after the pan ends. |

            
          
          [Example](#enable-dragpanhandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pan" interaction is active, i.e. currently being used.
            
          
          [Returns](#isactive-dragpanhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pan" interaction is active.
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pan" interaction is enabled.
          
          [Returns](#isenabled-dragpanhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pan" interaction is enabled.
            
        
      
    
  
  
    [DragRotateHandler](#dragrotatehandler)
    [src/ui/handler/shim/drag_rotate.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/shim/drag_rotate.ts)
      The `DragRotateHandler` allows the user to rotate the map by clicking and
        dragging the cursor while holding the right mouse button or `ctrl` key.
    
    [Methods](#dragrotatehandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "drag to rotate" interaction.
          
          [Example](#disable-dragrotatehandler-example)
          
            ```
``
```

          
        
      
    
    
      enable() 
                
              
      
        
            Enables the "drag to rotate" interaction.
          
          [Example](#enable-dragrotatehandler-example)
          
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns a Boolean indicating whether the "drag to rotate" interaction is active, i.e. currently being
              used.
          
          [Returns](#isactive-dragrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to rotate" interaction is active.
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "drag to rotate" interaction is enabled.
          
          [Returns](#isenabled-dragrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to rotate" interaction is enabled.
            
        
      
    
  
  
    [KeyboardHandler](#keyboardhandler)
    
    [src/ui/handler/keyboard.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/keyboard.ts)
      The `KeyboardHandler` allows the user to zoom, rotate, and pan the map using
        the following keyboard shortcuts:
      
        `=` / `+`: Increase the zoom level by 1.
        `Shift-=` / `Shift-+`: Increase the zoom level by 2.
        `-`: Decrease the zoom level by 1.
        `Shift--`: Decrease the zoom level by 2.
        Arrow keys: Pan by 100 pixels.
        `Shift+⇢`: Increase the rotation by 15 degrees.
        `Shift+⇠`: Decrease the rotation by 15 degrees.
        `Shift+⇡`: Increase the pitch by 10 degrees.
        `Shift+⇣`: Decrease the pitch by 10 degrees.
      
    
    [Methods](#keyboardhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "keyboard rotate and zoom" interaction.
          
          [Example](#disable-keyboardhandler-example)
          
            ```
``
```

          
        
      
    
    
      disableRotation() 
                
              
      
        
            Disables the "keyboard pan/rotate" interaction, leaving the
              "keyboard zoom" interaction enabled.
          
          [Example](#disablerotation-keyboardhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable() 
                
              
      
        
            Enables the "keyboard rotate and zoom" interaction.
          
          [Example](#enable-keyboardhandler-example)
          
          
            ```
``
```

          
        
      
    
    
      enableRotation() 
                
              
      
        
            Enables the "keyboard pan/rotate" interaction.
          
          [Example](#enablerotation-keyboardhandler-example)
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns true if the handler is enabled and has detected the start of a
              zoom/rotate gesture.
          
          [Returns](#isactive-keyboardhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the handler is enabled and has detected the
              start of a zoom/rotate gesture.
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "keyboard rotate and zoom"
              interaction is enabled.
          
          [Returns](#isenabled-keyboardhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "keyboard rotate and zoom"
              interaction is enabled.
            
        
      
    
  
  
    [DoubleClickZoomHandler](#doubleclickzoomhandler)
    [src/ui/handler/shim/dblclick_zoom.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/shim/dblclick_zoom.ts)
      The `DoubleClickZoomHandler` allows the user to zoom the map at a point by
        double clicking or double tapping.
    
    [Methods](#doubleclickzoomhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "double click to zoom" interaction.
          
          [Example](#disable-doubleclickzoomhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable() 
                
              
      
        
            Enables the "double click to zoom" interaction.
          
          [Example](#enable-doubleclickzoomhandler-example)
          
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns a Boolean indicating whether the "double click to zoom" interaction is active, i.e. currently
              being used.
          
          [Returns](#isactive-doubleclickzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "double click to zoom" interaction is active.
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "double click to zoom" interaction is enabled.
          
          [Returns](#isenabled-doubleclickzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "double click to zoom" interaction is enabled.
            
        
      
    
  
  
    [TwoFingersTouchPitchHandler](#twofingerstouchpitchhandler)
    [src/ui/handler/two_fingers_touch.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/two_fingers_touch.ts)
      The `TwoFingersTouchPitchHandler` allows the user to pitch the map by dragging up and down with two fingers.
      
    
    Extends TwoFingersTouchHandler.
    [Methods](#twofingerstouchpitchhandler-instance-members)
    
      disable 
                
              
      
        
            Disables the "drag to pitch" interaction.
          
          [Example](#disable-twofingerstouchpitchhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "drag to pitch" interaction.
          
          [Parameters](#enable-twofingerstouchpitchhandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object.
            
            
              
| If "center" is passed, map will zoom around the center |

            
          
          [Example](#enable-twofingerstouchpitchhandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      isActive 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pitch" interaction is active, i.e. currently being
              used.
          
          [Returns](#isactive-twofingerstouchpitchhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pitch" interaction is active.
            
        
      
    
    
      isEnabled 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pitch" interaction is enabled.
          
          [Returns](#isenabled-twofingerstouchpitchhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pitch" interaction is enabled.
            
        
      
    
  
  
    [TwoFingersTouchRotateHandler](#twofingerstouchrotatehandler)
    [src/ui/handler/two_fingers_touch.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/two_fingers_touch.ts)
      The `TwoFingersTouchRotateHandler` allows the user to rotate with two fingers.
      
    
    Extends TwoFingersTouchHandler.
    [Methods](#twofingerstouchrotatehandler-instance-members)
    
      disable 
                
              
      
        
            Disables the "drag to rotate" interaction.
          
          [Example](#disable-twofingerstouchrotatehandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "drag to pitch" interaction.
          
          [Parameters](#enable-twofingerstouchrotatehandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object.
            
            
              
| If "center" is passed, map will zoom around the center |

            
          
          [Example](#enable-twofingerstouchrotatehandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      isActive 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pitch" interaction is active, i.e. currently being
              used.
          
          [Returns](#isactive-twofingerstouchrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pitch" interaction is active.
            
        
      
    
    
      isEnabled 
                
              
      
        
            Returns a Boolean indicating whether the "drag to pitch" interaction is enabled.
          
          [Returns](#isenabled-twofingerstouchrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "drag to pitch" interaction is enabled.
            
        
      
    
  
  
    [TwoFingersTouchZoomHandler](#twofingerstouchzoomrotatehandler)
    [src/ui/handler/shim/two_fingers_touch.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/shim/two_fingers_touch.ts)
      The `TwoFingersTouchZoomHandler` allows the user to zoom the map two fingers.
    
    [Methods](#twofingerstouchzoomhandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "pinch to rotate and zoom" interaction.
          
          [Example](#disable-twofingerstouchzoomhandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "drag to zoom" interaction.
          
          [Parameters](#enable-twofingerstouchzoomhandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object.
            
            
              
| If "center" is passed, map will zoom around the center |

            
          
          [Example](#enable-twofingerstouchzoomhandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns true if the handler is enabled and has detected the start of a zoom/rotate gesture.
          
          [Returns](#isactive-twofingerstouchzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            //eslint-disable-line
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "pinch to rotate and zoom" interaction is enabled.
          
          [Returns](#isenabled-twofingerstouchzoomhandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "pinch to rotate and zoom" interaction is enabled.
            
        
      
    
  
  
    [TwoFingersTouchZoomRotateHandler](#twofingerstouchzoomrotatehandler)
    [src/ui/handler/shim/two_fingers_touch.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/handler/shim/two_fingers_touch.ts)
      The `TwoFingersTouchZoomRotateHandler` allows the user to zoom and rotate the map by
        pinching on a touchscreen.
      They can zoom with one finger by double tapping and dragging. On the second tap,
        hold the finger down and drag up or down to zoom in or out.
    
    [Methods](#twofingerstouchzoomrotatehandler-instance-members)
    
      disable() 
                
              
      
        
            Disables the "pinch to rotate and zoom" interaction.
          
          [Example](#disable-twofingerstouchzoomrotatehandler-example)
          
            ```
``
```

          
        
      
    
    
      disableRotation() 
                
              
      
        
            Disables the "pinch to rotate" interaction, leaving the "pinch to zoom"
              interaction enabled.
          
          [Example](#disablerotation-twofingerstouchzoomrotatehandler-example)
          
            ```
``
```

          
        
      
    
    
      enable(options?) 
                
              
      
        
            Enables the "pinch to rotate and zoom" interaction.
          
          [Parameters](#enable-twofingerstouchzoomrotatehandler-parameters)
          options`([Object](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)?)`Options
              object.
            
            
              
| If "center" is passed, map will zoom around the center |

            
          
          [Example](#enable-twofingerstouchzoomrotatehandler-example)
          
          
            ```
``
```

          
          
            ```
``
```

          
        
      
    
    
      enableRotation() 
                
              
      
        
            Enables the "pinch to rotate" interaction.
          
          [Example](#enablerotation-twofingerstouchzoomrotatehandler-example)
          
            ```
``
```

          
        
      
    
    
      isActive() 
                
              
      
        
            Returns true if the handler is enabled and has detected the start of a zoom/rotate gesture.
          
          [Returns](#isactive-twofingerstouchzoomrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            //eslint-disable-line
            
        
      
    
    
      isEnabled() 
                
              
      
        
            Returns a Boolean indicating whether the "pinch to rotate and zoom" interaction is enabled.
          
          [Returns](#isenabled-twofingerstouchzoomrotatehandler-returns)
          `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
            `true`
              if the "pinch to rotate and zoom" interaction is enabled.
