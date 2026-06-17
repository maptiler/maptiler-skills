# Source: https://docs.maptiler.com/sdk-js/api/color-ramp/

[ src/ColorRamp.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/ColorRamp.ts)
   

  A color ramp is a color gradient defined in a specific interval, for instance in [0, 1], 
  and for any value within this interval will retrieve a color. 
  They are defined by at least a color at each bound and usualy additional colors within the range.

  Color ramps are super useful to represent numerical data in a visual way: 
  the temperature, the population density, the average commute time, etc.

Example

```
``
```

  To use an already existing color ramp and access some of its values:

```
``
```

  Creating a new one consists in defining all the colors for each *color stops*. 
  The values can be in the range of interest and *do not* have to be in [0, 1]. 
  For example, let's recreate a *Viridis* color ramp but with a range going from 0 to 100:

```
``
```

  When defining a new ramp, the colors can be a 
  RGB array (`[number, number, number]`) or a 
  RGBA array (`[number, number, number, number]`).

  View more [Color Ramp examples](/sdk-js/examples/?q=%28color+ramp%29)

## [Parameters](#color-ramp-parameters)

  options? (ColorRampOptions) 
            
          
  
    
        Options to provide to the constructor
        (ColorRampOptions)
      
      [Properties](#color-ramp-options)
      
        
| The value the colorramp starts |
| The value the colorramp ends |
| Some color stops to copy from |

      
    
  

## [Methods](#color-ramp-methods)

  clone()
         
            
          
  
    
        Clone the color ramp.
        
      
      [Returns](#clone-returns)
      `[ColorRamp](#color-ramp)`: The cloned color ramp
      [Example](#clone-example)
      
        ```
``
```

      
    
  

  getBounds()
         
            
          
  
    
        Get the colorramp starts and end values.
        
      
      [Returns](#getBounds-returns)
      `Object`: The color ramp `min` and `max` values
      [Example](#getBounds-example)
      
        ```
``
```

      
    
  

  getCanvasStrip(options?)
         
            
          
  
    
        Get the colorramp starts and end values.
        
      
      [Parameters](#getCanvasStrip-parameters)
      
        options?
        (`Object`)
        : The options object.
        
          
|  |
|  |
|  |

        
      
      [Returns](#getCanvasStrip-returns)
      `HTMLCanvasElement`: The color ramp `canvas`
      [Example](#getCanvasStrip-example)
      
        ```
``
```

      
    
  

  
    
      getColor
        (value, options?)
         
            
          
        
      
    
  
  
    
      Get the color for a given value.
      [Parameters](#getColor-parameters)
      
        value
        ([`number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))
        : value from color 
        
      
      
        options?
        (`Object`)
        : The options object.
        
          
|  |

        
      
      [Returns](#getColor-returns)
      `RgbaColor`: The color for the given value
      [Example](#getColor-example)
      
        ```
``
```

      
    
  

  
    
      getColorHex
        (value, options?)
         
            
          
        
      
    
  
  
    
      Get the color as an hexadecimal string for a given value.
      [Parameters](#getColorHex-parameters)
      
        value
        ([`number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))
        : value from color 
        
      
      
        options?
        (`Object`)
        : The options object.
        
          
|  |
|  |

        
      
      [Returns](#getColorHex-returns)
      `HexColor`: The color for the given value
      [Example](#getColorHex-example)
      
        ```
``
```

      
    
  

  
    
      getColorRelative
        (value, options?)
         
            
          
        
      
    
  
  
    
      Get the color of the color ramp at a relative position in [0, 1]
      [Parameters](#getColorRelative-parameters)
      
        value
        ([`number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))
        : value from color 
        
      
      
        options?
        (`Object`)
        : The options object.
        
          
|  |

        
      
      [Returns](#getColorRelative-returns)
      `RgbaColor`: The color for the given value
      [Example](#getColorRelative-example)
      
        ```
``
```

      
    
  

  
    
      getRawColorStops
        ()
        
          
            
          
        
      
    
  
  
    
       Get color ramp color stops array.
      Returns
      `Array`: ColorStop
      Example
      
        ```
``
```

      
    
  

  
    
      reverse
        (options?)
        
          
            
          
        
      
    
  
  
    
      Reverse the color ramp.
      Parameters
      
        options?
        (`Object`)
        : The options object.
        
          
| Clone the reverse color ramp |

        
      
      Returns
      `ColorRamp`: The reversed color ramp
      Example
      
        ```
``
```

      
    
  

  
    
      scale
        (min, max, options?)
        
          
            
          
        
      
    
  
  
    
       Scale the color ramp min and max values.
      Parameters
      
        min
        (`number`)
        : Minimum color ramp value
      
      
        max
        (`number`)
        : Maximum color ramp value
      
      
        options?
        (`Object`)
        : The options object.
        
          
| Clone the scaled color ramp |

        
      
      Returns
      `ColorRamp`: The scaled color ramp
      Example
      
        ```
``
```

      
    
  

  
    
      setStops
        (stops, options?)
        
          
            
          
        
      
    
  
  
    
       Change the color ramp stops values and colors
      Parameters
      
        stops
        ([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<ColorStop>)
        : New color stops
      
      
        options?
        (`Object`)
        : The options object.
        
          
| Clone the color ramp |

        
      
      Returns
      `ColorRamp`: The color ramp with the new stops
      Example
      
        ```
``
```

      
    
  

  
    
      fromArrayDefinition
        (cr)
        
          
            
          
        
      
    
  
  
    
      `Static` Converts a array-definition color ramp definition into a usable ColorRamp instance. Note: units are not converted and may need to to be converted beforehand (eg. kelvin to centigrade)
      Parameters
      
        cr
        ([Array](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)<ArrayColorRampStop>)
        : A color ramp as per array definition
      
      Returns
      `ColorRamp`: The new color ramp
      Example
      
        ```
``
```

      
    
  

  
    
      resample
        (method, samples)
        
          
            
          
        
      
    
  
  
    
      Apply a non-linear ressampling. This will create a new instance of ColorRamp with the same bounds.
        Check out the [non-linear color ramps](#color-ramp-non-linear) section to see how to apply the resampling to a point layer visualization.
      
      Parameters
      
        method
        (`"ease-in-square"` |
        `"ease-out-square"` |
        `"ease-in-sqrt"` |
        `"ease-out-sqrt"` |
        `"ease-in-exp"` |
        `"ease-out-exp"`)
        : Ressampling method
      
      
        samples
        ([number](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number))
        : number of steps. Default: 15
      
      Returns
      `ColorRamp`: The new color ramp
      Example
      
        ```
``
```

      
    
  

  
    
      transparentStart
        ()
        
          
            
          
        
      
    
  
  
    
      Makes a clone of this color ramp that is fully transparant at the begining of their range.
      Returns
      `ColorRamp`: The new color ramp
      Example
      
        ```
``
```

      
    
  

  
    
      hasTransparentStart
        ()
        
          
            
          
        
      
    
  
  
    
       Check if this color ramp has a transparent start.
      Returns
      `Boolean`: color ramp has a transparent start
      Example
      
        ```
``
```

      
    
  

## [Non-linear color ramps](#color-ramp-non-linear)

  In this section we will see how to use the `resample` 
  function of a color ramp to improve the visualization of data from a point layer. 

  We are using a large dataset containing all the [public schools](/sdk-js/assets/schools.geojson) in the US.
  We are using the `PORTLAND` color ramp:

  For the purpose of visualising the number of students, we are going to scale the `PORTLAND` 
  color ramp on the range `300` to `4000` 
  as most schools will contains more than 300 students and less than 4000.

### [Linear](#color-ramp-linear)

  We used the following color ramp definition:

```
``
```

Here is how the data looks like over a New York City:

  It's not entirely bad, but only the very large schools stand out and it's quite difficult, 
  without looking at the numbers, to differentiate all the blue dots just from their color variations.

  Generally speaking in data visualisation, small variations matter towards the lower bound and large variations 
  matter towards the upper bound. For this particular dataset, we would like a schools with 300 students to show 
  differently from a school with 500 (IOW, a small difference of 200 in the lower bound), but we would like a school 
  with 3800 students to look roughly the same as one with 4000 students (IOW, a small difference on the upper bound). 
  And this is where **non linear rescaling** or color ramps comes into play!

[Non-linear: ease-out square-root](#color-ramp-non-linear-ease-out-square-root)

*Easing-out* is a way to say that something accelerates a lot at the beginning of a given interval 
  and slows down towards the end, while still increasing all the way (aka. monotonically increasing).

  To perform the nonlinear rescaling of color ramps, MapTiler SDK performs some intermediate range changes so 
  that only the range `[0, 1]` is actually relevant to observe 
  (but then rescaled to its original range). Here is how the square root function looks like, 
  naturally being of the ease-out kind:

To obtain a `PORTLAND` color ramp scaled with the square root method, we can do:

```
``
```

  This results in the following version of `PORTLAND`:

  As we can see if we compare with its linear version, this resampled color ramp is slightly left-skewed
  and shows much faster variations towards the beginning of the range. That's exactly what we want to leverage 
  to better visualise the differences between schools with fewer number of students.

Here is how the same data looks like now:

  It's no longer about blue dots everywhere! We can now fairly easily differentiate a school 
  with 400 students than one with 800.

[Non-linear going too far: ease-out exponential](#color-ramp-non-linear-ease-out-exp)

  Some functions have a much steeper slope than the square root function and would emphasise the differences 
  even more on the lower bound, maybe a bit too much, at the expense of clarity for the rest of the range.

  For very specific usages, the SDK features an exponential resampling. 
  Here is how its function looks like on `[0, 1]` range:

  As we can see, starting from `x = 0.5` there is very little variation left.

  Here is how to create the corresponding `PORTLAND` color ramp:

```
``
```

  The color ramp created looks very left-skewed:

  And the map visualisation:

  The South Bronx (north of Manhattan) contains many smaller schools that now look like they no longer have this 
  blue color representative of the lower bound from the Portland color ramp. 
  This is basically means we crossed a line in terms of resampling function and that our color ramp is no longer 
  suitable for our purpose.

  Of course, knowing that the granularity of the color ramp on the second half is very poor, 
  we can change its range, maybe double it to `[300, 8000]`:

```
``
```

  And we would still obtain a decent visualisation:

  But then, the process is backward and means the data range is adapted based on the capabilities and limitations 
  of the color ramp. This adds an unnecessary overhead. 

> [!IDEA]
> For this visualization we recommend using **Non-linear: ease-out square-root** `.resample("ease-out-sqrt)`.

  const colorrampContainer_portland = document.getElementById("colorramp-portland");
  const colorramp_portland = maptilersdk.ColorRampCollection.PORTLAND;
  createColorRampDiv(colorramp_portland, colorrampContainer_portland);
  const colorrampContainer_portland_ease_out_square_root = document.getElementById("colorramp-portland-ease-out-square-root");
  const colorramp_portland_ease_out_square_root = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-sqrt");
  createColorRampDiv(colorramp_portland_ease_out_square_root, colorrampContainer_portland_ease_out_square_root);
  const colorrampContainer_portland_ease_out_exp = document.getElementById("colorramp-portland-ease-out-exp");
  const colorramp_portland_ease_out_exp = maptilersdk.ColorRampCollection.PORTLAND.scale(300, 4000).resample("ease-out-exp");
  createColorRampDiv(colorramp_portland_ease_out_exp, colorrampContainer_portland_ease_out_exp);

  function createColorRampDiv(colorramp, containter, name) {
    const canvas = colorramp.getCanvasStrip();
    canvas.style.height = "30px";
    canvas.style.width = "100%";
    canvas.style.border = "1px dashed #00000059";

    const bounds = colorramp.getBounds()

    const div = document.createElement("div");
    if (name) {
      const descSpan = document.createElement("span");
      descSpan.innerHTML = `${name} (min: ${bounds.min}, max: ${bounds.max})`;
      div.appendChild(descSpan);
    }
    
    div.appendChild(canvas);
    containter.appendChild( div );
  }

## [Builtin color ramps](#color-ramp-builtin)

  The SDK includes many built-in ready to use color ramps as well as extra logic to manipulate them and create new ones, 
  here is the full list:

  const colorrampContainer = document.getElementById("colorramp-contain");
  Object.keys(maptilersdk.ColorRampCollection).forEach(k => {
    const colorramp = maptilersdk.ColorRampCollection[k];
    createColorRampDiv(colorramp, colorrampContainer, k);
  })

##### [Types and Interfaces](#types)

###### [ColorStop](#ColorStop)

```javascript

  {
    value: number, // The "value" at which this ColorStop should be applied.
    color: string // GB[A] - Array of 3-4 numbers. 0-255 per channel.
  }

```
