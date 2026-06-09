# MapTiler Android SDK API Reference - com.maptiler.maptilersdk.map.style.source

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk.map.style.source` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion/from-json-string.html

---
layout: mobile_sdk
title: "fromJsonString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fromJsonString"
id: from-json-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion"
---
# fromJsonString

fun fromJsonString(identifier: String, json: String): MTGeoJSONSource

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion/from-url.html

---
layout: mobile_sdk
title: "fromUrl"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "fromUrl"
id: from-url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion"
---
# fromUrl

fun fromUrl(identifier: String, url: URL): MTGeoJSONSource

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion/index.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-companion"
---
# Companion

object Companion

Members

## Functions

fromJsonString

fun fromJsonString(identifier: String, json: String): MTGeoJSONSource

fromUrl

fun fromUrl(identifier: String, url: URL): MTGeoJSONSource

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/-m-t-geo-j-s-o-n-source.html

---
layout: mobile_sdk
title: "MTGeoJSONSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTGeoJSONSource"
id: -m-t-geo-j-s-o-n-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# MTGeoJSONSource

constructor(identifier: String, attribution: String?, url: URL?, jsonString: String?, buffer: Int?, isCluster: Boolean, clusterMaxZoom: Double?, clusterRadius: Double?, maxZoom: Double?, tolerance: Double?, lineMetrics: Boolean?)constructor(identifier: String, url: URL)constructor(identifier: String, jsonString: String)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# attribution

var attribution: String?Attribution to be displayed when the map is shown to a user.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/buffer.html

---
layout: mobile_sdk
title: "buffer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "buffer"
id: buffer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# buffer

var buffer: Int?Size of the tile buffer on each side.Optional number between 0 and 512 inclusive. A value of 0 produces no buffer. A value of 512 produces a buffer as wide as the tile itself. Larger values produce fewer rendering artifacts near tile edges and slower performance. Defaults to 128.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/cluster-max-zoom.html

---
layout: mobile_sdk
title: "clusterMaxZoom"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "clusterMaxZoom"
id: cluster-max-zoom
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# clusterMaxZoom

var clusterMaxZoom: Double?Max zoom on which to cluster points if clustering is enabled.Defaults to one zoom less than maxzoom (so that last zoom features are not clustered).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/cluster-radius.html

---
layout: mobile_sdk
title: "clusterRadius"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "clusterRadius"
id: cluster-radius
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# clusterRadius

var clusterRadius: Double?Radius of each cluster if clustering is enabled.A value of 512 indicates a radius equal to the width of a tile.Defaults to 50.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/index.html

---
layout: mobile_sdk
title: "MTGeoJSONSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTGeoJSONSource"
id: -m-t-geo-j-s-o-n-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# MTGeoJSONSource

@Serializableclass MTGeoJSONSource : MTSourceA geojson source.

Members

## Constructors

MTGeoJSONSource

constructor(identifier: String, attribution: String?, url: URL?, jsonString: String?, buffer: Int?, isCluster: Boolean, clusterMaxZoom: Double?, clusterRadius: Double?, maxZoom: Double?, tolerance: Double?, lineMetrics: Boolean?)constructor(identifier: String, url: URL)constructor(identifier: String, jsonString: String)

## Types

Companion

object Companion

## Properties

attribution

var attribution: String?Attribution to be displayed when the map is shown to a user.

buffer

var buffer: Int?Size of the tile buffer on each side.

clusterMaxZoom

var clusterMaxZoom: Double?Max zoom on which to cluster points if clustering is enabled.

clusterRadius

var clusterRadius: Double?Radius of each cluster if clustering is enabled.

identifier

open override var identifier: StringUnique identifier of a source.

isCluster

@SerialName(value = "cluster")var isCluster: BooleanIf the data is a collection of point features, sets the points by radius into groups.

jsonString

var jsonString: String?GeoJSON String.

lineMetrics

var lineMetrics: Boolean?Specifies whether to calculate line distance metrics

maxZoom

@SerialName(value = "maxzoom")var maxZoom: Double?Maximum zoom level at which to create vector tiles.

tolerance

var tolerance: Double?Douglas-Peucker simplification tolerance.

type

open override var type: MTSourceTypeType of the layer.

url

@Serializable(with = URLAsStringSerializer::class)@SerialName(value = "data")open override var url: URL?A URL to a GeoJSON resource. Supported protocols are http, https.

## Functions

setData

fun setData(data: URL, mapViewController: MTMapViewController)Sets the data of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/is-cluster.html

---
layout: mobile_sdk
title: "isCluster"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isCluster"
id: is-cluster
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# isCluster

@SerialName(value = "cluster")var isCluster: BooleanIf the data is a collection of point features, sets the points by radius into groups.Defaults to false.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/json-string.html

---
layout: mobile_sdk
title: "jsonString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "jsonString"
id: json-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# jsonString

var jsonString: String?GeoJSON String.GeoJSON string parses coordinates as Longitude, Latitude pairs, in that order.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/line-metrics.html

---
layout: mobile_sdk
title: "lineMetrics"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "lineMetrics"
id: line-metrics
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# lineMetrics

var lineMetrics: Boolean?Specifies whether to calculate line distance metrics

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# maxZoom

@SerialName(value = "maxzoom")var maxZoom: Double?Maximum zoom level at which to create vector tiles.Higher value means greater detail at high zoom levels. Defaults to 18.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/set-data.html

---
layout: mobile_sdk
title: "setData"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setData"
id: set-data
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# setData

fun setData(data: URL, mapViewController: MTMapViewController)Sets the data of the source.Used for updating the source data.
#### Parameters

datadata to GeoJSON resource.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/tolerance.html

---
layout: mobile_sdk
title: "tolerance"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tolerance"
id: tolerance
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# tolerance

var tolerance: Double?Douglas-Peucker simplification tolerance.Higher value means simpler geometries and faster performance. Defaults to 0.375

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# type

open override var type: MTSourceTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-geo-j-s-o-n-source"
---
# url

@Serializable(with = URLAsStringSerializer::class)@SerialName(value = "data")open override var url: URL?A URL to a GeoJSON resource. Supported protocols are http, https.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/-m-t-image-source.html

---
layout: mobile_sdk
title: "MTImageSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTImageSource"
id: -m-t-image-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# MTImageSource

constructor(identifier: String, url: URL, coordinates: List<LngLat>)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/coordinates.html

---
layout: mobile_sdk
title: "coordinates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "coordinates"
id: coordinates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# coordinates

var coordinates: List<LngLat>Corners of the image in clockwise order starting at top-left.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/index.html

---
layout: mobile_sdk
title: "MTImageSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTImageSource"
id: -m-t-image-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# MTImageSource

class MTImageSource(var identifier: String, url: URL, var coordinates: List<LngLat>) : MTSourceAn image source.The url value contains the image location. The coordinates array contains longitude, latitude pairs for the image corners listed in clockwise order: top left, top right, bottom right, bottom left.

Members

## Constructors

MTImageSource

constructor(identifier: String, url: URL, coordinates: List<LngLat>)

## Properties

coordinates

var coordinates: List<LngLat>Corners of the image in clockwise order starting at top-left.

identifier

open override var identifier: StringUnique identifier of a source.

type

open override val type: MTSourceTypeType of the source.

url

open override var url: URL?URL pointing to the source resource.

## Functions

setCoordinates

fun setCoordinates(coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates the image corners.

updateImage

fun updateImage(url: URL, coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates both the image URL and its corner coordinates atomically.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/set-coordinates.html

---
layout: mobile_sdk
title: "setCoordinates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setCoordinates"
id: set-coordinates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# setCoordinates

fun setCoordinates(coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates the image corners.
#### Parameters

coordinatesFour coordinates in clockwise order starting at top-left.mapViewControllerMap controller that owns the style.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# type

open override val type: MTSourceTypeType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/update-image.html

---
layout: mobile_sdk
title: "updateImage"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "updateImage"
id: update-image
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# updateImage

fun updateImage(url: URL, coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates both the image URL and its corner coordinates atomically.
#### Parameters

urlNew image URL.coordinatesFour coordinates in clockwise order starting at top-left.mapViewControllerMap controller that owns the style.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-image-source"
---
# url

open override var url: URL?URL pointing to the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/-m-a-p-b-o-x/index.html

---
layout: mobile_sdk
title: "MAPBOX"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MAPBOX"
id: -m-a-p-b-o-x
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/-m-a-p-b-o-x"
---
# MAPBOX

@SerialName(value = "mapbox")MAPBOXTerrain RGB tiles (Mapbox/MapTiler RGB Terrain).

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/-t-e-r-r-a-r-i-u-m/index.html

---
layout: mobile_sdk
title: "TERRARIUM"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "TERRARIUM"
id: -t-e-r-r-a-r-i-u-m
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/-t-e-r-r-a-r-i-u-m"
---
# TERRARIUM

@SerialName(value = "terrarium")TERRARIUMTerrarium format PNG tiles.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/entries.html

---
layout: mobile_sdk
title: "entries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "entries"
id: entries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding"
---
# entries

val entries: EnumEntries<MTRasterDEMEncoding>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/index.html

---
layout: mobile_sdk
title: "MTRasterDEMEncoding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterDEMEncoding"
id: -m-t-raster-d-e-m-encoding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding"
---
# MTRasterDEMEncoding

@Serializableenum MTRasterDEMEncoding : Enum<MTRasterDEMEncoding> Encoding types for Raster DEM sources.

MembersEntries

## Entries

TERRARIUM

@SerialName(value = "terrarium")TERRARIUMTerrarium format PNG tiles.

MAPBOX

@SerialName(value = "mapbox")MAPBOXTerrain RGB tiles (Mapbox/MapTiler RGB Terrain).

## Properties

entries

val entries: EnumEntries<MTRasterDEMEncoding>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

valueOf

fun valueOf(value: String): MTRasterDEMEncodingReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTRasterDEMEncoding>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/to-string.html

---
layout: mobile_sdk
title: "toString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "toString"
id: to-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding"
---
# toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/value-of.html

---
layout: mobile_sdk
title: "valueOf"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "valueOf"
id: value-of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding"
---
# valueOf

fun valueOf(value: String): MTRasterDEMEncodingReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding/values.html

---
layout: mobile_sdk
title: "values"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "values"
id: values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-encoding"
---
# values

fun values(): Array<MTRasterDEMEncoding>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/-m-t-raster-d-e-m-source.html

---
layout: mobile_sdk
title: "MTRasterDEMSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterDEMSource"
id: -m-t-raster-d-e-m-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# MTRasterDEMSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, tileSize: Int, encoding: MTRasterDEMEncoding)constructor(identifier: String, url: URL)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat. Defaults to -180, -85.051129, 180, 85.051129.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/encoding.html

---
layout: mobile_sdk
title: "encoding"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "encoding"
id: encoding
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# encoding

var encoding: MTRasterDEMEncodingThe encoding used by this source. One of "terrarium" or "mapbox" (Terrain RGB). Defaults to MAPBOX.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/index.html

---
layout: mobile_sdk
title: "MTRasterDEMSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterDEMSource"
id: -m-t-raster-d-e-m-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# MTRasterDEMSource

class MTRasterDEMSource : MTTileSourceA raster DEM source. Only supports Terrain RGB encodings.For MapTiler Terrain RGB, the URL should typically point to a TileJSON resource.

Members

## Constructors

MTRasterDEMSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, tileSize: Int, encoding: MTRasterDEMEncoding)constructor(identifier: String, url: URL)

## Properties

attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat. Defaults to -180, -85.051129, 180, 85.051129.

encoding

var encoding: MTRasterDEMEncodingThe encoding used by this source. One of "terrarium" or "mapbox" (Terrain RGB). Defaults to MAPBOX.

identifier

open override var identifier: StringUnique identifier of a source.

maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available. Defaults to 22.

minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available. Defaults to 0.

tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

tileSize

var tileSize: IntTile size in pixels. Defaults to 512.

type

open override var type: MTSourceTypeType of the source.

url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

## Functions

setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source. Used for updating the source data.

setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source. Used for updating the source data.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available. Defaults to 22.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/set-tiles.html

---
layout: mobile_sdk
title: "setTiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTiles"
id: set-tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source. Used for updating the source data.
#### Parameters

tileslist of URLs with tile resources.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/set-u-r-l.html

---
layout: mobile_sdk
title: "setURL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setURL"
id: set-u-r-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source. Used for updating the source data.
#### Parameters

urlURL to raster DEM TileJSON resource.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/tile-size.html

---
layout: mobile_sdk
title: "tileSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tileSize"
id: tile-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# tileSize

var tileSize: IntTile size in pixels. Defaults to 512.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/tiles.html

---
layout: mobile_sdk
title: "tiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tiles"
id: tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# type

open override var type: MTSourceTypeType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-d-e-m-source"
---
# url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/-m-t-raster-tile-source.html

---
layout: mobile_sdk
title: "MTRasterTileSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterTileSource"
id: -m-t-raster-tile-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# MTRasterTileSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, scheme: MTTileScheme, tileSize: Int)constructor(identifier: String, url: URL)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat. Defaults to -180, -85.051129, 180, 85.051129.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/index.html

---
layout: mobile_sdk
title: "MTRasterTileSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTRasterTileSource"
id: -m-t-raster-tile-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# MTRasterTileSource

class MTRasterTileSource : MTTileSourceA raster tile source. Tiles must be in ZXY or TMS tile format. For raster tiles hosted by MapTiler, the URL should be of the form: https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=

Members

## Constructors

MTRasterTileSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, scheme: MTTileScheme, tileSize: Int)constructor(identifier: String, url: URL)

## Properties

attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat. Defaults to -180, -85.051129, 180, 85.051129.

identifier

open override var identifier: StringUnique identifier of a source.

maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available. Defaults to 22.

minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available. Defaults to 0.

scheme

var scheme: MTTileSchemeScheme used for tiles. Influences the y direction of the tile coordinates. Defaults to XYZ.

tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

tileSize

var tileSize: IntTile size in pixels. Only configurable for raster sources. Defaults to 512.

type

open override var type: MTSourceTypeType of the source.

url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

## Functions

setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source. Used for updating the source data.

setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source. Used for updating the source data.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available. Defaults to 22.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available. Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/scheme.html

---
layout: mobile_sdk
title: "scheme"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "scheme"
id: scheme
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# scheme

var scheme: MTTileSchemeScheme used for tiles. Influences the y direction of the tile coordinates. Defaults to XYZ.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/set-tiles.html

---
layout: mobile_sdk
title: "setTiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTiles"
id: set-tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source. Used for updating the source data.
#### Parameters

tileslist of URLs with tile resources.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/set-u-r-l.html

---
layout: mobile_sdk
title: "setURL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setURL"
id: set-u-r-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source. Used for updating the source data.
#### Parameters

urlURL to raster TileJSON resource.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/tile-size.html

---
layout: mobile_sdk
title: "tileSize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tileSize"
id: tile-size
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# tileSize

var tileSize: IntTile size in pixels. Only configurable for raster sources. Defaults to 512.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/tiles.html

---
layout: mobile_sdk
title: "tiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tiles"
id: tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# type

open override var type: MTSourceTypeType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-raster-tile-source"
---
# url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source"
---
# identifier

abstract var identifier: StringUnique id of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source/index.html

---
layout: mobile_sdk
title: "MTSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSource"
id: -m-t-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source"
---
# MTSource

interface MTSourceProtocol requirements for all types of Sources.
#### Inheritors

MTGeoJSONSourceMTImageSourceMTTileSourceMTVideoSource

Members

## Properties

identifier

abstract var identifier: StringUnique id of the source.

type

abstract val type: MTSourceTypeType of the source.

url

abstract var url: URL?URL pointing to the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source"
---
# type

abstract val type: MTSourceTypeType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source"
---
# url

abstract var url: URL?URL pointing to the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-g-e-o-j-s-o-n/index.html

---
layout: mobile_sdk
title: "GEOJSON"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "GEOJSON"
id: -g-e-o-j-s-o-n
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-g-e-o-j-s-o-n"
---
# GEOJSON

@SerialName(value = "geojson")GEOJSONGeoJSON source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-i-m-a-g-e/index.html

---
layout: mobile_sdk
title: "IMAGE"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "IMAGE"
id: -i-m-a-g-e
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-i-m-a-g-e"
---
# IMAGE

@SerialName(value = "image")IMAGEImage source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-r-a-s-t-e-r/index.html

---
layout: mobile_sdk
title: "RASTER"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RASTER"
id: -r-a-s-t-e-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-r-a-s-t-e-r"
---
# RASTER

@SerialName(value = "raster")RASTERRaster tile source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-r-a-s-t-e-r_-d-e-m/index.html

---
layout: mobile_sdk
title: "RASTER_DEM"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "RASTER_DEM"
id: -r-a-s-t-e-r_-d-e-m
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-r-a-s-t-e-r_-d-e-m"
---
# RASTER_DEM

@SerialName(value = "raster-dem")RASTER_DEMRaster DEM source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-v-e-c-t-o-r/index.html

---
layout: mobile_sdk
title: "VECTOR"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VECTOR"
id: -v-e-c-t-o-r
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-v-e-c-t-o-r"
---
# VECTOR

@SerialName(value = "vector")VECTORVector tile source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-v-i-d-e-o/index.html

---
layout: mobile_sdk
title: "VIDEO"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "VIDEO"
id: -v-i-d-e-o
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/-v-i-d-e-o"
---
# VIDEO

@SerialName(value = "video")VIDEOVideo source.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/entries.html

---
layout: mobile_sdk
title: "entries"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "entries"
id: entries
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type"
---
# entries

val entries: EnumEntries<MTSourceType>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/index.html

---
layout: mobile_sdk
title: "MTSourceType"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTSourceType"
id: -m-t-source-type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type"
---
# MTSourceType

@Serializableenum MTSourceType : Enum<MTSourceType> Types of sources.Sources state which data the map should display.

MembersEntries

## Entries

VECTOR

@SerialName(value = "vector")VECTORVector tile source.

RASTER

@SerialName(value = "raster")RASTERRaster tile source.

RASTER_DEM

@SerialName(value = "raster-dem")RASTER_DEMRaster DEM source.

GEOJSON

@SerialName(value = "geojson")GEOJSONGeoJSON source.

IMAGE

@SerialName(value = "image")IMAGEImage source.

VIDEO

@SerialName(value = "video")VIDEOVideo source.

## Properties

entries

val entries: EnumEntries<MTSourceType>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

toString

open override fun toString(): <Error class: unknown class>

valueOf

fun valueOf(value: String): MTSourceTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTSourceType>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/to-string.html

---
layout: mobile_sdk
title: "toString"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "toString"
id: to-string
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type"
---
# toString

open override fun toString(): <Error class: unknown class>

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/value-of.html

---
layout: mobile_sdk
title: "valueOf"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "valueOf"
id: value-of
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type"
---
# valueOf

fun valueOf(value: String): MTSourceTypeReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type/values.html

---
layout: mobile_sdk
title: "values"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "values"
id: values
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-source-type"
---
# values

fun values(): Array<MTSourceType>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# attribution

abstract var attribution: String?Attribution string.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# bounds

abstract var bounds: DoubleArrayBounds of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/index.html

---
layout: mobile_sdk
title: "MTTileSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTTileSource"
id: -m-t-tile-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# MTTileSource

interface MTTileSource : MTSourceProtocol requirements for all tile type sources.
#### Inheritors

MTRasterDEMSourceMTRasterTileSourceMTVectorTileSource

Members

## Properties

attribution

abstract var attribution: String?Attribution string.

bounds

abstract var bounds: DoubleArrayBounds of the source.

identifier

abstract var identifier: StringUnique id of the source.

maxZoom

abstract var maxZoom: DoubleMax zoom of the source.

minZoom

abstract var minZoom: DoubleMin zoom of the source.

tiles

abstract var tiles: Array<URL>?List of URLs pointing to the tiles resources.

type

abstract val type: MTSourceTypeType of the source.

url

abstract var url: URL?URL pointing to the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# maxZoom

abstract var maxZoom: DoubleMax zoom of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# minZoom

abstract var minZoom: DoubleMin zoom of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source/tiles.html

---
layout: mobile_sdk
title: "tiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tiles"
id: tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-tile-source"
---
# tiles

abstract var tiles: Array<URL>?List of URLs pointing to the tiles resources.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/-m-t-vector-tile-source.html

---
layout: mobile_sdk
title: "MTVectorTileSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTVectorTileSource"
id: -m-t-vector-tile-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# MTVectorTileSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, scheme: MTTileScheme)constructor(identifier: String, url: URL)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/attribution.html

---
layout: mobile_sdk
title: "attribution"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "attribution"
id: attribution
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/bounds.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat.Defaults to -180, -85.051129, 180, 85.051129.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/index.html

---
layout: mobile_sdk
title: "MTVectorTileSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTVectorTileSource"
id: -m-t-vector-tile-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# MTVectorTileSource

class MTVectorTileSource : MTTileSourceA vector tile source.

Members

## Constructors

MTVectorTileSource

constructor(identifier: String, attribution: String?, bounds: DoubleArray, maxZoom: Double, minZoom: Double, tiles: Array<URL>?, url: URL?, type: MTSourceType, scheme: MTTileScheme)constructor(identifier: String, url: URL)

## Properties

attribution

open override var attribution: String?Attribution to be displayed when the map is shown to a user.

bounds

open override var bounds: DoubleArrayAn array containing the longitude and latitude of the southwest and northeast corners of the source’s bounding box in the following order: sw.lng, sw.lat, ne.lng, ne.lat.

identifier

open override var identifier: StringUnique identifier of a source.

maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available.

minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available.

scheme

var scheme: MTTileSchemeScheme used for tiles. Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator) is assumed.

tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

type

open override var type: MTSourceTypeType of the layer.

url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

## Functions

setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source.

setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/max-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# maxZoom

open override var maxZoom: DoubleMaximum zoom level for which tiles are available.Defaults to 22.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/min-zoom.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# minZoom

open override var minZoom: DoubleMinimum zoom level for which tiles are available.Defaults to 0.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/scheme.html

---
layout: mobile_sdk
title: "scheme"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "scheme"
id: scheme
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# scheme

var scheme: MTTileSchemeScheme used for tiles. Influences the y direction of the tile coordinates. The global-mercator (aka Spherical Mercator) is assumed.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/set-tiles.html

---
layout: mobile_sdk
title: "setTiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setTiles"
id: set-tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# setTiles

fun setTiles(tiles: Array<URL>, mapViewController: MTMapViewController)Sets the tiles of the source.Used for updating the source data.
#### Parameters

tileslist of urls with tile resources.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/set-u-r-l.html

---
layout: mobile_sdk
title: "setURL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setURL"
id: set-u-r-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# setURL

fun setURL(url: URL, mapViewController: MTMapViewController)Sets the url of the source.Used for updating the source data.
#### Parameters

urlurl to Vector Tile resource.mapViewControllerMTMapViewController which holds the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/tiles.html

---
layout: mobile_sdk
title: "tiles"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "tiles"
id: tiles
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# tiles

open override var tiles: Array<URL>?An array of one or more tile source URLs.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# type

open override var type: MTSourceTypeType of the layer.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-vector-tile-source"
---
# url

open override var url: URL?A URL to a TileJSON resource. Supported protocols are http, https.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/-m-t-video-source.html

---
layout: mobile_sdk
title: "MTVideoSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTVideoSource"
id: -m-t-video-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# MTVideoSource

constructor(identifier: String, urls: List<URL>, coordinates: List<LngLat>)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/coordinates.html

---
layout: mobile_sdk
title: "coordinates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "coordinates"
id: coordinates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# coordinates

var coordinates: List<LngLat>Corners of the video in clockwise order starting at top-left.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/identifier.html

---
layout: mobile_sdk
title: "identifier"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "identifier"
id: identifier
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# identifier

open override var identifier: StringUnique identifier of a source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/index.html

---
layout: mobile_sdk
title: "MTVideoSource"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTVideoSource"
id: -m-t-video-source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# MTVideoSource

class MTVideoSource(var identifier: String, var urls: List<URL>, var coordinates: List<LngLat>) : MTSourceA video source.The urls value contains the video locations in preferred order. The coordinates array contains longitude, latitude pairs for the video corners listed in clockwise order: top left, top right, bottom right, bottom left.

Members

## Constructors

MTVideoSource

constructor(identifier: String, urls: List<URL>, coordinates: List<LngLat>)

## Properties

coordinates

var coordinates: List<LngLat>Corners of the video in clockwise order starting at top-left.

identifier

open override var identifier: StringUnique identifier of a source.

type

open override val type: MTSourceTypeType of the source.

url

open override var url: URL?URL pointing to the source resource.

urls

var urls: List<URL>URLs pointing to the video in preferred order (format variants).

## Functions

setCoordinates

fun setCoordinates(coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates the video corners.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/set-coordinates.html

---
layout: mobile_sdk
title: "setCoordinates"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "setCoordinates"
id: set-coordinates
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# setCoordinates

fun setCoordinates(coordinates: List<LngLat>, mapViewController: MTMapViewController)Updates the video corners.
#### Parameters

coordinatesFour coordinates in clockwise order starting at top-left.mapViewControllerMap controller that owns the style.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/type.html

---
layout: mobile_sdk
title: "type"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "type"
id: type
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# type

open override val type: MTSourceTypeType of the source.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/url.html

---
layout: mobile_sdk
title: "url"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "url"
id: url
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# url

open override var url: URL?URL pointing to the source resource.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source/urls.html

---
layout: mobile_sdk
title: "urls"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "urls"
id: urls
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-m-t-video-source"
---
# urls

var urls: List<URL>URLs pointing to the video in preferred order (format variants).

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer/descriptor.html

---
layout: mobile_sdk
title: "descriptor"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "descriptor"
id: descriptor
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer"
---
# descriptor

open override val descriptor: SerialDescriptor

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer/deserialize.html

---
layout: mobile_sdk
title: "deserialize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "deserialize"
id: deserialize
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer"
---
# deserialize

open override fun deserialize(decoder: Decoder): URL

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer/index.html

---
layout: mobile_sdk
title: "URLAsStringSerializer"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "URLAsStringSerializer"
id: -u-r-l-as-string-serializer
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer"
---
# URLAsStringSerializer

object URLAsStringSerializer : KSerializer<URL> 

Members

## Properties

descriptor

open override val descriptor: SerialDescriptor

## Functions

deserialize

open override fun deserialize(decoder: Decoder): URL

serialize

open override fun serialize(encoder: Encoder, value: URL)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer/serialize.html

---
layout: mobile_sdk
title: "serialize"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "serialize"
id: serialize
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/-u-r-l-as-string-serializer"
---
# serialize

open override fun serialize(encoder: Encoder, value: URL)

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk.map.style.source"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk.map.style.source"
id: com.maptiler.maptilersdk.map.style.source
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk.map.style.source"
---
# com.maptiler.maptilersdk.map.style.source

Types

## Types

MTGeoJSONSource

@Serializableclass MTGeoJSONSource : MTSourceA geojson source.

MTImageSource

class MTImageSource(var identifier: String, url: URL, var coordinates: List<LngLat>) : MTSourceAn image source.

MTRasterDEMEncoding

@Serializableenum MTRasterDEMEncoding : Enum<MTRasterDEMEncoding> Encoding types for Raster DEM sources.

MTRasterDEMSource

class MTRasterDEMSource : MTTileSourceA raster DEM source. Only supports Terrain RGB encodings.

MTRasterTileSource

class MTRasterTileSource : MTTileSourceA raster tile source. Tiles must be in ZXY or TMS tile format. For raster tiles hosted by MapTiler, the URL should be of the form: https://api.maptiler.com/tiles/[tilesetid]/tiles.json?key=

MTSource

interface MTSourceProtocol requirements for all types of Sources.

MTSourceType

@Serializableenum MTSourceType : Enum<MTSourceType> Types of sources.

MTTileSource

interface MTTileSource : MTSourceProtocol requirements for all tile type sources.

MTVectorTileSource

class MTVectorTileSource : MTTileSourceA vector tile source.

MTVideoSource

class MTVideoSource(var identifier: String, var urls: List<URL>, var coordinates: List<LngLat>) : MTSourceA video source.

URLAsStringSerializer

object URLAsStringSerializer : KSerializer<URL>

---

