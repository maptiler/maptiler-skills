# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat/-lng-lat.html

---
layout: mobile_sdk
title: "LngLat"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LngLat"
id: -lng-lat
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat"
---
# LngLat

constructor(lng: Double, lat: Double)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat/index.html

---
layout: mobile_sdk
title: "LngLat"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "LngLat"
id: -lng-lat
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat"
---
# LngLat

@Serializabledata class LngLat(val lng: Double, val lat: Double)A geographical location which contains a latitude, longitude pair.

Members

## Constructors

LngLat

constructor(lng: Double, lat: Double)

## Properties

lat

val lat: Double

lng

val lng: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat/lat.html

---
layout: mobile_sdk
title: "lat"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lat"
id: lat
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat"
---
# lat

val lat: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat/lng.html

---
layout: mobile_sdk
title: "lng"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lng"
id: lng
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-lng-lat"
---
# lng

val lng: Double

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion/camera-looking-at-center-coordinate.html

---
layout: mobile_sdk
title: "cameraLookingAtCenterCoordinate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "cameraLookingAtCenterCoordinate"
id: camera-looking-at-center-coordinate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion"
---
# cameraLookingAtCenterCoordinate

fun cameraLookingAtCenterCoordinate(centerCoordinate: LngLat, bearing: Double, pitch: Double, roll: Double, elevation: Double): MTMapCameraHelperReturns camera object with the given center coordinate, bearing, pitch, roll and elevation.fun cameraLookingAtCenterCoordinate(centerCoordinate: LngLat, bearing: Double, pitch: Double): MTMapCameraHelperReturns camera object with the given center coordinate, bearing and pitch.Looks for roll and elevation in the map's style object. If they are not specified in the style, they will default to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion/get-camera-from-map-style.html

---
layout: mobile_sdk
title: "getCameraFromMapStyle"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCameraFromMapStyle"
id: get-camera-from-map-style
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion"
---
# getCameraFromMapStyle

fun getCameraFromMapStyle(): MTMapCameraHelperReturns camera object initialized from map style options.If any of the properties is not set within the style, it will default to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion/get-camera.html

---
layout: mobile_sdk
title: "getCamera"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCamera"
id: get-camera
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion"
---
# getCamera

fun getCamera(): MTMapCameraHelperReturns camera object with all properties set to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion/index.html

---
layout: mobile_sdk
title: "Companion"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Companion"
id: -companion
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/-companion"
---
# Companion

object Companion

Members

## Functions

cameraLookingAtCenterCoordinate

fun cameraLookingAtCenterCoordinate(centerCoordinate: LngLat, bearing: Double, pitch: Double): MTMapCameraHelperReturns camera object with the given center coordinate, bearing and pitch.fun cameraLookingAtCenterCoordinate(centerCoordinate: LngLat, bearing: Double, pitch: Double, roll: Double, elevation: Double): MTMapCameraHelperReturns camera object with the given center coordinate, bearing, pitch, roll and elevation.

getCamera

fun getCamera(): MTMapCameraHelperReturns camera object with all properties set to 0.

getCameraFromMapStyle

fun getCameraFromMapStyle(): MTMapCameraHelperReturns camera object initialized from map style options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/bearing.html

---
layout: mobile_sdk
title: "bearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bearing"
id: bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# bearing

val bearing: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/center-coordinate.html

---
layout: mobile_sdk
title: "centerCoordinate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "centerCoordinate"
id: center-coordinate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# centerCoordinate

val centerCoordinate: LngLat? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/elevation.html

---
layout: mobile_sdk
title: "elevation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "elevation"
id: elevation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# elevation

val elevation: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/index.html

---
layout: mobile_sdk
title: "MTMapCameraHelper"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapCameraHelper"
id: -m-t-map-camera-helper
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# MTMapCameraHelper

class MTMapCameraHelperSets combination of center, bearing and pitch, as well as roll and elevation.

Members

## Types

Companion

object Companion

## Properties

bearing

val bearing: Double? = null

centerCoordinate

val centerCoordinate: LngLat? = null

elevation

val elevation: Double? = null

pitch

val pitch: Double? = null

roll

val roll: Double? = null

## Functions

isEqualTo

fun isEqualTo(otherCamera: MTMapCameraHelper): BooleanReturns boolean indicating whether camera object is equal to the receiver.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/is-equal-to.html

---
layout: mobile_sdk
title: "isEqualTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isEqualTo"
id: is-equal-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# isEqualTo

fun isEqualTo(otherCamera: MTMapCameraHelper): BooleanReturns boolean indicating whether camera object is equal to the receiver.
#### Parameters

otherCameraMTMapCameraHelper to compare with.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/pitch.html

---
layout: mobile_sdk
title: "pitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitch"
id: pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# pitch

val pitch: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper/roll.html

---
layout: mobile_sdk
title: "roll"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "roll"
id: roll
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-camera-helper"
---
# roll

val roll: Double? = null

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/-m-t-map-options.html

---
layout: mobile_sdk
title: "MTMapOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapOptions"
id: -m-t-map-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# MTMapOptions

constructor(center: LngLat?, zoom: Double?, bearing: Double?, pitch: Double?)Initializes map options with center, zoom, bearing, and pitch.constructor(center: LngLat?, zoom: Double?)Initializes map options with center and zoom.constructor(center: LngLat?, zoom: Double?, language: MTLanguage)Initializes map options with center, zoom and language.constructor(center: LngLat?, zoom: Double?, terrainIsEnabled: Boolean?, terrainExaggeration: Double?)Initializes map options with center, zoom and terrain.constructor(center: LngLat?, zoom: Double?, projection: MTProjectionType?)Initializes map options with center, zoom and projection.constructor()Full constructor with optional parameters for all properties.constructor(projection: MTProjectionType?, space: MTSpaceOption?)Initializes map options with projection and space option.constructor(space: MTSpace)Convenience: configuration-only space.constructor(spaceEnabled: Boolean)Convenience: enable space with default preset.constructor(halo: MTHalo)Convenience: configuration-only halo.constructor(halo: MTHaloOption?)Convenience: pass halo option directly (enabled or config).constructor(projection: MTProjectionType?, halo: MTHaloOption?)Convenience: projection + halo option (enabled or config).constructor(language: MTLanguage? = null, center: LngLat? = null, bounds: MTBounds? = null, projection: MTProjectionType? = null, zoom: Double? = null, maxZoom: Double? = null, maxBounds: MTBounds? = null, minZoom: Double? = null, bearing: Double? = null, bearingSnap: Double? = null, pitch: Double? = null, maxPitch: Double? = null, minPitch: Double? = null, roll: Double? = null, rollIsEnabled: Boolean? = null, elevation: Double? = null, terrainIsEnabled: Boolean? = null, terrainExaggeration: Double? = null, cancelPendingTileRequestsWhileZooming: Boolean? = null, isCenterClampedToGround: Boolean? = null, shouldCollectResourceTiming: Boolean? = null, crossSourceCollisionsAreEnabled: Boolean? = null, fadeDuration: Double? = null, isInteractionEnabled: Boolean? = null, logoPosition: MTMapCorner? = MTMapCorner.TOP_LEFT, maptilerLogoIsVisible: Boolean? = null, maxTileCacheSize: Double? = null, maxTileCacheZoomLevels: Double? = null, pixelRatio: Double? = null, shouldPitchWithRotate: Boolean? = null, shouldRefreshExpiredTiles: Boolean? = null, shouldRenderWorldCopies: Boolean? = null, shouldDragToPitch: Boolean? = null, shouldPinchToRotateAndZoom: Boolean? = null, doubleTapShouldZoom: Boolean? = null, dragPanIsEnabled: Boolean? = null, dragRotateIsEnabled: Boolean? = null, shouldValidateStyle: Boolean? = null, minimapIsVisible: Boolean? = false, attributionControlIsVisible: Boolean? = null, geolocateControlIsVisible: Boolean? = false, navigationControlIsVisible: Boolean? = false, projectionControlIsVisible: Boolean? = false, scaleControlIsVisible: Boolean? = false, terrainControlIsVisible: Boolean? = false, space: MTSpaceOption? = null, halo: MTHaloOption? = null, isSessionLogicEnabled: Boolean = true, eventLevel: MTEventLevel = MTEventLevel.CAMERA_ONLY, highFrequencyEventThrottleMs: Int? = 20)Flexible constructor: all options optional so you can mix and match with named args.Example usages:- MTMapOptions(projection = MTProjectionType.GLOBE, space = MTSpaceOption.Enabled, halo = MTHaloOption.Enabled)
- MTMapOptions(projection = MTProjectionType.GLOBE, halo = MTHaloOption.Config(MTHalo(scale = 1.2)))
- MTMapOptions(center = LngLat(14.4, 50.1), zoom = 6.0, pitch = 45.0)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/attribution-control-is-visible.html

---
layout: mobile_sdk
title: "attributionControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attributionControlIsVisible"
id: attribution-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# attributionControlIsVisible

@SerialName(value = "attributionControl")var attributionControlIsVisible: Boolean?Boolean indicating whether attribution control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/bearing-snap.html

---
layout: mobile_sdk
title: "bearingSnap"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bearingSnap"
id: bearing-snap
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# bearingSnap

var bearingSnap: Double?The threshold, measured in degrees, that determines when the map's bearing will snap to north.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/bearing.html

---
layout: mobile_sdk
title: "bearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bearing"
id: bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# bearing

var bearing: Double?The bearing of the map, measured in degrees counter-clockwise from north.If bearing is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to 0.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/bounds.html

---
layout: mobile_sdk
title: "bounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "bounds"
id: bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# bounds

var bounds: MTBounds?Geographical area that should be visible when the map initializes.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/cancel-pending-tile-requests-while-zooming.html

---
layout: mobile_sdk
title: "cancelPendingTileRequestsWhileZooming"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "cancelPendingTileRequestsWhileZooming"
id: cancel-pending-tile-requests-while-zooming
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# cancelPendingTileRequestsWhileZooming

var cancelPendingTileRequestsWhileZooming: Boolean?Determines whether to cancel, or retain, tiles from the current viewport which are still loading but which belong to a farther (smaller) zoom level than the current one.If true, when zooming in, tiles which didn't manage to load for previous zoom levels will become canceled. This might save some computing resources for slower devices, but the map details might appear more abruptly at the end of the zoom. If false, when zooming in, the previous zoom level(s) tiles will progressively appear, giving a smoother map details experience. However, more tiles will be rendered in a short period of time.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/center.html

---
layout: mobile_sdk
title: "center"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "center"
id: center
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# center

var center: LngLat?The geographical centerpoint of the map.If center is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to (latitude: 0.0, longitude: 0.0).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/cross-source-collisions-are-enabled.html

---
layout: mobile_sdk
title: "crossSourceCollisionsAreEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "crossSourceCollisionsAreEnabled"
id: cross-source-collisions-are-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# crossSourceCollisionsAreEnabled

@SerialName(value = "crossSourceCollisions")var crossSourceCollisionsAreEnabled: Boolean?Boolean indicating whether cross source collisions are enabled.If true, symbols from multiple sources can collide with each other during collision detection. If false, collision detection is run separately for the symbols in each source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/double-tap-should-zoom.html

---
layout: mobile_sdk
title: "doubleTapShouldZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "doubleTapShouldZoom"
id: double-tap-should-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# doubleTapShouldZoom

@SerialName(value = "doubleClickZoom")var doubleTapShouldZoom: Boolean?Boolean indicating whether the double tap to zoom interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/drag-pan-is-enabled.html

---
layout: mobile_sdk
title: "dragPanIsEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "dragPanIsEnabled"
id: drag-pan-is-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# dragPanIsEnabled

@SerialName(value = "dragPan")var dragPanIsEnabled: Boolean?Boolean indicating whether the drag to pan interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/drag-rotate-is-enabled.html

---
layout: mobile_sdk
title: "dragRotateIsEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "dragRotateIsEnabled"
id: drag-rotate-is-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# dragRotateIsEnabled

@SerialName(value = "dragRotate")var dragRotateIsEnabled: Boolean?Boolean indicating whether the drag to rotate interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/elevation.html

---
layout: mobile_sdk
title: "elevation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "elevation"
id: elevation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# elevation

var elevation: Double?The elevation of the geographical centerpoint of the map, in meters above sea level.If elevation is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to 0.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/enable-halo.html

---
layout: mobile_sdk
title: "enableHalo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "enableHalo"
id: enable-halo
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# enableHalo

fun enableHalo()Enables halo with default gradient.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/event-level.html

---
layout: mobile_sdk
title: "eventLevel"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "eventLevel"
id: event-level
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# eventLevel

var eventLevel: MTEventLevelControls which map events are sent from the map object.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/fade-duration.html

---
layout: mobile_sdk
title: "fadeDuration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fadeDuration"
id: fade-duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# fadeDuration

var fadeDuration: Double?The duration of the fade-in/fade-out animation for label collisions, in milliseconds.This setting affects all symbol layers. This setting does not affect the duration of runtime styling transitions or raster tile cross-fading.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/geolocate-control-is-visible.html

---
layout: mobile_sdk
title: "geolocateControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "geolocateControlIsVisible"
id: geolocate-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# geolocateControlIsVisible

@SerialName(value = "geolocateControl")var geolocateControlIsVisible: Boolean?Boolean indicating whether geolocate control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/halo.html

---
layout: mobile_sdk
title: "halo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "halo"
id: halo
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# halo

@SerialName(value = "halo")var halo: MTHaloOption?Halo option for the atmospheric glow. Can be a simple enable flag or a detailed config. Requires globe projection to be enabled to be visible.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/high-frequency-event-throttle-ms.html

---
layout: mobile_sdk
title: "highFrequencyEventThrottleMs"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "highFrequencyEventThrottleMs"
id: high-frequency-event-throttle-ms
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# highFrequencyEventThrottleMs

var highFrequencyEventThrottleMs: Int?Optional throttle in milliseconds applied to high-frequency events when eventLevel is MTEventLevel.ALL or MTEventLevel.CAMERA_ONLY. A value of 0 disables throttling.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/index.html

---
layout: mobile_sdk
title: "MTMapOptions"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapOptions"
id: -m-t-map-options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# MTMapOptions

@Serializableclass MTMapOptionsParameters of the map object.

MembersMembers & Extensions

## Constructors

MTMapOptions

constructor(center: LngLat?, zoom: Double?, bearing: Double?, pitch: Double?)Initializes map options with center, zoom, bearing, and pitch.constructor(center: LngLat?, zoom: Double?)Initializes map options with center and zoom.constructor(center: LngLat?, zoom: Double?, language: MTLanguage)Initializes map options with center, zoom and language.constructor(center: LngLat?, zoom: Double?, terrainIsEnabled: Boolean?, terrainExaggeration: Double?)Initializes map options with center, zoom and terrain.constructor(center: LngLat?, zoom: Double?, projection: MTProjectionType?)Initializes map options with center, zoom and projection.constructor()Full constructor with optional parameters for all properties.constructor(projection: MTProjectionType?, space: MTSpaceOption?)Initializes map options with projection and space option.constructor(space: MTSpace)Convenience: configuration-only space.constructor(spaceEnabled: Boolean)Convenience: enable space with default preset.constructor(halo: MTHalo)Convenience: configuration-only halo.constructor(halo: MTHaloOption?)Convenience: pass halo option directly (enabled or config).constructor(projection: MTProjectionType?, halo: MTHaloOption?)Convenience: projection + halo option (enabled or config).constructor(language: MTLanguage? = null, center: LngLat? = null, bounds: MTBounds? = null, projection: MTProjectionType? = null, zoom: Double? = null, maxZoom: Double? = null, maxBounds: MTBounds? = null, minZoom: Double? = null, bearing: Double? = null, bearingSnap: Double? = null, pitch: Double? = null, maxPitch: Double? = null, minPitch: Double? = null, roll: Double? = null, rollIsEnabled: Boolean? = null, elevation: Double? = null, terrainIsEnabled: Boolean? = null, terrainExaggeration: Double? = null, cancelPendingTileRequestsWhileZooming: Boolean? = null, isCenterClampedToGround: Boolean? = null, shouldCollectResourceTiming: Boolean? = null, crossSourceCollisionsAreEnabled: Boolean? = null, fadeDuration: Double? = null, isInteractionEnabled: Boolean? = null, logoPosition: MTMapCorner? = MTMapCorner.TOP_LEFT, maptilerLogoIsVisible: Boolean? = null, maxTileCacheSize: Double? = null, maxTileCacheZoomLevels: Double? = null, pixelRatio: Double? = null, shouldPitchWithRotate: Boolean? = null, shouldRefreshExpiredTiles: Boolean? = null, shouldRenderWorldCopies: Boolean? = null, shouldDragToPitch: Boolean? = null, shouldPinchToRotateAndZoom: Boolean? = null, doubleTapShouldZoom: Boolean? = null, dragPanIsEnabled: Boolean? = null, dragRotateIsEnabled: Boolean? = null, shouldValidateStyle: Boolean? = null, minimapIsVisible: Boolean? = false, attributionControlIsVisible: Boolean? = null, geolocateControlIsVisible: Boolean? = false, navigationControlIsVisible: Boolean? = false, projectionControlIsVisible: Boolean? = false, scaleControlIsVisible: Boolean? = false, terrainControlIsVisible: Boolean? = false, space: MTSpaceOption? = null, halo: MTHaloOption? = null, isSessionLogicEnabled: Boolean = true, eventLevel: MTEventLevel = MTEventLevel.CAMERA_ONLY, highFrequencyEventThrottleMs: Int? = 20)Flexible constructor: all options optional so you can mix and match with named args.

## Properties

attributionControlIsVisible

@SerialName(value = "attributionControl")var attributionControlIsVisible: Boolean?Boolean indicating whether attribution control is added directly to the map.

bearing

var bearing: Double?The bearing of the map, measured in degrees counter-clockwise from north.

bearingSnap

var bearingSnap: Double?The threshold, measured in degrees, that determines when the map's bearing will snap to north.

bounds

var bounds: MTBounds?Geographical area that should be visible when the map initializes.

cancelPendingTileRequestsWhileZooming

var cancelPendingTileRequestsWhileZooming: Boolean?Determines whether to cancel, or retain, tiles from the current viewport which are still loading but which belong to a farther (smaller) zoom level than the current one.

center

var center: LngLat?The geographical centerpoint of the map.

crossSourceCollisionsAreEnabled

@SerialName(value = "crossSourceCollisions")var crossSourceCollisionsAreEnabled: Boolean?Boolean indicating whether cross source collisions are enabled.

doubleTapShouldZoom

@SerialName(value = "doubleClickZoom")var doubleTapShouldZoom: Boolean?Boolean indicating whether the double tap to zoom interaction is enabled.

dragPanIsEnabled

@SerialName(value = "dragPan")var dragPanIsEnabled: Boolean?Boolean indicating whether the drag to pan interaction is enabled.

dragRotateIsEnabled

@SerialName(value = "dragRotate")var dragRotateIsEnabled: Boolean?Boolean indicating whether the drag to rotate interaction is enabled.

elevation

var elevation: Double?The elevation of the geographical centerpoint of the map, in meters above sea level.

eventLevel

var eventLevel: MTEventLevelControls which map events are sent from the map object.

fadeDuration

var fadeDuration: Double?The duration of the fade-in/fade-out animation for label collisions, in milliseconds.

geolocateControlIsVisible

@SerialName(value = "geolocateControl")var geolocateControlIsVisible: Boolean?Boolean indicating whether geolocate control is added directly to the map.

halo

@SerialName(value = "halo")var halo: MTHaloOption?Halo option for the atmospheric glow. Can be a simple enable flag or a detailed config. Requires globe projection to be enabled to be visible.

highFrequencyEventThrottleMs

var highFrequencyEventThrottleMs: Int?Optional throttle in milliseconds applied to high-frequency events when eventLevel is MTEventLevel.ALL or MTEventLevel.CAMERA_ONLY. A value of 0 disables throttling.

isCenterClampedToGround

@SerialName(value = "centerClampedToGround")var isCenterClampedToGround: Boolean?Boolean indicating whether center is clamped to the ground.

isInteractionEnabled

@SerialName(value = "interactive")var isInteractionEnabled: Boolean?Boolean indicating whether interaction on the map is enabled.

isSessionLogicEnabled

var isSessionLogicEnabled: BooleanBoolean indicating whether session logic is enabled.

language

@Serializable(with = MTLanguageSerializer::class)var language: MTLanguage?The language of the map.

logoPosition

var logoPosition: MTMapCorner?A value representing the position of the MapTiler wordmark on the map.

maptilerLogoIsVisible

@SerialName(value = "maptilerLogo")var maptilerLogoIsVisible: Boolean?Boolean indicating whether MapTiler logo is visible on the map.

maxBounds

var maxBounds: MTBounds?Restricts the viewport to the provided geographical bounds.

maxPitch

var maxPitch: Double?The maximum pitch of the map (0-85).

maxTileCacheSize

var maxTileCacheSize: Double?The maximum number of tiles stored in the tile cache for a given source.

maxTileCacheZoomLevels

var maxTileCacheZoomLevels: Double?The maximum number of zoom levels for which to store tiles for a given source.

maxZoom

var maxZoom: Double?The maximum zoom level of the map (0-24).

minimapIsVisible

@SerialName(value = "minimap")var minimapIsVisible: Boolean?Boolean indicating whether minimap control is added directly to the map.

minPitch

var minPitch: Double?The minimum pitch of the map (0-85).

minZoom

var minZoom: Double?The minimum zoom level of the map (0-24).

navigationControlIsVisible

@SerialName(value = "navigationControl")var navigationControlIsVisible: Boolean?Boolean indicating whether navigation control is added directly to the map.

pitch

var pitch: Double?The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).

pixelRatio

var pixelRatio: Double?Overrides the device pixel ratio used for rendering.

projection

var projection: MTProjectionType?Projection type of the map object.

projectionControlIsVisible

@SerialName(value = "projectionControl")var projectionControlIsVisible: Boolean?Boolean indicating whether projection control is added directly to the map.

roll

var roll: Double?The roll angle of the map, measured in degrees counter-clockwise about the camera boresight.

rollIsEnabled

@SerialName(value = "rollEnabled")var rollIsEnabled: Boolean?Boolean indicating whether the map's roll control with "drag to rotate" interaction is enabled.

scaleControlIsVisible

@SerialName(value = "scaleControl")var scaleControlIsVisible: Boolean?Boolean indicating whether scale control is added directly to the map.

shouldCollectResourceTiming

@SerialName(value = "collectResourceTiming")var shouldCollectResourceTiming: Boolean?Boolean indicating whether Resource Timing API information will be collected.

shouldDragToPitch

@SerialName(value = "touchPitch")var shouldDragToPitch: Boolean?Boolean indicating whether the drag to pitch interaction is enabled.

shouldPinchToRotateAndZoom

@SerialName(value = "touchZoomRotate")var shouldPinchToRotateAndZoom: Boolean?Boolean indicating whether the pinch to rotate and zoom interaction is enabled.

shouldPitchWithRotate

@SerialName(value = "pitchWithRotate")var shouldPitchWithRotate: Boolean?Boolean indicating whether the map's pitch control with drag to rotate interaction will be disabled.

shouldRefreshExpiredTiles

@SerialName(value = "refreshExpiredTiles")var shouldRefreshExpiredTiles: Boolean?Boolean indicating whether the map won't attempt to re-request tiles once they expire.

shouldRenderWorldCopies

@SerialName(value = "renderWorldCopies")var shouldRenderWorldCopies: Boolean?Boolean indicating whether multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.

shouldValidateStyle

var shouldValidateStyle: Boolean?Boolean indicating whether style should be validated.

space

@SerialName(value = "space")var space: MTSpaceOption?Space option for the globe background. Can be a simple enable flag or a detailed config. Requires globe projection to be enabled to be visible.

terrainControlIsVisible

@SerialName(value = "terrainControl")var terrainControlIsVisible: Boolean?Boolean indicating whether terrain control is added directly to the map.

terrainExaggeration

var terrainExaggeration: Double?3D terrain exaggeration factor.

terrainIsEnabled

@SerialName(value = "terrain")var terrainIsEnabled: Boolean?Boolean indicating whether 3D terrain is enabled.

zoom

var zoom: Double?The zoom level of the map.

## Functions

enableHalo

fun enableHalo()Enables halo with default gradient.

setHalo

fun setHalo(halo: MTHalo)Sets halo configuration.

setMapTilerLogoIsVisible

fun setMapTilerLogoIsVisible(isVisible: Boolean)

withBalancedPerformanceDefaults

fun MTMapOptions.withBalancedPerformanceDefaults(): MTMapOptionsReturns a new MTMapOptions with balanced performance defaults applied over this instance.

withHighFidelityDefaults

fun MTMapOptions.withHighFidelityDefaults(): MTMapOptionsReturns a new MTMapOptions with high-fidelity defaults applied over this instance.

withLeanPerformanceDefaults

fun MTMapOptions.withLeanPerformanceDefaults(): MTMapOptionsApplies the lean performance preset over this instance, returning a new options object.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/is-center-clamped-to-ground.html

---
layout: mobile_sdk
title: "isCenterClampedToGround"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isCenterClampedToGround"
id: is-center-clamped-to-ground
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# isCenterClampedToGround

@SerialName(value = "centerClampedToGround")var isCenterClampedToGround: Boolean?Boolean indicating whether center is clamped to the ground.If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if terrain is not enabled). If false, the elevation of the center point will default to sea level and will not automatically update. Needs to be set to false to keep the camera above ground when pitch 90 degrees.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/is-interaction-enabled.html

---
layout: mobile_sdk
title: "isInteractionEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isInteractionEnabled"
id: is-interaction-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# isInteractionEnabled

@SerialName(value = "interactive")var isInteractionEnabled: Boolean?Boolean indicating whether interaction on the map is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/is-session-logic-enabled.html

---
layout: mobile_sdk
title: "isSessionLogicEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isSessionLogicEnabled"
id: is-session-logic-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# isSessionLogicEnabled

var isSessionLogicEnabled: BooleanBoolean indicating whether session logic is enabled.This allows MapTiler to enable session-based billing. Defaults to true.
#### See also

https://docs.maptiler.com/guides/maps-apis/maps-platform/what-is-map-session-in-maptiler-cloud/

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/language.html

---
layout: mobile_sdk
title: "language"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "language"
id: language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# language

@Serializable(with = MTLanguageSerializer::class)var language: MTLanguage?The language of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/logo-position.html

---
layout: mobile_sdk
title: "logoPosition"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "logoPosition"
id: logo-position
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# logoPosition

var logoPosition: MTMapCorner?A value representing the position of the MapTiler wordmark on the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/maptiler-logo-is-visible.html

---
layout: mobile_sdk
title: "maptilerLogoIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maptilerLogoIsVisible"
id: maptiler-logo-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maptilerLogoIsVisible

@SerialName(value = "maptilerLogo")var maptilerLogoIsVisible: Boolean?Boolean indicating whether MapTiler logo is visible on the map.If true, the MapTiler logo will be shown. False will only work on premium accounts.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/max-bounds.html

---
layout: mobile_sdk
title: "maxBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxBounds"
id: max-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maxBounds

var maxBounds: MTBounds?Restricts the viewport to the provided geographical bounds.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/max-pitch.html

---
layout: mobile_sdk
title: "maxPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxPitch"
id: max-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maxPitch

var maxPitch: Double?The maximum pitch of the map (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/max-tile-cache-size.html

---
layout: mobile_sdk
title: "maxTileCacheSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxTileCacheSize"
id: max-tile-cache-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maxTileCacheSize

var maxTileCacheSize: Double?The maximum number of tiles stored in the tile cache for a given source.If omitted, the cache will be dynamically sized based on the current viewport.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/max-tile-cache-zoom-levels.html

---
layout: mobile_sdk
title: "maxTileCacheZoomLevels"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxTileCacheZoomLevels"
id: max-tile-cache-zoom-levels
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maxTileCacheZoomLevels

var maxTileCacheZoomLevels: Double?The maximum number of zoom levels for which to store tiles for a given source.Tile cache dynamic size is calculated by multiplying maxTileCacheZoomLevels with the approximate number of tiles in the viewport for a given source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/max-zoom.html

---
layout: mobile_sdk
title: "maxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "maxZoom"
id: max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# maxZoom

var maxZoom: Double?The maximum zoom level of the map (0-24).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/min-pitch.html

---
layout: mobile_sdk
title: "minPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minPitch"
id: min-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# minPitch

var minPitch: Double?The minimum pitch of the map (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/min-zoom.html

---
layout: mobile_sdk
title: "minZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minZoom"
id: min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# minZoom

var minZoom: Double?The minimum zoom level of the map (0-24).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/minimap-is-visible.html

---
layout: mobile_sdk
title: "minimapIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "minimapIsVisible"
id: minimap-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# minimapIsVisible

@SerialName(value = "minimap")var minimapIsVisible: Boolean?Boolean indicating whether minimap control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/navigation-control-is-visible.html

---
layout: mobile_sdk
title: "navigationControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "navigationControlIsVisible"
id: navigation-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# navigationControlIsVisible

@SerialName(value = "navigationControl")var navigationControlIsVisible: Boolean?Boolean indicating whether navigation control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/pitch.html

---
layout: mobile_sdk
title: "pitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pitch"
id: pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# pitch

var pitch: Double?The pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).If pitch is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to 0.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/pixel-ratio.html

---
layout: mobile_sdk
title: "pixelRatio"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "pixelRatio"
id: pixel-ratio
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# pixelRatio

var pixelRatio: Double?Overrides the device pixel ratio used for rendering.Set this to values greater than `1.0` to force high-DPI rendering on low-density devices, or lower values to favour performance over sharpness.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/projection-control-is-visible.html

---
layout: mobile_sdk
title: "projectionControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "projectionControlIsVisible"
id: projection-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# projectionControlIsVisible

@SerialName(value = "projectionControl")var projectionControlIsVisible: Boolean?Boolean indicating whether projection control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/projection.html

---
layout: mobile_sdk
title: "projection"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "projection"
id: projection
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# projection

var projection: MTProjectionType?Projection type of the map object.This will overwrite the projection property from the style (if any).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/roll-is-enabled.html

---
layout: mobile_sdk
title: "rollIsEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "rollIsEnabled"
id: roll-is-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# rollIsEnabled

@SerialName(value = "rollEnabled")var rollIsEnabled: Boolean?Boolean indicating whether the map's roll control with "drag to rotate" interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/roll.html

---
layout: mobile_sdk
title: "roll"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "roll"
id: roll
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# roll

var roll: Double?The roll angle of the map, measured in degrees counter-clockwise about the camera boresight.If roll is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to 0.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/scale-control-is-visible.html

---
layout: mobile_sdk
title: "scaleControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "scaleControlIsVisible"
id: scale-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# scaleControlIsVisible

@SerialName(value = "scaleControl")var scaleControlIsVisible: Boolean?Boolean indicating whether scale control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/set-halo.html

---
layout: mobile_sdk
title: "setHalo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setHalo"
id: set-halo
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# setHalo

fun setHalo(halo: MTHalo)Sets halo configuration.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/set-map-tiler-logo-is-visible.html

---
layout: mobile_sdk
title: "setMapTilerLogoIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMapTilerLogoIsVisible"
id: set-map-tiler-logo-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# setMapTilerLogoIsVisible

fun setMapTilerLogoIsVisible(isVisible: Boolean)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-collect-resource-timing.html

---
layout: mobile_sdk
title: "shouldCollectResourceTiming"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldCollectResourceTiming"
id: should-collect-resource-timing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldCollectResourceTiming

@SerialName(value = "collectResourceTiming")var shouldCollectResourceTiming: Boolean?Boolean indicating whether Resource Timing API information will be collected.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-drag-to-pitch.html

---
layout: mobile_sdk
title: "shouldDragToPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldDragToPitch"
id: should-drag-to-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldDragToPitch

@SerialName(value = "touchPitch")var shouldDragToPitch: Boolean?Boolean indicating whether the drag to pitch interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-pinch-to-rotate-and-zoom.html

---
layout: mobile_sdk
title: "shouldPinchToRotateAndZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldPinchToRotateAndZoom"
id: should-pinch-to-rotate-and-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldPinchToRotateAndZoom

@SerialName(value = "touchZoomRotate")var shouldPinchToRotateAndZoom: Boolean?Boolean indicating whether the pinch to rotate and zoom interaction is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-pitch-with-rotate.html

---
layout: mobile_sdk
title: "shouldPitchWithRotate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldPitchWithRotate"
id: should-pitch-with-rotate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldPitchWithRotate

@SerialName(value = "pitchWithRotate")var shouldPitchWithRotate: Boolean?Boolean indicating whether the map's pitch control with drag to rotate interaction will be disabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-refresh-expired-tiles.html

---
layout: mobile_sdk
title: "shouldRefreshExpiredTiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldRefreshExpiredTiles"
id: should-refresh-expired-tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldRefreshExpiredTiles

@SerialName(value = "refreshExpiredTiles")var shouldRefreshExpiredTiles: Boolean?Boolean indicating whether the map won't attempt to re-request tiles once they expire.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-render-world-copies.html

---
layout: mobile_sdk
title: "shouldRenderWorldCopies"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldRenderWorldCopies"
id: should-render-world-copies
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldRenderWorldCopies

@SerialName(value = "renderWorldCopies")var shouldRenderWorldCopies: Boolean?Boolean indicating whether multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/should-validate-style.html

---
layout: mobile_sdk
title: "shouldValidateStyle"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "shouldValidateStyle"
id: should-validate-style
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# shouldValidateStyle

var shouldValidateStyle: Boolean?Boolean indicating whether style should be validated.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/space.html

---
layout: mobile_sdk
title: "space"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "space"
id: space
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# space

@SerialName(value = "space")var space: MTSpaceOption?Space option for the globe background. Can be a simple enable flag or a detailed config. Requires globe projection to be enabled to be visible.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/terrain-control-is-visible.html

---
layout: mobile_sdk
title: "terrainControlIsVisible"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "terrainControlIsVisible"
id: terrain-control-is-visible
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# terrainControlIsVisible

@SerialName(value = "terrainControl")var terrainControlIsVisible: Boolean?Boolean indicating whether terrain control is added directly to the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/terrain-exaggeration.html

---
layout: mobile_sdk
title: "terrainExaggeration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "terrainExaggeration"
id: terrain-exaggeration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# terrainExaggeration

var terrainExaggeration: Double?3D terrain exaggeration factor.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/terrain-is-enabled.html

---
layout: mobile_sdk
title: "terrainIsEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "terrainIsEnabled"
id: terrain-is-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# terrainIsEnabled

@SerialName(value = "terrain")var terrainIsEnabled: Boolean?Boolean indicating whether 3D terrain is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options/zoom.html

---
layout: mobile_sdk
title: "zoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoom"
id: zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-options"
---
# zoom

var zoom: Double?The zoom level of the map.If zoom is not specified, SDK will look for it in the map style object. If it is not specified in the style, it will default to 0.0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic/-m-t-map-view-classic.html

---
layout: mobile_sdk
title: "MTMapViewClassic"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewClassic"
id: -m-t-map-view-classic
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic"
---
# MTMapViewClassic

constructor(context: Context, attrs: AttributeSet)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic/index.html

---
layout: mobile_sdk
title: "MTMapViewClassic"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewClassic"
id: -m-t-map-view-classic
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic"
---
# MTMapViewClassic

class MTMapViewClassic(context: Context, attrs: AttributeSet) : FrameLayoutObject representing the map on the screen. Used with XML.For Compose use MTMapView.

Members

## Constructors

MTMapViewClassic

constructor(context: Context, attrs: AttributeSet)

## Properties

scope

val scope: CoroutineScope

## Functions

addChildrenForAccessibility

open override fun addChildrenForAccessibility(p0: ArrayList<View>)

addExtraDataToAccessibilityNodeInfo

open override fun addExtraDataToAccessibilityNodeInfo(p0: AccessibilityNodeInfo, p1: String, p2: Bundle?)

addFocusables

open fun addFocusables(p0: ArrayList<View>, p1: Int)open override fun addFocusables(p0: ArrayList<View>, p1: Int, p2: Int)

addKeyboardNavigationClusters

open override fun addKeyboardNavigationClusters(p0: MutableCollection<View>, p1: Int)

addOnAttachStateChangeListener

open fun addOnAttachStateChangeListener(p0: View.OnAttachStateChangeListener)

addOnLayoutChangeListener

open fun addOnLayoutChangeListener(p0: View.OnLayoutChangeListener)

addOnUnhandledKeyEventListener

open fun addOnUnhandledKeyEventListener(p0: View.OnUnhandledKeyEventListener)

addStatesFromChildren

open fun addStatesFromChildren(): Boolean

addTouchables

open override fun addTouchables(p0: ArrayList<View>)

addView

open fun addView(p0: View)open override fun addView(p0: View, p1: ViewGroup.LayoutParams)open fun addView(p0: View, p1: Int)open fun addView(p0: View, p1: Int, p2: ViewGroup.LayoutParams)open fun addView(p0: View, p1: Int, p2: Int)

animate

open fun animate(): ViewPropertyAnimator

announceForAccessibility

open fun announceForAccessibility(p0: CharSequence)

autofill

open fun autofill(p0: SparseArray<AutofillValue>)open fun autofill(p0: AutofillValue)

bringChildToFront

open override fun bringChildToFront(p0: View)

bringToFront

open fun bringToFront()

buildDrawingCache

open fun buildDrawingCache()open fun buildDrawingCache(p0: Boolean)

buildLayer

open fun buildLayer()

callOnClick

open fun callOnClick(): Boolean

cancelDragAndDrop

fun cancelDragAndDrop()

cancelLongPress

open fun cancelLongPress()

cancelPendingInputEvents

fun cancelPendingInputEvents()

canResolveLayoutDirection

open fun canResolveLayoutDirection(): Boolean

canResolveTextAlignment

open fun canResolveTextAlignment(): Boolean

canResolveTextDirection

open fun canResolveTextDirection(): Boolean

canScrollHorizontally

open fun canScrollHorizontally(p0: Int): Boolean

canScrollVertically

open fun canScrollVertically(p0: Int): Boolean

checkInputConnectionProxy

open fun checkInputConnectionProxy(p0: View): Boolean

childDrawableStateChanged

open override fun childDrawableStateChanged(p0: View)

childHasTransientStateChanged

open override fun childHasTransientStateChanged(p0: View, p1: Boolean)

clearAnimation

open fun clearAnimation()

clearChildFocus

open override fun clearChildFocus(p0: View)

clearDisappearingChildren

open fun clearDisappearingChildren()

clearFocus

open override fun clearFocus()

clearPendingCredentialRequest

open fun clearPendingCredentialRequest()

clearViewTranslationCallback

open fun clearViewTranslationCallback()

computeScroll

open fun computeScroll()

computeSystemWindowInsets

open fun computeSystemWindowInsets(p0: WindowInsets, p1: Rect): WindowInsets

createAccessibilityNodeInfo

open fun createAccessibilityNodeInfo(): AccessibilityNodeInfo

createContextMenu

open fun createContextMenu(p0: ContextMenu)

destroyDrawingCache

open fun destroyDrawingCache()

dispatchApplyWindowInsets

open override fun dispatchApplyWindowInsets(p0: WindowInsets): WindowInsets

dispatchCapturedPointerEvent

open override fun dispatchCapturedPointerEvent(p0: MotionEvent): Boolean

dispatchConfigurationChanged

open override fun dispatchConfigurationChanged(p0: Configuration)

dispatchCreateViewTranslationRequest

open override fun dispatchCreateViewTranslationRequest(p0: MutableMap<AutofillId, LongArray>, p1: IntArray, p2: TranslationCapability, p3: MutableList<ViewTranslationRequest>)

dispatchDisplayHint

open override fun dispatchDisplayHint(p0: Int)

dispatchDragEvent

open override fun dispatchDragEvent(p0: DragEvent): Boolean

dispatchDrawableHotspotChanged

open override fun dispatchDrawableHotspotChanged(p0: Float, p1: Float)

dispatchFinishTemporaryDetach

open override fun dispatchFinishTemporaryDetach()

dispatchGenericMotionEvent

open fun dispatchGenericMotionEvent(p0: MotionEvent): Boolean

dispatchKeyEvent

open override fun dispatchKeyEvent(p0: KeyEvent): Boolean

dispatchKeyEventPreIme

open override fun dispatchKeyEventPreIme(p0: KeyEvent): Boolean

dispatchKeyShortcutEvent

open override fun dispatchKeyShortcutEvent(p0: KeyEvent): Boolean

dispatchNestedFling

open fun dispatchNestedFling(p0: Float, p1: Float, p2: Boolean): Boolean

dispatchNestedPreFling

open fun dispatchNestedPreFling(p0: Float, p1: Float): Boolean

dispatchNestedPrePerformAccessibilityAction

open fun dispatchNestedPrePerformAccessibilityAction(p0: Int, p1: Bundle?): Boolean

dispatchNestedPreScroll

open fun dispatchNestedPreScroll(p0: Int, p1: Int, p2: IntArray?, p3: IntArray?): Boolean

dispatchNestedScroll

open fun dispatchNestedScroll(p0: Int, p1: Int, p2: Int, p3: Int, p4: IntArray?): Boolean

dispatchPointerCaptureChanged

open override fun dispatchPointerCaptureChanged(p0: Boolean)

dispatchPopulateAccessibilityEvent

open fun dispatchPopulateAccessibilityEvent(p0: AccessibilityEvent): Boolean

dispatchProvideAutofillStructure

open override fun dispatchProvideAutofillStructure(p0: ViewStructure, p1: Int)

dispatchProvideStructure

open override fun dispatchProvideStructure(p0: ViewStructure)

dispatchScrollCaptureSearch

open override fun dispatchScrollCaptureSearch(p0: Rect, p1: Point, p2: Consumer<ScrollCaptureTarget>)

dispatchSetActivated

open override fun dispatchSetActivated(p0: Boolean)

dispatchSetSelected

open override fun dispatchSetSelected(p0: Boolean)

dispatchStartTemporaryDetach

open override fun dispatchStartTemporaryDetach()

dispatchSystemUiVisibilityChanged

open override fun dispatchSystemUiVisibilityChanged(p0: Int)

dispatchTouchEvent

open override fun dispatchTouchEvent(p0: MotionEvent): Boolean

dispatchTrackballEvent

open override fun dispatchTrackballEvent(p0: MotionEvent): Boolean

dispatchUnhandledMove

open override fun dispatchUnhandledMove(p0: View, p1: Int): Boolean

dispatchWindowFocusChanged

open override fun dispatchWindowFocusChanged(p0: Boolean)

dispatchWindowInsetsAnimationEnd

open override fun dispatchWindowInsetsAnimationEnd(p0: WindowInsetsAnimation)

dispatchWindowInsetsAnimationPrepare

open override fun dispatchWindowInsetsAnimationPrepare(p0: WindowInsetsAnimation)

dispatchWindowInsetsAnimationProgress

open override fun dispatchWindowInsetsAnimationProgress(p0: WindowInsets, p1: MutableList<WindowInsetsAnimation>): WindowInsets

dispatchWindowInsetsAnimationStart

open override fun dispatchWindowInsetsAnimationStart(p0: WindowInsetsAnimation, p1: WindowInsetsAnimation.Bounds): WindowInsetsAnimation.Bounds

dispatchWindowSystemUiVisiblityChanged

open override fun dispatchWindowSystemUiVisiblityChanged(p0: Int)

dispatchWindowVisibilityChanged

open override fun dispatchWindowVisibilityChanged(p0: Int)

draw

open fun draw(p0: Canvas)

drawableHotspotChanged

open fun drawableHotspotChanged(p0: Float, p1: Float)

endViewTransition

open fun endViewTransition(p0: View)

findFocus

open override fun findFocus(): View

findOnBackInvokedDispatcher

fun findOnBackInvokedDispatcher(): OnBackInvokedDispatcher?

findOnBackInvokedDispatcherForChild

open override fun findOnBackInvokedDispatcherForChild(p0: View, p1: View): OnBackInvokedDispatcher?

findViewById

fun <T : View> findViewById(p0: Int): T

findViewsWithText

open override fun findViewsWithText(p0: ArrayList<View>, p1: CharSequence, p2: Int)

findViewWithTag

fun <T : View> findViewWithTag(p0: Any): T

focusableViewAvailable

open override fun focusableViewAvailable(p0: View)

focusSearch

open fun focusSearch(p0: Int): Viewopen override fun focusSearch(p0: View, p1: Int): View

forceHasOverlappingRendering

open fun forceHasOverlappingRendering(p0: Boolean)

forceLayout

open fun forceLayout()

gatherTransparentRegion

open override fun gatherTransparentRegion(p0: Region?): Boolean

generateDisplayHash

open fun generateDisplayHash(p0: String, p1: Rect?, p2: Executor, p3: DisplayHashResultCallback)

generateLayoutParams

open override fun generateLayoutParams(p0: AttributeSet): FrameLayout.LayoutParams

getAccessibilityClassName

open override fun getAccessibilityClassName(): CharSequence

getAccessibilityDelegate

open fun getAccessibilityDelegate(): View.AccessibilityDelegate

getAccessibilityLiveRegion

open fun getAccessibilityLiveRegion(): Int

getAccessibilityNodeProvider

open fun getAccessibilityNodeProvider(): AccessibilityNodeProvider

getAccessibilityPaneTitle

open fun getAccessibilityPaneTitle(): CharSequence?

getAccessibilityTraversalAfter

open fun getAccessibilityTraversalAfter(): Int

getAccessibilityTraversalBefore

open fun getAccessibilityTraversalBefore(): Int

getAllowedHandwritingDelegatePackageName

open fun getAllowedHandwritingDelegatePackageName(): String?

getAllowedHandwritingDelegatorPackageName

open fun getAllowedHandwritingDelegatorPackageName(): String?

getAlpha

open fun getAlpha(): Float

getAnimation

open fun getAnimation(): Animation

getAnimationMatrix

open fun getAnimationMatrix(): Matrix?

getApplicationWindowToken

open fun getApplicationWindowToken(): IBinder

getAttributeResolutionStack

open fun getAttributeResolutionStack(p0: Int): IntArray

getAttributeSourceResourceMap

open fun getAttributeSourceResourceMap(): MutableMap<Int, Int>

getAutofillHints

open fun getAutofillHints(): Array<String>?

getAutofillId

fun getAutofillId(): AutofillId

getAutofillType

open fun getAutofillType(): Int

getAutofillValue

open fun getAutofillValue(): AutofillValue?

getBackground

open fun getBackground(): Drawable

getBackgroundTintBlendMode

open fun getBackgroundTintBlendMode(): BlendMode?

getBackgroundTintList

open fun getBackgroundTintList(): ColorStateList?

getBackgroundTintMode

open fun getBackgroundTintMode(): PorterDuff.Mode?

getBaseline

open fun getBaseline(): Int

getBottom

fun getBottom(): Int

getCameraDistance

open fun getCameraDistance(): Float

getChildAt

open fun getChildAt(p0: Int): View

getChildCount

open fun getChildCount(): Int

getChildDrawingOrder

fun getChildDrawingOrder(p0: Int): Int

getChildVisibleRect

open override fun getChildVisibleRect(p0: View, p1: Rect, p2: Point): Boolean

getClipBounds

open fun getClipBounds(): Rectopen fun getClipBounds(p0: Rect): Boolean

getClipChildren

open fun getClipChildren(): Boolean

getClipToOutline

fun getClipToOutline(): Boolean

getClipToPadding

open fun getClipToPadding(): Boolean

getConsiderGoneChildrenWhenMeasuring

open fun getConsiderGoneChildrenWhenMeasuring(): Boolean

getContentCaptureSession

fun getContentCaptureSession(): ContentCaptureSession?

getContentDescription

open fun getContentDescription(): CharSequence

getContentSensitivity

fun getContentSensitivity(): Int

getContext

fun getContext(): Context

getDefaultFocusHighlightEnabled

fun getDefaultFocusHighlightEnabled(): Boolean

getDescendantFocusability

open fun getDescendantFocusability(): Int

getDisplay

open fun getDisplay(): Display

getDrawableState

fun getDrawableState(): IntArray

getDrawingCache

open fun getDrawingCache(): Bitmapopen fun getDrawingCache(p0: Boolean): Bitmap

getDrawingCacheBackgroundColor

open fun getDrawingCacheBackgroundColor(): Int

getDrawingCacheQuality

open fun getDrawingCacheQuality(): Int

getDrawingRect

open fun getDrawingRect(p0: Rect)

getDrawingTime

open fun getDrawingTime(): Long

getElevation

open fun getElevation(): Float

getExplicitStyle

open fun getExplicitStyle(): Int

getFilterTouchesWhenObscured

open fun getFilterTouchesWhenObscured(): Boolean

getFitsSystemWindows

open fun getFitsSystemWindows(): Boolean

getFocusable

open fun getFocusable(): Int

getFocusables

open fun getFocusables(p0: Int): ArrayList<View>

getFocusedChild

open fun getFocusedChild(): View

getFocusedRect

open fun getFocusedRect(p0: Rect)

getForeground

open fun getForeground(): Drawable

getForegroundGravity

open fun getForegroundGravity(): Int

getForegroundTintBlendMode

open fun getForegroundTintBlendMode(): BlendMode?

getForegroundTintList

open fun getForegroundTintList(): ColorStateList?

getForegroundTintMode

open fun getForegroundTintMode(): PorterDuff.Mode?

getFrameContentVelocity

open fun getFrameContentVelocity(): Float

getGlobalVisibleRect

fun getGlobalVisibleRect(p0: Rect): Booleanopen fun getGlobalVisibleRect(p0: Rect, p1: Point): Boolean

getHandler

open fun getHandler(): Handler

getHandwritingBoundsOffsetBottom

open fun getHandwritingBoundsOffsetBottom(): Float

getHandwritingBoundsOffsetLeft

open fun getHandwritingBoundsOffsetLeft(): Float

getHandwritingBoundsOffsetRight

open fun getHandwritingBoundsOffsetRight(): Float

getHandwritingBoundsOffsetTop

open fun getHandwritingBoundsOffsetTop(): Float

getHandwritingDelegateFlags

open fun getHandwritingDelegateFlags(): Int

getHandwritingDelegatorCallback

open fun getHandwritingDelegatorCallback(): Runnable?

getHasOverlappingRendering

fun getHasOverlappingRendering(): Boolean

getHeight

fun getHeight(): Int

getHitRect

open fun getHitRect(p0: Rect)

getHorizontalFadingEdgeLength

open fun getHorizontalFadingEdgeLength(): Int

getHorizontalScrollbarThumbDrawable

open fun getHorizontalScrollbarThumbDrawable(): Drawable?

getHorizontalScrollbarTrackDrawable

open fun getHorizontalScrollbarTrackDrawable(): Drawable?

getId

open fun getId(): Int

getImportantForAccessibility

open fun getImportantForAccessibility(): Int

getImportantForAutofill

open fun getImportantForAutofill(): Int

getImportantForContentCapture

open fun getImportantForContentCapture(): Int

getKeepScreenOn

open fun getKeepScreenOn(): Boolean

getKeyDispatcherState

open fun getKeyDispatcherState(): KeyEvent.DispatcherState

getLabelFor

open fun getLabelFor(): Int

getLayerType

open fun getLayerType(): Int

getLayoutAnimation

open fun getLayoutAnimation(): LayoutAnimationController

getLayoutAnimationListener

open fun getLayoutAnimationListener(): Animation.AnimationListener

getLayoutDirection

open fun getLayoutDirection(): Int

getLayoutMode

open fun getLayoutMode(): Int

getLayoutParams

open fun getLayoutParams(): ViewGroup.LayoutParams

getLayoutTransition

open fun getLayoutTransition(): LayoutTransition

getLeft

fun getLeft(): Int

getLocalVisibleRect

fun getLocalVisibleRect(p0: Rect): Boolean

getLocationInSurface

open fun getLocationInSurface(p0: IntArray)

getLocationInWindow

open fun getLocationInWindow(p0: IntArray)

getLocationOnScreen

open fun getLocationOnScreen(p0: IntArray)

getMatrix

open fun getMatrix(): Matrix

getMeasureAllChildren

open fun getMeasureAllChildren(): Boolean

getMeasuredHeight

fun getMeasuredHeight(): Int

getMeasuredHeightAndState

fun getMeasuredHeightAndState(): Int

getMeasuredState

fun getMeasuredState(): Int

getMeasuredWidth

fun getMeasuredWidth(): Int

getMeasuredWidthAndState

fun getMeasuredWidthAndState(): Int

getMinimumHeight

open fun getMinimumHeight(): Int

getMinimumWidth

open fun getMinimumWidth(): Int

getNestedScrollAxes

open fun getNestedScrollAxes(): Int

getNextClusterForwardId

open fun getNextClusterForwardId(): Int

getNextFocusDownId

open fun getNextFocusDownId(): Int

getNextFocusForwardId

open fun getNextFocusForwardId(): Int

getNextFocusLeftId

open fun getNextFocusLeftId(): Int

getNextFocusRightId

open fun getNextFocusRightId(): Int

getNextFocusUpId

open fun getNextFocusUpId(): Int

getOnFocusChangeListener

open fun getOnFocusChangeListener(): View.OnFocusChangeListener

getOutlineAmbientShadowColor

open fun getOutlineAmbientShadowColor(): Int

getOutlineProvider

open fun getOutlineProvider(): ViewOutlineProvider

getOutlineSpotShadowColor

open fun getOutlineSpotShadowColor(): Int

getOverlay

open override fun getOverlay(): ViewGroupOverlay

getOverScrollMode

open fun getOverScrollMode(): Int

getPaddingBottom

open fun getPaddingBottom(): Int

getPaddingEnd

open fun getPaddingEnd(): Int

getPaddingLeft

open fun getPaddingLeft(): Int

getPaddingRight

open fun getPaddingRight(): Int

getPaddingStart

open fun getPaddingStart(): Int

getPaddingTop

open fun getPaddingTop(): Int

getParent

fun getParent(): ViewParent

getParentForAccessibility

open fun getParentForAccessibility(): ViewParent

getPendingCredentialCallback

fun getPendingCredentialCallback(): OutcomeReceiver<GetCredentialResponse, GetCredentialException>?

getPendingCredentialRequest

fun getPendingCredentialRequest(): GetCredentialRequest?

getPersistentDrawingCache

open fun getPersistentDrawingCache(): Int

getPivotX

open fun getPivotX(): Float

getPivotY

open fun getPivotY(): Float

getPointerIcon

open fun getPointerIcon(): PointerIcon

getPreferKeepClearRects

fun getPreferKeepClearRects(): MutableList<Rect>

getReceiveContentMimeTypes

open fun getReceiveContentMimeTypes(): Array<String>?

getRequestedFrameRate

open fun getRequestedFrameRate(): Float

getResources

open fun getResources(): Resources

getRevealOnFocusHint

fun getRevealOnFocusHint(): Boolean

getRight

fun getRight(): Int

getRootSurfaceControl

open fun getRootSurfaceControl(): AttachedSurfaceControl?

getRootView

open fun getRootView(): View

getRootWindowInsets

open fun getRootWindowInsets(): WindowInsets

getRotation

open fun getRotation(): Float

getRotationX

open fun getRotationX(): Float

getRotationY

open fun getRotationY(): Float

getScaleX

open fun getScaleX(): Float

getScaleY

open fun getScaleY(): Float

getScrollBarDefaultDelayBeforeFade

open fun getScrollBarDefaultDelayBeforeFade(): Int

getScrollBarFadeDuration

open fun getScrollBarFadeDuration(): Int

getScrollBarSize

open fun getScrollBarSize(): Int

getScrollBarStyle

open fun getScrollBarStyle(): Int

getScrollCaptureHint

open fun getScrollCaptureHint(): Int

getScrollIndicators

open fun getScrollIndicators(): Int

getScrollX

fun getScrollX(): Int

getScrollY

fun getScrollY(): Int

getSolidColor

open fun getSolidColor(): Int

getSourceLayoutResId

open fun getSourceLayoutResId(): Int

getStateDescription

fun getStateDescription(): CharSequence?

getStateListAnimator

open fun getStateListAnimator(): StateListAnimator

getSystemGestureExclusionRects

open fun getSystemGestureExclusionRects(): MutableList<Rect>

getSystemUiVisibility

open fun getSystemUiVisibility(): Int

getTag

open fun getTag(): Anyopen fun getTag(p0: Int): Any

getTextAlignment

open fun getTextAlignment(): Int

getTextDirection

open fun getTextDirection(): Int

getTooltipText

open fun getTooltipText(): CharSequence?

getTop

fun getTop(): Int

getTouchables

open fun getTouchables(): ArrayList<View>

getTouchDelegate

open fun getTouchDelegate(): TouchDelegate

getTouchscreenBlocksFocus

open fun getTouchscreenBlocksFocus(): Boolean

getTransitionAlpha

open fun getTransitionAlpha(): Float

getTransitionName

open fun getTransitionName(): String

getTranslationX

open fun getTranslationX(): Float

getTranslationY

open fun getTranslationY(): Float

getTranslationZ

open fun getTranslationZ(): Float

getUniqueDrawingId

open fun getUniqueDrawingId(): Long

getVerticalFadingEdgeLength

open fun getVerticalFadingEdgeLength(): Int

getVerticalScrollbarPosition

open fun getVerticalScrollbarPosition(): Int

getVerticalScrollbarThumbDrawable

open fun getVerticalScrollbarThumbDrawable(): Drawable?

getVerticalScrollbarTrackDrawable

open fun getVerticalScrollbarTrackDrawable(): Drawable?

getVerticalScrollbarWidth

open fun getVerticalScrollbarWidth(): Int

getViewTranslationResponse

open fun getViewTranslationResponse(): ViewTranslationResponse?

getViewTreeObserver

open fun getViewTreeObserver(): ViewTreeObserver

getVisibility

open fun getVisibility(): Int

getWidth

fun getWidth(): Int

getWindowId

open fun getWindowId(): WindowId

getWindowInsetsController

open fun getWindowInsetsController(): WindowInsetsController?

getWindowSystemUiVisibility

open fun getWindowSystemUiVisibility(): Int

getWindowToken

open fun getWindowToken(): IBinder

getWindowVisibility

open fun getWindowVisibility(): Int

getWindowVisibleDisplayFrame

open fun getWindowVisibleDisplayFrame(p0: Rect)

getX

open fun getX(): Float

getY

open fun getY(): Float

getZ

open fun getZ(): Float

hasExplicitFocusable

open fun hasExplicitFocusable(): Boolean

hasFocus

open override fun hasFocus(): Boolean

hasFocusable

open fun hasFocusable(): Boolean

hasNestedScrollingParent

open fun hasNestedScrollingParent(): Boolean

hasOnClickListeners

open fun hasOnClickListeners(): Boolean

hasOnLongClickListeners

open fun hasOnLongClickListeners(): Boolean

hasOverlappingRendering

open fun hasOverlappingRendering(): Boolean

hasPointerCapture

open fun hasPointerCapture(): Boolean

hasTransientState

open override fun hasTransientState(): Boolean

hasWindowFocus

open fun hasWindowFocus(): Boolean

indexOfChild

open fun indexOfChild(p0: View): Int

initialize

fun initialize(referenceStyle: MTMapReferenceStyle, options: MTMapOptions, controller: MTMapViewController, styleVariant: MTMapStyleVariant? = null)

invalidate

open fun invalidate()open fun invalidate(p0: Rect)open fun invalidate(p0: Int, p1: Int, p2: Int, p3: Int)

invalidateChild

override fun invalidateChild(p0: View, p1: Rect)

invalidateChildInParent

open override fun invalidateChildInParent(p0: IntArray, p1: Rect): ViewParent

invalidateDrawable

open override fun invalidateDrawable(p0: Drawable)

invalidateOutline

open fun invalidateOutline()

isAccessibilityDataSensitive

open fun isAccessibilityDataSensitive(): Boolean

isAccessibilityFocused

open fun isAccessibilityFocused(): Boolean

isAccessibilityHeading

open fun isAccessibilityHeading(): Boolean

isActivated

open fun isActivated(): Boolean

isAlwaysDrawnWithCacheEnabled

open fun isAlwaysDrawnWithCacheEnabled(): Boolean

isAnimationCacheEnabled

open fun isAnimationCacheEnabled(): Boolean

isAttachedToWindow

open fun isAttachedToWindow(): Boolean

isAutoHandwritingEnabled

open fun isAutoHandwritingEnabled(): Boolean

isClickable

open fun isClickable(): Boolean

isContentSensitive

fun isContentSensitive(): Boolean

isContextClickable

open fun isContextClickable(): Boolean

isCredential

open fun isCredential(): Boolean

isDirty

open fun isDirty(): Boolean

isDrawingCacheEnabled

open fun isDrawingCacheEnabled(): Boolean

isDuplicateParentStateEnabled

open fun isDuplicateParentStateEnabled(): Boolean

isEnabled

open fun isEnabled(): Boolean

isFocusable

fun isFocusable(): Boolean

isFocusableInTouchMode

fun isFocusableInTouchMode(): Boolean

isFocused

open fun isFocused(): Boolean

isFocusedByDefault

fun isFocusedByDefault(): Boolean

isForceDarkAllowed

open fun isForceDarkAllowed(): Boolean

isHandwritingDelegate

open fun isHandwritingDelegate(): Boolean

isHapticFeedbackEnabled

open fun isHapticFeedbackEnabled(): Boolean

isHardwareAccelerated

open fun isHardwareAccelerated(): Boolean

isHorizontalFadingEdgeEnabled

open fun isHorizontalFadingEdgeEnabled(): Boolean

isHorizontalScrollBarEnabled

open fun isHorizontalScrollBarEnabled(): Boolean

isHovered

open fun isHovered(): Boolean

isImportantForAccessibility

open fun isImportantForAccessibility(): Boolean

isImportantForAutofill

fun isImportantForAutofill(): Boolean

isImportantForContentCapture

fun isImportantForContentCapture(): Boolean

isInEditMode

open fun isInEditMode(): Boolean

isInLayout

open fun isInLayout(): Boolean

isInTouchMode

open fun isInTouchMode(): Boolean

isKeyboardNavigationCluster

fun isKeyboardNavigationCluster(): Boolean

isLaidOut

open fun isLaidOut(): Boolean

isLayoutDirectionResolved

open fun isLayoutDirectionResolved(): Boolean

isLayoutRequested

open fun isLayoutRequested(): Boolean

isLayoutSuppressed

open fun isLayoutSuppressed(): Boolean

isLongClickable

open fun isLongClickable(): Boolean

isMotionEventSplittingEnabled

open fun isMotionEventSplittingEnabled(): Boolean

isNestedScrollingEnabled

open fun isNestedScrollingEnabled(): Boolean

isOpaque

open fun isOpaque(): Boolean

isPaddingRelative

open fun isPaddingRelative(): Boolean

isPivotSet

open fun isPivotSet(): Boolean

isPreferKeepClear

fun isPreferKeepClear(): Boolean

isPressed

open fun isPressed(): Boolean

isSaveEnabled

open fun isSaveEnabled(): Boolean

isSaveFromParentEnabled

open fun isSaveFromParentEnabled(): Boolean

isScreenReaderFocusable

open fun isScreenReaderFocusable(): Boolean

isScrollbarFadingEnabled

open fun isScrollbarFadingEnabled(): Boolean

isScrollContainer

open fun isScrollContainer(): Boolean

isSelected

open fun isSelected(): Boolean

isShowingLayoutBounds

fun isShowingLayoutBounds(): Boolean

isShown

open fun isShown(): Boolean

isSoundEffectsEnabled

open fun isSoundEffectsEnabled(): Boolean

isTemporarilyDetached

fun isTemporarilyDetached(): Boolean

isTextAlignmentResolved

open fun isTextAlignmentResolved(): Boolean

isTextDirectionResolved

open fun isTextDirectionResolved(): Boolean

isTransitionGroup

open fun isTransitionGroup(): Boolean

isVerticalFadingEdgeEnabled

open fun isVerticalFadingEdgeEnabled(): Boolean

isVerticalScrollBarEnabled

open fun isVerticalScrollBarEnabled(): Boolean

isVisibleToUserForAutofill

open fun isVisibleToUserForAutofill(p0: Int): Boolean

jumpDrawablesToCurrentState

open override fun jumpDrawablesToCurrentState()

keyboardNavigationClusterSearch

open fun keyboardNavigationClusterSearch(p0: View, p1: Int): View

layout

override fun layout(p0: Int, p1: Int, p2: Int, p3: Int)

measure

fun measure(p0: Int, p1: Int)

notifySubtreeAccessibilityStateChanged

open override fun notifySubtreeAccessibilityStateChanged(p0: View, p1: View, p2: Int)

offsetDescendantRectToMyCoords

fun offsetDescendantRectToMyCoords(p0: View, p1: Rect)

offsetLeftAndRight

open fun offsetLeftAndRight(p0: Int)

offsetRectIntoDescendantCoords

fun offsetRectIntoDescendantCoords(p0: View, p1: Rect)

offsetTopAndBottom

open fun offsetTopAndBottom(p0: Int)

onApplyWindowInsets

open fun onApplyWindowInsets(p0: WindowInsets): WindowInsets

onCancelPendingInputEvents

open fun onCancelPendingInputEvents()

onCapturedPointerEvent

open fun onCapturedPointerEvent(p0: MotionEvent): Boolean

onCheckIsTextEditor

open fun onCheckIsTextEditor(): Boolean

onCreateInputConnection

open fun onCreateInputConnection(p0: EditorInfo): InputConnection

onCreateViewTranslationRequest

open fun onCreateViewTranslationRequest(p0: IntArray, p1: Consumer<ViewTranslationRequest>)

onCreateVirtualViewTranslationRequests

open fun onCreateVirtualViewTranslationRequests(p0: LongArray, p1: IntArray, p2: Consumer<ViewTranslationRequest>)

onDescendantInvalidated

open override fun onDescendantInvalidated(p0: View, p1: View)

onDragEvent

open fun onDragEvent(p0: DragEvent): Boolean

onDrawForeground

open fun onDrawForeground(p0: Canvas)

onFilterTouchEventForSecurity

open fun onFilterTouchEventForSecurity(p0: MotionEvent): Boolean

onFinishTemporaryDetach

open fun onFinishTemporaryDetach()

onGenericMotionEvent

open fun onGenericMotionEvent(p0: MotionEvent): Boolean

onHoverChanged

open fun onHoverChanged(p0: Boolean)

onHoverEvent

open fun onHoverEvent(p0: MotionEvent): Boolean

onInitializeAccessibilityEvent

open fun onInitializeAccessibilityEvent(p0: AccessibilityEvent)

onInitializeAccessibilityNodeInfo

open fun onInitializeAccessibilityNodeInfo(p0: AccessibilityNodeInfo)

onInterceptHoverEvent

open fun onInterceptHoverEvent(p0: MotionEvent): Boolean

onInterceptTouchEvent

open fun onInterceptTouchEvent(p0: MotionEvent): Boolean

onKeyDown

open override fun onKeyDown(p0: Int, p1: KeyEvent): Boolean

onKeyLongPress

open override fun onKeyLongPress(p0: Int, p1: KeyEvent): Boolean

onKeyMultiple

open override fun onKeyMultiple(p0: Int, p1: Int, p2: KeyEvent): Boolean

onKeyPreIme

open fun onKeyPreIme(p0: Int, p1: KeyEvent): Boolean

onKeyShortcut

open fun onKeyShortcut(p0: Int, p1: KeyEvent): Boolean

onKeyUp

open override fun onKeyUp(p0: Int, p1: KeyEvent): Boolean

onNestedFling

open override fun onNestedFling(p0: View, p1: Float, p2: Float, p3: Boolean): Boolean

onNestedPreFling

open override fun onNestedPreFling(p0: View, p1: Float, p2: Float): Boolean

onNestedPrePerformAccessibilityAction

open override fun onNestedPrePerformAccessibilityAction(p0: View, p1: Int, p2: Bundle?): Boolean

onNestedPreScroll

open override fun onNestedPreScroll(p0: View, p1: Int, p2: Int, p3: IntArray)

onNestedScroll

open override fun onNestedScroll(p0: View, p1: Int, p2: Int, p3: Int, p4: Int)

onNestedScrollAccepted

open override fun onNestedScrollAccepted(p0: View, p1: View, p2: Int)

onPointerCaptureChange

open fun onPointerCaptureChange(p0: Boolean)

onPopulateAccessibilityEvent

open fun onPopulateAccessibilityEvent(p0: AccessibilityEvent)

onProvideAutofillStructure

open fun onProvideAutofillStructure(p0: ViewStructure, p1: Int)

onProvideAutofillVirtualStructure

open fun onProvideAutofillVirtualStructure(p0: ViewStructure, p1: Int)

onProvideContentCaptureStructure

open fun onProvideContentCaptureStructure(p0: ViewStructure, p1: Int)

onProvideStructure

open fun onProvideStructure(p0: ViewStructure)

onProvideVirtualStructure

open fun onProvideVirtualStructure(p0: ViewStructure)

onReceiveContent

open fun onReceiveContent(p0: ContentInfo): ContentInfo?

onRequestSendAccessibilityEvent

open fun onRequestSendAccessibilityEvent(p0: View, p1: AccessibilityEvent): Boolean

onResolvePointerIcon

open override fun onResolvePointerIcon(p0: MotionEvent, p1: Int): PointerIcon

onRtlPropertiesChanged

open fun onRtlPropertiesChanged(p0: Int)

onScreenStateChanged

open fun onScreenStateChanged(p0: Int)

onScrollCaptureSearch

open fun onScrollCaptureSearch(p0: Rect, p1: Point, p2: Consumer<ScrollCaptureTarget>)

onStartNestedScroll

open override fun onStartNestedScroll(p0: View, p1: View, p2: Int): Boolean

onStartTemporaryDetach

open fun onStartTemporaryDetach()

onStopNestedScroll

open override fun onStopNestedScroll(p0: View)

onTouchEvent

open fun onTouchEvent(p0: MotionEvent): Boolean

onTrackballEvent

open fun onTrackballEvent(p0: MotionEvent): Boolean

onViewAdded

open fun onViewAdded(p0: View)

onViewRemoved

open fun onViewRemoved(p0: View)

onViewTranslationResponse

open fun onViewTranslationResponse(p0: ViewTranslationResponse)

onVirtualViewTranslationResponses

open fun onVirtualViewTranslationResponses(p0: LongSparseArray<ViewTranslationResponse>)

onVisibilityAggregated

open fun onVisibilityAggregated(p0: Boolean)

onWindowFocusChanged

open fun onWindowFocusChanged(p0: Boolean)

onWindowSystemUiVisibilityChanged

open fun onWindowSystemUiVisibilityChanged(p0: Int)

performAccessibilityAction

open fun performAccessibilityAction(p0: Int, p1: Bundle?): Boolean

performClick

open fun performClick(): Boolean

performContextClick

open fun performContextClick(): Booleanopen fun performContextClick(p0: Float, p1: Float): Boolean

performHapticFeedback

open fun performHapticFeedback(p0: Int): Booleanopen fun performHapticFeedback(p0: Int, p1: Int): Boolean

performLongClick

open fun performLongClick(): Booleanopen fun performLongClick(p0: Float, p1: Float): Boolean

performReceiveContent

open fun performReceiveContent(p0: ContentInfo): ContentInfo?

playSoundEffect

open fun playSoundEffect(p0: Int)

post

open fun post(p0: Runnable): Boolean

postDelayed

open fun postDelayed(p0: Runnable, p1: Long): Boolean

postInvalidate

open fun postInvalidate()open fun postInvalidate(p0: Int, p1: Int, p2: Int, p3: Int)

postInvalidateDelayed

open fun postInvalidateDelayed(p0: Long)open fun postInvalidateDelayed(p0: Long, p1: Int, p2: Int, p3: Int, p4: Int)

postInvalidateOnAnimation

open fun postInvalidateOnAnimation()open fun postInvalidateOnAnimation(p0: Int, p1: Int, p2: Int, p3: Int)

postOnAnimation

open fun postOnAnimation(p0: Runnable)

postOnAnimationDelayed

open fun postOnAnimationDelayed(p0: Runnable, p1: Long)

recomputeViewAttributes

open override fun recomputeViewAttributes(p0: View)

refreshDrawableState

open fun refreshDrawableState()

releasePointerCapture

open fun releasePointerCapture()

removeAllViews

open fun removeAllViews()

removeAllViewsInLayout

open fun removeAllViewsInLayout()

removeCallbacks

open fun removeCallbacks(p0: Runnable): Boolean

removeOnAttachStateChangeListener

open fun removeOnAttachStateChangeListener(p0: View.OnAttachStateChangeListener)

removeOnLayoutChangeListener

open fun removeOnLayoutChangeListener(p0: View.OnLayoutChangeListener)

removeOnUnhandledKeyEventListener

open fun removeOnUnhandledKeyEventListener(p0: View.OnUnhandledKeyEventListener)

removeView

open override fun removeView(p0: View)

removeViewAt

open fun removeViewAt(p0: Int)

removeViewInLayout

open fun removeViewInLayout(p0: View)

removeViews

open fun removeViews(p0: Int, p1: Int)

removeViewsInLayout

open fun removeViewsInLayout(p0: Int, p1: Int)

requestApplyInsets

open fun requestApplyInsets()

requestChildFocus

open override fun requestChildFocus(p0: View, p1: View)

requestChildRectangleOnScreen

open override fun requestChildRectangleOnScreen(p0: View, p1: Rect, p2: Boolean): Boolean

requestDisallowInterceptTouchEvent

open override fun requestDisallowInterceptTouchEvent(p0: Boolean)

requestFitSystemWindows

open fun requestFitSystemWindows()

requestFocus

fun requestFocus(): Booleanfun requestFocus(p0: Int): Booleanopen override fun requestFocus(p0: Int, p1: Rect): Boolean

requestFocusFromTouch

fun requestFocusFromTouch(): Boolean

requestLayout

open fun requestLayout()

requestPointerCapture

open fun requestPointerCapture()

requestRectangleOnScreen

open fun requestRectangleOnScreen(p0: Rect): Booleanopen fun requestRectangleOnScreen(p0: Rect, p1: Boolean): Boolean

requestSendAccessibilityEvent

open override fun requestSendAccessibilityEvent(p0: View, p1: AccessibilityEvent): Boolean

requestTransparentRegion

open override fun requestTransparentRegion(p0: View)

requestUnbufferedDispatch

fun requestUnbufferedDispatch(p0: MotionEvent)fun requestUnbufferedDispatch(p0: Int)

requireViewById

fun <T : View> requireViewById(p0: Int): T & Any

resetPivot

open fun resetPivot()

restoreDefaultFocus

open override fun restoreDefaultFocus(): Boolean

restoreHierarchyState

open fun restoreHierarchyState(p0: SparseArray<Parcelable>)

saveAttributeDataForStyleable

fun saveAttributeDataForStyleable(p0: Context, p1: IntArray, p2: AttributeSet?, p3: TypedArray, p4: Int, p5: Int)

saveHierarchyState

open fun saveHierarchyState(p0: SparseArray<Parcelable>)

scheduleDrawable

open override fun scheduleDrawable(p0: Drawable, p1: Runnable, p2: Long)

scheduleLayoutAnimation

open fun scheduleLayoutAnimation()

scrollBy

open fun scrollBy(p0: Int, p1: Int)

scrollTo

open fun scrollTo(p0: Int, p1: Int)

sendAccessibilityEvent

open override fun sendAccessibilityEvent(p0: Int)

sendAccessibilityEventUnchecked

open override fun sendAccessibilityEventUnchecked(p0: AccessibilityEvent)

setAccessibilityDataSensitive

open fun setAccessibilityDataSensitive(p0: Int)

setAccessibilityDelegate

open fun setAccessibilityDelegate(p0: View.AccessibilityDelegate?)

setAccessibilityHeading

open fun setAccessibilityHeading(p0: Boolean)

setAccessibilityLiveRegion

open fun setAccessibilityLiveRegion(p0: Int)

setAccessibilityPaneTitle

open fun setAccessibilityPaneTitle(p0: CharSequence?)

setAccessibilityTraversalAfter

open fun setAccessibilityTraversalAfter(p0: Int)

setAccessibilityTraversalBefore

open fun setAccessibilityTraversalBefore(p0: Int)

setActivated

open fun setActivated(p0: Boolean)

setAddStatesFromChildren

open fun setAddStatesFromChildren(p0: Boolean)

setAllowClickWhenDisabled

open fun setAllowClickWhenDisabled(p0: Boolean)

setAllowedHandwritingDelegatePackage

open fun setAllowedHandwritingDelegatePackage(p0: String?)

setAllowedHandwritingDelegatorPackage

open fun setAllowedHandwritingDelegatorPackage(p0: String?)

setAlpha

open fun setAlpha(p0: Float)

setAlwaysDrawnWithCacheEnabled

open fun setAlwaysDrawnWithCacheEnabled(p0: Boolean)

setAnimation

open fun setAnimation(p0: Animation)

setAnimationCacheEnabled

open fun setAnimationCacheEnabled(p0: Boolean)

setAnimationMatrix

open fun setAnimationMatrix(p0: Matrix?)

setAutofillHints

open fun setAutofillHints(vararg p0: String)

setAutofillId

open fun setAutofillId(p0: AutofillId?)

setAutoHandwritingEnabled

open fun setAutoHandwritingEnabled(p0: Boolean)

setBackground

open fun setBackground(p0: Drawable)

setBackgroundColor

open fun setBackgroundColor(p0: Int)

setBackgroundDrawable

open fun setBackgroundDrawable(p0: Drawable)

setBackgroundResource

open fun setBackgroundResource(p0: Int)

setBackgroundTintBlendMode

open fun setBackgroundTintBlendMode(p0: BlendMode?)

setBackgroundTintList

open fun setBackgroundTintList(p0: ColorStateList?)

setBackgroundTintMode

open fun setBackgroundTintMode(p0: PorterDuff.Mode?)

setBottom

fun setBottom(p0: Int)

setCameraDistance

open fun setCameraDistance(p0: Float)

setClickable

open fun setClickable(p0: Boolean)

setClipBounds

open fun setClipBounds(p0: Rect)

setClipChildren

open fun setClipChildren(p0: Boolean)

setClipToOutline

open fun setClipToOutline(p0: Boolean)

setClipToPadding

open fun setClipToPadding(p0: Boolean)

setContentCaptureSession

open fun setContentCaptureSession(p0: ContentCaptureSession?)

setContentDescription

open fun setContentDescription(p0: CharSequence)

setContentSensitivity

fun setContentSensitivity(p0: Int)

setContextClickable

open fun setContextClickable(p0: Boolean)

setDefaultFocusHighlightEnabled

open fun setDefaultFocusHighlightEnabled(p0: Boolean)

setDescendantFocusability

open fun setDescendantFocusability(p0: Int)

setDrawingCacheBackgroundColor

open fun setDrawingCacheBackgroundColor(p0: Int)

setDrawingCacheEnabled

open fun setDrawingCacheEnabled(p0: Boolean)

setDrawingCacheQuality

open fun setDrawingCacheQuality(p0: Int)

setDuplicateParentStateEnabled

open fun setDuplicateParentStateEnabled(p0: Boolean)

setElevation

open fun setElevation(p0: Float)

setEnabled

open fun setEnabled(p0: Boolean)

setFadingEdgeLength

open fun setFadingEdgeLength(p0: Int)

setFilterTouchesWhenObscured

open fun setFilterTouchesWhenObscured(p0: Boolean)

setFitsSystemWindows

open fun setFitsSystemWindows(p0: Boolean)

setFocusable

open fun setFocusable(p0: Boolean)open fun setFocusable(p0: Int)

setFocusableInTouchMode

open fun setFocusableInTouchMode(p0: Boolean)

setFocusedByDefault

open fun setFocusedByDefault(p0: Boolean)

setForceDarkAllowed

open fun setForceDarkAllowed(p0: Boolean)

setForeground

open fun setForeground(p0: Drawable)

setForegroundGravity

open override fun setForegroundGravity(p0: Int)

setForegroundTintBlendMode

open fun setForegroundTintBlendMode(p0: BlendMode?)

setForegroundTintList

open fun setForegroundTintList(p0: ColorStateList?)

setForegroundTintMode

open fun setForegroundTintMode(p0: PorterDuff.Mode?)

setFrameContentVelocity

open fun setFrameContentVelocity(p0: Float)

setHandwritingBoundsOffsets

open fun setHandwritingBoundsOffsets(p0: Float, p1: Float, p2: Float, p3: Float)

setHandwritingDelegateFlags

open fun setHandwritingDelegateFlags(p0: Int)

setHandwritingDelegatorCallback

open fun setHandwritingDelegatorCallback(p0: Runnable?)

setHapticFeedbackEnabled

open fun setHapticFeedbackEnabled(p0: Boolean)

setHasTransientState

open fun setHasTransientState(p0: Boolean)

setHorizontalFadingEdgeEnabled

open fun setHorizontalFadingEdgeEnabled(p0: Boolean)

setHorizontalScrollBarEnabled

open fun setHorizontalScrollBarEnabled(p0: Boolean)

setHorizontalScrollbarThumbDrawable

open fun setHorizontalScrollbarThumbDrawable(p0: Drawable?)

setHorizontalScrollbarTrackDrawable

open fun setHorizontalScrollbarTrackDrawable(p0: Drawable?)

setHovered

open fun setHovered(p0: Boolean)

setId

open fun setId(p0: Int)

setImportantForAccessibility

open fun setImportantForAccessibility(p0: Int)

setImportantForAutofill

open fun setImportantForAutofill(p0: Int)

setImportantForContentCapture

open fun setImportantForContentCapture(p0: Int)

setIsCredential

open fun setIsCredential(p0: Boolean)

setIsHandwritingDelegate

open fun setIsHandwritingDelegate(p0: Boolean)

setKeepScreenOn

open fun setKeepScreenOn(p0: Boolean)

setKeyboardNavigationCluster

open fun setKeyboardNavigationCluster(p0: Boolean)

setLabelFor

open fun setLabelFor(p0: Int)

setLayerPaint

open fun setLayerPaint(p0: Paint?)

setLayerType

open fun setLayerType(p0: Int, p1: Paint?)

setLayoutAnimation

open fun setLayoutAnimation(p0: LayoutAnimationController)

setLayoutAnimationListener

open fun setLayoutAnimationListener(p0: Animation.AnimationListener)

setLayoutDirection

open fun setLayoutDirection(p0: Int)

setLayoutMode

open fun setLayoutMode(p0: Int)

setLayoutParams

open fun setLayoutParams(p0: ViewGroup.LayoutParams)

setLayoutTransition

open fun setLayoutTransition(p0: LayoutTransition)

setLeft

fun setLeft(p0: Int)

setLeftTopRightBottom

fun setLeftTopRightBottom(p0: Int, p1: Int, p2: Int, p3: Int)

setLongClickable

open fun setLongClickable(p0: Boolean)

setMeasureAllChildren

open fun setMeasureAllChildren(p0: Boolean)

setMinimumHeight

open fun setMinimumHeight(p0: Int)

setMinimumWidth

open fun setMinimumWidth(p0: Int)

setMotionEventSplittingEnabled

open fun setMotionEventSplittingEnabled(p0: Boolean)

setNestedScrollingEnabled

open fun setNestedScrollingEnabled(p0: Boolean)

setNextClusterForwardId

open fun setNextClusterForwardId(p0: Int)

setNextFocusDownId

open fun setNextFocusDownId(p0: Int)

setNextFocusForwardId

open fun setNextFocusForwardId(p0: Int)

setNextFocusLeftId

open fun setNextFocusLeftId(p0: Int)

setNextFocusRightId

open fun setNextFocusRightId(p0: Int)

setNextFocusUpId

open fun setNextFocusUpId(p0: Int)

setOnApplyWindowInsetsListener

open fun setOnApplyWindowInsetsListener(p0: View.OnApplyWindowInsetsListener)

setOnCapturedPointerListener

open fun setOnCapturedPointerListener(p0: View.OnCapturedPointerListener)

setOnClickListener

open fun setOnClickListener(p0: View.OnClickListener?)

setOnContextClickListener

open fun setOnContextClickListener(p0: View.OnContextClickListener?)

setOnCreateContextMenuListener

open fun setOnCreateContextMenuListener(p0: View.OnCreateContextMenuListener)

setOnDragListener

open fun setOnDragListener(p0: View.OnDragListener)

setOnFocusChangeListener

open fun setOnFocusChangeListener(p0: View.OnFocusChangeListener)

setOnGenericMotionListener

open fun setOnGenericMotionListener(p0: View.OnGenericMotionListener)

setOnHierarchyChangeListener

open fun setOnHierarchyChangeListener(p0: ViewGroup.OnHierarchyChangeListener)

setOnHoverListener

open fun setOnHoverListener(p0: View.OnHoverListener)

setOnKeyListener

open fun setOnKeyListener(p0: View.OnKeyListener)

setOnLongClickListener

open fun setOnLongClickListener(p0: View.OnLongClickListener?)

setOnReceiveContentListener

open fun setOnReceiveContentListener(p0: Array<String>?, p1: OnReceiveContentListener?)

setOnScrollChangeListener

open fun setOnScrollChangeListener(p0: View.OnScrollChangeListener)

setOnSystemUiVisibilityChangeListener

open fun setOnSystemUiVisibilityChangeListener(p0: View.OnSystemUiVisibilityChangeListener)

setOnTouchListener

open fun setOnTouchListener(p0: View.OnTouchListener)

setOutlineAmbientShadowColor

open fun setOutlineAmbientShadowColor(p0: Int)

setOutlineProvider

open fun setOutlineProvider(p0: ViewOutlineProvider)

setOutlineSpotShadowColor

open fun setOutlineSpotShadowColor(p0: Int)

setOverScrollMode

open fun setOverScrollMode(p0: Int)

setPadding

open fun setPadding(p0: Int, p1: Int, p2: Int, p3: Int)

setPaddingRelative

open fun setPaddingRelative(p0: Int, p1: Int, p2: Int, p3: Int)

setPendingCredentialRequest

open fun setPendingCredentialRequest(p0: GetCredentialRequest, p1: OutcomeReceiver<GetCredentialResponse, GetCredentialException>)

setPersistentDrawingCache

open fun setPersistentDrawingCache(p0: Int)

setPivotX

open fun setPivotX(p0: Float)

setPivotY

open fun setPivotY(p0: Float)

setPointerIcon

open fun setPointerIcon(p0: PointerIcon)

setPreferKeepClear

fun setPreferKeepClear(p0: Boolean)

setPreferKeepClearRects

fun setPreferKeepClearRects(p0: MutableList<Rect>)

setPressed

open fun setPressed(p0: Boolean)

setRenderEffect

open fun setRenderEffect(p0: RenderEffect?)

setRequestedFrameRate

open fun setRequestedFrameRate(p0: Float)

setRevealOnFocusHint

fun setRevealOnFocusHint(p0: Boolean)

setRight

fun setRight(p0: Int)

setRotation

open fun setRotation(p0: Float)

setRotationX

open fun setRotationX(p0: Float)

setRotationY

open fun setRotationY(p0: Float)

setSaveEnabled

open fun setSaveEnabled(p0: Boolean)

setSaveFromParentEnabled

open fun setSaveFromParentEnabled(p0: Boolean)

setScaleX

open fun setScaleX(p0: Float)

setScaleY

open fun setScaleY(p0: Float)

setScreenReaderFocusable

open fun setScreenReaderFocusable(p0: Boolean)

setScrollBarDefaultDelayBeforeFade

open fun setScrollBarDefaultDelayBeforeFade(p0: Int)

setScrollBarFadeDuration

open fun setScrollBarFadeDuration(p0: Int)

setScrollbarFadingEnabled

open fun setScrollbarFadingEnabled(p0: Boolean)

setScrollBarSize

open fun setScrollBarSize(p0: Int)

setScrollBarStyle

open fun setScrollBarStyle(p0: Int)

setScrollCaptureCallback

fun setScrollCaptureCallback(p0: ScrollCaptureCallback?)

setScrollCaptureHint

open fun setScrollCaptureHint(p0: Int)

setScrollContainer

open fun setScrollContainer(p0: Boolean)

setScrollIndicators

open fun setScrollIndicators(p0: Int)open fun setScrollIndicators(p0: Int, p1: Int)

setScrollX

open fun setScrollX(p0: Int)

setScrollY

open fun setScrollY(p0: Int)

setSelected

open fun setSelected(p0: Boolean)

setSoundEffectsEnabled

open fun setSoundEffectsEnabled(p0: Boolean)

setStateDescription

open fun setStateDescription(p0: CharSequence?)

setStateListAnimator

open fun setStateListAnimator(p0: StateListAnimator)

setSystemGestureExclusionRects

open fun setSystemGestureExclusionRects(p0: MutableList<Rect>)

setSystemUiVisibility

open fun setSystemUiVisibility(p0: Int)

setTag

open fun setTag(p0: Any)open fun setTag(p0: Int, p1: Any)

setTextAlignment

open fun setTextAlignment(p0: Int)

setTextDirection

open fun setTextDirection(p0: Int)

setTooltipText

open fun setTooltipText(p0: CharSequence?)

setTop

fun setTop(p0: Int)

setTouchDelegate

open fun setTouchDelegate(p0: TouchDelegate)

setTouchscreenBlocksFocus

open fun setTouchscreenBlocksFocus(p0: Boolean)

setTransitionAlpha

open fun setTransitionAlpha(p0: Float)

setTransitionGroup

open fun setTransitionGroup(p0: Boolean)

setTransitionName

fun setTransitionName(p0: String)

setTransitionVisibility

open fun setTransitionVisibility(p0: Int)

setTranslationX

open fun setTranslationX(p0: Float)

setTranslationY

open fun setTranslationY(p0: Float)

setTranslationZ

open fun setTranslationZ(p0: Float)

setVerticalFadingEdgeEnabled

open fun setVerticalFadingEdgeEnabled(p0: Boolean)

setVerticalScrollBarEnabled

open fun setVerticalScrollBarEnabled(p0: Boolean)

setVerticalScrollbarPosition

open fun setVerticalScrollbarPosition(p0: Int)

setVerticalScrollbarThumbDrawable

open fun setVerticalScrollbarThumbDrawable(p0: Drawable?)

setVerticalScrollbarTrackDrawable

open fun setVerticalScrollbarTrackDrawable(p0: Drawable?)

setViewTranslationCallback

open fun setViewTranslationCallback(p0: ViewTranslationCallback)

setVisibility

open fun setVisibility(p0: Int)

setWillNotCacheDrawing

open fun setWillNotCacheDrawing(p0: Boolean)

setWillNotDraw

open fun setWillNotDraw(p0: Boolean)

setWindowInsetsAnimationCallback

open override fun setWindowInsetsAnimationCallback(p0: WindowInsetsAnimation.Callback?)

setX

open fun setX(p0: Float)

setY

open fun setY(p0: Float)

setZ

open fun setZ(p0: Float)

shouldDelayChildPressedState

open override fun shouldDelayChildPressedState(): Boolean

showContextMenu

open fun showContextMenu(): Booleanopen fun showContextMenu(p0: Float, p1: Float): Boolean

showContextMenuForChild

open override fun showContextMenuForChild(p0: View): Booleanopen override fun showContextMenuForChild(p0: View, p1: Float, p2: Float): Boolean

startActionMode

open fun startActionMode(p0: ActionMode.Callback): ActionModeopen fun startActionMode(p0: ActionMode.Callback, p1: Int): ActionMode

startActionModeForChild

open override fun startActionModeForChild(p0: View, p1: ActionMode.Callback): ActionModeopen override fun startActionModeForChild(p0: View, p1: ActionMode.Callback, p2: Int): ActionMode

startAnimation

open fun startAnimation(p0: Animation)

startDrag

fun startDrag(p0: ClipData, p1: View.DragShadowBuilder, p2: Any, p3: Int): Boolean

startDragAndDrop

fun startDragAndDrop(p0: ClipData, p1: View.DragShadowBuilder, p2: Any, p3: Int): Boolean

startLayoutAnimation

open fun startLayoutAnimation()

startNestedScroll

open fun startNestedScroll(p0: Int): Boolean

startViewTransition

open fun startViewTransition(p0: View)

stopNestedScroll

open fun stopNestedScroll()

suppressLayout

open fun suppressLayout(p0: Boolean)

toString

open override fun toString(): String

transformMatrixToGlobal

open fun transformMatrixToGlobal(p0: Matrix)

transformMatrixToLocal

open fun transformMatrixToLocal(p0: Matrix)

unscheduleDrawable

open fun unscheduleDrawable(p0: Drawable)open override fun unscheduleDrawable(p0: Drawable, p1: Runnable)

updateDragShadow

fun updateDragShadow(p0: View.DragShadowBuilder)

updateViewLayout

open override fun updateViewLayout(p0: View, p1: ViewGroup.LayoutParams)

willNotCacheDrawing

open fun willNotCacheDrawing(): Boolean

willNotDraw

open fun willNotDraw(): Boolean

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic/initialize.html

---
layout: mobile_sdk
title: "initialize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "initialize"
id: initialize
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic"
---
# initialize

fun initialize(referenceStyle: MTMapReferenceStyle, options: MTMapOptions, controller: MTMapViewController, styleVariant: MTMapStyleVariant? = null)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic/scope.html

---
layout: mobile_sdk
title: "scope"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "scope"
id: scope
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-classic"
---
# scope

val scope: CoroutineScope

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-content-delegate/index.html

---
layout: mobile_sdk
title: "MTMapViewContentDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewContentDelegate"
id: -m-t-map-view-content-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-content-delegate"
---
# MTMapViewContentDelegate

interface MTMapViewContentDelegateSecondary event listener for map events, intended for overlay/content components that must react to map movement (e.g., custom Compose annotation views).This delegate is additive and does not replace MTMapViewDelegate.
#### Inheritors

MTCustomAnnotationViewClassic

Members

## Functions

onEvent

abstract fun onEvent(event: MTEvent, data: MTData?)Called whenever a map event is fired.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-content-delegate/on-event.html

---
layout: mobile_sdk
title: "onEvent"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onEvent"
id: on-event
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-content-delegate"
---
# onEvent

abstract fun onEvent(event: MTEvent, data: MTData?)Called whenever a map event is fired.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/-m-t-map-view-controller.html

---
layout: mobile_sdk
title: "MTMapViewController"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewController"
id: -m-t-map-view-controller
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# MTMapViewController

constructor(context: Context)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/add-content-delegate.html

---
layout: mobile_sdk
title: "addContentDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addContentDelegate"
id: add-content-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# addContentDelegate

fun addContentDelegate(delegate: MTMapViewContentDelegate)Registers a content delegate that observes map events without replacing the primary delegate.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/add-sprite.html

---
layout: mobile_sdk
title: "addSprite"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "addSprite"
id: add-sprite
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# addSprite

fun addSprite(identifier: String, url: URL)Registers a sprite resource that can be referenced from style layers.
#### Parameters

identifierUnique identifier for the sprite.urlFully qualified URL to the sprite image.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/are-tiles-loaded.html

---
layout: mobile_sdk
title: "areTilesLoaded"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "areTilesLoaded"
id: are-tiles-loaded
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# areTilesLoaded

open suspend override fun areTilesLoaded(): BooleanReturns whether all currently requested tiles are loaded.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/center-on-ip-point.html

---
layout: mobile_sdk
title: "centerOnIpPoint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "centerOnIpPoint"
id: center-on-ip-point
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# centerOnIpPoint

open override fun centerOnIpPoint()Centers the map on the coarse location inferred from the device's public IP address.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/delegate.html

---
layout: mobile_sdk
title: "delegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "delegate"
id: delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# delegate

var delegate: MTMapViewDelegate?Delegate object responsible for event propagation

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/destroy.html

---
layout: mobile_sdk
title: "destroy"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "destroy"
id: destroy
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# destroy

fun destroy()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/ease-to.html

---
layout: mobile_sdk
title: "easeTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "easeTo"
id: ease-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# easeTo

open override fun easeTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing and pitch with an animated transition between old and new values.
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/fit-bounds.html

---
layout: mobile_sdk
title: "fitBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fitBounds"
id: fit-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# fitBounds

open override fun fitBounds(bounds: MTBounds, options: MTFitBoundsOptions?)Fits the viewport so that the supplied bounds are fully visible, applying optional padding or animation overrides.
#### Parameters

boundsGeographical box that must be visible when the transition finishes.optionsOptional animation and padding configuration that fine-tunes the fitting behaviour.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/fit-screen-coordinates.html

---
layout: mobile_sdk
title: "fitScreenCoordinates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fitScreenCoordinates"
id: fit-screen-coordinates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# fitScreenCoordinates

open override fun fitScreenCoordinates(p0: MTPoint, p1: MTPoint, bearing: Double, options: MTFitBoundsOptions?)Pans, rotates and zooms the map to to fit the box made by points p0 and p1 once the map is rotated to the specified bearing. To zoom without rotating, pass in the current map bearing.
#### Parameters

p0First point on screen, in pixel coordinates.p1Second point on screen, in pixel coordinates.bearingDesired map bearing at end of animation, in degrees.optionsOptional animation and padding configuration.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/fit-to-ip-bounds.html

---
layout: mobile_sdk
title: "fitToIpBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fitToIpBounds"
id: fit-to-ip-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# fitToIpBounds

open override fun fitToIpBounds()Initiates an animated fit to the coarse bounds derived from the device's public IP address.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/fly-to.html

---
layout: mobile_sdk
title: "flyTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "flyTo"
id: fly-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# flyTo

open override fun flyTo(cameraOptions: MTCameraOptions, flyToOptions: MTFlyToOptions?)Changes any combination of center, zoom, bearing, and pitch, animating the transition along a curve that evokes flight.
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.flyToOptionsOptions describing the destination and animation of the transition.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/gesture-service.html

---
layout: mobile_sdk
title: "gestureService"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "gestureService"
id: gesture-service
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# gestureService

var gestureService: MTGestureService?Service responsible for gestures handling

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-bearing.html

---
layout: mobile_sdk
title: "getBearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getBearing"
id: get-bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getBearing

open suspend override fun getBearing(): DoubleReturns the map's current bearing.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-bounds.html

---
layout: mobile_sdk
title: "getBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getBounds"
id: get-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getBounds

open suspend override fun getBounds(): MTBoundsReturns the geographical bounds currently visible within the viewport.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-camera-target-elevation.html

---
layout: mobile_sdk
title: "getCameraTargetElevation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCameraTargetElevation"
id: get-camera-target-elevation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getCameraTargetElevation

open suspend override fun getCameraTargetElevation(): DoubleReturns the elevation of the location currently targeted by the camera, in meters above sea level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-center-clamped-to-ground.html

---
layout: mobile_sdk
title: "getCenterClampedToGround"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCenterClampedToGround"
id: get-center-clamped-to-ground
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getCenterClampedToGround

open suspend override fun getCenterClampedToGround(): BooleanReturns whether the map's center is clamped to the ground.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-center-elevation.html

---
layout: mobile_sdk
title: "getCenterElevation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCenterElevation"
id: get-center-elevation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getCenterElevation

open suspend override fun getCenterElevation(): DoubleReturns the elevation of the map's center point in meters above sea level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-center.html

---
layout: mobile_sdk
title: "getCenter"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getCenter"
id: get-center
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getCenter

open suspend override fun getCenter(): LngLatReturns the map's current center.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-maptiler-session-id.html

---
layout: mobile_sdk
title: "getMaptilerSessionId"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMaptilerSessionId"
id: get-maptiler-session-id
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMaptilerSessionId

suspend fun getMaptilerSessionId(): StringReturns the current SDK session UUID used for sessionized requests and telemetry.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-max-bounds.html

---
layout: mobile_sdk
title: "getMaxBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMaxBounds"
id: get-max-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMaxBounds

open suspend override fun getMaxBounds(): MTBounds?Returns the geographical constraints currently applied to the map, if any.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-max-pitch.html

---
layout: mobile_sdk
title: "getMaxPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMaxPitch"
id: get-max-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMaxPitch

open suspend override fun getMaxPitch(): DoubleReturns the map's maximum pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-max-zoom.html

---
layout: mobile_sdk
title: "getMaxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMaxZoom"
id: get-max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMaxZoom

open suspend override fun getMaxZoom(): DoubleReturns the map's maximum zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-min-pitch.html

---
layout: mobile_sdk
title: "getMinPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMinPitch"
id: get-min-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMinPitch

open suspend override fun getMinPitch(): DoubleReturns the map's minimum pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-min-zoom.html

---
layout: mobile_sdk
title: "getMinZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getMinZoom"
id: get-min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getMinZoom

open suspend override fun getMinZoom(): DoubleReturns the map's minimum zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-padding.html

---
layout: mobile_sdk
title: "getPadding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getPadding"
id: get-padding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getPadding

open suspend override fun getPadding(): MTPaddingOptionsReturns the current viewport padding as {top, right, bottom, left}. Use to retrieve padding applied for camera transitions and UI layout.
#### Return

The current viewport padding.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-pitch.html

---
layout: mobile_sdk
title: "getPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getPitch"
id: get-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getPitch

open suspend override fun getPitch(): DoubleReturns the map's current pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-pixel-ratio.html

---
layout: mobile_sdk
title: "getPixelRatio"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getPixelRatio"
id: get-pixel-ratio
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getPixelRatio

open suspend override fun getPixelRatio(): DoubleReturns the pixel ratio currently used to render the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-projection.html

---
layout: mobile_sdk
title: "getProjection"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getProjection"
id: get-projection
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getProjection

suspend fun getProjection(): MTProjectionTypeReturns the current map projection type. Defaults to MTProjectionType.MERCATOR if unavailable.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-render-world-copies.html

---
layout: mobile_sdk
title: "getRenderWorldCopies"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getRenderWorldCopies"
id: get-render-world-copies
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getRenderWorldCopies

open suspend override fun getRenderWorldCopies(): BooleanReturns whether the map is set to render multiple world copies.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-roll.html

---
layout: mobile_sdk
title: "getRoll"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getRoll"
id: get-roll
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getRoll

open suspend override fun getRoll(): DoubleReturns the map's current roll.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/get-zoom.html

---
layout: mobile_sdk
title: "getZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "getZoom"
id: get-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# getZoom

open suspend override fun getZoom(): DoubleReturns the map's current zoom level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/gpx-to-geo-j-s-o-n.html

---
layout: mobile_sdk
title: "gpxToGeoJSON"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "gpxToGeoJSON"
id: gpx-to-geo-j-s-o-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# gpxToGeoJSON

suspend fun gpxToGeoJSON(gpxXml: String): String?Converts a GPX XML payload to a GeoJSON FeatureCollection string using the SDK converter.This does not mutate the map and can be used to prepare data for a `GeoJSON` source.
#### Return

The GeoJSON FeatureCollection as a compact JSON string, or null on failure.
#### Parameters

gpxXmlThe GPX file contents as a string.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/has-terrain.html

---
layout: mobile_sdk
title: "hasTerrain"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "hasTerrain"
id: has-terrain
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# hasTerrain

suspend fun hasTerrain(): BooleanReturns true if 3D terrain visualization is enabled.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/index.html

---
layout: mobile_sdk
title: "MTMapViewController"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewController"
id: -m-t-map-view-controller
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# MTMapViewController

class MTMapViewController(context: Context) : WebViewExecutorDelegate, EventProcessorDelegate, MTJavascriptDelegate, MTZoomable, MTNavigableObject exposing methods and properties that enable changes to the map, and events that can be interacted with.

Members

## Constructors

MTMapViewController

constructor(context: Context)

## Properties

delegate

var delegate: MTMapViewDelegate?Delegate object responsible for event propagation

gestureService

var gestureService: MTGestureService?Service responsible for gestures handling

options

var options: MTMapOptions?Current options of the map object.

style

var style: MTStyle?Proxy style object of the map.

## Functions

addContentDelegate

fun addContentDelegate(delegate: MTMapViewContentDelegate)Registers a content delegate that observes map events without replacing the primary delegate.

addSprite

fun addSprite(identifier: String, url: URL)Registers a sprite resource that can be referenced from style layers.

areTilesLoaded

open suspend override fun areTilesLoaded(): BooleanReturns whether all currently requested tiles are loaded.

centerOnIpPoint

open override fun centerOnIpPoint()Centers the map on the coarse location inferred from the device's public IP address.

destroy

fun destroy()

easeTo

open override fun easeTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing and pitch with an animated transition between old and new values.

fitBounds

open override fun fitBounds(bounds: MTBounds, options: MTFitBoundsOptions?)Fits the viewport so that the supplied bounds are fully visible, applying optional padding or animation overrides.

fitScreenCoordinates

open override fun fitScreenCoordinates(p0: MTPoint, p1: MTPoint, bearing: Double, options: MTFitBoundsOptions?)Pans, rotates and zooms the map to to fit the box made by points p0 and p1 once the map is rotated to the specified bearing. To zoom without rotating, pass in the current map bearing.

fitToIpBounds

open override fun fitToIpBounds()Initiates an animated fit to the coarse bounds derived from the device's public IP address.

flyTo

open override fun flyTo(cameraOptions: MTCameraOptions, flyToOptions: MTFlyToOptions?)Changes any combination of center, zoom, bearing, and pitch, animating the transition along a curve that evokes flight.

getBearing

open suspend override fun getBearing(): DoubleReturns the map's current bearing.

getBounds

open suspend override fun getBounds(): MTBoundsReturns the geographical bounds currently visible within the viewport.

getCameraTargetElevation

open suspend override fun getCameraTargetElevation(): DoubleReturns the elevation of the location currently targeted by the camera, in meters above sea level.

getCenter

open suspend override fun getCenter(): LngLatReturns the map's current center.

getCenterClampedToGround

open suspend override fun getCenterClampedToGround(): BooleanReturns whether the map's center is clamped to the ground.

getCenterElevation

open suspend override fun getCenterElevation(): DoubleReturns the elevation of the map's center point in meters above sea level.

getMaptilerSessionId

suspend fun getMaptilerSessionId(): StringReturns the current SDK session UUID used for sessionized requests and telemetry.

getMaxBounds

open suspend override fun getMaxBounds(): MTBounds?Returns the geographical constraints currently applied to the map, if any.

getMaxPitch

open suspend override fun getMaxPitch(): DoubleReturns the map's maximum pitch.

getMaxZoom

open suspend override fun getMaxZoom(): DoubleReturns the map's maximum zoom level.

getMinPitch

open suspend override fun getMinPitch(): DoubleReturns the map's minimum pitch.

getMinZoom

open suspend override fun getMinZoom(): DoubleReturns the map's minimum zoom level.

getPadding

open suspend override fun getPadding(): MTPaddingOptionsReturns the current viewport padding as {top, right, bottom, left}. Use to retrieve padding applied for camera transitions and UI layout.

getPitch

open suspend override fun getPitch(): DoubleReturns the map's current pitch.

getPixelRatio

open suspend override fun getPixelRatio(): DoubleReturns the pixel ratio currently used to render the map.

getProjection

suspend fun getProjection(): MTProjectionTypeReturns the current map projection type. Defaults to MTProjectionType.MERCATOR if unavailable.

getRenderWorldCopies

open suspend override fun getRenderWorldCopies(): BooleanReturns whether the map is set to render multiple world copies.

getRoll

open suspend override fun getRoll(): DoubleReturns the map's current roll.

getZoom

open suspend override fun getZoom(): DoubleReturns the map's current zoom level.

gpxToGeoJSON

suspend fun gpxToGeoJSON(gpxXml: String): String?Converts a GPX XML payload to a GeoJSON FeatureCollection string using the SDK converter.

hasTerrain

suspend fun hasTerrain(): BooleanReturns true if 3D terrain visualization is enabled.

isGlobeProjection

suspend fun isGlobeProjection(): BooleanReturns true if the current projection is globe; otherwise false.

isMoving

open suspend override fun isMoving(): BooleanReturns true while any camera movement is active.

isRotating

open suspend override fun isRotating(): BooleanReturns true while the map is rotating.

isStyleLoaded

suspend fun isStyleLoaded(): BooleanReturns true once the style and its resources are fully loaded. Use before manipulating layers/sources programmatically.

isZooming

open suspend override fun isZooming(): BooleanReturns true while the map is zooming.

jumpTo

open override fun jumpTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing, and pitch, without an animated transition

kmlToGeoJSON

suspend fun kmlToGeoJSON(kmlXml: String): String?Converts a KML XML payload to a GeoJSON FeatureCollection string using the SDK converter.

loaded

open suspend override fun loaded(): BooleanReturns true when no ongoing operations remain and all sources/tiles are loaded.

onError

open override fun onError(message: String)Map error handler.

onEvent

open override fun onEvent(event: MTEvent, data: MTData?)

onEventTriggered

open override fun onEventTriggered(processor: EventProcessor, event: MTEvent, data: MTData?)

onNavigationFinished

open override fun onNavigationFinished(url: String)

onWebGLContextLost

open override fun onWebGLContextLost()WebGL Context error handler

panBy

open override fun panBy(offset: MTPoint)Pans the map by the specified offset.

panTo

open override fun panTo(coordinates: LngLat)Pans the map to the specified location with an animated transition.

project

open suspend override fun project(coordinates: LngLat): MTPointProject coordinates to point on the container.

redraw

fun redraw()Schedules a re-render of the map. Useful before reading pixels or screenshots.

reload

fun reload()

removeContentDelegate

fun removeContentDelegate(delegate: MTMapViewContentDelegate)Unregisters a previously registered content delegate.

removeSprite

fun removeSprite(id: String)Removes a previously added sprite by id. Use to detach a sprite and free related resources.

repaint

fun repaint()Requests the map be repainted on the next animation frame.

resetNorth

open override fun resetNorth(options: MTAnimationOptions?)Resets bearing to 0 degrees.

resetNorthPitch

open override fun resetNorthPitch(options: MTAnimationOptions?)Resets bearing to 0 and pitch to default.

rotateTo

open override fun rotateTo(bearing: Double, options: MTAnimationOptions?)Rotates the map to a given bearing, with an animated transition.

setBearing

open override fun setBearing(bearing: Double)Sets bearing of the map.

setCenter

open override fun setCenter(center: LngLat)Sets the geographical center of the map.

setCenterElevation

open override fun setCenterElevation(elevation: Double)Sets the elevation of the map's center point, in meters above sea level.

setIsCenterClampedToGround

open override fun setIsCenterClampedToGround(isCenterClampedToGround: Boolean)Sets the center clamped to the ground.

setMaxBounds

open override fun setMaxBounds(bounds: MTBounds?)Constrains map interactions to the provided bounds, or removes the constraint when null is supplied.

setMaxParallelImageRequests

fun setMaxParallelImageRequests(numRequests: Int)Sets the maximum number of images (raster tiles, sprites, icons) to load in parallel.

setMaxPitch

open override fun setMaxPitch(maxPitch: Double)Sets the map's maximum pitch limit in degrees (0-85).

setMaxZoom

open override fun setMaxZoom(maxZoom: Double)Sets the map's maximum zoom.

setMinPitch

open override fun setMinPitch(minPitch: Double)Sets the map's minimum pitch limit in degrees (0-85).

setMinZoom

open override fun setMinZoom(minZoom: Double)Sets the map's minimum zoom.

setPadding

open override fun setPadding(padding: MTPaddingOptions)Sets the padding in pixels around the viewport.

setPitch

open override fun setPitch(pitch: Double)Sets the map's pitch in degrees (0-85).

setPixelRatio

open override fun setPixelRatio(pixelRatio: Double)Overrides the pixel ratio used to render the map.

setRoll

open override fun setRoll(roll: Double)Sets the map's roll angle.

setRTLTextPlugin

fun setRTLTextPlugin(pluginUrl: String, deferred: Boolean = false)Sets the map's RTL text plugin. Necessary for supporting the right-to-left text direction found in languages like Arabic and Hebrew.

setSecondaryLanguage

fun setSecondaryLanguage(language: MTLanguage)Sets the secondary map language.

setSprite

fun setSprite(spriteUrl: String)Updates the sprite of the map.

setTerrain

fun setTerrain(terrain: MTTerrainSpecification?)Set the map terrain.

setTerrainAnimationDuration

fun setTerrainAnimationDuration(duration: Double)Set the duration (millisec) of the terrain animation for growing or flattening. Must be positive.

setTerrainExaggeration

fun setTerrainExaggeration(exaggeration: Double, animate: Boolean? = null)Change the terrain exaggeration.

setVerticalFieldOfView

open override fun setVerticalFieldOfView(verticalFieldOfView: Double)Sets the map's vertical field of view in degrees (defaults to 36.87 degrees).

setZoom

open override fun setZoom(zoom: Double)Sets the map's zoom level.

showCollisionBoxes

fun showCollisionBoxes(show: Boolean)Show or hide collision boxes

showOverdrawInpector

fun showOverdrawInpector(show: Boolean)Show or hide overdraw inspector

showPadding

fun showPadding(show: Boolean)Show or hide padding

showTileBoundaries

fun showTileBoundaries(show: Boolean)Show or hide tile boundaries

snapToNorth

open override fun snapToNorth(options: MTAnimationOptions?)Snaps the map so that north is up (bearing 0), animating the transition.

stop

open override fun stop()Stops any animated transition underway.

triggerRepaint

fun triggerRepaint()Trigger the rendering of a single frame. Use this method with custom layers to repaint the map when the layer changes. Calling this multiple times before the next frame is rendered will still result in only a single frame being rendered.

unproject

open suspend override fun unproject(point: MTPoint): LngLatUnproject a point on the container to geographical coordinates.

zoomIn

open override fun zoomIn()Increases the map's zoom level by 1.

zoomOut

open override fun zoomOut()Decreases the map's zoom level by 1.

zoomTo

open override fun zoomTo(zoom: Double, options: MTAnimationOptions?)Zooms the map to the specified zoom level, with an optional animation.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/is-globe-projection.html

---
layout: mobile_sdk
title: "isGlobeProjection"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isGlobeProjection"
id: is-globe-projection
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# isGlobeProjection

suspend fun isGlobeProjection(): BooleanReturns true if the current projection is globe; otherwise false.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/is-moving.html

---
layout: mobile_sdk
title: "isMoving"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isMoving"
id: is-moving
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# isMoving

open suspend override fun isMoving(): BooleanReturns true while any camera movement is active.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/is-rotating.html

---
layout: mobile_sdk
title: "isRotating"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isRotating"
id: is-rotating
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# isRotating

open suspend override fun isRotating(): BooleanReturns true while the map is rotating.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/is-style-loaded.html

---
layout: mobile_sdk
title: "isStyleLoaded"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isStyleLoaded"
id: is-style-loaded
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# isStyleLoaded

suspend fun isStyleLoaded(): BooleanReturns true once the style and its resources are fully loaded. Use before manipulating layers/sources programmatically.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/is-zooming.html

---
layout: mobile_sdk
title: "isZooming"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isZooming"
id: is-zooming
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# isZooming

open suspend override fun isZooming(): BooleanReturns true while the map is zooming.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/jump-to.html

---
layout: mobile_sdk
title: "jumpTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "jumpTo"
id: jump-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# jumpTo

open override fun jumpTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing, and pitch, without an animated transition
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/kml-to-geo-j-s-o-n.html

---
layout: mobile_sdk
title: "kmlToGeoJSON"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "kmlToGeoJSON"
id: kml-to-geo-j-s-o-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# kmlToGeoJSON

suspend fun kmlToGeoJSON(kmlXml: String): String?Converts a KML XML payload to a GeoJSON FeatureCollection string using the SDK converter.This does not mutate the map and can be used to prepare data for a `GeoJSON` source.
#### Return

The GeoJSON FeatureCollection as a compact JSON string, or null on failure.
#### Parameters

kmlXmlThe KML file contents as a string.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/loaded.html

---
layout: mobile_sdk
title: "loaded"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "loaded"
id: loaded
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# loaded

open suspend override fun loaded(): BooleanReturns true when no ongoing operations remain and all sources/tiles are loaded.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/on-error.html

---
layout: mobile_sdk
title: "onError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onError"
id: on-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# onError

open override fun onError(message: String)Map error handler.
#### Parameters

messageError message.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/on-event-triggered.html

---
layout: mobile_sdk
title: "onEventTriggered"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onEventTriggered"
id: on-event-triggered
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# onEventTriggered

open override fun onEventTriggered(processor: EventProcessor, event: MTEvent, data: MTData?)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/on-event.html

---
layout: mobile_sdk
title: "onEvent"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onEvent"
id: on-event
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# onEvent

open override fun onEvent(event: MTEvent, data: MTData?)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/on-navigation-finished.html

---
layout: mobile_sdk
title: "onNavigationFinished"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onNavigationFinished"
id: on-navigation-finished
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# onNavigationFinished

open override fun onNavigationFinished(url: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/on-web-g-l-context-lost.html

---
layout: mobile_sdk
title: "onWebGLContextLost"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onWebGLContextLost"
id: on-web-g-l-context-lost
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# onWebGLContextLost

open override fun onWebGLContextLost()WebGL Context error handler

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/options.html

---
layout: mobile_sdk
title: "options"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "options"
id: options
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# options

var options: MTMapOptions?Current options of the map object.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/pan-by.html

---
layout: mobile_sdk
title: "panBy"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "panBy"
id: pan-by
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# panBy

open override fun panBy(offset: MTPoint)Pans the map by the specified offset.
#### Parameters

offsetOffset to pan by.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/pan-to.html

---
layout: mobile_sdk
title: "panTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "panTo"
id: pan-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# panTo

open override fun panTo(coordinates: LngLat)Pans the map to the specified location with an animated transition.
#### Parameters

coordinatesCoordinates to pan to.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/project.html

---
layout: mobile_sdk
title: "project"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "project"
id: project
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# project

open suspend override fun project(coordinates: LngLat): MTPointProject coordinates to point on the container.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/redraw.html

---
layout: mobile_sdk
title: "redraw"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "redraw"
id: redraw
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# redraw

fun redraw()Schedules a re-render of the map. Useful before reading pixels or screenshots.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/reload.html

---
layout: mobile_sdk
title: "reload"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "reload"
id: reload
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# reload

fun reload()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/remove-content-delegate.html

---
layout: mobile_sdk
title: "removeContentDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "removeContentDelegate"
id: remove-content-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# removeContentDelegate

fun removeContentDelegate(delegate: MTMapViewContentDelegate)Unregisters a previously registered content delegate.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/remove-sprite.html

---
layout: mobile_sdk
title: "removeSprite"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "removeSprite"
id: remove-sprite
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# removeSprite

fun removeSprite(id: String)Removes a previously added sprite by id. Use to detach a sprite and free related resources.
#### Parameters

idThe ID of the sprite.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/repaint.html

---
layout: mobile_sdk
title: "repaint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "repaint"
id: repaint
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# repaint

fun repaint()Requests the map be repainted on the next animation frame.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/reset-north-pitch.html

---
layout: mobile_sdk
title: "resetNorthPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "resetNorthPitch"
id: reset-north-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# resetNorthPitch

open override fun resetNorthPitch(options: MTAnimationOptions?)Resets bearing to 0 and pitch to default.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/reset-north.html

---
layout: mobile_sdk
title: "resetNorth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "resetNorth"
id: reset-north
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# resetNorth

open override fun resetNorth(options: MTAnimationOptions?)Resets bearing to 0 degrees.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/rotate-to.html

---
layout: mobile_sdk
title: "rotateTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "rotateTo"
id: rotate-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# rotateTo

open override fun rotateTo(bearing: Double, options: MTAnimationOptions?)Rotates the map to a given bearing, with an animated transition.
#### Parameters

bearingThe desired bearing in degrees.optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-bearing.html

---
layout: mobile_sdk
title: "setBearing"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setBearing"
id: set-bearing
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setBearing

open override fun setBearing(bearing: Double)Sets bearing of the map.
#### Parameters

bearingThe bearing of the map, measured in degrees counter-clockwise from north.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-center-elevation.html

---
layout: mobile_sdk
title: "setCenterElevation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setCenterElevation"
id: set-center-elevation
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setCenterElevation

open override fun setCenterElevation(elevation: Double)Sets the elevation of the map's center point, in meters above sea level.
#### Parameters

elevationDesired elevation.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-center.html

---
layout: mobile_sdk
title: "setCenter"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setCenter"
id: set-center
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setCenter

open override fun setCenter(center: LngLat)Sets the geographical center of the map.
#### Parameters

centerGeographical center of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-is-center-clamped-to-ground.html

---
layout: mobile_sdk
title: "setIsCenterClampedToGround"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setIsCenterClampedToGround"
id: set-is-center-clamped-to-ground
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setIsCenterClampedToGround

open override fun setIsCenterClampedToGround(isCenterClampedToGround: Boolean)Sets the center clamped to the ground.If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if terrain is not enabled). If false, the elevation of the center point will default to sea level and will not automatically update.
#### Parameters

isCenterClampedToGroundBoolean indicating whether center is clamped to the ground.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-max-bounds.html

---
layout: mobile_sdk
title: "setMaxBounds"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMaxBounds"
id: set-max-bounds
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMaxBounds

open override fun setMaxBounds(bounds: MTBounds?)Constrains map interactions to the provided bounds, or removes the constraint when null is supplied.
#### Parameters

boundsBounding box limiting map navigation. Use null to clear existing constraints.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-max-parallel-image-requests.html

---
layout: mobile_sdk
title: "setMaxParallelImageRequests"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMaxParallelImageRequests"
id: set-max-parallel-image-requests
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMaxParallelImageRequests

fun setMaxParallelImageRequests(numRequests: Int)Sets the maximum number of images (raster tiles, sprites, icons) to load in parallel.
#### Parameters

numRequestsThe maximum number of parallel image requests.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-max-pitch.html

---
layout: mobile_sdk
title: "setMaxPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMaxPitch"
id: set-max-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMaxPitch

open override fun setMaxPitch(maxPitch: Double)Sets the map's maximum pitch limit in degrees (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-max-zoom.html

---
layout: mobile_sdk
title: "setMaxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMaxZoom"
id: set-max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMaxZoom

open override fun setMaxZoom(maxZoom: Double)Sets the map's maximum zoom.
#### Parameters

maxZoomDesired zoom.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-min-pitch.html

---
layout: mobile_sdk
title: "setMinPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMinPitch"
id: set-min-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMinPitch

open override fun setMinPitch(minPitch: Double)Sets the map's minimum pitch limit in degrees (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-min-zoom.html

---
layout: mobile_sdk
title: "setMinZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setMinZoom"
id: set-min-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setMinZoom

open override fun setMinZoom(minZoom: Double)Sets the map's minimum zoom.
#### Parameters

minZoomDesired zoom.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-padding.html

---
layout: mobile_sdk
title: "setPadding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setPadding"
id: set-padding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setPadding

open override fun setPadding(padding: MTPaddingOptions)Sets the padding in pixels around the viewport.
#### Parameters

paddingCustom options to use.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-pitch.html

---
layout: mobile_sdk
title: "setPitch"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setPitch"
id: set-pitch
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setPitch

open override fun setPitch(pitch: Double)Sets the map's pitch in degrees (0-85).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-pixel-ratio.html

---
layout: mobile_sdk
title: "setPixelRatio"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setPixelRatio"
id: set-pixel-ratio
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setPixelRatio

open override fun setPixelRatio(pixelRatio: Double)Overrides the pixel ratio used to render the map.
#### Parameters

pixelRatioDesired pixel ratio. Values above `1.0` improve sharpness, values below trade detail for performance.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-r-t-l-text-plugin.html

---
layout: mobile_sdk
title: "setRTLTextPlugin"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setRTLTextPlugin"
id: set-r-t-l-text-plugin
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setRTLTextPlugin

fun setRTLTextPlugin(pluginUrl: String, deferred: Boolean = false)Sets the map's RTL text plugin. Necessary for supporting the right-to-left text direction found in languages like Arabic and Hebrew.
#### Parameters

pluginUrlURL pointing to the Mapbox RTL text plugin source.deferredIf true, the plugin will not be loaded immediately but deferred until needed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-roll.html

---
layout: mobile_sdk
title: "setRoll"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setRoll"
id: set-roll
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setRoll

open override fun setRoll(roll: Double)Sets the map's roll angle.
#### Parameters

rollDesired roll.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-secondary-language.html

---
layout: mobile_sdk
title: "setSecondaryLanguage"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setSecondaryLanguage"
id: set-secondary-language
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setSecondaryLanguage

fun setSecondaryLanguage(language: MTLanguage)Sets the secondary map language.
#### Parameters

languageDesired secondary language of the map labels.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-sprite.html

---
layout: mobile_sdk
title: "setSprite"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setSprite"
id: set-sprite
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setSprite

fun setSprite(spriteUrl: String)Updates the sprite of the map.
#### Parameters

spriteUrlThe URL string pointing to the sprite image and JSON.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-terrain-animation-duration.html

---
layout: mobile_sdk
title: "setTerrainAnimationDuration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTerrainAnimationDuration"
id: set-terrain-animation-duration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setTerrainAnimationDuration

fun setTerrainAnimationDuration(duration: Double)Set the duration (millisec) of the terrain animation for growing or flattening. Must be positive.
#### Parameters

durationThe duration in milliseconds.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-terrain-exaggeration.html

---
layout: mobile_sdk
title: "setTerrainExaggeration"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTerrainExaggeration"
id: set-terrain-exaggeration
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setTerrainExaggeration

fun setTerrainExaggeration(exaggeration: Double, animate: Boolean? = null)Change the terrain exaggeration.
#### Parameters

exaggerationThe new exaggeration factor.animateIf true, the transition will be animated.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-terrain.html

---
layout: mobile_sdk
title: "setTerrain"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTerrain"
id: set-terrain
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setTerrain

fun setTerrain(terrain: MTTerrainSpecification?)Set the map terrain.
#### Parameters

terrainThe terrain specification or null to disable terrain.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-vertical-field-of-view.html

---
layout: mobile_sdk
title: "setVerticalFieldOfView"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setVerticalFieldOfView"
id: set-vertical-field-of-view
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setVerticalFieldOfView

open override fun setVerticalFieldOfView(verticalFieldOfView: Double)Sets the map's vertical field of view in degrees (defaults to 36.87 degrees).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/set-zoom.html

---
layout: mobile_sdk
title: "setZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setZoom"
id: set-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# setZoom

open override fun setZoom(zoom: Double)Sets the map's zoom level.
#### Parameters

zoomThe zoom level to set (0-20).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/show-collision-boxes.html

---
layout: mobile_sdk
title: "showCollisionBoxes"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "showCollisionBoxes"
id: show-collision-boxes
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# showCollisionBoxes

fun showCollisionBoxes(show: Boolean)Show or hide collision boxes

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/show-overdraw-inpector.html

---
layout: mobile_sdk
title: "showOverdrawInpector"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "showOverdrawInpector"
id: show-overdraw-inpector
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# showOverdrawInpector

fun showOverdrawInpector(show: Boolean)Show or hide overdraw inspector

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/show-padding.html

---
layout: mobile_sdk
title: "showPadding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "showPadding"
id: show-padding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# showPadding

fun showPadding(show: Boolean)Show or hide padding

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/show-tile-boundaries.html

---
layout: mobile_sdk
title: "showTileBoundaries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "showTileBoundaries"
id: show-tile-boundaries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# showTileBoundaries

fun showTileBoundaries(show: Boolean)Show or hide tile boundaries

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/snap-to-north.html

---
layout: mobile_sdk
title: "snapToNorth"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "snapToNorth"
id: snap-to-north
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# snapToNorth

open override fun snapToNorth(options: MTAnimationOptions?)Snaps the map so that north is up (bearing 0), animating the transition.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/stop.html

---
layout: mobile_sdk
title: "stop"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "stop"
id: stop
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# stop

open override fun stop()Stops any animated transition underway.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/style.html

---
layout: mobile_sdk
title: "style"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "style"
id: style
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# style

var style: MTStyle?Proxy style object of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/trigger-repaint.html

---
layout: mobile_sdk
title: "triggerRepaint"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "triggerRepaint"
id: trigger-repaint
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# triggerRepaint

fun triggerRepaint()Trigger the rendering of a single frame. Use this method with custom layers to repaint the map when the layer changes. Calling this multiple times before the next frame is rendered will still result in only a single frame being rendered.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/unproject.html

---
layout: mobile_sdk
title: "unproject"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "unproject"
id: unproject
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# unproject

open suspend override fun unproject(point: MTPoint): LngLatUnproject a point on the container to geographical coordinates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/zoom-in.html

---
layout: mobile_sdk
title: "zoomIn"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomIn"
id: zoom-in
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# zoomIn

open override fun zoomIn()Increases the map's zoom level by 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/zoom-out.html

---
layout: mobile_sdk
title: "zoomOut"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomOut"
id: zoom-out
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# zoomOut

open override fun zoomOut()Decreases the map's zoom level by 1.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller/zoom-to.html

---
layout: mobile_sdk
title: "zoomTo"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "zoomTo"
id: zoom-to
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-controller"
---
# zoomTo

open override fun zoomTo(zoom: Double, options: MTAnimationOptions?)Zooms the map to the specified zoom level, with an optional animation.
#### Parameters

zoomThe zoom level to transition to.optionsOptions object describing the destination and animation of the transition.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate/index.html

---
layout: mobile_sdk
title: "MTMapViewDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapViewDelegate"
id: -m-t-map-view-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate"
---
# MTMapViewDelegate

interface MTMapViewDelegate
#### Inheritors

MTBenchmark

Members

## Functions

onEventTriggered

abstract fun onEventTriggered(event: MTEvent, data: MTData?)

onMapViewInitialized

abstract fun onMapViewInitialized()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate/on-event-triggered.html

---
layout: mobile_sdk
title: "onEventTriggered"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onEventTriggered"
id: on-event-triggered
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate"
---
# onEventTriggered

abstract fun onEventTriggered(event: MTEvent, data: MTData?)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate/on-map-view-initialized.html

---
layout: mobile_sdk
title: "onMapViewInitialized"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "onMapViewInitialized"
id: on-map-view-initialized
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view-delegate"
---
# onMapViewInitialized

abstract fun onMapViewInitialized()

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/-m-t-map-view.html

---
layout: mobile_sdk
title: "MTMapView"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTMapView"
id: -m-t-map-view
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map"
---
# MTMapView

@Composablefun MTMapView(referenceStyle: MTMapReferenceStyle, options: MTMapOptions, controller: MTMapViewController, modifier: Modifier = Modifier, styleVariant: MTMapStyleVariant? = null)Object representing the map on the screen.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map"
id: com.maptiler.maptilersdk.map
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map"
---
# com.maptiler.maptilersdk.map

TypesFunctions

## Types

LngLat

@Serializabledata class LngLat(val lng: Double, val lat: Double)A geographical location which contains a latitude, longitude pair.

MTMapCameraHelper

class MTMapCameraHelperSets combination of center, bearing and pitch, as well as roll and elevation.

MTMapOptions

@Serializableclass MTMapOptionsParameters of the map object.

MTMapViewClassic

class MTMapViewClassic(context: Context, attrs: AttributeSet) : FrameLayoutObject representing the map on the screen. Used with XML.

MTMapViewContentDelegate

interface MTMapViewContentDelegateSecondary event listener for map events, intended for overlay/content components that must react to map movement (e.g., custom Compose annotation views).

MTMapViewController

class MTMapViewController(context: Context) : WebViewExecutorDelegate, EventProcessorDelegate, MTJavascriptDelegate, MTZoomable, MTNavigableObject exposing methods and properties that enable changes to the map, and events that can be interacted with.

MTMapViewDelegate

interface MTMapViewDelegate

## Functions

MTMapView

@Composablefun MTMapView(referenceStyle: MTMapReferenceStyle, options: MTMapOptions, controller: MTMapViewController, modifier: Modifier = Modifier, styleVariant: MTMapStyleVariant? = null)Object representing the map on the screen.

---

