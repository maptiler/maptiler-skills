# MapTiler Android SDK API Reference - root

This document is a part of the Android SDK API reference documentation, covering the `root` package.

---

## File: index.html

---
layout: mobile_sdk
title: "MapTilerSDK"
title_size: regular
category: mobile-sdk-android
categories: mobile-sdk mobile-sdk-android android
group: API Reference
group_number: 999
description: "Complete API reference for MapTiler Kotlin SDK. Detailed technical documentation for building native Android map applications, including classes for map initialization, event handling, and performance throttling."
id: index
breadcrumb: "Mobile SDK/Android/Reference"
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

# MapTilerSDK

## Packages

com.maptiler.maptilersdk

androidJvm

com.maptiler.maptilersdk.annotations

androidJvm

com.maptiler.maptilersdk.bridge

androidJvm

com.maptiler.maptilersdk.colorramp

androidJvm

com.maptiler.maptilersdk.events

androidJvm

com.maptiler.maptilersdk.helpers

androidJvm

com.maptiler.maptilersdk.location

androidJvm

com.maptiler.maptilersdk.logging

androidJvm

com.maptiler.maptilersdk.map

androidJvm

com.maptiler.maptilersdk.map.gestures

androidJvm

com.maptiler.maptilersdk.map.options

androidJvm

com.maptiler.maptilersdk.map.style

androidJvm

com.maptiler.maptilersdk.map.style.dsl

androidJvm

com.maptiler.maptilersdk.map.style.image

androidJvm

com.maptiler.maptilersdk.map.style.layer

androidJvm

com.maptiler.maptilersdk.map.style.layer.background

androidJvm

com.maptiler.maptilersdk.map.style.layer.circle

androidJvm

com.maptiler.maptilersdk.map.style.layer.fill

androidJvm

com.maptiler.maptilersdk.map.style.layer.fillextrusion

androidJvm

com.maptiler.maptilersdk.map.style.layer.heatmap

androidJvm

com.maptiler.maptilersdk.map.style.layer.hillshade

androidJvm

com.maptiler.maptilersdk.map.style.layer.line

androidJvm

com.maptiler.maptilersdk.map.style.layer.raster

androidJvm

com.maptiler.maptilersdk.map.style.layer.symbol

androidJvm

com.maptiler.maptilersdk.map.style.source

androidJvm

com.maptiler.maptilersdk.map.types

androidJvm

com.maptiler.maptilersdk.map.workers.navigable

androidJvm

com.maptiler.maptilersdk.map.workers.stylable

androidJvm

com.maptiler.maptilersdk.map.workers.zoomable

androidJvm

---

