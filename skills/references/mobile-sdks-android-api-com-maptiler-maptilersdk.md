# MapTiler Android SDK API Reference - com.maptiler.maptilersdk

This document is a part of the Android SDK API reference documentation, covering the `com.maptiler.maptilersdk` package.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/api-key.html

---
layout: mobile_sdk
title: "apiKey"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "apiKey"
id: api-key
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# apiKey

var apiKey: StringMapTiler API Key

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/index.html

---
layout: mobile_sdk
title: "MTConfig"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTConfig"
id: -m-t-config
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# MTConfig

object MTConfigObject representing the SDK global settings.Exposes properties and options such as API Key and caching preferences.

Members

## Properties

apiKey

var apiKey: StringMapTiler API Key

isCachingEnabled

var isCachingEnabled: BooleanBoolean indicating whether caching is enabled.

isSessionLogicEnabled

var isSessionLogicEnabled: BooleanBoolean indicating whether session logic is enabled.

isTelemetryEnabled

var isTelemetryEnabled: BooleanBoolean indicating whether telemetry is enabled.

logLevel

var logLevel: MTLogLevelSDK log level.

unit

var unit: MTUnitUnit of measurement.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/is-caching-enabled.html

---
layout: mobile_sdk
title: "isCachingEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isCachingEnabled"
id: is-caching-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# isCachingEnabled

var isCachingEnabled: BooleanBoolean indicating whether caching is enabled.Defaults to true.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/is-session-logic-enabled.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# isSessionLogicEnabled

var isSessionLogicEnabled: BooleanBoolean indicating whether session logic is enabled.This allows MapTiler to enable session-based billing. Defaults to true. For more information about sessions, see Map Sessions.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/is-telemetry-enabled.html

---
layout: mobile_sdk
title: "isTelemetryEnabled"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "isTelemetryEnabled"
id: is-telemetry-enabled
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# isTelemetryEnabled

var isTelemetryEnabled: BooleanBoolean indicating whether telemetry is enabled.The telemetry is very valuable to the team at MapTiler because it shares information about where to add extra effort. It also helps spot some incompatibility issues that may arise between the SDK and a specific version of a module. It consists of sending the SDK version, API Key, MapTiler session ID, whether tile caching is enabled, whether a language is specified at initialization, whether terrain is activated at initialization, and whether globe projection is activated at initialization. Defaults to true.
#### See also

https://docs.maptiler.com/guides/maps-apis/maps-platform/what-is-map-session-in-maptiler-cloud/

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/log-level.html

---
layout: mobile_sdk
title: "logLevel"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "logLevel"
id: log-level
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# logLevel

var logLevel: MTLogLevelSDK log level.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config/unit.html

---
layout: mobile_sdk
title: "unit"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "unit"
id: unit
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-config"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# unit

var unit: MTUnitUnit of measurement.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-i-m-p-e-r-i-a-l/index.html

---
layout: mobile_sdk
title: "IMPERIAL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "IMPERIAL"
id: -i-m-p-e-r-i-a-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-i-m-p-e-r-i-a-l"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# IMPERIAL

IMPERIALImperial units.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-m-e-t-r-i-c/index.html

---
layout: mobile_sdk
title: "METRIC"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "METRIC"
id: -m-e-t-r-i-c
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-m-e-t-r-i-c"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# METRIC

METRICMetric units.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-n-a-u-t-i-c-a-l/index.html

---
layout: mobile_sdk
title: "NAUTICAL"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "NAUTICAL"
id: -n-a-u-t-i-c-a-l
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/-n-a-u-t-i-c-a-l"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# NAUTICAL

NAUTICALNautical units.

Members

## Properties

name

val name: String

ordinal

val ordinal: Int

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/entries.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# entries

val entries: EnumEntries<MTUnit>Returns a representation of an immutable list of all enum entries, in the order they're declared.This method may be used to iterate over the enum entries.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/index.html

---
layout: mobile_sdk
title: "MTUnit"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "MTUnit"
id: -m-t-unit
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# MTUnit

enum MTUnit : Enum<MTUnit> Units of measurement used in MTMapView object.

MembersEntries

## Entries

IMPERIAL

IMPERIALImperial units.

METRIC

METRICMetric units.

NAUTICAL

NAUTICALNautical units.

## Properties

entries

val entries: EnumEntries<MTUnit>Returns a representation of an immutable list of all enum entries, in the order they're declared.

name

val name: String

ordinal

val ordinal: Int

## Functions

valueOf

fun valueOf(value: String): MTUnitReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

values

fun values(): Array<MTUnit>Returns an array containing the constants of this enum type, in the order they're declared.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/value-of.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# valueOf

fun valueOf(value: String): MTUnitReturns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
#### Throws

IllegalArgumentExceptionif this enum type has no constant with the specified name

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit/values.html

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
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk/-m-t-unit"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# values

fun values(): Array<MTUnit>Returns an array containing the constants of this enum type, in the order they're declared.This method may be used to iterate over the constants.

---

## File: -map-tiler-s-d-k/com.maptiler.maptilersdk/index.html

---
layout: mobile_sdk
title: "com.maptiler.maptilersdk"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "com.maptiler.maptilersdk"
id: com.maptiler.maptilersdk
breadcrumb: "Mobile SDK/Android/Reference/-map-tiler-s-d-k/com.maptiler.maptilersdk"
---

MapTilerSDK

com.maptiler.maptilersdk

MTConfig

MTUnit

IMPERIAL

METRIC

NAUTICAL

com.maptiler.maptilersdk.annotations

MTAnchor

CENTER

TOP

BOTTOM

LEFT

RIGHT

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTAnnotation

MTCustomAnnotationView()

MTCustomAnnotationViewClassic

MTMarker

MTPitchAlignment

MAP

VIEWPORT

AUTO

MTRotationAlignment

MAP

VIEWPORT

AUTO

MTTextPopup

com.maptiler.maptilersdk.bridge

MTError

BridgeNotLoaded

ExceptionError

InvalidResultType

MissingParent

Unknown

UnsupportedReturnType

MTException

com.maptiler.maptilersdk.colorramp

MTArrayColorRampStop

MTBuiltinColorRamp

NULL

GRAY

JET

HSV

HOT

SPRING

SUMMER

AUTOMN

WINTER

BONE

COPPER

GREYS

YIGNBU

GREENS

YIORRD

BLUERED

RDBU

PICNIC

RAINBOW

PORTLAND

BLACKBODY

EARTH

ELECTRIC

VIRIDIS

INFERNO

MAGMA

PLASMA

WARM

COOL

RAINBOW_SOFT

BATHYMETRY

CDOM

CHLOROPHYLL

DENSITY

FREESURFACE_BLUE

FREESURFACE_RED

OXYGEN

PAR

PHASE

SALINITY

TEMPERATURE

TURBIDITY

VELOCITY_BLUE

VELOCITY_GREEN

CUBEHELIX

CIVIDIS

TURBO

ROCKET

MAKO

MTColorRamp

Companion

MTColorRampBounds

MTColorRampCanvasOptions

MTColorRampCloneOptions

MTColorRampCollection

MTColorRampGetColorOptions

MTColorRampOptions

MTColorRampResamplingMethod

EASE_IN_SQUARE

EASE_OUT_SQUARE

EASE_IN_SQRT

EASE_OUT_SQRT

EASE_IN_EXP

EASE_OUT_EXP

MTColorStop

com.maptiler.maptilersdk.events

EventProcessor

EventProcessorDelegate

MTEvent

ON_BOX_ZOOM_CANCEL

ON_BOX_ZOOM_END

ON_BOX_ZOOM_START

ON_TAP

ON_COOPERATIVE_GESTURE_PREVENTED

ON_DATA_UPDATE

ON_DATA_UPDATE_ABORT

ON_DATA_UPDATE_START

ON_DOUBLE_TAP

ON_DRAG

ON_POPUP_OPEN

ON_POPUP_CLOSE

ON_DRAG_END

ON_DRAG_START

ON_MARKER_DRAG

ON_MARKER_DRAG_END

ON_MARKER_DRAG_START

ON_IDLE

ON_LOAD

ON_LOAD_WITH_TERRAIN

ON_MOVE

ON_MOVE_END

ON_MOVE_START

ON_PITCH_UPDATE

ON_PITCH_UPDATE_END

ON_PITCH_UPDATE_START

ON_PROJECTION_MODIFY

ON_READY

ON_REMOVE

ON_RENDER

ON_RESIZE

ON_ROTATE

ON_ROTATE_END

ON_ROTATE_START

ON_SOURCE_UPDATE

ON_SOURCE_UPDATE_ABORT

ON_SOURCE_UPDATE_START

ON_STYLE_UPDATE

ON_STYLE_UPDATE_START

ON_STYLE_IMAGE_MISSING

ON_TERRAIN_CHANGE

ON_TERRAIN_ANIMATION_START

ON_TERRAIN_ANIMATION_STOP

ON_TOUCH_CANCEL

ON_TOUCH_END

ON_TOUCH_MOVE

ON_TOUCH_START

ON_ZOOM

ON_ZOOM_END

ON_ZOOM_START

com.maptiler.maptilersdk.helpers

JsonConfig

MTBenchmark

MTColorValue

Companion

MTColorValueAsStringSerializer

MTDashArrayOption

Numbers

StringValue

MTDashArrayOptionSerializer

MTHeatmapLayerHelper

MTHeatmapLayerOptions

MTHelperPropertyValue

MTNumberOrPropertyValues

Number

PropertyMap

MTNumberOrPropertyValuesSerializer

MTNumberOrZoomNumberValues

Number

Ramp

MTNumberOrZoomNumberValuesSerializer

MTOutlinePosition

CENTER

INSIDE

OUTSIDE

MTPerformancePresets

MTPitchLimitHelper

MTPointLayerHelper

MTPointLayerOptions

MTPolygonLayerHelper

MTPolygonLayerOptions

MTPolylineLayerHelper

MTPolylineLayerOptions

MTPropertyValues

MTRadiusOption

Number

Property

Zoom

MTRadiusOptionSerializer

MTStringOrZoomStringValues

ColorHex

Companion

Ramp

StringValue

MTStringOrZoomStringValuesSerializer

MTZoomNumberValue

MTZoomNumberValues

MTZoomStringValue

MTZoomStringValues

toHexString()

withBalancedPerformanceDefaults()

withHighFidelityDefaults()

withLeanPerformanceDefaults()

com.maptiler.maptilersdk.location

MTLocationError

PermissionDenied

MTLocationManager

MTLocationManagerDelegate

com.maptiler.maptilersdk.logging

MTLog

MTLoggable

MTLogger

MTLogLevel

Debug

Info

None

MTLogType

INFO

WARNING

ERROR

CRITICAL_ERROR

EVENT

OSLogger

com.maptiler.maptilersdk.map

LngLat

MTMapCameraHelper

Companion

MTMapOptions

MTMapView()

MTMapViewClassic

MTMapViewContentDelegate

MTMapViewController

MTMapViewDelegate

com.maptiler.maptilersdk.map.gestures

MTDoubleTapZoomInGesture

Companion

MTDragPanGesture

Companion

MTGesture

MTGestureService

Companion

MTGestureType

DOUBLE_TAP_ZOOM_IN

DRAG_PAN

TWO_FINGERS_DRAG_PITCH

PINCH_ROTATE_AND_ZOOM

MTPinchRotateAndZoomGesture

Companion

MTTwoFingersDragPitchGesture

Companion

com.maptiler.maptilersdk.map.options

MTAnimationOptions

MTCameraOptions

MTDragPanOptions

MTEventLevel

ESSENTIAL

CAMERA_ONLY

ALL

OFF

MTFitBoundsOptions

MTFlyToOptions

MTHalo

MTHaloOption

Config

Enabled

MTHaloOptionSerializer

MTHaloStop

MTPaddingOptions

MTSky

Companion

MTSpace

MTSpaceFaces

MTSpaceOption

Config

Enabled

MTSpaceOptionSerializer

MTSpacePath

MTSpacePreset

SPACE

STARS

MILKYWAY

MILKYWAY_SUBTLE

MILKYWAY_BRIGHT

MILKYWAY_COLORED

com.maptiler.maptilersdk.map.style

MTMapReferenceStyle

AQUARELLE

BACKDROP

BASIC

BRIGHT

Companion

CUSTOM

DATAVIZ

LANDSCAPE

OCEAN

OPENSTREETMAP

OUTDOOR

SATELLITE

STREETS

TONER

TOPO

WINTER

MTMapStyleVariant

DEFAULT_VARIANT

DARK

LIGHT

PASTEL

NIGHT

SHINY

TOPOGRAPHIQUE

LITE

LINES

BACKGROUND

VIVID

MTStyle

MTStyleError

LayerAlreadyExists

LayerNotFound

SourceAlreadyExists

SourceNotFound

MTTerrainSpecification

MTTileScheme

XYZ

TMS

setCircleColorStep()

setCircleColorStepAwait()

setCircleRadiusStep()

setCircleRadiusStepAwait()

setTextAllowOverlap()

setTextAllowOverlapAwait()

setTextFieldToken()

setTextFieldTokenAwait()

setTextSize()

setTextSizeAwait()

com.maptiler.maptilersdk.map.style.dsl

MTExpression

MTFeatureKey

POINT_COUNT

CLUSTER_ID

MTFilter

MTTextToken

POINT_COUNT_ABBREVIATED

PropertyValue

Arr

Bool

Color

Companion

Num

RawJs

Str

StyleValue

Bool

Color

Expression

Number

Str

com.maptiler.maptilersdk.map.style.image

MTAddImageOptions

com.maptiler.maptilersdk.map.style.layer

MTLayer

MTLayerType

FILL

LINE

SYMBOL

RASTER

CIRCLE

FILL_EXTRUSION

HEATMAP

HILLSHADE

BACKGROUND

MTLayerVisibility

Companion

VISIBLE

NONE

com.maptiler.maptilersdk.map.style.layer.background

MTBackgroundLayer

com.maptiler.maptilersdk.map.style.layer.circle

colorConst()

colorExpr()

MTCircleLayer

MTCirclePitchAlignment

VIEWPORT

MAP

MTCirclePitchScale

VIEWPORT

MAP

MTCircleTranslateAnchor

MAP

VIEWPORT

radiusConst()

radiusExpr()

com.maptiler.maptilersdk.map.style.layer.fill

ColorAsHexSerializer

MTFillLayer

MTFillTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.fillextrusion

MTFillExtrusionLayer

MTFillExtrusionTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.heatmap

colorConst()

colorExpr()

intensityConst()

intensityExpr()

MTHeatmapLayer

opacityConst()

opacityExpr()

radiusConst()

radiusExpr()

weightConst()

weightExpr()

com.maptiler.maptilersdk.map.style.layer.hillshade

MTHillshadeIlluminationAnchor

MAP

VIEWPORT

MTHillshadeLayer

com.maptiler.maptilersdk.map.style.layer.line

MTLineCap

BUTT

ROUND

SQUARE

MTLineJoin

BEVEL

ROUND

MITER

MTLineLayer

MTLineTranslateAnchor

MAP

VIEWPORT

com.maptiler.maptilersdk.map.style.layer.raster

MTRasterLayer

MTRasterResampling

LINEAR

NEAREST

com.maptiler.maptilersdk.map.style.layer.symbol

MTSymbolLayer

MTTextAnchor

Companion

CENTER

LEFT

RIGHT

TOP

BOTTOM

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

textAllowOverlap()

textAnchor()

textColorConst()

textColorExpr()

textField()

textFont()

textSize()

com.maptiler.maptilersdk.map.style.source

MTGeoJSONSource

Companion

MTImageSource

MTRasterDEMEncoding

TERRARIUM

MAPBOX

MTRasterDEMSource

MTRasterTileSource

MTSource

MTSourceType

VECTOR

RASTER

RASTER_DEM

GEOJSON

IMAGE

VIDEO

MTTileSource

MTVectorTileSource

MTVideoSource

URLAsStringSerializer

com.maptiler.maptilersdk.map.types

MTBounds

MTCountryLanguage

ALBANIAN

AMHARIC

ARABIC

ARMENIAN

AZERBAIJANI

BASQUE

BELARUSIAN

BENGALI

BOSNIAN

BRETON

BULGARIAN

CATALAN

CHINESE

TRADITIONAL_CHINESE

SIMPLIFIED_CHINESE

CORSICAN

CROATIAN

CZECH

DANISH

DUTCH

ENGLISH

ESPERANTO

ESTONIAN

FINNISH

FRENCH

FRISIAN

GALICIAN

GEORGIAN

GERMAN

GREEK

HEBREW

HINDI

HUNGARIAN

ICELANDIC

INDONESIAN

IRISH

ITALIAN

JAPANESE

JAPANESE_HIRAGANA

JAPANESE_LATIN

JAPANESE_KANA

KANNADA

KAZAKH

KOREAN

KOREAN_LATIN

KURDISH

CLASSICAL_LATIN

LATVIAN

LITHUANIAN

LUXEMBOURGISH

MACEDONIAN

MALAY

MALTESE

MARATHI

MONGOLIAN

NEPALI

NORWEGIAN

OCCITAN

PERSIAN

POLISH

PORTUGUESE

PUNJABI

WESTERN_PUNJABI

ROMANIAN

ROMANSH

RUSSIAN

SARDINIAN

SCOTTISH_GAELIC

SERBIAN_CYRILLIC

SERBIAN_LATIN

SLOVAK

SLOVENE

SPANISH

SWAHILI

SWEDISH

TAGALOG

TAMIL

TELUGU

THAI

TURKISH

UKRAINIAN

URDU

VIETNAMESE

WELSH

MTData

MTLanguage

Country

Special

MTLanguageSerializer

MTMapCorner

TOP_LEFT

TOP_RIGHT

BOTTOM_LEFT

BOTTOM_RIGHT

MTPoint

MTProjectionType

MERCATOR

GLOBE

MTSourceData

MTSpecialLanguage

AUTO

INTERNATIONAL

LATIN

LOCAL

NON_LATIN

STYLE

VISITOR

VISITOR_ENGLISH

com.maptiler.maptilersdk.map.workers.navigable

MTNavigable

com.maptiler.maptilersdk.map.workers.stylable

MTStylable

com.maptiler.maptilersdk.map.workers.zoomable

MTZoomable

# com.maptiler.maptilersdk

Types

## Types

MTConfig

object MTConfigObject representing the SDK global settings.

MTUnit

enum MTUnit : Enum<MTUnit> Units of measurement used in MTMapView object.

---

