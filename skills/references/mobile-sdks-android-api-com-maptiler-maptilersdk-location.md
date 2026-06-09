# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.location

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.location` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-error/-permission-denied/index.html

---
layout: mobile_sdk
title: "PermissionDenied"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "PermissionDenied"
id: -permission-denied
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-error/-permission-denied"
---
# PermissionDenied

object PermissionDenied : MTLocationErrorLocation permission denied.

Members

## Properties

cause

open val cause: Throwable?

message

open val message: String?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-error/index.html

---
layout: mobile_sdk
title: "MTLocationError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLocationError"
id: -m-t-location-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-error"
---
# MTLocationError

sealed class MTLocationError : ExceptionRepresents MTLocationManager errors.
#### Inheritors

PermissionDenied

Members

## Types

PermissionDenied

object PermissionDenied : MTLocationErrorLocation permission denied.

## Properties

cause

open val cause: Throwable?

message

open val message: String?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/-m-t-location-manager.html

---
layout: mobile_sdk
title: "MTLocationManager"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLocationManager"
id: -m-t-location-manager
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# MTLocationManager

constructor(context: Context, minTimeMs: Long = 1000, minDistanceM: Float = 0.0f)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/delegate.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# delegate

var delegate: MTLocationManagerDelegate?

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/has-location-permission.html

---
layout: mobile_sdk
title: "hasLocationPermission"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "hasLocationPermission"
id: has-location-permission
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# hasLocationPermission

fun hasLocationPermission(): BooleanReturns true if coarse or fine location permission is granted.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/index.html

---
layout: mobile_sdk
title: "MTLocationManager"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLocationManager"
id: -m-t-location-manager
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# MTLocationManager

class MTLocationManager(context: Context, minTimeMs: Long = 1000, minDistanceM: Float = 0.0f)Class responsible for location updates.This manager uses the platform LocationManager and calls delegate callbacks on the main thread. Runtime permission requests must be handled by the app; use hasLocationPermission to check state.

Members

## Constructors

MTLocationManager

constructor(context: Context, minTimeMs: Long = 1000, minDistanceM: Float = 0.0f)

## Properties

delegate

var delegate: MTLocationManagerDelegate?

## Functions

hasLocationPermission

fun hasLocationPermission(): BooleanReturns true if coarse or fine location permission is granted.

requestLocationOnce

fun requestLocationOnce()Requests location only once and calls MTLocationManagerDelegate.didUpdateLocation.

startLocationUpdates

fun startLocationUpdates()Starts the location updates.

stopLocationUpdates

fun stopLocationUpdates()Stops the location updates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/request-location-once.html

---
layout: mobile_sdk
title: "requestLocationOnce"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "requestLocationOnce"
id: request-location-once
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# requestLocationOnce

fun requestLocationOnce()Requests location only once and calls MTLocationManagerDelegate.didUpdateLocation.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/start-location-updates.html

---
layout: mobile_sdk
title: "startLocationUpdates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "startLocationUpdates"
id: start-location-updates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# startLocationUpdates

fun startLocationUpdates()Starts the location updates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager/stop-location-updates.html

---
layout: mobile_sdk
title: "stopLocationUpdates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "stopLocationUpdates"
id: stop-location-updates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager"
---
# stopLocationUpdates

fun stopLocationUpdates()Stops the location updates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate/did-fail-with-error.html

---
layout: mobile_sdk
title: "didFailWithError"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "didFailWithError"
id: did-fail-with-error
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate"
---
# didFailWithError

@MainThreadabstract fun didFailWithError(error: Throwable)Triggered when location updates fail.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate/did-update-location.html

---
layout: mobile_sdk
title: "didUpdateLocation"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "didUpdateLocation"
id: did-update-location
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate"
---
# didUpdateLocation

@MainThreadabstract fun didUpdateLocation(location: Location)Triggered when location updates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate/index.html

---
layout: mobile_sdk
title: "MTLocationManagerDelegate"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTLocationManagerDelegate"
id: -m-t-location-manager-delegate
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location/-m-t-location-manager-delegate"
---
# MTLocationManagerDelegate

interface MTLocationManagerDelegateProtocol requirements for location manager delegate.

Members

## Functions

didFailWithError

@MainThreadabstract fun didFailWithError(error: Throwable)Triggered when location updates fail.

didUpdateLocation

@MainThreadabstract fun didUpdateLocation(location: Location)Triggered when location updates.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.location/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.location"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.location"
id: com.maptiler.maptilersdk.location
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.location"
---
# com.maptiler.maptilersdk.location

Types

## Types

MTLocationError

sealed class MTLocationError : ExceptionRepresents MTLocationManager errors.

MTLocationManager

class MTLocationManager(context: Context, minTimeMs: Long = 1000, minDistanceM: Float = 0.0f)Class responsible for location updates.

MTLocationManagerDelegate

interface MTLocationManagerDelegateProtocol requirements for location manager delegate.

---

