# Source: https://docs.maptiler.com/sdk-js/api/map-styles/

[ src/mapstyle.ts](https://github.com/maptiler/maptiler-sdk-js/blob/main/src/mapstyle.ts)
  

  
    The built-in map styles defined in the [Client JS library](/client-js/#map-styles) are exposed
    by the SDK so that they can easily be used.
  
  MapTiler teams maintains a few styles that we have decided to expose as style shorthand from the SDK.
    Our built-in styles are designed to make it easier for you to create beautiful maps, without the need for extra
    coding or worrying about outdated versions.
    This has several advantages:
  
    If we make an update to a style, you won't have to modify your codebase. Always use the latest version of
      styles.
    They are easier to remember, no need to type along style URL. No more putting the API key in every URL.
    Code completion: reducing typos and other common mistakes.
  
  
  
    The built-in styles generaly defines a purpose for which this style is the most relevant: street navigation, outdoor
    adventure, minimalist dashboard, etc.
    Then, each style offers a range of variants that contain the same level of information and has the same purpose but
    using different colors schemes like dark, light, etc.
  
  
    [ReferenceMapStyle](#referencemapstyle)
    
      
    
  
  A reference syle sets some guidelines about what kind of information is displayed, the granularity of the
    information,
    and more generaly defines a purpose for which this style is the most relevant: street navigation, outdoor adventure,
    minimalist dashboard, etc.
  
    The `MapStyle.REFERENCE_MAP_STYLE` is an instance of the class [ReferenceMapStyle](https://github.com/maptiler/maptiler-client-js/blob/main/src/mapstyle.ts) (with a
    proxy layer).
  
  [Example](#referencemapstyle-example)
  
## Reference Styles & Variants — Authoritative Full List

MapTiler exposes 15 reference styles via the `MapStyle` proxy. Each reference style can be used directly (`MapStyle.STREETS`) or with a variant (`MapStyle.STREETS.DARK`). Requesting a non-existent variant silently falls back to `.DEFAULT`.

| Reference Style | Purpose | Variants |
| :--- | :--- | :--- |
| `MapStyle.AQUARELLE` | Artistic watercolor map | `.DARK`, `.VIVID` |
| `MapStyle.BACKDROP` | Monochrome context map | `.DARK`, `.LIGHT` |
| `MapStyle.BASE` | Clear general-purpose map | `.DARK`, `.LIGHT` |
| `MapStyle.BRIGHT` | Shiny map for context or navigation | `.DARK`, `.LIGHT`, `.PASTEL` |
| `MapStyle.DATAVIZ` | Simple data visualization map | `.DARK`, `.LIGHT` |
| `MapStyle.HYBRID` | Beautiful satellite map with context (labels, borders, roads) | `.DARK` |
| `MapStyle.LANDSCAPE` | Light hillshade map | `.DARK`, `.VIVID` |
| `MapStyle.OCEAN` | Seabed and bathymetry map | `.DARK` |
| `MapStyle.OPENSTREETMAP` | Rich, familiar OSM community style | `.DARK` |
| `MapStyle.OUTDOOR` | Map for hiking and sports (peaks, parks, isolines) | `.DARK` |
| `MapStyle.SATELLITE` | Beautiful satellite map (high resolution imagery) | `.DARK` |
| `MapStyle.STREETS` | Comprehensive street map, perfect for urban areas | `.DARK`, `.PASTEL` |
| `MapStyle.TONER` | Contrasted monochrome map | `.LITE` |
| `MapStyle.TOPO` | General-purpose topographic map | `.DARK`, `.PASTEL`, `.TOPOGRAPHIQUE` |
| `MapStyle.WINTER` | Map for winter activities (skiing, snowboarding) | `.DARK` |

**Legacy alias**: `MapStyle.BASIC` resolves to `MapStyle.BASE` in current SDKs. Prefer `BASE` in new code — it matches the underlying `base-v4` URL slug.

---

## Original API Docs (scraped)

The remainder of this file is the scraped API documentation for the `ReferenceMapStyle` and `MapStyleVariant` classes. The original page also listed a subset of styles below — those tables are kept here only for completeness; **the authoritative list is the table above**.

  [Methods](#referencemapstyle-methods)
  
  
    
      addVariant(v)
            
              
            
    
    
      
        
          Add a variant to the reference style
        
        
          [Parameters](#addVariant-referencemapstyle-parameters)
        
        
          v(MapStyleVariant)
          Map style variant to add.
          
        
      
    
  
  
    
      getDefaultVariant()
            
              
            
    
    
      
        
          Get the defualt variant for the reference style.
          
        
        
          [Returns](#getDefaultVariant-referencemapstyle-returns)
        
        MapStyleVariant
      
    
  
  
    
      getId()
            
              
            
    
    
      
        
          Get the id of the reference style
        
        
          [Returns](#getId-referencemapstyle-returns)
        
        string: id of the style
      
    
  
  
    
      getName()
            
              
            
    
    
      
        
          Get the human-friendly name of the reference style
        
        
          [Returns](#getName-referencemapstyle-returns)
        
        string: human-friendly name of the style
      
    
  
  
    
      getVariant(variantType)
            
              
            
    
    
      
        
          Get a given variant. If the given type of variant does not exist for this reference style,
            then the most relevant default variant is returned instead.
          
        
        
          [Parameters](#getVariant-referencemapstyle-parameters)
        
        
          variantType(string)
          Name of the style variant to get.
          
        
        
          [Returns](#getVariant-referencemapstyle-returns)
        
        MapStyleVariant
      
    
  
  
    
      getVariants()
            
              
            
    
    
      
        
          Get the list of variants for this reference style.
          
        
        
          [Returns](#getVariants-referencemapstyle-returns)
        
        Array[MapStyleVariant]: list of variants
      
    
  
  
    
      hasVariant(variantType)
            
              
            
    
    
      
        
          Check if a given variant type exists for this reference style
        
        
          [Parameters](#hasVariant-referencemapstyle-parameters)
        
        
          variantType(string)
          Name of the style variant to check.
          
        
        
          [Returns](#hasVariant-referencemapstyle-returns)
        
        boolean
      
    
  

  
    [MapStyleVariant](#mapstylevariant)
    
      
    
  
  
    Each reference style offers a range of variants that contain the same level of information and has the same purpose
    but using different colors schemes.
  
  
    The `MapStyle.REFERENCE_MAP_STYLE.MAP_STYLE_VARIANT` is an instance of the
    class [MapStyleVariant](https://github.com/maptiler/maptiler-client-js/blob/main/src/mapstyle.ts).
    The proxy layer on top of each ReferenceMapStyle instance is useful to catch any inexistant variant and still
    fallback on the default one.
  
  For example, `MapStyle.STREETS` is an proxied instance of ReferenceMapStyle
    and if we look for the DARK variant
    (instance of the class MapStyleVariant), we need to type `MapStyle.STREETS.DARK` but if we were looking for an inexisting variant,
    such as `MapStyle.STREETS.INDIGO` then `MapStyle.STREETS` will fallback on
    `MapStyle.STREETS.DEFAULT` (the advantage of a proxy compared to a classic
    getter is the dynamic resolution of the property)
  
  [Example](#mapstylevariant-example)
  
| `MapStyle.DATAVIZ.DARK` |  | A minimalist style for data visualization. Also available in color and light mode |
| `MapStyle.DATAVIZ.LIGHT` |  | A minimalist style for data visualization. Also available in color and dark mode |
| `MapStyle.BRIGHT.PASTEL` |  | A minimalist style for high contrast navigation. Also available in color, dark and light mode |

  [Methods](#mapstylevariant-methods)
  
  
    
      getDescription()
            
              
            
    
    
      
        
          Get the human-friendly description
        
        
          [Returns](#getDescription-mapstylevariant-returns)
        
        string: human-friendly description of the style
      
    
  
  
    
      getExpandedStyleURL()
            
              
            
    
    
      
        
          Get the style as usable by MapLibre, a string (URL) or a plain style description (StyleSpecification)
        
        
          [Returns](#getExpandedStyleURL-mapstylevariant-returns)
        
        string: string (URL) or a plain style description (StyleSpecification)
      
    
  
  
    
      getFullName()
            
              
            
    
    
      
        
          Get the full name of the style variant
        
        
          [Returns](#getFullName-mapstylevariant-returns)
        
        string: full name of the style
      
    
  
  
    
      getId()
            
              
            
    
    
      
        
          Get the MapTiler id
        
        
          [Returns](#getId-mapstylevariant-returns)
        
        string: id of the style
      
    
  
  
    
      getImageURL()
            
              
            
    
    
      
        
          Get the image URL that represent this variant
        
        
          [Returns](#getImageURL-mapstylevariant-returns)
        
        string: image url of the style
      
    
  
  
    
      getName()
            
              
            
    
    
      
        
          Get the human-friendly name
        
        
          [Returns](#getName-mapstylevariant-returns)
        
        string: human-friendly name of the style
      
    
  
  
    
      getReferenceStyle()
            
              
            
    
    
      
        
          Get the reference style this variant belongs to.
          
        
        
          [Returns](#getReferenceStyle-mapstylevariant-returns)
        
        ReferenceMapStyle
      
    
  
  
    
      getType()
            
              
            
    
    
      
        
          Get the variant type (eg. "DEFAULT", "DARK", "PASTEL", etc.)
        
        
          [Returns](#getType-mapstylevariant-returns)
        
        string: varian type
      
    
  
  
    
      getVariant(variantType)
            
              
            
    
    
      
        
          Retrieve the variant of a given type. If not found, will return the "DEFAULT" variant.
            (eg. _this_ "DARK" variant does not have any "PASTEL" variant, then the "DEFAULT" is returned).
          
        
        
          [Parameters](#getVariant-mapstylevariant-parameters)
        
        
          variantType(string)
          Name of the style variant to get.
          
        
        
          [Returns](#getVariant-mapstylevariant-returns)
        
        MapStyleVariant
      
    
  
  
    
      getVariants()
            
              
            
    
    
      
        
          Get all the variants for this variants, except this current one.
          
        
        
          [Returns](#getVariants-mapstylevariant-returns)
        
        Array[MapStyleVariant]: list of variants
      
    
  
  
    
      hasVariant(variantType)
            
              
            
    
    
      
        
          Check if a variant of a given type exists for this variants
            (eg. if this is a "DARK", then we can check if there is a "LIGHT" variant of it).
          
        
        
          [Parameters](#hasVariant-mapstylevariant-parameters)
        
        
          variantType(string)
          Name of the style variant to check.
          
        
        
          [Returns](#hasVariant-mapstylevariant-returns)
        
        boolean
      
    
  

  
    [Map Styles list](#mapstylelist)
    
      
    
  
  
    MapTiler provides some **reference styles** as well as some **variants** for each. See the **Reference Styles & Variants — Authoritative Full List** table at the top of this file.

  

  [Related examples](#mapstyle-related)
  
  
    [Built-in map styles](/sdk-js/examples/built-in-styles/)
      
    
    [How to display a style switcher control](/sdk-js/examples/control-style-switcher/)
      
    
    [How to display your custom map on the web page](/sdk-js/examples/custom-map/)
