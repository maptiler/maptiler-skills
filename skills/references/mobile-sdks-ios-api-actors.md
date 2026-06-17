# MapTiler iOS SDK API Reference - Actors

This document is a part of the iOS SDK API reference documentation, covering the `Actors` category.

---

## File: Actors/MTConfig.html

---
layout: mobile_sdk
title: "MTConfig"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Object representing the SDK global settings."
id: mtconfig
breadcrumb: "Mobile SDK/iOS/Reference/Actors"
---

# MTConfig

`public actor MTConfig`

Object representing the SDK global settings.

Exposes properties and options such as API Key and caching preferences.

- 

shared

Undocumented

#### Declaration

Swift
`public static let shared: MTConfig`

- 

logLevel

SDK log level.

#### Declaration

Swift
`public private(set) var logLevel: MTLogLevel { get }`

- 

isCachingEnabled

Boolean indicating whether caching is enabled.

Note
Defaults to true.

#### Declaration

Swift
`public private(set) var isCachingEnabled: Bool { get }`

- 

isSessionLogicEnabled

Boolean indicating whether session logic is enabled.

This allows MapTiler to enable “session based billing”.

Note
Defaults to true.

See also
`https://docs.maptiler.com/guides/maps-apis/maps-platform/what-is-map-session-in-maptiler-cloud/`

#### Declaration

Swift
`public private(set) var isSessionLogicEnabled: Bool { get }`

- 

isTelemetryEnabled

Boolean indicating whether telemetry is enabled.

The telemetry is very valuable to the team at MapTiler because it shares information about
where to add the extra effort. It also helps spotting some incompatibility issues that may
arise between the SDK and a specific version of a module. It consist in sending the SDK version,
API Key, MapTiler session ID, if tile caching is enabled, if language specified at initialization,
if terrain is activated at initialization, if globe projection is activated at initialization.

Note
Defaults to true.

#### Declaration

Swift
`public private(set) var isTelemetryEnabled: Bool { get }`

- 

setLogLevel(_:)

Sets the SDK log level.

#### Declaration

Swift
`public func setLogLevel(_ level: MTLogLevel)`

#### Parameters

| level | The desired SDK log level. |

- 

setAPIKey(_:for:)

Sets the MapTiler API key.

#### Declaration

Swift
`public func setAPIKey(_ apiKey: String, for map: MTMapView? = nil)`

#### Parameters

| apiKey | The MapTiler API Key. |
| map | Map view to apply to. |

- 

getAPIKey()

Returns the MapTiler API key.

#### Declaration

Swift
`public func getAPIKey() -> String?`

- 

setCaching(_:for:)

Sets the caching mechanism.

Note
Enabled by default

#### Declaration

Swift
`public func setCaching(_ isEnabled: Bool, for map: MTMapView)`

#### Parameters

| isEnabled | Boolean indicating whether caching is enabled. |
| map | Map view to apply to. |

- 

setSessionLogic(_:for:)

Sets the session logic.

Make sure to call before map init or use MTMapOptions to supply before map init.

Note
Enabled by default

See also
`https://docs.maptiler.com/guides/maps-apis/maps-platform/what-is-map-session-in-maptiler-cloud/`

#### Declaration

Swift
`public func setSessionLogic(_ isEnabled: Bool, for map: MTMapView)`

#### Parameters

| isEnabled | Boolean indicating whether session logic is enabled. |
| map | Map view to apply to. |

- 

setUnit(_:for:)

Sets the unit of measurement.

Note
Default: .metric

#### Declaration

Swift
`public func setUnit(_ unit: MTUnit, for map: MTMapView)`

#### Parameters

| unit | The MTUnit type. |
| map | Map view to apply to. |

- 

getUnit()

Returns the unit of measurement.

#### Declaration

Swift
`public func getUnit() -> MTUnit?`

- 

setTelemetry(_:for:)

Sets the telemetry.

Note
Enabled by default

#### Declaration

Swift
`public func setTelemetry(_ isEnabled: Bool, for map: MTMapView)`

#### Parameters

| isEnabled | Boolean indicating whether telemetry is enabled. |
| map | Map view to apply to. |

---

