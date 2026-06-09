# MapTiler iOS SDK API Reference - Protocols

This document is a part of the iOS SDK API reference documentation, covering the `Protocols` category.

---

## File: Protocols/MTAnnotation.html

---
layout: mobile_sdk
title: "MTAnnotation"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirements for all annotation objects."
id: mtannotation
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTAnnotation

`public protocol MTAnnotation : Sendable`

Protocol requirements for all annotation objects.

- 

identifier

Unique id.

#### Declaration

Swift
`var identifier: String { get }`

- 

coordinates

Geographical coordinates.

#### Declaration

Swift
`var coordinates: CLLocationCoordinate2D { get }`

- 

setCoordinates(_:in:)

Asynchronous

Sets the coordinates.

#### Declaration

Swift
`func setCoordinates(_ coordinates: CLLocationCoordinate2D, in mapView: MTMapView) async`

#### Parameters

| coordinates | Coordinates to set. |
| mapView | Map view to apply to. |

---

## File: Protocols/MTControllable.html

---
layout: mobile_sdk
title: "MTControllable"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines methods for adding the map controls."
id: mtcontrollable
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTControllable

@MainActor
public protocol MTControllable

Defines methods for adding the map controls.

- 

addMapTilerLogoControl(position:)

Asynchronous

Adds the MapTiler logo control to the map.

#### Declaration

Swift
@MainActor
func addMapTilerLogoControl(position: MTMapCorner) async

#### Parameters

| position | Map position to add the control to. |

- 

addLogoControl(name:logoURL:linkURL:position:)

Asynchronous

Adds the logo control to the map.

#### Declaration

Swift
@MainActor
func addLogoControl(name: String, logoURL: URL, linkURL: URL, position: MTMapCorner) async

#### Parameters

| logoURL | URL of the logo image resource. |
| linkURL | URL of the anchor link. |
| position | Map position to add the control to. |

---

## File: Protocols/MTGesture.html

---
layout: mobile_sdk
title: "MTGesture"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines gestures behaviour."
id: mtgesture
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTGesture

@MainActor
public protocol MTGesture

Defines gestures behaviour.

- 

type

Type of the gesture.

#### Declaration

Swift
@MainActor
var type: MTGestureType { get }

- 

disable()

Asynchronous

Disables the gesture.

#### Declaration

Swift
@MainActor
func disable() async

- 

enable()

Asynchronous

Enables the gesture.

#### Declaration

Swift
@MainActor
func enable() async

---

## File: Protocols/MTLayer.html

---
layout: mobile_sdk
title: "MTLayer"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirements for all types of Layers."
id: mtlayer
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTLayer

`public protocol MTLayer : AnyObject, MTMapViewContent, Sendable`

Protocol requirements for all types of Layers.

- 

identifier

Unique id of the layer.

#### Declaration

Swift
`var identifier: String { get set }`

- 

type

Type of the layer.

#### Declaration

Swift
`var type: MTLayerType { get }`

- 

sourceIdentifier

Identifier of the source.

#### Declaration

Swift
`var sourceIdentifier: String { get set }`

- 

maxZoom

Max zoom of the layer.

#### Declaration

Swift
`var maxZoom: Double? { get set }`

- 

minZoom

Min zoom of the layer.

#### Declaration

Swift
`var minZoom: Double? { get set }`

- 

sourceLayer

Identifier of the source (main) layer to use.

#### Declaration

Swift
`var sourceLayer: String? { get set }`

---

## File: Protocols/MTLocationManagerDelegate.html

---
layout: mobile_sdk
title: "MTLocationManagerDelegate"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirements for location manager."
id: mtlocationmanagerdelegate
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTLocationManagerDelegate

@MainActor
public protocol MTLocationManagerDelegate : AnyObject

Protocol requirements for location manager.

- 

didUpdateLocation(_:)

Trigger when location updates.

#### Declaration

Swift
@MainActor
func didUpdateLocation(_ location: CLLocation)

- 

didFailWithError(_:)

Triggers when location updates fail.

#### Declaration

Swift
@MainActor
func didFailWithError(_ error: Error)

---

## File: Protocols/MTLoggable.html

---
layout: mobile_sdk
title: "MTLoggable"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirement for all Logger objects."
id: mtloggable
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTLoggable

`public protocol MTLoggable : Sendable`

Protocol requirement for all Logger objects.

- 

log(_:type:)

Asynchronous

Logs the message with type.

#### Declaration

Swift
`func log(_ message: String, type: MTLogType) async`

---

## File: Protocols/MTMapViewContent.html

---
layout: mobile_sdk
title: "MTMapViewContent"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Map view content requirements."
id: mtmapviewcontent
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTMapViewContent

`public protocol MTMapViewContent`

Map view content requirements.

- 

addToMap(_:)

Adds the content to the map DSL style.

#### Declaration

Swift
`func addToMap(_ mapView: MTMapView)`

---

## File: Protocols/MTMapViewDelegate.html

---
layout: mobile_sdk
title: "MTMapViewDelegate"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Delegate responsible for map event propagation"
id: mtmapviewdelegate
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTMapViewDelegate

@MainActor
public protocol MTMapViewDelegate : AnyObject

Delegate responsible for map event propagation

- 

mapViewDidInitialize(_:)

Triggers when map is fully initialized.

#### Declaration

Swift
@MainActor
func mapViewDidInitialize(_ mapView: MTMapView)

- 

mapView(_:didTriggerEvent:with:)

Triggers when event ocurrs.

#### Declaration

Swift
@MainActor
func mapView(_ mapView: MTMapView, didTriggerEvent event: MTEvent, with data: MTData?)

- 

mapView(_:didUpdateLocation:)

Default implementation

Triggers when location is updated.

#### Default Implementation

#### Declaration

Swift
@MainActor
func mapView(_ mapView: MTMapView, didUpdateLocation location: CLLocation)

---

## File: Protocols/MTNavigable.html

---
layout: mobile_sdk
title: "MTNavigable"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines methods for navigating the map."
id: mtnavigable
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTNavigable

@MainActor
public protocol MTNavigable

Defines methods for navigating the map.

- 

setBearing(_:)

Asynchronous

Sets bearing of the map.

#### Declaration

Swift
@MainActor
func setBearing(_ bearing: Double) async

#### Parameters

| bearing | The bearing of the map, measured in degrees counter-clockwise from north. |

- 

setCenter(_:)

Asynchronous

Sets the geographical center of the map.

#### Declaration

Swift
@MainActor
func setCenter(_ center: CLLocationCoordinate2D) async

#### Parameters

| center | Geographical center of the map. |

- 

flyTo(_:options:animationOptions:)

Asynchronous

Changes any combination of center, zoom, bearing, and pitch,
animating the transition along a curve that evokes flight.

#### Declaration

Swift
@MainActor
func flyTo(_ center: CLLocationCoordinate2D, options: MTFlyToOptions?, animationOptions: MTAnimationOptions?) async

#### Parameters

| center | Geographical center of the map. |
| options | FlyTo options. |
| animationOptions | animation options. |

- 

easeTo(_:options:animationOptions:)

Asynchronous

Changes any combination of center, zoom, bearing and pitch
with an animated transition between old and new values.

#### Declaration

Swift
@MainActor
func easeTo(
_ center: CLLocationCoordinate2D,
options: MTCameraOptions?,
animationOptions: MTAnimationOptions?
) async

#### Parameters

| center | Geographical center of the map. |
| options | Camera options. |
| animationOptions | animation options. |

- 

jumpTo(_:options:)

Asynchronous

Changes any combination of center, zoom, bearing, and pitch, without an animated transition

#### Declaration

Swift
@MainActor
func jumpTo(_ center: CLLocationCoordinate2D, options: MTCameraOptions?) async

#### Parameters

| center | Geographical center of the map. |
| options | Camera options. |

- 

fitBounds(_:options:)

Asynchronous

Fits the camera so that the provided bounds are fully visible within the viewport.

#### Declaration

Swift
@MainActor
func fitBounds(_ bounds: MTBounds, options: MTFitBoundsOptions?) async

#### Parameters

| bounds | Geographic bounds to display. |
| options | Additional fit configuration. |

- 

panBy(_:)

Asynchronous

Pans the map by the specified offset.

#### Declaration

Swift
@MainActor
func panBy(_ offset: MTPoint) async

#### Parameters

| offset | Offset to pan by. |

- 

panTo(_:)

Asynchronous

Pans the map to the specified location with an animated transition.

#### Declaration

Swift
@MainActor
func panTo(_ coordinates: CLLocationCoordinate2D) async

#### Parameters

| coordinates | Coordinates to pan to. |

- 

stop()

Asynchronous

Stops any ongoing animated transition.

#### Declaration

Swift
@MainActor
func stop() async

- 

snapToNorth(animationOptions:)

Asynchronous

Snaps the map so that north is up.

#### Declaration

Swift
@MainActor
func snapToNorth(animationOptions: MTAnimationOptions?) async

#### Parameters

| animationOptions | Animation options. |

- 

setPadding(_:)

Asynchronous

Sets the padding in pixels around the viewport.

#### Declaration

Swift
@MainActor
func setPadding(_ options: MTPaddingOptions) async

#### Parameters

| options | Padding options. |

- 

fitToIpBounds()

Asynchronous

Fits the map to the country-level bounds inferred from the current IP address.

#### Declaration

Swift
@MainActor
func fitToIpBounds() async

- 

setIsCenterClampedToGround(_:)

Asynchronous

Sets the center clamped to the ground.

If true, the elevation of the center point will automatically be set to the
terrain elevation (or zero if terrain is not enabled). If false, the elevation
of the center point will default to sea level and will not automatically update.

#### Declaration

Swift
@MainActor
func setIsCenterClampedToGround(_ isCenterClampedToGround: Bool) async

#### Parameters

| isCenterClampedToGround | Boolean indicating whether center is clamped to the ground. |

- 

setCenterElevation(_:)

Asynchronous

Sets the elevation of the map’s center point, in meters above sea level.

#### Declaration

Swift
@MainActor
func setCenterElevation(_ elevation: Double) async

#### Parameters

| elevation | Desired elevation. |

- 

setMaxPitch(_:)

Asynchronous

Sets the map’s maximum pitch.

#### Declaration

Swift
@MainActor
func setMaxPitch(_ maxPitch: Double?) async throws

#### Parameters

| maxPitch | Desired pitch. |

- 

setMaxZoom(_:)

Asynchronous

Sets the map’s maximum zoom.

#### Declaration

Swift
@MainActor
func setMaxZoom(_ maxZoom: Double?) async throws

#### Parameters

| maxZoom | Desired zoom. |

- 

setMinPitch(_:)

Asynchronous

Sets the map’s minimum pitch.

#### Declaration

Swift
@MainActor
func setMinPitch(_ minPitch: Double?) async throws

#### Parameters

| minPitch | Desired pitch. |

- 

setMinZoom(_:)

Asynchronous

Sets the map’s minimum zoom.

#### Declaration

Swift
@MainActor
func setMinZoom(_ minZoom: Double?) async throws

#### Parameters

| minZoom | Desired zoom. |

- 

setMaxBounds(_:)

Asynchronous

Sets or clears the maximum bounds constraint applied to the map.

#### Declaration

Swift
@MainActor
func setMaxBounds(_ bounds: MTBounds?) async throws

#### Parameters

| bounds | Geographic bounds to restrict panning, or `nil` to remove the constraint. |

- 

setPitch(_:)

Asynchronous

Sets the map’s pitch.

#### Declaration

Swift
@MainActor
func setPitch(_ pitch: Double) async

#### Parameters

| pitch | The pitch to set, measured in degrees away from the plane of the screen (0-60). |

- 

setRoll(_:)

Asynchronous

Sets the map’s roll angle.

#### Declaration

Swift
@MainActor
func setRoll(_ roll: Double) async

#### Parameters

| roll | Desired roll. |

- 

getPitch()

Asynchronous

Returns the map’s current pitch.

#### Declaration

Swift
@MainActor
func getPitch() async -> Double

- 

getMaxPitch()

Asynchronous

Returns the map’s maximum pitch.

#### Declaration

Swift
@MainActor
func getMaxPitch() async -> Double

- 

getMaxZoom()

Asynchronous

Returns the map’s maximum zoom.

#### Declaration

Swift
@MainActor
func getMaxZoom() async -> Double

- 

getMinPitch()

Asynchronous

Returns the map’s minimum pitch.

#### Declaration

Swift
@MainActor
func getMinPitch() async -> Double

- 

getMinZoom()

Asynchronous

Returns the map’s minimum zoom.

#### Declaration

Swift
@MainActor
func getMinZoom() async -> Double

- 

getCenter()

Asynchronous

Returns the map’s current center.

#### Declaration

Swift
@MainActor
func getCenter() async -> CLLocationCoordinate2D

- 

getBounds()

Asynchronous

Returns the current viewport bounds.

#### Declaration

Swift
@MainActor
func getBounds() async -> MTBounds

- 

getMaxBounds()

Asynchronous

Returns the maximum allowed bounds constraint if one is set.

#### Declaration

Swift
@MainActor
func getMaxBounds() async -> MTBounds?

- 

getCenterClampedToGround()

Asynchronous

Returns the state of the center clamped to ground flag.

#### Declaration

Swift
@MainActor
func getCenterClampedToGround() async -> Bool

- 

getCenterElevation()

Asynchronous

Returns the elevation of the map’s center point in meters above sea level.

#### Declaration

Swift
@MainActor
func getCenterElevation() async -> Double

- 

getCameraTargetElevation()

Asynchronous

Returns the elevation for the point where the camera is looking,
in meters above sea level multiplied by exaggeration.

#### Declaration

Swift
@MainActor
func getCameraTargetElevation() async -> Double

- 

getBearing()

Asynchronous

Returns the map’s current bearing.

#### Declaration

Swift
@MainActor
func getBearing() async -> Double

- 

getRoll()

Asynchronous

Returns the map’s current roll.

#### Declaration

Swift
@MainActor
func getRoll() async -> Double

---

## File: Protocols/MTRendering.html

---
layout: mobile_sdk
title: "MTRendering"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines methods for adjusting rendering parameters."
id: mtrendering
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTRendering

@MainActor
public protocol MTRendering

Defines methods for adjusting rendering parameters.

- 

getPixelRatio()

Asynchronous

Returns the pixel ratio currently used by the map.

#### Declaration

Swift
@MainActor
func getPixelRatio() async -> Double

- 

setPixelRatio(_:)

Asynchronous

Sets the pixel ratio to use when rendering the map.

#### Declaration

Swift
@MainActor
func setPixelRatio(_ pixelRatio: Double) async

#### Parameters

| pixelRatio | Pixel ratio value to apply. |

- 

triggerRepaint()

Asynchronous

Trigger the rendering of a single frame. Use this method with custom layers to repaint the map
when the layer changes. Calling this multiple times before the next frame is rendered will still
result in only a single frame being rendered.

#### Declaration

Swift
@MainActor
func triggerRepaint() async

- 

setShowTileBoundaries(_:)

Asynchronous

Displays tile boundaries on the map.

#### Declaration

Swift
@MainActor
func setShowTileBoundaries(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show tile boundaries. |

- 

setShowPadding(_:)

Asynchronous

Displays padding on the map.

#### Declaration

Swift
@MainActor
func setShowPadding(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show padding. |

- 

setShowOverdrawInspector(_:)

Asynchronous

Displays the overdraw inspector on the map.

#### Declaration

Swift
@MainActor
func setShowOverdrawInspector(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show the overdraw inspector. |

- 

setShowCollisionBoxes(_:)

Asynchronous

Displays collision boxes on the map.

#### Declaration

Swift
@MainActor
func setShowCollisionBoxes(_ show: Bool) async

#### Parameters

| show | A boolean value indicating whether to show collision boxes. |

- 

setMaxParallelImageRequests(_:)

Asynchronous

Sets the maximum number of images loaded in parallel.

#### Declaration

Swift
@MainActor
func setMaxParallelImageRequests(_ maxParallelImageRequests: Int) async

#### Parameters

| maxParallelImageRequests | The maximum number of images. |

- 

setRTLTextPlugin(pluginURL:deferred:)

Asynchronous

Sets the map’s RTL text plugin.

#### Declaration

Swift
@MainActor
func setRTLTextPlugin(pluginURL: String, deferred: Bool) async

#### Parameters

| pluginURL | URL pointing to the Mapbox RTL text plugin source. |
| deferred | A boolean indicating if the plugin evaluation should be deferred. |

---

## File: Protocols/MTSource.html

---
layout: mobile_sdk
title: "MTSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirements for all types of Sources."
id: mtsource
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTSource

`public protocol MTSource : AnyObject, MTMapViewContent, Sendable`

Protocol requirements for all types of Sources.

- 

identifier

Unique id of the source.

#### Declaration

Swift
`var identifier: String { get set }`

- 

url

URL pointing to the source resource.

#### Declaration

Swift
`var url: URL? { get set }`

- 

type

Type of the source.

#### Declaration

Swift
`var type: MTSourceType { get }`

---

## File: Protocols/MTStylable.html

---
layout: mobile_sdk
title: "MTStylable"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines methods for map styling methods."
id: mtstylable
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTStylable

@MainActor
public protocol MTStylable

Defines methods for map styling methods.

- 

setGlyphs(url:options:)

Asynchronous

Sets the value of the style’s glyphs property.

#### Declaration

Swift
@MainActor
func setGlyphs(url: URL, options: MTStyleSetterOptions?) async

#### Parameters

| url | URL pointing to the glyphs resource. |
| options | Style setter options. |

- 

setLanguage(_:)

Asynchronous

Sets the map labels language.

The language generally depends on the style. Whenever a label is not supported in the defined language,
it falls back to `Latin`.

#### Declaration

Swift
@MainActor
func setLanguage(_ language: MTLanguage) async

#### Parameters

| language | The language to be applied. |

- 

setSecondaryLanguage(_:)

Asynchronous

Sets the map labels secondary language.

#### Declaration

Swift
@MainActor
func setSecondaryLanguage(_ language: MTLanguage) async

#### Parameters

| language | The language to be applied. |

- 

setSprite(_:)

Asynchronous

Sets the map sprite.

#### Declaration

Swift
@MainActor
func setSprite(_ url: URL) async

#### Parameters

| url | The URL pointing to the sprite resource. |

- 

setLight(_:options:)

Asynchronous

Sets the any combination of light values.

#### Declaration

Swift
@MainActor
func setLight(_ light: MTLight, options: MTStyleSetterOptions?) async

#### Parameters

| light | Light options. |
| options | Style setter options. |

- 

setSky(_:options:)

Asynchronous

Sets the sky configuration for the map.

#### Declaration

Swift
@MainActor
func setSky(_ sky: MTSky, options: MTStyleSetterOptions?) async

#### Parameters

| sky | Sky definition. |
| options | Style setter options. |

- 

setSpace(_:)

Asynchronous

Sets the space background for globe projection (cubemap/spacebox).

Note
Make sure space is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@MainActor
func setSpace(_ space: MTSpaceOption) async

#### Parameters

| space | Space configuration or a boolean to enable default. |

- 

setHalo(_:)

Asynchronous

Sets the atmospheric halo (glow) around the globe.

Note
Make sure halo is enabled and projection is set to Globe before initializing the map via MTMapOptions.

#### Declaration

Swift
@MainActor
func setHalo(_ halo: MTHaloOption) async

#### Parameters

| halo | Halo configuration or a boolean to enable default. |

- 

disableHaloAnimations()

Asynchronous

Disables state transitions/animations for halo updates.

#### Declaration

Swift
@MainActor
func disableHaloAnimations() async

- 

disableSpaceAnimations()

Asynchronous

Disables state transitions/animations for space updates.

#### Declaration

Swift
@MainActor
func disableSpaceAnimations() async

- 

setShouldRenderWorldCopies(_:)

Asynchronous

Sets the state where multiple copies of the world will be rendered
side by side beyond -180 and 180 degrees longitude.

#### Declaration

Swift
@MainActor
func setShouldRenderWorldCopies(_ shouldRenderWorldCopies: Bool) async

#### Parameters

| shouldRenderWorldCopies | Boolean indicating whether world copies should be rendered. |

- 

addImage(name:image:options:)

Asynchronous

Registers an image with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@MainActor
func addImage(name: String, image: UIImage, options: MTStyleImageOptions?) async

#### Parameters

| name | Unique identifier for the image. |
| image | Image to register. |
| options | Additional configuration that controls how the image is rendered. |

- 

addSprite(id:url:)

Asynchronous

Registers a sprite with the current style so it can be referenced by layers and annotations.

#### Declaration

Swift
@MainActor
func addSprite(id: String, url: URL) async

#### Parameters

| id | Unique identifier for the sprite. |
| url | URL pointing to the sprite resource. |

- 

addMarker(_:)

Asynchronous

Adds the marker to the map.

#### Declaration

Swift
@MainActor
func addMarker(_ marker: MTMarker) async

#### Parameters

| marker | Marker to add to the map. |

- 

addMarkers(_:withSingleIcon:)

Asynchronous

Adds multiple markers to the map.

Batch adding is preferred way of adding multiple markers to the map.

#### Declaration

Swift
@MainActor
func addMarkers(_ markers: [MTMarker], withSingleIcon: UIImage?) async

#### Parameters

| markers | Markers to be added to the map. |
| withSingleIcon | Optional single image to use for all markers. |

- 

removeMarker(_:)

Asynchronous

Removes a marker from the map.

#### Declaration

Swift
@MainActor
func removeMarker(_ marker: MTMarker) async

#### Parameters

| marker | Marker to be removed from the map. |

- 

removeMarkers(_:)

Asynchronous

Removes multiple markers from the map.

Batch removing is preferred way of removing multiple markers from the map.

#### Declaration

Swift
@MainActor
func removeMarkers(_ markers: [MTMarker]) async

#### Parameters

| markers | Markers to be removed from the map. |

- 

enableGlobeProjection()

Asynchronous

Enables the globe projection visualization.

#### Declaration

Swift
@MainActor
func enableGlobeProjection() async

- 

enableMercatorProjection()

Asynchronous

Enables the mercator projection visualization.

#### Declaration

Swift
@MainActor
func enableMercatorProjection() async

- 

enableTerrain(exaggerationFactor:)

Asynchronous

Enables the 3D terrain visualization.

Note
Default is 1.

#### Declaration

Swift
@MainActor
func enableTerrain(exaggerationFactor: Double) async

#### Parameters

| exaggerationFactor | Factor for volume boosting. |

- 

disableTerrain()

Asynchronous

Disables  the 3D terrain visualization.

#### Declaration

Swift
@MainActor
func disableTerrain() async

- 

setTerrainExaggeration(_:animate:)

Asynchronous

Sets the terrain exaggeration.

#### Declaration

Swift
@MainActor
func setTerrainExaggeration(_ exaggeration: Double, animate: Bool) async

#### Parameters

| exaggeration | The new exaggeration factor. |
| animate | Whether to animate the transition. Defaults to `true`. |

- 

setTerrainAnimationDuration(_:)

Asynchronous

Sets the animation duration of the terrain transitions.

#### Declaration

Swift
@MainActor
func setTerrainAnimationDuration(_ duration: Double) async

#### Parameters

| duration | The duration in milliseconds. |

- 

setTerrain(sourceId:exaggeration:)

Asynchronous

Sets the 3D terrain on the map.

#### Declaration

Swift
@MainActor
func setTerrain(sourceId: String, exaggeration: Double?) async

#### Parameters

| sourceId | The ID of the terrain source. |
| exaggeration | Factor for volume boosting. |

- 

setTerrain()

Asynchronous

Removes the 3D terrain from the map.

#### Declaration

Swift
@MainActor
func setTerrain() async

- 

setVerticalFieldOfView(degrees:)

Asynchronous

Sets the map’s vertical field of view, in degrees.

The internal camera has a default vertical field of view of a wide ~36.86 degrees. In globe mode,
such a large FOV reduces the amount of the Earth that can be seen at once and exaggerates
the central part, comparably to a fisheye lens. In many cases, a narrower FOV is preferable.

Note
Default is 36.87.

#### Declaration

Swift
@MainActor
func setVerticalFieldOfView(degrees: Double) async

#### Parameters

| degrees | The vertical field of view to set, in degrees (0-180). |

- 

isSourceLoaded(id:)

Asynchronous

Returns boolean value indicating whether the source with provided id is loaded.

#### Declaration

Swift
@MainActor
func isSourceLoaded(id: String) async -> Bool

#### Parameters

| id | The id of the source. |

---

## File: Protocols/MTTileSource.html

---
layout: mobile_sdk
title: "MTTileSource"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Protocol requirements for all tile type sources."
id: mttilesource
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTTileSource

`public protocol MTTileSource : MTSource`

Protocol requirements for all tile type sources.

- 

attribution

Attribution string.

#### Declaration

Swift
`var attribution: String? { get set }`

- 

bounds

Bounds of the source.

#### Declaration

Swift
`var bounds: [Double] { get set }`

- 

maxZoom

Max zoom of the source.

#### Declaration

Swift
`var maxZoom: Double { get set }`

- 

minZoom

Min zoom of the source.

#### Declaration

Swift
`var minZoom: Double { get set }`

- 

tiles

List of URLs pointing to the tiles resources.

#### Declaration

Swift
`var tiles: [URL]? { get set }`

---

## File: Protocols/MTVectorLayerHelper.html

---
layout: mobile_sdk
title: "MTVectorLayerHelper"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Base protocol adopted by vector layer helpers to share defaults
and common option normalization logic."
id: mtvectorlayerhelper
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTVectorLayerHelper

`public protocol MTVectorLayerHelper : AnyObject`

Base protocol adopted by vector layer helpers to share defaults
and common option normalization logic.

- 

style

Undocumented

#### Declaration

Swift
`var style: MTStyle { get }`

- 

baseMinZoom

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseMinZoom: Double { get }`

- 

baseMaxZoom

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseMaxZoom: Double { get }`

- 

baseOutline

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseOutline: Bool { get }`

- 

baseOutlineColor

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseOutlineColor: MTStringOrZoomStringValues { get }`

- 

baseOutlineWidth

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseOutlineWidth: MTNumberOrZoomNumberValues { get }`

- 

baseOutlineOpacity

Default implementation

Undocumented

#### Default Implementation

Undocumented

#### Declaration

Swift
`static var baseOutlineOpacity: MTNumberOrZoomNumberValues { get }`

- 

applyCommonDefaults(to:)

Extension method

Undocumented

#### Declaration

Swift
`func applyCommonDefaults(to options: MTHeatmapLayerOptions) -> MTHeatmapLayerOptions`

- 

applyCommonDefaults(to:)

Extension method

Undocumented

#### Declaration

Swift
`func applyCommonDefaults(to options: MTPointLayerOptions) -> MTPointLayerOptions`

---

## File: Protocols/MTZoomable.html

---
layout: mobile_sdk
title: "MTZoomable"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines methods for manipulating zoom level."
id: mtzoomable
breadcrumb: "Mobile SDK/iOS/Reference/Protocols"
---

# MTZoomable

@MainActor
public protocol MTZoomable

Defines methods for manipulating zoom level.

- 

zoomIn()

Asynchronous

Increases the map’s zoom level by 1.

#### Declaration

Swift
@MainActor
func zoomIn() async

- 

zoomOut()

Asynchronous

Decreases the map’s zoom level by 1.

#### Declaration

Swift
@MainActor
func zoomOut() async

- 

getZoom()

Asynchronous

Returns the map’s current zoom level.

#### Declaration

Swift
@MainActor
func getZoom() async -> Double

- 

setZoom(_:)

Asynchronous

Sets the map’s zoom level.

#### Declaration

Swift
@MainActor
func setZoom(_ zoom: Double) async

---

