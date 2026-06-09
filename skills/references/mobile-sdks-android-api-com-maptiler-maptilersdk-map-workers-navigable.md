# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.workers.navigable

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.workers.navigable` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/are-tiles-loaded.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# areTilesLoaded

abstract suspend fun areTilesLoaded(): BooleanReturns whether all currently requested tiles are loaded.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/center-on-ip-point.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# centerOnIpPoint

abstract fun centerOnIpPoint()Centers the map on the visitor's location inferred from their public IP address.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/ease-to.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# easeTo

abstract fun easeTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing and pitch with an animated transition between old and new values.
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/fit-bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# fitBounds

abstract fun fitBounds(bounds: MTBounds, options: MTFitBoundsOptions? = null)Adjusts the camera to ensure the entire bounding box is visible.
#### Parameters

boundsGeographical area that must be visible once the transition completes.optionsOptional animation and padding configuration applied while fitting the bounds.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/fit-screen-coordinates.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# fitScreenCoordinates

abstract fun fitScreenCoordinates(p0: MTPoint, p1: MTPoint, bearing: Double, options: MTFitBoundsOptions? = null)Pans, rotates and zooms the map to to fit the box made by points p0 and p1 once the map is rotated to the specified bearing. To zoom without rotating, pass in the current map bearing.
#### Parameters

p0First point on screen, in pixel coordinates.p1Second point on screen, in pixel coordinates.bearingDesired map bearing at end of animation, in degrees.optionsOptional animation and padding configuration.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/fit-to-ip-bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# fitToIpBounds

abstract fun fitToIpBounds()Fits the camera to the coarse bounds inferred from the user's public IP address.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/fly-to.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# flyTo

abstract fun flyTo(cameraOptions: MTCameraOptions, flyToOptions: MTFlyToOptions?)Changes any combination of center, zoom, bearing, and pitch, animating the transition along a curve that evokes flight.
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.flyToOptionsOptions describing the destination and animation of the transition.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-bearing.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getBearing

abstract suspend fun getBearing(): DoubleReturns the map's current bearing.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getBounds

abstract suspend fun getBounds(): MTBoundsReturns the geographical bounds currently visible in the viewport.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-camera-target-elevation.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getCameraTargetElevation

abstract suspend fun getCameraTargetElevation(): DoubleReturns the elevation of the point currently targeted by the camera, in meters above sea level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-center-clamped-to-ground.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getCenterClampedToGround

abstract suspend fun getCenterClampedToGround(): BooleanReturns whether the map's center is clamped to the ground.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-center-elevation.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getCenterElevation

abstract suspend fun getCenterElevation(): DoubleReturns the elevation of the map's center point in meters above sea level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-center.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getCenter

abstract suspend fun getCenter(): LngLatReturns the map's current center.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-max-bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getMaxBounds

abstract suspend fun getMaxBounds(): MTBounds?Returns the geographical constraints currently applied to the map, if any.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-max-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getMaxPitch

abstract suspend fun getMaxPitch(): DoubleReturns the map's maximum pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-min-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getMinPitch

abstract suspend fun getMinPitch(): DoubleReturns the map's minimum pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-padding.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getPadding

abstract suspend fun getPadding(): MTPaddingOptionsReturns the current viewport padding as {top, right, bottom, left}. Use to retrieve padding applied for camera transitions and UI layout.
#### Return

The current viewport padding.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getPitch

abstract suspend fun getPitch(): DoubleReturns the map's current pitch.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-pixel-ratio.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getPixelRatio

abstract suspend fun getPixelRatio(): DoubleReturns the pixel ratio currently used to render the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-render-world-copies.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getRenderWorldCopies

abstract suspend fun getRenderWorldCopies(): BooleanReturns whether the map is set to render multiple world copies.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/get-roll.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# getRoll

abstract suspend fun getRoll(): DoubleReturns the map's current roll.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/index.html

---
layout: mobile_sdk
title: "MTNavigable"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTNavigable"
id: -m-t-navigable
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# MTNavigable

interface MTNavigableDefines methods for navigating the map.
#### Inheritors

MTMapViewController

Members

## Functions

areTilesLoaded

abstract suspend fun areTilesLoaded(): BooleanReturns whether all currently requested tiles are loaded.

centerOnIpPoint

abstract fun centerOnIpPoint()Centers the map on the visitor's location inferred from their public IP address.

easeTo

abstract fun easeTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing and pitch with an animated transition between old and new values.

fitBounds

abstract fun fitBounds(bounds: MTBounds, options: MTFitBoundsOptions? = null)Adjusts the camera to ensure the entire bounding box is visible.

fitScreenCoordinates

abstract fun fitScreenCoordinates(p0: MTPoint, p1: MTPoint, bearing: Double, options: MTFitBoundsOptions? = null)Pans, rotates and zooms the map to to fit the box made by points p0 and p1 once the map is rotated to the specified bearing. To zoom without rotating, pass in the current map bearing.

fitToIpBounds

abstract fun fitToIpBounds()Fits the camera to the coarse bounds inferred from the user's public IP address.

flyTo

abstract fun flyTo(cameraOptions: MTCameraOptions, flyToOptions: MTFlyToOptions?)Changes any combination of center, zoom, bearing, and pitch, animating the transition along a curve that evokes flight.

getBearing

abstract suspend fun getBearing(): DoubleReturns the map's current bearing.

getBounds

abstract suspend fun getBounds(): MTBoundsReturns the geographical bounds currently visible in the viewport.

getCameraTargetElevation

abstract suspend fun getCameraTargetElevation(): DoubleReturns the elevation of the point currently targeted by the camera, in meters above sea level.

getCenter

abstract suspend fun getCenter(): LngLatReturns the map's current center.

getCenterClampedToGround

abstract suspend fun getCenterClampedToGround(): BooleanReturns whether the map's center is clamped to the ground.

getCenterElevation

abstract suspend fun getCenterElevation(): DoubleReturns the elevation of the map's center point in meters above sea level.

getMaxBounds

abstract suspend fun getMaxBounds(): MTBounds?Returns the geographical constraints currently applied to the map, if any.

getMaxPitch

abstract suspend fun getMaxPitch(): DoubleReturns the map's maximum pitch.

getMinPitch

abstract suspend fun getMinPitch(): DoubleReturns the map's minimum pitch.

getPadding

abstract suspend fun getPadding(): MTPaddingOptionsReturns the current viewport padding as {top, right, bottom, left}. Use to retrieve padding applied for camera transitions and UI layout.

getPitch

abstract suspend fun getPitch(): DoubleReturns the map's current pitch.

getPixelRatio

abstract suspend fun getPixelRatio(): DoubleReturns the pixel ratio currently used to render the map.

getRenderWorldCopies

abstract suspend fun getRenderWorldCopies(): BooleanReturns whether the map is set to render multiple world copies.

getRoll

abstract suspend fun getRoll(): DoubleReturns the map's current roll.

isMoving

abstract suspend fun isMoving(): BooleanReturns true while any camera movement is active.

isRotating

abstract suspend fun isRotating(): BooleanReturns true while the map is rotating.

isZooming

abstract suspend fun isZooming(): BooleanReturns true while the map is zooming.

jumpTo

abstract fun jumpTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing, and pitch, without an animated transition

loaded

abstract suspend fun loaded(): BooleanReturns true when no ongoing operations remain and all sources/tiles are loaded.

panBy

abstract fun panBy(offset: MTPoint)Pans the map by the specified offset.

panTo

abstract fun panTo(coordinates: LngLat)Pans the map to the specified location with an animated transition.

project

abstract suspend fun project(coordinates: LngLat): MTPointProjects geographical coordinates to a point on the container.

resetNorth

abstract fun resetNorth(options: MTAnimationOptions? = null)Resets bearing to 0 degrees.

resetNorthPitch

abstract fun resetNorthPitch(options: MTAnimationOptions? = null)Resets bearing to 0 and pitch to default.

rotateTo

abstract fun rotateTo(bearing: Double, options: MTAnimationOptions? = null)Rotates the map to a given bearing, with an animated transition.

setBearing

abstract fun setBearing(bearing: Double)Sets bearing of the map.

setCenter

abstract fun setCenter(center: LngLat)Sets the geographical center of the map.

setCenterElevation

abstract fun setCenterElevation(elevation: Double)Sets the elevation of the map's center point, in meters above sea level.

setIsCenterClampedToGround

abstract fun setIsCenterClampedToGround(isCenterClampedToGround: Boolean)Sets the center clamped to the ground.

setMaxBounds

abstract fun setMaxBounds(bounds: MTBounds?)Applies or clears the geographical constraints that clamp user interaction.

setMaxPitch

abstract fun setMaxPitch(maxPitch: Double)Sets the map's maximum pitch limit.

setMinPitch

abstract fun setMinPitch(minPitch: Double)Sets the map's minimum pitch limit.

setPadding

abstract fun setPadding(padding: MTPaddingOptions)Sets the padding in pixels around the viewport.

setPitch

abstract fun setPitch(pitch: Double)Sets the map's pitch.

setPixelRatio

abstract fun setPixelRatio(pixelRatio: Double)Overrides the pixel ratio used to render the map.

setRoll

abstract fun setRoll(roll: Double)Sets the map's roll angle.

setVerticalFieldOfView

abstract fun setVerticalFieldOfView(verticalFieldOfView: Double)Sets the map's vertical field of view in degrees (defaults to 36.87 degrees).

snapToNorth

abstract fun snapToNorth(options: MTAnimationOptions? = null)Snaps the map so that north is up (bearing 0), animating the transition.

stop

abstract fun stop()Stops any animated transition underway.

unproject

abstract suspend fun unproject(point: MTPoint): LngLatUnprojects a point on the container to geographical coordinates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/is-moving.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# isMoving

abstract suspend fun isMoving(): BooleanReturns true while any camera movement is active.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/is-rotating.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# isRotating

abstract suspend fun isRotating(): BooleanReturns true while the map is rotating.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/is-zooming.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# isZooming

abstract suspend fun isZooming(): BooleanReturns true while the map is zooming.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/jump-to.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# jumpTo

abstract fun jumpTo(cameraOptions: MTCameraOptions)Changes any combination of center, zoom, bearing, and pitch, without an animated transition
#### Parameters

cameraOptionsOptions for controlling the desired location, zoom, bearing, and pitch of the camera.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/loaded.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# loaded

abstract suspend fun loaded(): BooleanReturns true when no ongoing operations remain and all sources/tiles are loaded.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/pan-by.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# panBy

abstract fun panBy(offset: MTPoint)Pans the map by the specified offset.
#### Parameters

offsetOffset to pan by.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/pan-to.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# panTo

abstract fun panTo(coordinates: LngLat)Pans the map to the specified location with an animated transition.
#### Parameters

coordinatesCoordinates to pan to.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/project.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# project

abstract suspend fun project(coordinates: LngLat): MTPointProjects geographical coordinates to a point on the container.
#### Return

Screen-space point in pixels.
#### Parameters

coordinatesThe geographical coordinate to project.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/reset-north-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# resetNorthPitch

abstract fun resetNorthPitch(options: MTAnimationOptions? = null)Resets bearing to 0 and pitch to default.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/reset-north.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# resetNorth

abstract fun resetNorth(options: MTAnimationOptions? = null)Resets bearing to 0 degrees.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/rotate-to.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# rotateTo

abstract fun rotateTo(bearing: Double, options: MTAnimationOptions? = null)Rotates the map to a given bearing, with an animated transition.
#### Parameters

bearingThe desired bearing in degrees.optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-bearing.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setBearing

abstract fun setBearing(bearing: Double)Sets bearing of the map.
#### Parameters

bearingThe bearing of the map, measured in degrees counter-clockwise from north.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-center-elevation.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setCenterElevation

abstract fun setCenterElevation(elevation: Double)Sets the elevation of the map's center point, in meters above sea level.
#### Parameters

elevationDesired elevation.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-center.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setCenter

abstract fun setCenter(center: LngLat)Sets the geographical center of the map.
#### Parameters

centerGeographical center of the map.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-is-center-clamped-to-ground.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setIsCenterClampedToGround

abstract fun setIsCenterClampedToGround(isCenterClampedToGround: Boolean)Sets the center clamped to the ground.If true, the elevation of the center point will automatically be set to the terrain elevation (or zero if terrain is not enabled). If false, the elevation of the center point will default to sea level and will not automatically update.
#### Parameters

isCenterClampedToGroundBoolean indicating whether center is clamped to the ground.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-max-bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setMaxBounds

abstract fun setMaxBounds(bounds: MTBounds?)Applies or clears the geographical constraints that clamp user interaction.Passing `null` removes the bounds restriction.
#### Parameters

boundsGeographical limits for map interactions, or null to remove restrictions.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-max-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setMaxPitch

abstract fun setMaxPitch(maxPitch: Double)Sets the map's maximum pitch limit.
#### Parameters

maxPitchDesired max pitch in degrees (0-85 default constraints).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-min-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setMinPitch

abstract fun setMinPitch(minPitch: Double)Sets the map's minimum pitch limit.
#### Parameters

minPitchDesired min pitch in degrees (0-85 default constraints).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-padding.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setPadding

abstract fun setPadding(padding: MTPaddingOptions)Sets the padding in pixels around the viewport.
#### Parameters

paddingCustom options to use.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-pitch.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setPitch

abstract fun setPitch(pitch: Double)Sets the map's pitch.
#### Parameters

pitchDesired pitch in degrees (0-85 default constraints).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-pixel-ratio.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setPixelRatio

abstract fun setPixelRatio(pixelRatio: Double)Overrides the pixel ratio used to render the map.
#### Parameters

pixelRatioDesired pixel ratio. Values above `1.0` improve sharpness, values below trade detail for performance.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-roll.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setRoll

abstract fun setRoll(roll: Double)Sets the map's roll angle.
#### Parameters

rollDesired roll.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/set-vertical-field-of-view.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# setVerticalFieldOfView

abstract fun setVerticalFieldOfView(verticalFieldOfView: Double)Sets the map's vertical field of view in degrees (defaults to 36.87 degrees).
#### Parameters

verticalFieldOfViewDesired vertical field of view.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/snap-to-north.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# snapToNorth

abstract fun snapToNorth(options: MTAnimationOptions? = null)Snaps the map so that north is up (bearing 0), animating the transition.
#### Parameters

optionsAnimation options.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/stop.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# stop

abstract fun stop()Stops any animated transition underway.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable/unproject.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/-m-t-navigable"
---
# unproject

abstract suspend fun unproject(point: MTPoint): LngLatUnprojects a point on the container to geographical coordinates.
#### Return

Geographical coordinate.
#### Parameters

pointThe screen-space point in pixels.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.workers.navigable"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.workers.navigable"
id: com.maptiler.maptilersdk.map.workers.navigable
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.workers.navigable"
---
# com.maptiler.maptilersdk.map.workers.navigable

Types

## Types

MTNavigable

interface MTNavigableDefines methods for navigating the map.

---

