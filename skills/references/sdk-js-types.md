# Source: https://docs.maptiler.com/sdk-js/api/types/

# 

  ## [CameraUpdateTransformFunction](#CameraUpdateTransformFunction)

  [src/ui/camera.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/camera.ts)
    A callback hook that allows manipulating the camera and being notified about camera updates before they happen.
  

  ```
``
```

  [Parameters](#CameraUpdateTransformFunction-parameters)
  next
      
        { bearing: number; center: LngLat; elevation: number; pitch: number; roll: number; zoom: number; }
      
  
  
    next.bearing
    `number`
  
  
    next.center
    `LngLat`
  
  
    next.elevation
    `number`
  
  
    next.pitch
    `number`
  
  
    next.roll
    `number`
  
  
    next.zoom
    `number`
  

  ## [RequestTransformFunction](#RequestTransformFunction)

  [src/util/request_manager.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/request_manager.ts)
    This function is used to tranform a request. It is used just before executing the relevant request.
  

  ```
``
```

  [Parameters](#RequestTransformFunction-parameters)
  
    url
    `string`
  
  
    resourceType ?
    [`ResourceType`](#ResourceType)
  

  ## [ResourceType](#ResourceType)

  [src/util/request_manager.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/request_manager.ts)
    A type of MapLibre resource.
  
  [Enumeration members](#ResourceType-enumeration)
  
    Glyphs
  
  
    Image
  
  
    Source
  
  
    SpriteImage
  
  
    SpriteJSON
  
  
    Style
  
  
    Tile
  
  
    Unknown
  

  ## [Subscription](#Subscription)

  [src/util/util.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/util/util.ts)
    Allows to unsubscribe from events without the need to store the method reference.
  
  [Methods](#Subscription-methods)
  [unsubscribe()](#unsubscribe)
  
    Unsubscribes from the event.
  
  [Returns](#unsubscribe-returns)
  `void`

  ## [StyleSetterOptions](#StyleSetterOptions)

  [src/style/style.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/style/style.ts)
    Supporting type to add validation to another style related type.
  
  [Type declaration](#StyleSetterOptions-types)
  
    validate?
    `boolean`
    Whether to check if the filter conforms to the MapLibre Style Specification. 
      Disabling validation is a performance optimization that should only be used if you have previously validated 
      the values you will be passing to this function.
    
  

  
    [CubemapLayerConstructorOptions](#CubemapLayerConstructorOptions)
  [src/custom-layers/CubemapLayer/types.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/custom-layers/CubemapLayer/types.ts)
    Constructor options for the CubemapLayer.
  
  [Usage](#CubemapLayerConstructorOptions-usage)
  
    [Simple space](#simple-usage)
  You can enable a simple space background with a solid color:
  ```
``
```

  
  
  [Predefined Presets](#predefined-presets-usage)
  Alternatively, you can provide a cubemap for a space backround using one of the following methods:
  
    
      `space`
      : Dark blue hsl(210, 100%, 4%) background and white stars (transparent background image). 
      Space color changes the background color, stars always stay white.
    
    
      `stars`
      (default): Black background (image mask), space color changes the stars color, background always stays black.
    
    
      `milkyway`
      : Black half-transparent background with standard milkyway and stars. 
      Space color changes the stars and milkyway color, background always stays black.
    
    
      `milkyway-subtle`
      : Black half-transparent background with subtle milkyway and less stars. 
      Space color changes the stars and milkyway color, background always stays black.
      Black half-transparent background with standard milkyway and stars. 
      Space color changes the stars and milkyway color, background always stays black.
    
    
      `milkyway-bright`
      : Black half-transparent background with bright milkyway and more stars. 
      Space color changes the stars and milkyway color, background always stays black.
    
  
  ```
``
```

  
  
    [Cubemap Images (Custom Skybox)](#cubemap-images-usage)
  Load your custom cubemap images:
  ```
``
```

  
  
    [Cubemap Path with image format](#cubemap-path-format-usage)
  This fetches all images from a path, this assumes all files are named px, nx, py, ny, pz, nz and 
  suffixed with the appropriate extension specified in `format`.
  ```
``
```

  
  
    [Set the space background dynamically](#space-dynamically-usage)
    You can also set the space dynamically after the map loads:
  ```
``
```

  
  
    
      
        Cubemap face images must be square and have a height / width of a power of 2 512px, 1024px
        if `space.color` or 
          `` are not explicitly 
            set in the call to `setSpace`, 
            then the previous value will remain for this field. 
            To override the default, set the required field to `null`.
      
    
  

  
    [RadialGradientLayerConstructorOptions](#RadialGradientLayerConstructorOptions)
  [src/custom-layers/RadialGradientLayer/types.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/custom-layers/RadialGradientLayer/types.ts)
    Options for constructing a RadialGradientLaye.
  
  [Usage](#RadialGradientLayerConstructorOptions-usage)
  
    [Simple halo](#simple-halo-usage)
  You can enable a simple halo by setting it to `true`:
  ```
``
```

  
  
    [Radial gradient](#radial-gradient-halo-usage)
  For more customization, you can define a radial gradient with scale and stops:
  ```
``
```

  
  
    [Set the halo dynamically](#halo-dynamically-usage)
    You can also set the halo dynamically after the map loads:
  ```
``
```

  

  ## [MaptilerCustomControlCallback](#MaptilerCustomControlCallback)

  [src/controls/MaptilerCustomControl.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/controls/MaptilerCustomControl.ts)
    A callback hook used by a [MaptilerCustomControl](/sdk-js/api/controls/#maptilercustomcontrol).
  

  ```
``
```

  [Parameters](#MaptilerCustomControlCallback-parameters)
  map
      `SDKMap`
  
  
    element
    `HTMLElement`
  
  
    event
    `Event`
  

 
  ## [ImageMetadata](#ImageMetadata)

  [src/ImageViewer/ImageViewer.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ImageViewer/ImageViewer.ts)
    The metadata of the image. This is the shape of the response from the API. And used to convert px to lnglat and vice versa..
  
  
  ```
``
```

  
  [Type declaration](#StyleSetterOptions-types)
  
    attribution
    `string`
  
  
    description
    `string`
  
  
    height
    `number`
  
  
    id
    `string`
  
  
    maxzoom
    `number`
  
  
    minzoom
    `number`
  
  
    tileSize
    `number`
  
  
    width
    `number`
