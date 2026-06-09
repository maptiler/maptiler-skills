# Source: https://docs.maptiler.com/sdk-js/api/geography/

# 

    General utilities and types that relate to working with and manipulating geographic information or geometries.
    
  
  
  
  ## [LngLat](#lnglat)

  [src/geo/lng_lat.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/lng_lat.ts#L31-L151)
    A `LngLat` object represents a given longitude and latitude coordinate, measured in degrees.
      These coordinates are based on the WGS84
        (EPSG:4326) standard.
    SDK JS uses longitude, latitude coordinate order (as opposed to latitude, longitude) to match the
      [GeoJSON specification](https://tools.ietf.org/html/rfc7946).
    
    Note that any SDK JS method that accepts a `LngLat` object as an argument or option
      can also accept an `Array` of two numbers and will perform an implicit conversion.
      This flexible type is documented as [LngLatLike](/sdk-js/api/geography/#lnglatlike).
  
  ### [Example](#lnglat-example)

  
    ```
``
```

  
  [Parameters](#lnglat-parameters)
  lng`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`Longitude,
      measured in degrees.
    
  lat`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`Latitude,
      measured in degrees.
    
  [Static Members](#lnglat-static-members)
  
    convert(input) 
              
            
    
      
          Converts an array of two numbers or an object with `lng` and `lat` or
            `lon` and `lat` properties
            to a `LngLat` object.
          If a `LngLat` object is passed in, the function returns it unchanged.
        
        [Parameters](#convert-lnglat-parameters)
        input`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`An
            array of two numbers or object to convert, or a
            `LngLat`
            object to return.
          
        [Returns](#convert-lnglat-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: A new
            `LngLat`
            object, if a conversion occurred, or the original
            `LngLat`
            object.
          
        [Example](#convert-lnglat-example)
        
          ```
``
```

        
      
    
  
  [Methods](#lnglat-instance-members)
  
    distanceTo(lngLat) 
              
            
    
      
          Returns the approximate distance between a pair of coordinates in meters
            Uses the Haversine Formula (from R.W. Sinnott, "Virtues of the Haversine", Sky and Telescope, vol. 68, no.
            2, 1984, p. 159)
        
        [Parameters](#distanceto-parameters)
        lngLat`([LngLat](/sdk-js/api/geography/#lnglat))`coordinates
            to compute the distance to
          
        [Returns](#distanceto-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          Distance in meters between the two coordinates.
          
        [Example](#distanceto-example)
        
          ```
``
```

        
      
    
  
  
    toArray() 
              
            
    
      
          Returns the coordinates represented as an array of two numbers.
        
        [Returns](#toarray-lnglat-returns)
        `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>`:
          The coordinates represeted as an array of longitude and latitude.
          
        [Example](#toarray-lnglat-example)
        
          ```
``
```

        
      
    
  
  
    toString() 
              
            
    
      
          Returns the coordinates represent as a string.
        
        [Returns](#tostring-lnglat-returns)
        `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`:
          The coordinates represented as a string of the format
            `'LngLat(lng, lat)'`
            .
          
        [Example](#tostring-lnglat-example)
        
          ```
``
```

        
      
    
  
  
    wrap() 
              
            
    
      
          Returns a new `LngLat` object whose longitude is wrapped to the range (-180, 180).
        
        [Returns](#wrap-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`:
          The wrapped
            `LngLat`
            object.
          
        [Example](#wrap-example)
        
        
          ```
``
```

        
      
    
  
  ### [Related examples](#lnglat-related)

  
    Get coordinates of the mouse
          pointer
      
    [Display a popup](/sdk-js/examples/popup/)
      
    Create a timeline
          animation
      
  

  
  [Point](#point)
    
      
    
  
  
    
    
    [ src/Point.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)
    
  
  
    A [Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts) two numbers representing
      `x` and `y` screen coordinates in pixels.
  
  [Example](#point-example)
  
  
    ```
``
```

  
  [Parameters](#point-parameters)
x`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`Longitude,
    measured in degrees.
  
y`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`Latitude,
    measured in degrees.
  

  [Static Members](#point-static-members)

    
      convert(a | p) 
                
              
      
        
            Construct a point from an array if necessary, otherwise if the input is already a Point, or an unknown type, return it unchanged.
          
          [Parameters](#convert-point-parameters)
          a`([Array[number]](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array))`An array of two numbers
              
          p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the point to return
            
          [Returns](#convert-point-returns)
          
          `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
            The new constructed point, or passed-through value..
            
          [Example](#convert-point-example)
          
          
            ```
``
```

          
        
      
      

  [Methods](#point-instance-members)

  add(p) 
            
          
  
    
        Add this point's x & y coordinates to another point, yielding a new point.
      
      [Parameters](#add-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#add-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#add-example)
      
      
        ```
``
```

      
    
  

  angle() 
            
          
  
    
        Get the angle from the 0, 0 coordinate to this point, in radians coordinates.
      
      [Returns](#angle-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The angle in radians.
        
      [Example](#angle-example)
      
      
        ```
``
```

      
    
  

  angleTo(p) 
            
          
  
    
        Get the angle from this point to another point, in radians
      
      [Parameters](#angleTo-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#angleTo-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The angle in radians.
        
      [Example](#angleTo-example)
      
      
        ```
``
```

      
    
  

  angleWith(p) 
            
          
  
    
        Get the angle between this point and another point, in radians
      
      [Parameters](#angleWith-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#angleWith-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The angle in radians.
        
      [Example](#angleWith-example)
      
      
        ```
``
```

      
    
  

  angleWithSep(x, y) 
            
          
  
    
        Find the angle of the two vectors, solving the formula for the cross product a x b = |a||b|sin(θ) for θ.
      
      [Parameters](#angleWithSep-parameters)
      x`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the x-coordinate
        
        y`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the y-coordinate
        
      [Returns](#angleWithSep-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The angle in radians.
        
      [Example](#angleWithSep-example)
      
      
        ```
``
```

      
    
  

  clone() 
            
          
  
    
        Clone this point, returning a new point that can be modified without affecting the old one.
      
      [Returns](#clone-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#clone-example)
      
      
        ```
``
```

      
    
  

  dist(p) 
            
          
  
    
        Calculate the distance from this point to another point.
      
      [Parameters](#dist-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#dist-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The distance.
        
      [Example](#dist-example)
      
      
        ```
``
```

      
    
  

  distSqr(p) 
            
          
  
    
        Calculate the distance from this point to another point, without the square root step. Useful if you're comparing relative distances.
      
      [Parameters](#distSqr-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#distSqr-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The distance.
        
      [Example](#distSqr-example)
      
      
        ```
``
```

      
    
  

  div(k) 
            
          
  
    
        Divide this point's x & y coordinates by a factor, yielding a new point.
      
      [Parameters](#div-parameters)
      k`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the factor
        
      [Returns](#div-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#div-example)
      
      
        ```
``
```

      
    
  

  divByPoint(p) 
            
          
  
    
        Divide this point's x & y coordinates by point, yielding a new point.
      
      [Parameters](#divByPoint-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#divByPoint-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#divByPoint-example)
      
      
        ```
``
```

      
    
  

  equals(p) 
            
          
  
    
        Judge whether this point is equal to another point, returning true or false.
      
      [Parameters](#equals-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#equals-returns)
      
      `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
        Whether the points are equal.
        
      [Example](#equals-example)
      
      
        ```
``
```

      
    
  

  mag() 
            
          
  
    
        Return the magnitude of this point: this is the Euclidean distance from the 0, 0 coordinate to this point's x and y coordinates.
      
      [Returns](#mag-returns)
      
      `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
        The magnitude.
        
      [Example](#mag-example)
      
      
        ```
``
```

      
    
  

  matMult(m) 
            
          
  
    
        Multiply this point by a 4x1 transformation matrix.
      
      [Parameters](#matMult-parameters)
      m`([Matrix2](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`Transformation matrix
        
      [Returns](#matMult-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#matMult-example)
      
      
        ```
``
```

      
    
  

  mult(k) 
            
          
  
    
        Multiply this point's x & y coordinates by a factor, yielding a new point.
      
      [Parameters](#mult-parameters)
      k`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the factor
        
      [Returns](#mult-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#mult-example)
      
      
        ```
``
```

      
    
  

  multByPoint(p) 
            
          
  
    
        Multiply this point's x & y coordinates by point, yielding a new point.
      
      [Parameters](#multByPoint-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#multByPoint-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#multByPoint-example)
      
      
        ```
``
```

      
    
  

  perp() 
            
          
  
    
        Compute a perpendicular point, where the new y coordinate is the old x coordinate and the new x coordinate is the old y coordinate multiplied by -1.
      
      [Returns](#perp-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The perpendicular point.
        
      [Example](#perp-example)
      
      
        ```
``
```

      
    
  

  rotate(a) 
            
          
  
    
        Rotate this point around the 0, 0 origin by an angle a, given in radians.
      
      [Parameters](#rotate-parameters)
      a`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`angle to rotate around, in radians
        
      [Returns](#rotate-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#rotate-example)
      
      
        ```
``
```

      
    
  

  rotateAround(a, p) 
            
          
  
    
        Rotate this point around p point by an angle a, given in radians.
      
      [Parameters](#rotateAround-parameters)
      a`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`angle to rotate around, in radians
        
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`Point to rotate around
        
      [Returns](#rotateAround-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#rotateAround-example)
      
      
        ```
``
```

      
    
  

  round() 
            
          
  
    
        Return a version of this point with the x & y coordinates rounded to integers.
      
      [Returns](#round-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new rounded point.
        
      [Example](#round-example)
      
      
        ```
``
```

      
    
  

  sub(p) 
            
          
  
    
        Subtract this point's x & y coordinates to from point, yielding a new point.
      
      [Parameters](#sub-parameters)
      p`([Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts))`the other point
        
      [Returns](#sub-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The new point.
        
      [Example](#sub-example)
      
      
        ```
``
```

      
    
  

  unit() 
            
          
  
    
        Calculate this point but as a unit vector from 0, 0, meaning that the distance from the resulting point to the 0, 0 coordinate will be equal to 1 and the angle from the resulting point to the 0, 0 coordinate will be the same as before.
      
      [Returns](#unit-returns)
      
      `[Point](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/Point.ts)`:
        The unit vector point.
        
      [Example](#unit-example)
      
      
        ```
``
```

      
    
  

  
  
  ## [LngLatBounds](#lnglatbounds)

  [src/geo/lng_lat_bounds.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/lng_lat_bounds.ts#L22-L258)
    A `LngLatBounds` object represents a geographical bounding box,
      defined by its southwest and northeast points in longitude and latitude.
    If no arguments are provided to the constructor, a `null` bounding box is created.
    Note that any GL method that accepts a `LngLatBounds` object as an argument or option
      can also accept an `Array` of two [LngLatLike](/sdk-js/api/geography/#lnglatlike) constructs and will perform an implicit
      conversion.
      This flexible type is documented as [LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike).
  
  [Example](#lnglatbounds-example)

  ```
``
```

  [Parameters](#lnglatbounds-parameters)
  sw`([LngLatLike](/sdk-js/api/geography/#lnglatlike)?)`The
      southwest corner of the bounding box.
    
  ne`([LngLatLike](/sdk-js/api/geography/#lnglatlike)?)`The
      northeast corner of the bounding box.
    
  [Static Members](#lnglatbounds-static-members)
  
    convert(input) 
              
            
    
      
          Converts an array to a `LngLatBounds` object.
          If a `LngLatBounds` object is passed in, the function returns it unchanged.
          Internally, the function calls `LngLat#convert` to convert arrays to `LngLat`
            values.
        
        [Parameters](#convert-lnglatbounds-parameters)
        input`([LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike))`An
            array of two coordinates to convert, or a
            `LngLatBounds`
            object to return.
          
        [Returns](#convert-lnglatbounds-returns)
        `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
          A new
            `LngLatBounds`
            object, if a conversion occurred, or the original
            `LngLatBounds`
            object.
          
        [Example](#convert-lnglatbounds-example)
        
          ```
``
```

        
      
    
  
  
    fromLngLat(center, radius) 
              
            
    
      
          Returns a `LngLatBounds` from the coordinates extended by a given `radius`. The
            returned `LngLatBounds` completely contains the `radius`.
        
        [Parameters](#fromLngLat-lnglatbounds-parameters)
        center`([LngLat](/sdk-js/api/geography/#lnglat))`(default
          `undefined`)Center coordinates of the new bounds.
        
        radius`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
            `0`)Distance in meters from the coordinates to extend the bounds.
          
        [Returns](#fromLngLat-lnglatbounds-returns)
        `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
          A new
            `LngLatBounds`
            object representing the coordinates extended by the
            `radius`
            .
          
        [Example](#fromLngLat-lnglatbounds-example)
        
          ```
``
```

        
      
    
  
  [Methods](#lnglatbounds-instance-members)
  
    contains(lnglat) 
              
            
    
      
          Check if the point is within the bounding box.
        
        [Parameters](#contains-parameters)
        lnglat`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`geographic
            point to check against.
          
        [Returns](#contains-returns)
        `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
          True if the point is within the bounding box.
          
        [Example](#contains-example)
        
          ```
``
```

        
      
    
  
  
    extend(obj) 
              
            
    
      
          Extend the bounds to include a given LngLatLike or LngLatBoundsLike.
        
        [Parameters](#extend-parameters)
        obj`(([LngLatLike](/sdk-js/api/geography/#lnglatlike) | [LngLatBoundsLike](/sdk-js/api/geography/#lnglatboundslike)))`object
            to extend to
          
        [Returns](#extend-returns)
        
        `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
          `this`
          
      
    
  
  
    getCenter() 
              
            
    
      
          Returns the geographical coordinate equidistant from the bounding box's corners.
        
        [Returns](#getcenter-lnglatbounds-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            bounding box's center.
          
        [Example](#getcenter-lnglatbounds-example)
        
          ```
``
```

        
      
    
  
  
    getEast() 
              
            
    
      
          Returns the east edge of the bounding box.
        
        [Returns](#geteast-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          The east edge of the bounding box.
          
      
    
  
  
    getNorth() 
              
            
    
      
          Returns the north edge of the bounding box.
        
        [Returns](#getnorth-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          The north edge of the bounding box.
          
      
    
  
  
    getNorthEast() 
              
            
    
      
          Returns the northeast corner of the bounding box.
        
        [Returns](#getnortheast-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            northeast corner of the bounding box.
          
      
    
  
  
    getNorthWest() 
              
            
    
      
          Returns the northwest corner of the bounding box.
        
        [Returns](#getnorthwest-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            northwest corner of the bounding box.
          
      
    
  
  
    getSouth() 
              
            
    
      
          Returns the south edge of the bounding box.
        
        [Returns](#getsouth-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          The south edge of the bounding box.
          
      
    
  
  
    getSouthEast() 
              
            
    
      
          Returns the southeast corner of the bounding box.
        
        [Returns](#getsoutheast-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            southeast corner of the bounding box.
          
      
    
  
  
    getSouthWest() 
              
            
    
      
          Returns the southwest corner of the bounding box.
        
        [Returns](#getsouthwest-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            southwest corner of the bounding box.
          
      
    
  
  
    getWest() 
              
            
    
      
          Returns the west edge of the bounding box.
        
        [Returns](#getwest-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          The west edge of the bounding box.
          
      
    
  
  
    isEmpty() 
              
            
    
      
          Check if the bounding box is an empty/`null`-type box.
        
        [Returns](#isempty-returns)
        `[boolean](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)`:
          True if bounds have been defined, otherwise false.
          
      
    
  
  
    setNorthEast(ne) 
              
            
    
      
          Set the northeast corner of the bounding box
        
        [Parameters](#setnortheast-parameters)
        ne`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`a
            [LngLatLike](/sdk-js/api/geography/#lnglatlike)
            object describing the northeast corner of the bounding box.
          
        [Returns](#setnortheast-returns)
        `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
          `this`
          
      
    
  
  
    setSouthWest(sw) 
              
            
    
      
          Set the southwest corner of the bounding box
        
        [Parameters](#setsouthwest-parameters)
        sw`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`a
            [LngLatLike](/sdk-js/api/geography/#lnglatlike)
            object describing the southwest corner of the bounding box.
          
        [Returns](#setsouthwest-returns)
        `[LngLatBounds](/sdk-js/api/geography/#lnglatbounds)`:
          `this`
          
      
    
  
  
    toArray() 
              
            
    
      
          Returns the bounding box represented as an array.
        
        [Returns](#toarray-lnglatbounds-returns)
        `[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)>>`:
          The bounding box represented as an array, consisting of the
            southwest and northeast coordinates of the bounding represented as arrays of numbers.
          
        [Example](#toarray-lnglatbounds-example)
        
          ```
``
```

        
      
    
  
  
    toString() 
              
            
    
      
          Return the bounding box represented as a string.
        
        [Returns](#tostring-lnglatbounds-returns)
        `[string](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)`:
          The bounding box represents as a string of the format

            `'LngLatBounds(LngLat(lng, lat), LngLat(lng, lat))'`
            .
          
        [Example](#tostring-lnglatbounds-example)
        
          ```
``
```

        
      
    
  

  
  
  ## [LngLatLike](#lnglatlike)

  [src/geo/lng_lat.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/lng_lat.ts#L153-L162)
    A [LngLat](/sdk-js/api/geography/#lnglat) object, an array of two numbers representing
      longitude and latitude,
      or an object with `lng` and `lat` or `lon` and `lat` properties.
  
  [Example](#lnglatlike-example)
  
    ```
``
```

  

  
  ## [PointLike](#pointlike)

  [src/ui/camera.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/ui/camera.ts#L17-L24)
    A [Point](https://github.com/mapbox/point-geometry) or an array of two numbers representing
      `x` and `y` screen coordinates in pixels.
  
  [Example](#pointlike-example)
  
  
    ```
``
```

  

  
  [LngLatBoundsLike](#lnglatboundslike)
  
  [src/geo/lng_lat_bounds.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/lng_lat_bounds.ts#L260-L272)
    A [LngLatBounds](/sdk-js/api/geography/#lnglatbounds) object, an array of [LngLatLike](/sdk-js/api/geography/#lnglatlike) objects in [sw, ne] order,
      or an array of numbers in [west, south, east, north] order.
  
  [Example](#lnglatboundslike-example)
  
    ```
``
```

  

  
  [MercatorCoordinate](#mercatorcoordinate)
  [src/geo/mercator_coordinate.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/mercator_coordinate.ts#L77-L146)
    A `MercatorCoordinate` object represents a projected three dimensional position.
    `MercatorCoordinate` uses the web mercator projection ([EPSG:3857](https://epsg.io/3857))
      with slightly different units:
    
      the size of 1 unit is the width of the projected world instead of the "mercator meter"
      the origin of the coordinate space is at the north-west corner instead of the middle
    
    For example, `MercatorCoordinate(0, 0, 0)` is the north-west corner of the mercator world and
      `MercatorCoordinate(1, 1, 0)` is the south-east corner. If you are familiar with
      [vector tiles](https://github.com/mapbox/vector-tile-spec) it may be helpful to think
      of the coordinate space as the `0/0/0` tile with an extent of `1`.
    
    The `z` dimension of `MercatorCoordinate` is conformal. A cube in the mercator coordinate
      space would be rendered as a cube.
  
  [Example](#mercatorcoordinate-example)

  ```
``
```

  [Parameters](#mercatorcoordinate-parameters)
  x`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
      x component of the position.
    
  y`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`The
      y component of the position.
    
  z`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
      `0`)The z component of the position.
    
  [Static Members](#mercatorcoordinate-static-members)
  
    fromLngLat(lngLatLike,
            altitude) 
              
            
    
      
          Project a `LngLat` to a `MercatorCoordinate`.
        
        [Parameters](#fromlnglat-mercatorcoordinate-parameters)
        lngLatLike`([LngLatLike](/sdk-js/api/geography/#lnglatlike))`The
            location to project.
          
        altitude`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
            `0`)The altitude in meters of the position.
          
        [Returns](#fromlnglat-mercatorcoordinate-returns)
        `[MercatorCoordinate](/sdk-js/api/geography/#mercatorcoordinate)`:
          The projected mercator coordinate.
          
        [Example](#fromlnglat-mercatorcoordinate-example)
        
          ```
``
```

        
      
    
  
  [Methods](#mercatorcoordinate-instance-members)
  
    meterInMercatorCoordinateUnits() 
              
            
    
      
          Returns the distance of 1 meter in `MercatorCoordinate` units at this latitude.
          For coordinates in real world units using meters, this naturally provides the scale
            to transform into `MercatorCoordinate`s.
        
        [Returns](#meterinmercatorcoordinateunits-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          Distance of 1 meter in
            `MercatorCoordinate`
            units.
          
      
    
  
  
    toAltitude() 
              
            
    
      
          Returns the altitude in meters of the coordinate.
        
        [Returns](#toaltitude-returns)
        `[number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)`:
          The altitude in meters.
          
        [Example](#toaltitude-example)
        
          ```
``
```

        
      
    
  
  
    toLngLat() 
              
            
    
      
          Returns the `LngLat` for the coordinate.
        
        [Returns](#tolnglat-returns)
        `[LngLat](/sdk-js/api/geography/#lnglat)`: The
            `LngLat`
            object.
          
        [Example](#tolnglat-example)
        
          ```
``
```

        
      
    
  
  [Related examples](#mercatorcoordinate-related)
  
    Add a custom style
          layer
      
  

  
  
  ## [EdgeInsets](#edgeinsets)

  [src/geo/edge_insets.ts](https://github.com/maplibre/maplibre-gl-js/tree//src/geo/edge_insets.ts#L15-L97)
    An `EdgeInset` object represents screen space padding applied to the edges of the viewport.
      This shifts the apprent center or the vanishing point of the map. This is useful for adding floating UI elements
      on top of the map and having the vanishing point shift as UI elements resize.
  
  [Parameters](#edgeinsets-parameters)
  top`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
      `0`)
  bottom`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
      `0`)
  left`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
      `0`)
  right`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`(default
      `0`)
  [Static Members](#edgeinsets-static-members)
  
    getCenter(width, height) 
              
            
    
      
          Utility method that computes the new apprent center or vanishing point after applying insets.
            This is in pixels and with the top left being (0.0) and +y being downwards.
        
        [Parameters](#getcenter-edgeinsets-parameters)
        width`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the
            width
          
        height`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`the
            height
          
        [Returns](#getcenter-edgeinsets-returns)`Point`: the point
          
      
    
  
  
    interpolate(start, target, t) 
              
            
    
      
          Interpolates the inset in-place.
            This maintains the current inset value for any inset not present in `target`.
        
        [Parameters](#interpolate-parameters)
        start`(([PaddingOptions](/sdk-js/api/properties/#paddingoptions) | [EdgeInsets](/sdk-js/api/geography/#edgeinsets)))`interpolation
            start
          
        target`([PaddingOptions](/sdk-js/api/properties/#paddingoptions))`interpolation
            target
          
        t`([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))`interpolation
            step/weight
          
        [Returns](#interpolate-returns)
        `[EdgeInsets](/sdk-js/api/geography/#edgeinsets)`:
          the insets
          
      
    
  
  
    toJSON() 
              
            
    
      
          Returns the current state as json, useful when you want to have a
            read-only representation of the inset.
        
        [Returns](#tojson-returns)
        
        `[PaddingOptions](/sdk-js/api/properties/#paddingoptions)`:
          state as json
