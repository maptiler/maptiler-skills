# MapTiler iOS SDK API Reference - root

This document is a part of the iOS SDK API reference documentation, covering the `root` category.

---

## File: Actors.html

---
layout: mobile_sdk
title: "Actors"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following actors are available globally."
id: actors
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Actors

The following actors are available globally.

- 

MTConfig

Object representing the SDK global settings.

Exposes properties and options such as API Key and caching preferences.

See more

#### Declaration

Swift
`public actor MTConfig`

---

## File: Classes.html

---
layout: mobile_sdk
title: "Classes"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following classes are available globally."
id: classes
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Classes

The following classes are available globally.

- 

MTCustomAnnotationView

Subclassable view for adding custom annotations to the map.

See more

#### Declaration

Swift
@MainActor
open class MTCustomAnnotationView : UIView, @preconcurrency MTAnnotation
`extension MTCustomAnnotationView: @preconcurrency MTMapViewContent`

- 

MTMarker

Annotation element that can be added to the map.

See more

#### Declaration

Swift
`public class MTMarker : MTAnnotation, MTMapViewContent, @unchecked Sendable`

- 

MTTextPopup

Basic text popup.

Can be attached to MTMarker or standalone.

See more

#### Declaration

Swift
`public class MTTextPopup : MTAnnotation, MTMapViewContent, @unchecked Sendable`

- 

MTBenchmark

Basic benchmarking class.

See more

#### Declaration

Swift
@MainActor
public final class MTBenchmark : MTMapViewDelegate

- 

MTMapView

Object representing the map on the screen.

Exposes methods and properties that enable changes to the map,
and fires events that can be interacted with.

See more

#### Declaration

Swift
@MainActor
open class MTMapView : UIView, Sendable
`extension MTMapView: MTControllable`
`extension MTMapView: MTNavigable`
`extension MTMapView: MTRendering`
`extension MTMapView: MTStylable`
`extension MTMapView: MTZoomable`
`extension MTMapView: MTLocationManagerDelegate`

- 

MTHeatmapLayerHelper

Helper for creating a heatmap visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTHeatmapLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPointLayerHelper

Helper for creating a point visualization layer from data and styling options.

Uses the current style to create the underlying source and layers.

See more

#### Declaration

Swift
`public final class MTPointLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPolygonLayerHelper

Helper for creating a polygon (fill) visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTPolygonLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPolylineLayerHelper

Helper for creating a polyline (line) visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTPolylineLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTLogger

Logger class used for SDK logs.

See more

#### Declaration

Swift
`public class MTLogger`

- 

MTLocationManager

Class responsible for location updates.

See more

#### Declaration

Swift
`public class MTLocationManager : NSObject, @preconcurrency CLLocationManagerDelegate`

- 

MTGestureService

Service responsible for gesture handling and state.

See more

#### Declaration

Swift
@MainActor
public class MTGestureService

- 

MTMapCameraHelper

Sets combination of center, bearing and pitch, as well as roll and elevation.

See more

#### Declaration

Swift
`public class MTMapCameraHelper`

- 

MTStyle

The proxy object for the current map style.

Set of convenience methods for style, sources and layers manipulation.
MTStyle is nil until map loading is complete.
Since it is loaded asynchronously it should be manipulated only after `MTEvent.didLoad` triggers.

See more

#### Declaration

Swift
@MainActor
public class MTStyle

- 

MTBackgroundLayer

The background style layer covers the entire map.
Use a background style layer to configure a color or pattern to show below all other map content.
If the background layer is transparent or omitted from the style, any part of the map view that
does not show another style layer is transparent.

See more

#### Declaration

Swift
`public class MTBackgroundLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTCircleLayer

The circle style layer renders one or more filled circles on the map.

See more

#### Declaration

Swift
`public class MTCircleLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTCircleLayer: Equatable`

- 

MTFillLayer

The fill style layer that renders one or more filled (and optionally stroked) polygons on a map.

See more

#### Declaration

Swift
`public class MTFillLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillLayer: Equatable`

- 

MTFillExtrusionLayer

A fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map.

See more

#### Declaration

Swift
`public class MTFillExtrusionLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillExtrusionLayer: Equatable`

- 

MTHeatmapLayer

A heatmap style layer renders a range of colors to represent the density of points in an area.

See more

#### Declaration

Swift
`public class MTHeatmapLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTHeatmapLayer: Equatable`

- 

MTHillshadeLayer

A hillshade style layer renders digital elevation model (DEM) data on the client-side.
Supports Terrain RGB and Mapzen Terrarium tiles via a `raster-dem` source.

See more

#### Declaration

Swift
`public class MTHillshadeLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTLineLayer

The line style layer that renders one or more stroked polylines on the map.

See more

#### Declaration

Swift
`public class MTLineLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTRasterLayer

The raster style layer renders raster map textures such as imagery.

See more

#### Declaration

Swift
`public class MTRasterLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTSymbolLayer

The symbol style that layer renders icon and text labels at points or along lines on a map.

See more

#### Declaration

Swift
`public class MTSymbolLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTSymbolLayer: Equatable`

- 

MTGeoJSONSource

A geojson source.

See more

#### Declaration

Swift
`public class MTGeoJSONSource : MTSource, @unchecked Sendable, Codable`

- 

MTImageSource

An image source.

The `url` value contains the image location.
The `coordinates` array contains [longitude, latitude] pairs for the image corners
listed in clockwise order: top left, top right, bottom right, bottom left.

See more

#### Declaration

Swift
`public class MTImageSource : MTSource, @unchecked Sendable`

- 

MTRasterDEMSource

A raster DEM source. Only supports Terrain RGB.

See more

#### Declaration

Swift
`public class MTRasterDEMSource : MTTileSource, @unchecked Sendable`

- 

MTRasterTileSource

A raster tile source.

For raster tiles hosted by MapTiler, the “url” value should be of the form
https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=

See more

#### Declaration

Swift
`public class MTRasterTileSource : MTTileSource, @unchecked Sendable`

- 

MTVectorTileSource

Undocumented

See more

#### Declaration

Swift
`public class MTVectorTileSource : MTTileSource, @unchecked Sendable`

- 

MTVideoSource

A video source.

The `urls` value is an array. For each URL in the array, a video element source will be created.
The `coordinates` array contains [longitude, latitude] pairs for the video corners listed in
clockwise order: top left, top right, bottom right, bottom left.

See more

#### Declaration

Swift
`public class MTVideoSource : MTSource, @unchecked Sendable`

- 

MTColorRamp

Swift wrapper over the MapTiler SDK ColorRamp class.

See more

#### Declaration

Swift
@MainActor
public final class MTColorRamp : @unchecked Sendable

---

## File: Enums.html

---
layout: mobile_sdk
title: "Enumerations"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following enumerations are available globally."
id: enums
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Enumerations

The following enumerations are available globally.

- 

MTAnchor

Anchor positions for marker placement.

See more

#### Declaration

Swift
`public enum MTAnchor : String, Sendable, Codable`

- 

MTMarkerRotationAlignment

Alignment for marker rotation relative to map or viewport.

See more

#### Declaration

Swift
`public enum MTMarkerRotationAlignment : String, Sendable, Codable`

- 

MTMarkerPitchAlignment

Alignment for marker pitch relative to map or viewport.

See more

#### Declaration

Swift
`public enum MTMarkerPitchAlignment : String, Sendable, Codable`

- 

MTError

Represents all the errors that can occur in the MapTiler SDK.

All methods within the SDK throw MTError.

See more

#### Declaration

Swift
`public enum MTError : Error`

- 

MTLogLevel

SDK log level.

See more

#### Declaration

Swift
`public enum MTLogLevel : Sendable, Equatable`

- 

MTLogType

Type of log messages in the SDK.

See more

#### Declaration

Swift
`public enum MTLogType : Sendable`

- 

MTEvent

Events triggered by the SDK

See more

#### Declaration

Swift
`public enum MTEvent : String`

- 

MTLanguage

Language of the map labels.

See more

#### Declaration

Swift
`public enum MTLanguage : Sendable, Codable`

- 

MTSpecialLanguage

Custom language options.

See more

#### Declaration

Swift
`public enum MTSpecialLanguage : String, Sendable, Codable`

- 

MTCountryLanguage

Languages available for MTMapView object.

See more

#### Declaration

Swift
`public enum MTCountryLanguage : String, Sendable, Codable, CaseIterable`

- 

MTLocationError

Enum representing MTLocationManager errors.

See more

#### Declaration

Swift
`public enum MTLocationError : Error`

- 

MTUnit

Units of measurement used in MTMapView object.

See more

#### Declaration

Swift
`public enum MTUnit : String, Sendable`

- 

MTGestureType

Gesture types available in the SDK.

See more

#### Declaration

Swift
@MainActor
public enum MTGestureType

- 

MTEventLevel

Controls which map events are forwarded from the map object.

essential: Low-frequency lifecycle events only (ready, load, moveend, etc.) plus taps.

- cameraOnly: Forwards only camera events (move, zoom) in addition to minimal lifecycle.

- all: Default. Forwards all events including high-frequency move/zoom/touch/render
(use with caution on low-end devices).

- off: Minimal wiring to keep internal lifecycle (ready/load) functioning; all other events are suppressed.

See more

#### Declaration

Swift
`public enum MTEventLevel : String, Codable, Sendable`

- 

MTPerformancePresets

Performance-oriented presets for MapTiler Swift SDK.

See more

#### Declaration

Swift
`public enum MTPerformancePresets`

- 

MTFitBoundsPadding

Padding values accepted by `MTFitBoundsOptions`.

See more

#### Declaration

Swift
`public enum MTFitBoundsPadding : Sendable, Codable, Equatable`

- 

MTExpression

Helper to construct common style expressions without raw strings.

See more

#### Declaration

Swift
`public enum MTExpression`

- 

MTFeatureKey

Commonly-used feature keys

See more

#### Declaration

Swift
`public enum MTFeatureKey : String, Sendable`

- 

MTFilter

Helper to construct common filter expressions without raw strings.

See more

#### Declaration

Swift
`public enum MTFilter`

- 

MTCirclePaintProperty

Typed keys for circle paint properties.

See more

#### Declaration

Swift
`public enum MTCirclePaintProperty : String, Sendable`

- 

MTSymbolLayoutProperty

Typed keys for symbol layout properties.

See more

#### Declaration

Swift
`public enum MTSymbolLayoutProperty : String, Sendable`

- 

MTSymbolPaintProperty

Typed keys for symbol paint properties.

See more

#### Declaration

Swift
`public enum MTSymbolPaintProperty : String, Sendable`

- 

MTCirclePitchAlignment

Orientation of the circle when map is pitched.

See more

#### Declaration

Swift
`public enum MTCirclePitchAlignment : String`

- 

MTCirclePitchScale

Controls the scaling behavior of the circle when the map is pitched.

See more

#### Declaration

Swift
`public enum MTCirclePitchScale : String`

- 

MTCircleTranslateAnchor

Controls the frame of reference for circle translate.

See more

#### Declaration

Swift
`public enum MTCircleTranslateAnchor : String`

- 

MTFillTranslateAnchor

Enum controlling the frame of reference for fill translate.

See more

#### Declaration

Swift
`public enum MTFillTranslateAnchor : String`

- 

MTFillExtrusionTranslateAnchor

Controls the frame of reference for fill-extrusion translate.

See more

#### Declaration

Swift
`public enum MTFillExtrusionTranslateAnchor : String`

- 

MTHillshadeIlluminationAnchor

Direction of light source when map is rotated.

See more

#### Declaration

Swift
`public enum MTHillshadeIlluminationAnchor : String`

- 

MTLineCap

The display of line endings.

See more

#### Declaration

Swift
`public enum MTLineCap : String`

- 

MTLineJoin

The display of lines when joining.

See more

#### Declaration

Swift
`public enum MTLineJoin : String`

- 

MTLineTranslateAnchor

Controls the frame of reference for line translate.

See more

#### Declaration

Swift
`public enum MTLineTranslateAnchor : String`

- 

MTLayerType

Types of layers.

See more

#### Declaration

Swift
`public enum MTLayerType : String, Codable`

- 

MTLayerVisibility

Enum representing the visibility of the layer.

See more

#### Declaration

Swift
`public enum MTLayerVisibility : String`

- 

MTRasterResampling

Resampling/interpolation method to use for overscaling.

See more

#### Declaration

Swift
`public enum MTRasterResampling : String, Codable, Sendable`

- 

MTMapReferenceStyle

Defines purpose and guidelines on what information is displayed.

See more

#### Declaration

Swift
`public enum MTMapReferenceStyle : Identifiable, Hashable, Sendable`

- 

MTMapStyleVariant

Variants of the reference styles.

See more

#### Declaration

Swift
`public enum MTMapStyleVariant : String, Sendable, CaseIterable, Identifiable`

- 

MTPropertyValue

A typed value container

See more

#### Declaration

Swift
`public enum MTPropertyValue : Sendable`

- 

MTStyleError

Represents the exceptions raised by the MTStyle object.

See more

#### Declaration

Swift
`public enum MTStyleError : Error`

- 

MTStyleValue

A unified style value that may be a constant or an expression.

See more

#### Declaration

Swift
`public enum MTStyleValue : Sendable`

- 

MTTileScheme

A scheme used for tiles.

See more

#### Declaration

Swift
`public enum MTTileScheme : String`

- 

MTRasterDEMEncoding

Encoding used by the Raster DEM source.

See more

#### Declaration

Swift
`public enum MTRasterDEMEncoding : String, Sendable`

- 

MTSourceType

Types of sources.

Sources state which data the map should display.

See more

#### Declaration

Swift
`public enum MTSourceType : String, Codable`

- 

MTTextAnchor

Symbol text anchor positions.

See more

#### Declaration

Swift
`public enum MTTextAnchor : String, Sendable`

- 

MTTextToken

Common text field tokens

See more

#### Declaration

Swift
`public enum MTTextToken : String, Sendable`

- 

MTEasing

Representing the control of the change rate of the animation.

See more

#### Declaration

Swift
`public enum MTEasing : String, Sendable, Codable`

- 

MTHaloOption

Option that can enable default halo or configure it.

See more

#### Declaration

Swift
`public enum MTHaloOption : Sendable, Codable`

- 

MTLightAnchor

Sets whether extruded geometries are lit relative to the map or viewport.

See more

#### Declaration

Swift
`public enum MTLightAnchor : String, Sendable, Codable`

- 

MTMapCorner

Represents corners of the map.

See more

#### Declaration

Swift
`public enum MTMapCorner : String, Sendable, Codable`

- 

MTProjectionType

Type of projection the map uses.

See more

#### Declaration

Swift
`public enum MTProjectionType : String, Sendable, Codable`

- 

MTSpacePreset

Predefined cubemap presets for space backgrounds.

See more

#### Declaration

Swift
`public enum MTSpacePreset : String, Sendable, Codable, CaseIterable`

- 

MTSpaceOption

Option that can enable default space or configure it.

See more

#### Declaration

Swift
`public enum MTSpaceOption : Sendable, Codable`

- 

MTColorRampResampleMethod

Resampling methods supported by MapTiler SDK.

See more

#### Declaration

Swift
`public enum MTColorRampResampleMethod : String, Sendable, Codable, CaseIterable`

- 

MTColorRampPreset

Built-in presets shipped with the SDK.

See more

#### Declaration

Swift
`public enum MTColorRampPreset : String, Sendable, Codable, CaseIterable`

Union helper types for encoding mixed-value options

- 

MTNumberOrZoomNumberValues

Either a numeric value or zoom-ramped numeric values.

See more

#### Declaration

Swift
`public enum MTNumberOrZoomNumberValues : Codable, Sendable`

- 

MTStringOrZoomStringValues

Either a string value or zoom-ramped string values.

See more

#### Declaration

Swift
`public enum MTStringOrZoomStringValues : Codable, Sendable`

- 

MTNumberOrPropertyValues

Either a numeric value or property-mapped numeric values.

See more

#### Declaration

Swift
`public enum MTNumberOrPropertyValues : Codable, Sendable`

- 

MTRadiusOption

Heatmap radius can be a number, zoom-ramped numbers, or property-mapped numbers.

See more

#### Declaration

Swift
`public enum MTRadiusOption : Codable, Sendable`

Line-specific helper values

- 

MTDashArrayValue

Represents a dash pattern that can be provided as an array of numbers or as a string pattern
composed of underscores and spaces (e.g. “___ _ ”).

See more

#### Declaration

Swift
`public enum MTDashArrayValue : Codable, Sendable`

- 

MTSkyExpression

Expression element used to build MapTiler style expressions for sky values.

See more

#### Declaration

Swift
`public enum MTSkyExpression : Sendable, Codable, Equatable`

- 

MTSkyColorValue

Represents a color or expression for the sky configuration.

See more

#### Declaration

Swift
`public enum MTSkyColorValue : Sendable, Codable, Equatable`

- 

MTSkyNumberValue

Represents a numeric value or expression for the sky configuration.

See more

#### Declaration

Swift
`public enum MTSkyNumberValue : Sendable, Codable, Equatable`

---

## File: Extensions.html

---
layout: mobile_sdk
title: "Extensions"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following extensions are available globally."
id: extensions
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Extensions

The following extensions are available globally.

- 

UIColor

See more

#### Declaration

Swift
`extension UIColor`

- 

CLLocationCoordinate2D

See more

#### Declaration

Swift
`extension CLLocationCoordinate2D: @retroactive Equatable`
`extension CLLocationCoordinate2D: Codable`

---

## File: index.html

---
layout: mobile_sdk
title: "MapTiler SDK Swift API Reference"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Complete API reference for MapTiler Swift SDK. Detailed technical documentation for integrating high-performance, interactive vector maps into native iOS applications."
id: index
breadcrumb: "Mobile SDK/iOS/Reference"
---

# MapTiler SDK Swift API Reference

## Actors

The following actors are available globally.

- 

MTConfig

Object representing the SDK global settings.

Exposes properties and options such as API Key and caching preferences.

See more

#### Declaration

Swift
`public actor MTConfig`

## Classes

The following classes are available globally.

- 

MTCustomAnnotationView

Subclassable view for adding custom annotations to the map.

See more

#### Declaration

Swift
@MainActor
open class MTCustomAnnotationView : UIView, @preconcurrency MTAnnotation
`extension MTCustomAnnotationView: @preconcurrency MTMapViewContent`

- 

MTMarker

Annotation element that can be added to the map.

See more

#### Declaration

Swift
`public class MTMarker : MTAnnotation, MTMapViewContent, @unchecked Sendable`

- 

MTTextPopup

Basic text popup.

Can be attached to MTMarker or standalone.

See more

#### Declaration

Swift
`public class MTTextPopup : MTAnnotation, MTMapViewContent, @unchecked Sendable`

- 

MTBenchmark

Basic benchmarking class.

See more

#### Declaration

Swift
@MainActor
public final class MTBenchmark : MTMapViewDelegate

- 

MTMapView

Object representing the map on the screen.

Exposes methods and properties that enable changes to the map,
and fires events that can be interacted with.

See more

#### Declaration

Swift
@MainActor
open class MTMapView : UIView, Sendable
`extension MTMapView: MTControllable`
`extension MTMapView: MTNavigable`
`extension MTMapView: MTRendering`
`extension MTMapView: MTStylable`
`extension MTMapView: MTZoomable`
`extension MTMapView: MTLocationManagerDelegate`

- 

MTHeatmapLayerHelper

Helper for creating a heatmap visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTHeatmapLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPointLayerHelper

Helper for creating a point visualization layer from data and styling options.

Uses the current style to create the underlying source and layers.

See more

#### Declaration

Swift
`public final class MTPointLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPolygonLayerHelper

Helper for creating a polygon (fill) visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTPolygonLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTPolylineLayerHelper

Helper for creating a polyline (line) visualization layer from data and styling options.

See more

#### Declaration

Swift
`public final class MTPolylineLayerHelper : MTVectorLayerHelper, @unchecked Sendable`

- 

MTLogger

Logger class used for SDK logs.

See more

#### Declaration

Swift
`public class MTLogger`

- 

MTLocationManager

Class responsible for location updates.

See more

#### Declaration

Swift
`public class MTLocationManager : NSObject, @preconcurrency CLLocationManagerDelegate`

- 

MTGestureService

Service responsible for gesture handling and state.

See more

#### Declaration

Swift
@MainActor
public class MTGestureService

- 

MTMapCameraHelper

Sets combination of center, bearing and pitch, as well as roll and elevation.

See more

#### Declaration

Swift
`public class MTMapCameraHelper`

- 

MTStyle

The proxy object for the current map style.

Set of convenience methods for style, sources and layers manipulation.
MTStyle is nil until map loading is complete.
Since it is loaded asynchronously it should be manipulated only after `MTEvent.didLoad` triggers.

See more

#### Declaration

Swift
@MainActor
public class MTStyle

- 

MTBackgroundLayer

The background style layer covers the entire map.
Use a background style layer to configure a color or pattern to show below all other map content.
If the background layer is transparent or omitted from the style, any part of the map view that
does not show another style layer is transparent.

See more

#### Declaration

Swift
`public class MTBackgroundLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTCircleLayer

The circle style layer renders one or more filled circles on the map.

See more

#### Declaration

Swift
`public class MTCircleLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTCircleLayer: Equatable`

- 

MTFillLayer

The fill style layer that renders one or more filled (and optionally stroked) polygons on a map.

See more

#### Declaration

Swift
`public class MTFillLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillLayer: Equatable`

- 

MTFillExtrusionLayer

A fill-extrusion style layer renders one or more filled (and optionally stroked) extruded (3D) polygons on a map.

See more

#### Declaration

Swift
`public class MTFillExtrusionLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTFillExtrusionLayer: Equatable`

- 

MTHeatmapLayer

A heatmap style layer renders a range of colors to represent the density of points in an area.

See more

#### Declaration

Swift
`public class MTHeatmapLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTHeatmapLayer: Equatable`

- 

MTHillshadeLayer

A hillshade style layer renders digital elevation model (DEM) data on the client-side.
Supports Terrain RGB and Mapzen Terrarium tiles via a `raster-dem` source.

See more

#### Declaration

Swift
`public class MTHillshadeLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTLineLayer

The line style layer that renders one or more stroked polylines on the map.

See more

#### Declaration

Swift
`public class MTLineLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTRasterLayer

The raster style layer renders raster map textures such as imagery.

See more

#### Declaration

Swift
`public class MTRasterLayer : MTLayer, @unchecked Sendable, Codable`

- 

MTSymbolLayer

The symbol style that layer renders icon and text labels at points or along lines on a map.

See more

#### Declaration

Swift
`public class MTSymbolLayer : MTLayer, @unchecked Sendable, Codable`
`extension MTSymbolLayer: Equatable`

- 

MTGeoJSONSource

A geojson source.

See more

#### Declaration

Swift
`public class MTGeoJSONSource : MTSource, @unchecked Sendable, Codable`

- 

MTImageSource

An image source.

The `url` value contains the image location.
The `coordinates` array contains [longitude, latitude] pairs for the image corners
listed in clockwise order: top left, top right, bottom right, bottom left.

See more

#### Declaration

Swift
`public class MTImageSource : MTSource, @unchecked Sendable`

- 

MTRasterDEMSource

A raster DEM source. Only supports Terrain RGB.

See more

#### Declaration

Swift
`public class MTRasterDEMSource : MTTileSource, @unchecked Sendable`

- 

MTRasterTileSource

A raster tile source.

For raster tiles hosted by MapTiler, the “url” value should be of the form
https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=

See more

#### Declaration

Swift
`public class MTRasterTileSource : MTTileSource, @unchecked Sendable`

- 

MTVectorTileSource

Undocumented

See more

#### Declaration

Swift
`public class MTVectorTileSource : MTTileSource, @unchecked Sendable`

- 

MTVideoSource

A video source.

The `urls` value is an array. For each URL in the array, a video element source will be created.
The `coordinates` array contains [longitude, latitude] pairs for the video corners listed in
clockwise order: top left, top right, bottom right, bottom left.

See more

#### Declaration

Swift
`public class MTVideoSource : MTSource, @unchecked Sendable`

- 

MTColorRamp

Swift wrapper over the MapTiler SDK ColorRamp class.

See more

#### Declaration

Swift
@MainActor
public final class MTColorRamp : @unchecked Sendable

## Enumerations

The following enumerations are available globally.

- 

MTAnchor

Anchor positions for marker placement.

See more

#### Declaration

Swift
`public enum MTAnchor : String, Sendable, Codable`

- 

MTMarkerRotationAlignment

Alignment for marker rotation relative to map or viewport.

See more

#### Declaration

Swift
`public enum MTMarkerRotationAlignment : String, Sendable, Codable`

- 

MTMarkerPitchAlignment

Alignment for marker pitch relative to map or viewport.

See more

#### Declaration

Swift
`public enum MTMarkerPitchAlignment : String, Sendable, Codable`

- 

MTError

Represents all the errors that can occur in the MapTiler SDK.

All methods within the SDK throw MTError.

See more

#### Declaration

Swift
`public enum MTError : Error`

- 

MTLogLevel

SDK log level.

See more

#### Declaration

Swift
`public enum MTLogLevel : Sendable, Equatable`

- 

MTLogType

Type of log messages in the SDK.

See more

#### Declaration

Swift
`public enum MTLogType : Sendable`

- 

MTEvent

Events triggered by the SDK

See more

#### Declaration

Swift
`public enum MTEvent : String`

- 

MTLanguage

Language of the map labels.

See more

#### Declaration

Swift
`public enum MTLanguage : Sendable, Codable`

- 

MTSpecialLanguage

Custom language options.

See more

#### Declaration

Swift
`public enum MTSpecialLanguage : String, Sendable, Codable`

- 

MTCountryLanguage

Languages available for MTMapView object.

See more

#### Declaration

Swift
`public enum MTCountryLanguage : String, Sendable, Codable, CaseIterable`

- 

MTLocationError

Enum representing MTLocationManager errors.

See more

#### Declaration

Swift
`public enum MTLocationError : Error`

- 

MTUnit

Units of measurement used in MTMapView object.

See more

#### Declaration

Swift
`public enum MTUnit : String, Sendable`

- 

MTGestureType

Gesture types available in the SDK.

See more

#### Declaration

Swift
@MainActor
public enum MTGestureType

- 

MTEventLevel

Controls which map events are forwarded from the map object.

essential: Low-frequency lifecycle events only (ready, load, moveend, etc.) plus taps.

- cameraOnly: Forwards only camera events (move, zoom) in addition to minimal lifecycle.

- all: Default. Forwards all events including high-frequency move/zoom/touch/render
(use with caution on low-end devices).

- off: Minimal wiring to keep internal lifecycle (ready/load) functioning; all other events are suppressed.

See more

#### Declaration

Swift
`public enum MTEventLevel : String, Codable, Sendable`

- 

MTPerformancePresets

Performance-oriented presets for MapTiler Swift SDK.

See more

#### Declaration

Swift
`public enum MTPerformancePresets`

- 

MTFitBoundsPadding

Padding values accepted by `MTFitBoundsOptions`.

See more

#### Declaration

Swift
`public enum MTFitBoundsPadding : Sendable, Codable, Equatable`

- 

MTExpression

Helper to construct common style expressions without raw strings.

See more

#### Declaration

Swift
`public enum MTExpression`

- 

MTFeatureKey

Commonly-used feature keys

See more

#### Declaration

Swift
`public enum MTFeatureKey : String, Sendable`

- 

MTFilter

Helper to construct common filter expressions without raw strings.

See more

#### Declaration

Swift
`public enum MTFilter`

- 

MTCirclePaintProperty

Typed keys for circle paint properties.

See more

#### Declaration

Swift
`public enum MTCirclePaintProperty : String, Sendable`

- 

MTSymbolLayoutProperty

Typed keys for symbol layout properties.

See more

#### Declaration

Swift
`public enum MTSymbolLayoutProperty : String, Sendable`

- 

MTSymbolPaintProperty

Typed keys for symbol paint properties.

See more

#### Declaration

Swift
`public enum MTSymbolPaintProperty : String, Sendable`

- 

MTCirclePitchAlignment

Orientation of the circle when map is pitched.

See more

#### Declaration

Swift
`public enum MTCirclePitchAlignment : String`

- 

MTCirclePitchScale

Controls the scaling behavior of the circle when the map is pitched.

See more

#### Declaration

Swift
`public enum MTCirclePitchScale : String`

- 

MTCircleTranslateAnchor

Controls the frame of reference for circle translate.

See more

#### Declaration

Swift
`public enum MTCircleTranslateAnchor : String`

- 

MTFillTranslateAnchor

Enum controlling the frame of reference for fill translate.

See more

#### Declaration

Swift
`public enum MTFillTranslateAnchor : String`

- 

MTFillExtrusionTranslateAnchor

Controls the frame of reference for fill-extrusion translate.

See more

#### Declaration

Swift
`public enum MTFillExtrusionTranslateAnchor : String`

- 

MTHillshadeIlluminationAnchor

Direction of light source when map is rotated.

See more

#### Declaration

Swift
`public enum MTHillshadeIlluminationAnchor : String`

- 

MTLineCap

The display of line endings.

See more

#### Declaration

Swift
`public enum MTLineCap : String`

- 

MTLineJoin

The display of lines when joining.

See more

#### Declaration

Swift
`public enum MTLineJoin : String`

- 

MTLineTranslateAnchor

Controls the frame of reference for line translate.

See more

#### Declaration

Swift
`public enum MTLineTranslateAnchor : String`

- 

MTLayerType

Types of layers.

See more

#### Declaration

Swift
`public enum MTLayerType : String, Codable`

- 

MTLayerVisibility

Enum representing the visibility of the layer.

See more

#### Declaration

Swift
`public enum MTLayerVisibility : String`

- 

MTRasterResampling

Resampling/interpolation method to use for overscaling.

See more

#### Declaration

Swift
`public enum MTRasterResampling : String, Codable, Sendable`

- 

MTMapReferenceStyle

Defines purpose and guidelines on what information is displayed.

See more

#### Declaration

Swift
`public enum MTMapReferenceStyle : Identifiable, Hashable, Sendable`

- 

MTMapStyleVariant

Variants of the reference styles.

See more

#### Declaration

Swift
`public enum MTMapStyleVariant : String, Sendable, CaseIterable, Identifiable`

- 

MTPropertyValue

A typed value container

See more

#### Declaration

Swift
`public enum MTPropertyValue : Sendable`

- 

MTStyleError

Represents the exceptions raised by the MTStyle object.

See more

#### Declaration

Swift
`public enum MTStyleError : Error`

- 

MTStyleValue

A unified style value that may be a constant or an expression.

See more

#### Declaration

Swift
`public enum MTStyleValue : Sendable`

- 

MTTileScheme

A scheme used for tiles.

See more

#### Declaration

Swift
`public enum MTTileScheme : String`

- 

MTRasterDEMEncoding

Encoding used by the Raster DEM source.

See more

#### Declaration

Swift
`public enum MTRasterDEMEncoding : String, Sendable`

- 

MTSourceType

Types of sources.

Sources state which data the map should display.

See more

#### Declaration

Swift
`public enum MTSourceType : String, Codable`

- 

MTTextAnchor

Symbol text anchor positions.

See more

#### Declaration

Swift
`public enum MTTextAnchor : String, Sendable`

- 

MTTextToken

Common text field tokens

See more

#### Declaration

Swift
`public enum MTTextToken : String, Sendable`

- 

MTEasing

Representing the control of the change rate of the animation.

See more

#### Declaration

Swift
`public enum MTEasing : String, Sendable, Codable`

- 

MTHaloOption

Option that can enable default halo or configure it.

See more

#### Declaration

Swift
`public enum MTHaloOption : Sendable, Codable`

- 

MTLightAnchor

Sets whether extruded geometries are lit relative to the map or viewport.

See more

#### Declaration

Swift
`public enum MTLightAnchor : String, Sendable, Codable`

- 

MTMapCorner

Represents corners of the map.

See more

#### Declaration

Swift
`public enum MTMapCorner : String, Sendable, Codable`

- 

MTProjectionType

Type of projection the map uses.

See more

#### Declaration

Swift
`public enum MTProjectionType : String, Sendable, Codable`

- 

MTSpacePreset

Predefined cubemap presets for space backgrounds.

See more

#### Declaration

Swift
`public enum MTSpacePreset : String, Sendable, Codable, CaseIterable`

- 

MTSpaceOption

Option that can enable default space or configure it.

See more

#### Declaration

Swift
`public enum MTSpaceOption : Sendable, Codable`

- 

MTColorRampResampleMethod

Resampling methods supported by MapTiler SDK.

See more

#### Declaration

Swift
`public enum MTColorRampResampleMethod : String, Sendable, Codable, CaseIterable`

- 

MTColorRampPreset

Built-in presets shipped with the SDK.

See more

#### Declaration

Swift
`public enum MTColorRampPreset : String, Sendable, Codable, CaseIterable`

Union helper types for encoding mixed-value options

- 

MTNumberOrZoomNumberValues

Either a numeric value or zoom-ramped numeric values.

See more

#### Declaration

Swift
`public enum MTNumberOrZoomNumberValues : Codable, Sendable`

- 

MTStringOrZoomStringValues

Either a string value or zoom-ramped string values.

See more

#### Declaration

Swift
`public enum MTStringOrZoomStringValues : Codable, Sendable`

- 

MTNumberOrPropertyValues

Either a numeric value or property-mapped numeric values.

See more

#### Declaration

Swift
`public enum MTNumberOrPropertyValues : Codable, Sendable`

- 

MTRadiusOption

Heatmap radius can be a number, zoom-ramped numbers, or property-mapped numbers.

See more

#### Declaration

Swift
`public enum MTRadiusOption : Codable, Sendable`

Line-specific helper values

- 

MTDashArrayValue

Represents a dash pattern that can be provided as an array of numbers or as a string pattern
composed of underscores and spaces (e.g. “___ _ ”).

See more

#### Declaration

Swift
`public enum MTDashArrayValue : Codable, Sendable`

- 

MTSkyExpression

Expression element used to build MapTiler style expressions for sky values.

See more

#### Declaration

Swift
`public enum MTSkyExpression : Sendable, Codable, Equatable`

- 

MTSkyColorValue

Represents a color or expression for the sky configuration.

See more

#### Declaration

Swift
`public enum MTSkyColorValue : Sendable, Codable, Equatable`

- 

MTSkyNumberValue

Represents a numeric value or expression for the sky configuration.

See more

#### Declaration

Swift
`public enum MTSkyNumberValue : Sendable, Codable, Equatable`

## Extensions

The following extensions are available globally.

- 

UIColor

See more

#### Declaration

Swift
`extension UIColor`

- 

CLLocationCoordinate2D

See more

#### Declaration

Swift
`extension CLLocationCoordinate2D: @retroactive Equatable`
`extension CLLocationCoordinate2D: Codable`

## Protocols

The following protocols are available globally.

- 

MTAnnotation

Protocol requirements for all annotation objects.

See more

#### Declaration

Swift
`public protocol MTAnnotation : Sendable`

- 

MTVectorLayerHelper

Base protocol adopted by vector layer helpers to share defaults
and common option normalization logic.

See more

#### Declaration

Swift
`public protocol MTVectorLayerHelper : AnyObject`

- 

MTLoggable

Protocol requirement for all Logger objects.

See more

#### Declaration

Swift
`public protocol MTLoggable : Sendable`

- 

MTLocationManagerDelegate

Protocol requirements for location manager.

See more

#### Declaration

Swift
@MainActor
public protocol MTLocationManagerDelegate : AnyObject

- 

MTControllable

Defines methods for adding the map controls.

See more

#### Declaration

Swift
@MainActor
public protocol MTControllable

- 

MTNavigable

Defines methods for navigating the map.

See more

#### Declaration

Swift
@MainActor
public protocol MTNavigable

- 

MTRendering

Defines methods for adjusting rendering parameters.

See more

#### Declaration

Swift
@MainActor
public protocol MTRendering

- 

MTStylable

Defines methods for map styling methods.

See more

#### Declaration

Swift
@MainActor
public protocol MTStylable

- 

MTZoomable

Defines methods for manipulating zoom level.

See more

#### Declaration

Swift
@MainActor
public protocol MTZoomable

- 

MTGesture

Defines gestures behaviour.

See more

#### Declaration

Swift
@MainActor
public protocol MTGesture

- 

MTMapViewContent

Map view content requirements.

See more

#### Declaration

Swift
`public protocol MTMapViewContent`

- 

MTMapViewDelegate

Delegate responsible for map event propagation

See more

#### Declaration

Swift
@MainActor
public protocol MTMapViewDelegate : AnyObject

- 

MTLayer

Protocol requirements for all types of Layers.

See more

#### Declaration

Swift
`public protocol MTLayer : AnyObject, MTMapViewContent, Sendable`

- 

MTSource

Protocol requirements for all types of Sources.

See more

#### Declaration

Swift
`public protocol MTSource : AnyObject, MTMapViewContent, Sendable`

- 

MTTileSource

Protocol requirements for all tile type sources.

See more

#### Declaration

Swift
`public protocol MTTileSource : MTSource`

## Structures

The following structures are available globally.

- 

MTException

Represents body of the MTError exception.

See more

#### Declaration

Swift
`public struct MTException : Sendable`

- 

MTColor

Color wrapper.

See more

#### Declaration

Swift
`public struct MTColor : Sendable, Codable, Equatable`

- 

MTHeatmapLayerOptions

Options for building a heatmap visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTHeatmapLayerOptions : Codable, Sendable`

- 

MTPointLayerOptions

Options for building a point visualization layer through the helper.

Mirrors the available configuration including common shape options.

See more

#### Declaration

Swift
`public struct MTPointLayerOptions : Codable, Sendable`

- 

MTPolygonLayerOptions

Options for building a polygon (fill) visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTPolygonLayerOptions : Codable, Sendable`

- 

MTPolylineLayerOptions

Options for building a polyline (line) visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTPolylineLayerOptions : Codable, Sendable`

- 

MTLog

Log object used with MTLogger.

See more

#### Declaration

Swift
`public struct MTLog`

- 

MTDoubleTapZoomInGesture

Handles zooming in the map with double tap.

See more

#### Declaration

Swift
@MainActor
public struct MTDoubleTapZoomInGesture : MTGesture

- 

MTDragPanGesture

Handles panning the map by dragging.

See more

#### Declaration

Swift
@MainActor
public struct MTDragPanGesture : MTGesture

- 

MTPinchRotateAndZoomGesture

Handles zoom and rotate by pinching with two fingers.

See more

#### Declaration

Swift
@MainActor
public struct MTPinchRotateAndZoomGesture : MTGesture

- 

MTTwoFingersDragPitchGesture

Handles changing the pitch by dragging with two fingers.

See more

#### Declaration

Swift
@MainActor
public struct MTTwoFingersDragPitchGesture : MTGesture

- 

MTMapContentBuilder

Map view content builder.

See more

#### Declaration

Swift
@resultBuilder
public struct MTMapContentBuilder

- 

MTMapOptions

Parameters of the map object.

See more

#### Declaration

Swift
`public struct MTMapOptions : Sendable`
`extension MTMapOptions: Codable`

- 

MTMapViewContainer

Declarative Map view for use in SwiftUI

See more

#### Declaration

Swift
@MainActor
public struct MTMapViewContainer : View

- 

MTAnimationOptions

Provides animation options for navigation functions.

See more

#### Declaration

Swift
`public struct MTAnimationOptions : Sendable, Codable`

- 

MTCameraOptions

Options for controlling the desired location, zoom, bearing, and pitch of the camera.

See more

#### Declaration

Swift
`public struct MTCameraOptions : Sendable`
`extension MTCameraOptions: Codable`

- 

MTDragPanOptions

Options for drag and pan gesstures.

See more

#### Declaration

Swift
`public struct MTDragPanOptions : Sendable, Codable`

- 

MTFitBoundsOptions

Options that configure how the map fits to a set of bounds.

See more

#### Declaration

Swift
`public struct MTFitBoundsOptions : Sendable, Codable`

- 

MTFlyToOptions

Options describing the destination and animation of the flyTo transition.

See more

#### Declaration

Swift
`public struct MTFlyToOptions : Sendable, Codable`

- 

MTPaddingOptions

Options for setting padding on calls to map methods.

See more

#### Declaration

Swift
`public struct MTPaddingOptions : Sendable, Codable, Equatable`

- 

MTStyleSetterOptions

Supporting type to add validation to another style related type.

See more

#### Declaration

Swift
`public struct MTStyleSetterOptions : Sendable, Codable`

- 

MTStyleImageOptions

Configuration that controls how an image is registered within the MapTiler style.

See more

#### Declaration

Swift
`public struct MTStyleImageOptions : Codable, Equatable, Sendable`

- 

MTBounds

Represents rectangular geographic bounds defined by southwest and northeast corners.

See more

#### Declaration

Swift
`public struct MTBounds : Sendable, Codable, Equatable`

- 

MTData

Object sent together with MTEvent.

See more

#### Declaration

Swift
`public struct MTData : Codable`

- 

MTHaloStop

One stop in the halo radial gradient: position in [0,1] and color.

See more

#### Declaration

Swift
`public struct MTHaloStop : Sendable, Codable`

- 

MTHalo

Configuration for the atmospheric glow (halo).

See more

#### Declaration

Swift
`public struct MTHalo : Sendable, Codable`

- 

MTLight

A style’s light property provides a global light source for that style.

See more

#### Declaration

Swift
`public struct MTLight : Sendable, Codable`

- 

MTPoint

Two numbers representing x and y screen coordinates in pixels.

See more

#### Declaration

Swift
`public struct MTPoint : Codable, Sendable`

- 

MTSourceData

The style spec representation of the source if the event has a dataType of source .

See more

#### Declaration

Swift
`public struct MTSourceData : Codable`

- 

MTSpaceFaces

Faces definition for a custom cubemap.

See more

#### Declaration

Swift
`public struct MTSpaceFaces : Sendable, Codable`

- 

MTSpacePath

Path-based configuration for cubemap files.

This fetches all images from a path, this assumes all files are named px, nx, py, ny, pz, nz
and suffixed with the appropriate extension specified in format.

See more

#### Declaration

Swift
`public struct MTSpacePath : Sendable, Codable`

- 

MTSpace

Configuration for the “space” background.

See more

#### Declaration

Swift
`public struct MTSpace : Sendable, Codable`

- 

MTRGBAColor

RGBA color represented by 0…255 components.

See more

#### Declaration

Swift
`public struct MTRGBAColor : Sendable, Codable`

- 

MTColorRampStop

A stop describing the value and color to apply.

See more

#### Declaration

Swift
`public struct MTColorRampStop : Sendable, Codable`

- 

MTColorRampBounds

Bounds of a color ramp.

See more

#### Declaration

Swift
`public struct MTColorRampBounds : Sendable, Codable`

- 

MTColorRampOptions

Options used when instantiating a color ramp.

See more

#### Declaration

Swift
`public struct MTColorRampOptions : Sendable, Codable`

- 

MTColorRampCanvasStripOptions

Options for rendering the ramp to a canvas strip.

See more

#### Declaration

Swift
`public struct MTColorRampCanvasStripOptions : Sendable, Codable`

- 

MTColorRampArrayStop

Array-based stop definition for `fromArrayDefinition`.

See more

#### Declaration

Swift
`public struct MTColorRampArrayStop : Sendable, Codable`

- 

MTZoomStringValue

A single string value at a given zoom level.

See more

#### Declaration

Swift
`public struct MTZoomStringValue : Codable, Sendable`

- 

MTZoomNumberValue

A single numeric value at a given zoom level.

See more

#### Declaration

Swift
`public struct MTZoomNumberValue : Codable, Sendable`

- 

MTHelperPropertyValue

A single mapping from a property value to an associated numeric value.

See more

#### Declaration

Swift
`public struct MTHelperPropertyValue : Codable, Sendable`

Colors

- 

MTColorValue

Encodes a color to a hex string when converted to JSON.
Accepts either a hex color string (e.g. “#RRGGBB”) or a UIColor.

See more

#### Declaration

Swift
`public struct MTColorValue : Codable, Sendable`

- 

MTSky

Sky configuration used by `map.setSky`.

See more

#### Declaration

Swift
`public struct MTSky : Sendable, Codable, Equatable`

---

## File: Protocols.html

---
layout: mobile_sdk
title: "Protocols"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following protocols are available globally."
id: protocols
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Protocols

The following protocols are available globally.

- 

MTAnnotation

Protocol requirements for all annotation objects.

See more

#### Declaration

Swift
`public protocol MTAnnotation : Sendable`

- 

MTVectorLayerHelper

Base protocol adopted by vector layer helpers to share defaults
and common option normalization logic.

See more

#### Declaration

Swift
`public protocol MTVectorLayerHelper : AnyObject`

- 

MTLoggable

Protocol requirement for all Logger objects.

See more

#### Declaration

Swift
`public protocol MTLoggable : Sendable`

- 

MTLocationManagerDelegate

Protocol requirements for location manager.

See more

#### Declaration

Swift
@MainActor
public protocol MTLocationManagerDelegate : AnyObject

- 

MTControllable

Defines methods for adding the map controls.

See more

#### Declaration

Swift
@MainActor
public protocol MTControllable

- 

MTNavigable

Defines methods for navigating the map.

See more

#### Declaration

Swift
@MainActor
public protocol MTNavigable

- 

MTRendering

Defines methods for adjusting rendering parameters.

See more

#### Declaration

Swift
@MainActor
public protocol MTRendering

- 

MTStylable

Defines methods for map styling methods.

See more

#### Declaration

Swift
@MainActor
public protocol MTStylable

- 

MTZoomable

Defines methods for manipulating zoom level.

See more

#### Declaration

Swift
@MainActor
public protocol MTZoomable

- 

MTGesture

Defines gestures behaviour.

See more

#### Declaration

Swift
@MainActor
public protocol MTGesture

- 

MTMapViewContent

Map view content requirements.

See more

#### Declaration

Swift
`public protocol MTMapViewContent`

- 

MTMapViewDelegate

Delegate responsible for map event propagation

See more

#### Declaration

Swift
@MainActor
public protocol MTMapViewDelegate : AnyObject

- 

MTLayer

Protocol requirements for all types of Layers.

See more

#### Declaration

Swift
`public protocol MTLayer : AnyObject, MTMapViewContent, Sendable`

- 

MTSource

Protocol requirements for all types of Sources.

See more

#### Declaration

Swift
`public protocol MTSource : AnyObject, MTMapViewContent, Sendable`

- 

MTTileSource

Protocol requirements for all tile type sources.

See more

#### Declaration

Swift
`public protocol MTTileSource : MTSource`

---

## File: Structs.html

---
layout: mobile_sdk
title: "Structures"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following structures are available globally."
id: structs
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Structures

The following structures are available globally.

- 

MTException

Represents body of the MTError exception.

See more

#### Declaration

Swift
`public struct MTException : Sendable`

- 

MTColor

Color wrapper.

See more

#### Declaration

Swift
`public struct MTColor : Sendable, Codable, Equatable`

- 

MTHeatmapLayerOptions

Options for building a heatmap visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTHeatmapLayerOptions : Codable, Sendable`

- 

MTPointLayerOptions

Options for building a point visualization layer through the helper.

Mirrors the available configuration including common shape options.

See more

#### Declaration

Swift
`public struct MTPointLayerOptions : Codable, Sendable`

- 

MTPolygonLayerOptions

Options for building a polygon (fill) visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTPolygonLayerOptions : Codable, Sendable`

- 

MTPolylineLayerOptions

Options for building a polyline (line) visualization layer through the helper.

See more

#### Declaration

Swift
`public struct MTPolylineLayerOptions : Codable, Sendable`

- 

MTLog

Log object used with MTLogger.

See more

#### Declaration

Swift
`public struct MTLog`

- 

MTDoubleTapZoomInGesture

Handles zooming in the map with double tap.

See more

#### Declaration

Swift
@MainActor
public struct MTDoubleTapZoomInGesture : MTGesture

- 

MTDragPanGesture

Handles panning the map by dragging.

See more

#### Declaration

Swift
@MainActor
public struct MTDragPanGesture : MTGesture

- 

MTPinchRotateAndZoomGesture

Handles zoom and rotate by pinching with two fingers.

See more

#### Declaration

Swift
@MainActor
public struct MTPinchRotateAndZoomGesture : MTGesture

- 

MTTwoFingersDragPitchGesture

Handles changing the pitch by dragging with two fingers.

See more

#### Declaration

Swift
@MainActor
public struct MTTwoFingersDragPitchGesture : MTGesture

- 

MTMapContentBuilder

Map view content builder.

See more

#### Declaration

Swift
@resultBuilder
public struct MTMapContentBuilder

- 

MTMapOptions

Parameters of the map object.

See more

#### Declaration

Swift
`public struct MTMapOptions : Sendable`
`extension MTMapOptions: Codable`

- 

MTMapViewContainer

Declarative Map view for use in SwiftUI

See more

#### Declaration

Swift
@MainActor
public struct MTMapViewContainer : View

- 

MTAnimationOptions

Provides animation options for navigation functions.

See more

#### Declaration

Swift
`public struct MTAnimationOptions : Sendable, Codable`

- 

MTCameraOptions

Options for controlling the desired location, zoom, bearing, and pitch of the camera.

See more

#### Declaration

Swift
`public struct MTCameraOptions : Sendable`
`extension MTCameraOptions: Codable`

- 

MTDragPanOptions

Options for drag and pan gesstures.

See more

#### Declaration

Swift
`public struct MTDragPanOptions : Sendable, Codable`

- 

MTFitBoundsOptions

Options that configure how the map fits to a set of bounds.

See more

#### Declaration

Swift
`public struct MTFitBoundsOptions : Sendable, Codable`

- 

MTFlyToOptions

Options describing the destination and animation of the flyTo transition.

See more

#### Declaration

Swift
`public struct MTFlyToOptions : Sendable, Codable`

- 

MTPaddingOptions

Options for setting padding on calls to map methods.

See more

#### Declaration

Swift
`public struct MTPaddingOptions : Sendable, Codable, Equatable`

- 

MTStyleSetterOptions

Supporting type to add validation to another style related type.

See more

#### Declaration

Swift
`public struct MTStyleSetterOptions : Sendable, Codable`

- 

MTStyleImageOptions

Configuration that controls how an image is registered within the MapTiler style.

See more

#### Declaration

Swift
`public struct MTStyleImageOptions : Codable, Equatable, Sendable`

- 

MTBounds

Represents rectangular geographic bounds defined by southwest and northeast corners.

See more

#### Declaration

Swift
`public struct MTBounds : Sendable, Codable, Equatable`

- 

MTData

Object sent together with MTEvent.

See more

#### Declaration

Swift
`public struct MTData : Codable`

- 

MTHaloStop

One stop in the halo radial gradient: position in [0,1] and color.

See more

#### Declaration

Swift
`public struct MTHaloStop : Sendable, Codable`

- 

MTHalo

Configuration for the atmospheric glow (halo).

See more

#### Declaration

Swift
`public struct MTHalo : Sendable, Codable`

- 

MTLight

A style’s light property provides a global light source for that style.

See more

#### Declaration

Swift
`public struct MTLight : Sendable, Codable`

- 

MTPoint

Two numbers representing x and y screen coordinates in pixels.

See more

#### Declaration

Swift
`public struct MTPoint : Codable, Sendable`

- 

MTSourceData

The style spec representation of the source if the event has a dataType of source .

See more

#### Declaration

Swift
`public struct MTSourceData : Codable`

- 

MTSpaceFaces

Faces definition for a custom cubemap.

See more

#### Declaration

Swift
`public struct MTSpaceFaces : Sendable, Codable`

- 

MTSpacePath

Path-based configuration for cubemap files.

This fetches all images from a path, this assumes all files are named px, nx, py, ny, pz, nz
and suffixed with the appropriate extension specified in format.

See more

#### Declaration

Swift
`public struct MTSpacePath : Sendable, Codable`

- 

MTSpace

Configuration for the “space” background.

See more

#### Declaration

Swift
`public struct MTSpace : Sendable, Codable`

- 

MTRGBAColor

RGBA color represented by 0…255 components.

See more

#### Declaration

Swift
`public struct MTRGBAColor : Sendable, Codable`

- 

MTColorRampStop

A stop describing the value and color to apply.

See more

#### Declaration

Swift
`public struct MTColorRampStop : Sendable, Codable`

- 

MTColorRampBounds

Bounds of a color ramp.

See more

#### Declaration

Swift
`public struct MTColorRampBounds : Sendable, Codable`

- 

MTColorRampOptions

Options used when instantiating a color ramp.

See more

#### Declaration

Swift
`public struct MTColorRampOptions : Sendable, Codable`

- 

MTColorRampCanvasStripOptions

Options for rendering the ramp to a canvas strip.

See more

#### Declaration

Swift
`public struct MTColorRampCanvasStripOptions : Sendable, Codable`

- 

MTColorRampArrayStop

Array-based stop definition for `fromArrayDefinition`.

See more

#### Declaration

Swift
`public struct MTColorRampArrayStop : Sendable, Codable`

- 

MTZoomStringValue

A single string value at a given zoom level.

See more

#### Declaration

Swift
`public struct MTZoomStringValue : Codable, Sendable`

- 

MTZoomNumberValue

A single numeric value at a given zoom level.

See more

#### Declaration

Swift
`public struct MTZoomNumberValue : Codable, Sendable`

- 

MTHelperPropertyValue

A single mapping from a property value to an associated numeric value.

See more

#### Declaration

Swift
`public struct MTHelperPropertyValue : Codable, Sendable`

Colors

- 

MTColorValue

Encodes a color to a hex string when converted to JSON.
Accepts either a hex color string (e.g. “#RRGGBB”) or a UIColor.

See more

#### Declaration

Swift
`public struct MTColorValue : Codable, Sendable`

- 

MTSky

Sky configuration used by `map.setSky`.

See more

#### Declaration

Swift
`public struct MTSky : Sendable, Codable, Equatable`

---

## File: Typealiases.html

---
layout: mobile_sdk
title: "Type Aliases"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The following type aliases are available globally."
id: typealiases
breadcrumb: "Mobile SDK/iOS/Reference/."
---

# Type Aliases

The following type aliases are available globally.

- 

MTZoomStringValues

Array of string values that depend on zoom level.

#### Declaration

Swift
`public typealias MTZoomStringValues = [MTZoomStringValue]`

- 

MTZoomNumberValues

Array of number values that depend on zoom level.

#### Declaration

Swift
`public typealias MTZoomNumberValues = [MTZoomNumberValue]`

- 

MTPropertyValues

Array mapping a property input value to an associated numeric output value.

#### Declaration

Swift
`public typealias MTPropertyValues = [MTHelperPropertyValue]`

---

