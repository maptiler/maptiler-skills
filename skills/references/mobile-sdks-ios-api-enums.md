# MapTiler iOS SDK API Reference - Enums

This document is a part of the iOS SDK API reference documentation, covering the `Enums` category.

---

## File: Enums/MTAnchor.html

---
layout: mobile_sdk
title: "MTAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Anchor positions for marker placement."
id: mtanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTAnchor

`public enum MTAnchor : String, Sendable, Codable`

Anchor positions for marker placement.

- 

center

Undocumented

#### Declaration

Swift
`case center`

- 

left

Undocumented

#### Declaration

Swift
`case left`

- 

right

Undocumented

#### Declaration

Swift
`case right`

- 

top

Undocumented

#### Declaration

Swift
`case top`

- 

bottom

Undocumented

#### Declaration

Swift
`case bottom`

- 

topLeft

Undocumented

#### Declaration

Swift
`case topLeft = "top-left"`

- 

topRight

Undocumented

#### Declaration

Swift
`case topRight = "top-right"`

- 

bottomLeft

Undocumented

#### Declaration

Swift
`case bottomLeft = "bottom-left"`

- 

bottomRight

Undocumented

#### Declaration

Swift
`case bottomRight = "bottom-right"`

---

## File: Enums/MTCirclePaintProperty.html

---
layout: mobile_sdk
title: "MTCirclePaintProperty"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Typed keys for circle paint properties."
id: mtcirclepaintproperty
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTCirclePaintProperty

`public enum MTCirclePaintProperty : String, Sendable`

Typed keys for circle paint properties.

- 

blur

Undocumented

#### Declaration

Swift
`case blur = "circle-blur"`

- 

color

Undocumented

#### Declaration

Swift
`case color = "circle-color"`

- 

opacity

Undocumented

#### Declaration

Swift
`case opacity = "circle-opacity"`

- 

radius

Undocumented

#### Declaration

Swift
`case radius = "circle-radius"`

- 

strokeColor

Undocumented

#### Declaration

Swift
`case strokeColor = "circle-stroke-color"`

- 

strokeOpacity

Undocumented

#### Declaration

Swift
`case strokeOpacity = "circle-stroke-opacity"`

- 

strokeWidth

Undocumented

#### Declaration

Swift
`case strokeWidth = "circle-stroke-width"`

- 

translate

Undocumented

#### Declaration

Swift
`case translate = "circle-translate"`

- 

translateAnchor

Undocumented

#### Declaration

Swift
`case translateAnchor = "circle-translate-anchor"`

- 

pitchAlignment

Undocumented

#### Declaration

Swift
`case pitchAlignment = "circle-pitch-alignment"`

- 

pitchScale

Undocumented

#### Declaration

Swift
`case pitchScale = "circle-pitch-scale"`

---

## File: Enums/MTCirclePitchAlignment.html

---
layout: mobile_sdk
title: "MTCirclePitchAlignment"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Orientation of the circle when map is pitched."
id: mtcirclepitchalignment
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTCirclePitchAlignment

`public enum MTCirclePitchAlignment : String`

Orientation of the circle when map is pitched.

- 

map

Undocumented

#### Declaration

Swift
`case map`

- 

viewport

Undocumented

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTCirclePitchScale.html

---
layout: mobile_sdk
title: "MTCirclePitchScale"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Controls the scaling behavior of the circle when the map is pitched."
id: mtcirclepitchscale
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTCirclePitchScale

`public enum MTCirclePitchScale : String`

Controls the scaling behavior of the circle when the map is pitched.

- 

map

Undocumented

#### Declaration

Swift
`case map`

- 

viewport

Undocumented

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTCircleTranslateAnchor.html

---
layout: mobile_sdk
title: "MTCircleTranslateAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Controls the frame of reference for circle translate."
id: mtcircletranslateanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTCircleTranslateAnchor

`public enum MTCircleTranslateAnchor : String`

Controls the frame of reference for circle translate.

- 

map

The circle is translated relative to the map.

#### Declaration

Swift
`case map`

- 

viewport

The circle is translated relative to the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTColorRampPreset.html

---
layout: mobile_sdk
title: "MTColorRampPreset"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Built-in presets shipped with the SDK."
id: mtcolorramppreset
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTColorRampPreset

`public enum MTColorRampPreset : String, Sendable, Codable, CaseIterable`

Built-in presets shipped with the SDK.

- 

null

Undocumented

#### Declaration

Swift
`case null = "NULL"`

- 

gray

Undocumented

#### Declaration

Swift
`case gray = "GRAY"`

- 

jet

Undocumented

#### Declaration

Swift
`case jet = "JET"`

- 

hsv

Undocumented

#### Declaration

Swift
`case hsv = "HSV"`

- 

hot

Undocumented

#### Declaration

Swift
`case hot = "HOT"`

- 

spring

Undocumented

#### Declaration

Swift
`case spring = "SPRING"`

- 

summer

Undocumented

#### Declaration

Swift
`case summer = "SUMMER"`

- 

automn

Undocumented

#### Declaration

Swift
`case automn = "AUTOMN"`

- 

winter

Undocumented

#### Declaration

Swift
`case winter = "WINTER"`

- 

bone

Undocumented

#### Declaration

Swift
`case bone = "BONE"`

- 

copper

Undocumented

#### Declaration

Swift
`case copper = "COPPER"`

- 

greys

Undocumented

#### Declaration

Swift
`case greys = "GREYS"`

- 

yignbu

Undocumented

#### Declaration

Swift
`case yignbu = "YIGNBU"`

- 

greens

Undocumented

#### Declaration

Swift
`case greens = "GREENS"`

- 

yiorrd

Undocumented

#### Declaration

Swift
`case yiorrd = "YIORRD"`

- 

bluered

Undocumented

#### Declaration

Swift
`case bluered = "BLUERED"`

- 

rdbu

Undocumented

#### Declaration

Swift
`case rdbu = "RDBU"`

- 

picnic

Undocumented

#### Declaration

Swift
`case picnic = "PICNIC"`

- 

rainbow

Undocumented

#### Declaration

Swift
`case rainbow = "RAINBOW"`

- 

portland

Undocumented

#### Declaration

Swift
`case portland = "PORTLAND"`

- 

blackbody

Undocumented

#### Declaration

Swift
`case blackbody = "BLACKBODY"`

- 

earth

Undocumented

#### Declaration

Swift
`case earth = "EARTH"`

- 

electric

Undocumented

#### Declaration

Swift
`case electric = "ELECTRIC"`

- 

viridis

Undocumented

#### Declaration

Swift
`case viridis = "VIRIDIS"`

- 

inferno

Undocumented

#### Declaration

Swift
`case inferno = "INFERNO"`

- 

magma

Undocumented

#### Declaration

Swift
`case magma = "MAGMA"`

- 

plasma

Undocumented

#### Declaration

Swift
`case plasma = "PLASMA"`

- 

warm

Undocumented

#### Declaration

Swift
`case warm = "WARM"`

- 

cool

Undocumented

#### Declaration

Swift
`case cool = "COOL"`

- 

rainbowSoft

Undocumented

#### Declaration

Swift
`case rainbowSoft = "RAINBOW_SOFT"`

- 

bathymetry

Undocumented

#### Declaration

Swift
`case bathymetry = "BATHYMETRY"`

- 

cdom

Undocumented

#### Declaration

Swift
`case cdom = "CDOM"`

- 

chlorophyll

Undocumented

#### Declaration

Swift
`case chlorophyll = "CHLOROPHYLL"`

- 

density

Undocumented

#### Declaration

Swift
`case density = "DENSITY"`

- 

freesurfaceBlue

Undocumented

#### Declaration

Swift
`case freesurfaceBlue = "FREESURFACE_BLUE"`

- 

freesurfaceRed

Undocumented

#### Declaration

Swift
`case freesurfaceRed = "FREESURFACE_RED"`

- 

oxygen

Undocumented

#### Declaration

Swift
`case oxygen = "OXYGEN"`

- 

par

Undocumented

#### Declaration

Swift
`case par = "PAR"`

- 

phase

Undocumented

#### Declaration

Swift
`case phase = "PHASE"`

- 

salinity

Undocumented

#### Declaration

Swift
`case salinity = "SALINITY"`

- 

temperature

Undocumented

#### Declaration

Swift
`case temperature = "TEMPERATURE"`

- 

turbidity

Undocumented

#### Declaration

Swift
`case turbidity = "TURBIDITY"`

- 

velocityBlue

Undocumented

#### Declaration

Swift
`case velocityBlue = "VELOCITY_BLUE"`

- 

velocityGreen

Undocumented

#### Declaration

Swift
`case velocityGreen = "VELOCITY_GREEN"`

- 

cubehelix

Undocumented

#### Declaration

Swift
`case cubehelix = "CUBEHELIX"`

- 

cividis

Undocumented

#### Declaration

Swift
`case cividis = "CIVIDIS"`

- 

turbo

Undocumented

#### Declaration

Swift
`case turbo = "TURBO"`

- 

rocket

Undocumented

#### Declaration

Swift
`case rocket = "ROCKET"`

- 

mako

Undocumented

#### Declaration

Swift
`case mako = "MAKO"`

---

## File: Enums/MTColorRampResampleMethod.html

---
layout: mobile_sdk
title: "MTColorRampResampleMethod"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Resampling methods supported by MapTiler SDK."
id: mtcolorrampresamplemethod
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTColorRampResampleMethod

`public enum MTColorRampResampleMethod : String, Sendable, Codable, CaseIterable`

Resampling methods supported by MapTiler SDK.

- 

easeInSquare

Undocumented

#### Declaration

Swift
`case easeInSquare = "ease-in-square"`

- 

easeOutSquare

Undocumented

#### Declaration

Swift
`case easeOutSquare = "ease-out-square"`

- 

easeInSqrt

Undocumented

#### Declaration

Swift
`case easeInSqrt = "ease-in-sqrt"`

- 

easeOutSqrt

Undocumented

#### Declaration

Swift
`case easeOutSqrt = "ease-out-sqrt"`

- 

easeInExp

Undocumented

#### Declaration

Swift
`case easeInExp = "ease-in-exp"`

- 

easeOutExp

Undocumented

#### Declaration

Swift
`case easeOutExp = "ease-out-exp"`

---

## File: Enums/MTCountryLanguage.html

---
layout: mobile_sdk
title: "MTCountryLanguage"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Languages available for MTMapView object."
id: mtcountrylanguage
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTCountryLanguage

`public enum MTCountryLanguage : String, Sendable, Codable, CaseIterable`

Languages available for MTMapView object.

- 

albanian

Albanian language.

#### Declaration

Swift
`case albanian = "sq"`

- 

amharic

Amharic language.

#### Declaration

Swift
`case amharic = "am"`

- 

arabic

Arabic language.

#### Declaration

Swift
`case arabic = "ar"`

- 

armenian

Armenian language.

#### Declaration

Swift
`case armenian = "hy"`

- 

azerbaijani

Azerbaijani language.

#### Declaration

Swift
`case azerbaijani = "az"`

- 

basque

Basque language.

#### Declaration

Swift
`case basque = "eu"`

- 

belarusian

Belarusian language.

#### Declaration

Swift
`case belarusian = "be"`

- 

bengali

Bengali language.

#### Declaration

Swift
`case bengali = "bn"`

- 

bosnian

Bosnian language.

#### Declaration

Swift
`case bosnian = "bs"`

- 

breton

Breton language.

#### Declaration

Swift
`case breton = "br"`

- 

bulgarian

Bulgarian language.

#### Declaration

Swift
`case bulgarian = "bg"`

- 

catalan

Catalan language.

#### Declaration

Swift
`case catalan = "ca"`

- 

chinese

Chinese  language.

#### Declaration

Swift
`case chinese = "zh"`

- 

traditionalChinese

Traditional Chinese language.

#### Declaration

Swift
`case traditionalChinese = "zh-Hant"`

- 

simplifiedChinese

Simplified Chinese language.

#### Declaration

Swift
`case simplifiedChinese = "zh-Hans"`

- 

corsican

Corsican language.

#### Declaration

Swift
`case corsican = "co"`

- 

croatian

Croatian language.

#### Declaration

Swift
`case croatian = "hr"`

- 

czech

Czech language.

#### Declaration

Swift
`case czech = "cs"`

- 

danish

Danish language.

#### Declaration

Swift
`case danish = "da"`

- 

dutch

Dutch language.

#### Declaration

Swift
`case dutch = "nl"`

- 

english

English language.

#### Declaration

Swift
`case english = "en"`

- 

esperanto

Esperanto language.

#### Declaration

Swift
`case esperanto = "eo"`

- 

estonian

Estonian language.

#### Declaration

Swift
`case estonian = "et"`

- 

finnish

Finnish language.

#### Declaration

Swift
`case finnish = "fi"`

- 

french

French language.

#### Declaration

Swift
`case french = "fr"`

- 

frisian

Frisian language.

#### Declaration

Swift
`case frisian = "fy"`

- 

galician

Galician language.

#### Declaration

Swift
`case galician = "gl"`

- 

georgian

Georgian language.

#### Declaration

Swift
`case georgian = "ka"`

- 

german

German language.

#### Declaration

Swift
`case german = "de"`

- 

greek

Greek language.

#### Declaration

Swift
`case greek = "el"`

- 

hebrew

Hebrew language.

#### Declaration

Swift
`case hebrew = "he"`

- 

hindi

Hindi language.

#### Declaration

Swift
`case hindi = "hi"`

- 

hungarian

Hungarian language.

#### Declaration

Swift
`case hungarian = "hu"`

- 

icelandic

Icelandic language.

#### Declaration

Swift
`case icelandic = "is"`

- 

indonesian

Indonesian language.

#### Declaration

Swift
`case indonesian = "id"`

- 

irish

Irish language.

#### Declaration

Swift
`case irish = "ga"`

- 

italian

Italian language.

#### Declaration

Swift
`case italian = "it"`

- 

japanese

Japanese language.

#### Declaration

Swift
`case japanese = "ja"`

- 

japaneseHiragana

Japanese language in Hiragana form.

#### Declaration

Swift
`case japaneseHiragana = "ja-Hira"`

- 

japaneseLatin

Japanese language (latin script).

#### Declaration

Swift
`case japaneseLatin = "ja-Latn"`

- 

japaneseKana

Japanese language in Kana form (non-latin script).

#### Declaration

Swift
`case japaneseKana = "ja_kana"`

- 

kannada

Kannada language

#### Declaration

Swift
`case kannada = "kn"`

- 

kazakh

Kazakh language.

#### Declaration

Swift
`case kazakh = "kk"`

- 

korean

Korean language.

#### Declaration

Swift
`case korean = "ko"`

- 

koreanlatin

Korean language (latin script).

#### Declaration

Swift
`case koreanlatin = "ko-Latn"`

- 

kurdish

Kurdish language.

#### Declaration

Swift
`case kurdish = "ku"`

- 

classicalLatin

Classical latin language.

#### Declaration

Swift
`case classicalLatin = "la"`

- 

latvian

Latvian language.

#### Declaration

Swift
`case latvian = "lv"`

- 

lithuanian

Lithuanian language.

#### Declaration

Swift
`case lithuanian = "lt"`

- 

luxembourgish

Luxembourgish language.

#### Declaration

Swift
`case luxembourgish = "lb"`

- 

macedonian

Macedonian language.

#### Declaration

Swift
`case macedonian = "mk"`

- 

malay

Malay language.

#### Declaration

Swift
`case malay = "ml"`

- 

maltese

Maltese language.

#### Declaration

Swift
`case maltese = "mt"`

- 

marathi

Marathi language.

#### Declaration

Swift
`case marathi = "mr"`

- 

mongolian

Mongolian language.

#### Declaration

Swift
`case mongolian = "mn"`

- 

nepali

Nepali language.

#### Declaration

Swift
`case nepali = "ne"`

- 

norwegian

Norwegian language.

#### Declaration

Swift
`case norwegian = "no"`

- 

occitan

Occitan language.

#### Declaration

Swift
`case occitan = "oc"`

- 

persian

Persian language.

#### Declaration

Swift
`case persian = "fa"`

- 

polish

Polish language.

#### Declaration

Swift
`case polish = "pl"`

- 

portuguese

Portuguese language.

#### Declaration

Swift
`case portuguese = "pt"`

- 

punjabi

Punjabi language.

#### Declaration

Swift
`case punjabi = "pa"`

- 

westernPunjabi

Western Punjabi language.

#### Declaration

Swift
`case westernPunjabi = "pnb"`

- 

romanian

Romanian language.

#### Declaration

Swift
`case romanian = "ro"`

- 

romansh

Romansh language.

#### Declaration

Swift
`case romansh = "rm"`

- 

russian

Russian language.

#### Declaration

Swift
`case russian = "ru"`

- 

sardinian

Sardinian language.

#### Declaration

Swift
`case sardinian = "sc"`

- 

scottishGaelic

Scottish Gaelic language.

#### Declaration

Swift
`case scottishGaelic = "gd"`

- 

serbianCyrillic

Serbian language.

#### Declaration

Swift
`case serbianCyrillic = "sr"`

- 

serbianLatin

Serbian language.

#### Declaration

Swift
`case serbianLatin = "sr-Latn"`

- 

slovak

Slovak language.

#### Declaration

Swift
`case slovak = "sk"`

- 

slovene

Slovenian language.

#### Declaration

Swift
`case slovene = "sl"`

- 

spanish

Spanish language.

#### Declaration

Swift
`case spanish = "es"`

- 

swahili

Swahili language.

#### Declaration

Swift
`case swahili = "sw"`

- 

swedish

Swedish language.

#### Declaration

Swift
`case swedish = "sv"`

- 

tagalog

Tagalog language.

#### Declaration

Swift
`case tagalog = "tl"`

- 

tamil

Tamil language.

#### Declaration

Swift
`case tamil = "ta"`

- 

telugu

Telugu language.

#### Declaration

Swift
`case telugu = "te"`

- 

thai

Thai language.

#### Declaration

Swift
`case thai = "th"`

- 

turkish

Turkish language.

#### Declaration

Swift
`case turkish = "tr"`

- 

ukrainian

Ukrainian language.

#### Declaration

Swift
`case ukrainian = "uk"`

- 

urdu

Urdu language.

#### Declaration

Swift
`case urdu = "ur"`

- 

vietnamese

Vietnamese language.

#### Declaration

Swift
`case vietnamese = "vi"`

- 

welsh

Welsh language.

#### Declaration

Swift
`case welsh = "cy"`

---

## File: Enums/MTDashArrayValue.html

---
layout: mobile_sdk
title: "MTDashArrayValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents a dash pattern that can be provided as an array of numbers or as a string pattern
composed of underscores and spaces (e.g. “___ _ ”)."
id: mtdasharrayvalue
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTDashArrayValue

`public enum MTDashArrayValue : Codable, Sendable`

Represents a dash pattern that can be provided as an array of numbers or as a string pattern
composed of underscores and spaces (e.g. “___ _ ”).

- 

array(_:)

Undocumented

#### Declaration

Swift
`case array([Double])`

- 

pattern(_:)

Undocumented

#### Declaration

Swift
`case pattern(String)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

---

## File: Enums/MTEasing.html

---
layout: mobile_sdk
title: "MTEasing"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Representing the control of the change rate of the animation."
id: mteasing
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTEasing

`public enum MTEasing : String, Sendable, Codable`

Representing the control of the change rate of the animation.

- 

bezierCurve

Follows the bezier curve.

#### Declaration

Swift
`case bezierCurve`

- 

quint

Stars fast with a long, slow wind-down.

#### Declaration

Swift
`case quint`

- 

cubic

Starts slow and gradually increases speed.

#### Declaration

Swift
`case cubic`

---

## File: Enums/MTError.html

---
layout: mobile_sdk
title: "MTError"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents all the errors that can occur in the MapTiler SDK."
id: mterror
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTError

`public enum MTError : Error`

Represents all the errors that can occur in the MapTiler SDK.

All methods within the SDK throw MTError.

- 

exception(body:)

Method execution failed with exception.

#### Declaration

Swift
`case exception(body: MTException)`

#### Parameters

| body | Exception details. |

- 

invalidResultType(description:)

Method execution returned an invalid result.

#### Declaration

Swift
`case invalidResultType(description: String)`

#### Parameters

| description | Debug description of the return type. |

- 

unsupportedReturnType(description:)

Method execution returned unsupported type.

#### Declaration

Swift
`case unsupportedReturnType(description: String)`

#### Parameters

| description | Debug description of the command that returned unsupported type. |

- 

unknown(description:)

Method execution resulted in an unknown error.

#### Declaration

Swift
`case unknown(description: String)`

#### Parameters

| description | Debug description of error. |

- 

bridgeNotLoaded

Method execution halted. Bridge and/or Map are not loaded.

#### Declaration

Swift
`case bridgeNotLoaded`

- 

missingParent

Method execution failed due to missing parent entity.

#### Declaration

Swift
`case missingParent`

- 

code

Numerical code of the exception.

#### Declaration

Swift
`public var code: Int { get }`

- 

reason

Explanation of the exception.

#### Declaration

Swift
`public var reason: String { get }`

---

## File: Enums/MTEvent.html

---
layout: mobile_sdk
title: "MTEvent"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Events triggered by the SDK"
id: mtevent
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTEvent

`public enum MTEvent : String`

Events triggered by the SDK

- 

popupDidOpen

Triggered when a popup has been opened and added to the map.

#### Declaration

Swift
`case popupDidOpen = "open"`

- 

popupDidClose

Triggered when a popup has been closed and removed from the map.

#### Declaration

Swift
`case popupDidClose = "close"`

- 

boxZoomDidCancel

Triggered when the user cancels a “box zoom” interaction,
or when the bounding box does not meet the minimum size threshold.

#### Declaration

Swift
`case boxZoomDidCancel = "boxzoomcancel"`

- 

boxZoomDidEnd

Triggered when a “box zoom” interaction ends.

#### Declaration

Swift
`case boxZoomDidEnd = "boxzoomend"`

- 

boxZoomDidStart

Triggered when a “box zoom” interaction starts.

#### Declaration

Swift
`case boxZoomDidStart = "boxzoomstart"`

- 

didTap

Triggered when user taps and releases at the same point on the map.

#### Declaration

Swift
`case didTap = "click"`

- 

didPreventCooperativeGesture

Triggered whenever the cooperativeGestures option prevents a gesture from being handled by the map.

#### Declaration

Swift
`case didPreventCooperativeGesture = "cooperativegestureprevented"`

- 

dataDidUpdate

Triggered when any map data loads or changes.

#### Declaration

Swift
`case dataDidUpdate = "data"`

- 

dataUpdateDidAbort

Triggered when a request for one of the map’s sources’ tiles is aborted.
Triggered when a request for one of the map’s sources’ data is aborted.

#### Declaration

Swift
`case dataUpdateDidAbort = "dataabort"`

- 

dataLoadingDidStart

Triggered when any map data (style, source, tile, etc) begins loading or changing asynchronously.

All data loading events are followed by a dataDidUpdate, dataUpdateDidAbort or error events.

#### Declaration

Swift
`case dataLoadingDidStart = "dataloading"`

- 

didDoubleTap

Triggered when a user taps and releases twice at the same point on the map in rapid succession.

#### Declaration

Swift
`case didDoubleTap = "doubleTapped"`

- 

isDragging

Triggered repeatedly during a “drag to pan” interaction

#### Declaration

Swift
`case isDragging = "drag"`

- 

dragDidEnd

Triggered when a “drag to pan” interaction ends.

#### Declaration

Swift
`case dragDidEnd = "dragend"`

- 

dragDidStart

Triggered when a “drag to pan” interaction starts.

#### Declaration

Swift
`case dragDidStart = "dragstart"`

- 

isIdle

Triggered after the last frame rendered before the map enters an “idle” state.

Idle state means that no camera transitions are in progress, all currently requested tiles have loaded,
and all fade/transition animations have completed

#### Declaration

Swift
`case isIdle = "idle"`

- 

didLoad

Triggered immediately after all necessary resources have been downloaded
and the first visually complete rendering of the map has occurred.

#### Declaration

Swift
`case didLoad = "load"`

- 

didLoadWithTerrain

Triggered only once in a Map instance lifecycle, when both the load event
and the terrain event with non-null terrain are triggered.

#### Declaration

Swift
`case didLoadWithTerrain = "loadWithTerrain"`

- 

isMoving

Triggered repeatedly during an animated transition from one view to another,
as the result of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case isMoving = "move"`

- 

moveDidEnd

Triggered just after the map completes a transition from one view to another,
as the result of either user interaction or methods such as jumpTo.

#### Declaration

Swift
`case moveDidEnd = "moveend"`

- 

moveDidStart

Triggered just before the map begins a transition from one view to another,
as the result of either user interaction or methods such as jumpTo.

#### Declaration

Swift
`case moveDidStart = "movestart"`

- 

didUpdatePitch

Triggered repeatedly during the map’s pitch (tilt) animation between one state and another
as the result of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case didUpdatePitch = "pitch"`

- 

pitchUpdateDidEnd

Triggered immediately after the map’s pitch (tilt) finishes changing as the result
of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case pitchUpdateDidEnd = "pitchend"`

- 

pitchUpdateDidStart

Triggered whenever the map’s pitch (tilt) begins a change as the result
of either user interaction or methods such as flyTo .

#### Declaration

Swift
`case pitchUpdateDidStart = "pitchstart"`

- 

projectionDidModify

Triggered when map’s projection is modified in other ways than by map being moved.

#### Declaration

Swift
`case projectionDidModify = "projectiontransition"`

- 

isReady

Triggered only once after load and wait for all the controls managed by the Map constructor to be dealt with.

Since the ready event waits that all the basic controls are nicely positioned,
it is safer to use ready than load if you plan to add other custom controls.

#### Declaration

Swift
`case isReady = "ready"`

- 

didRemove

Triggered immediately after the map has been removed.

#### Declaration

Swift
`case didRemove = "remove"`

- 

didRender

Triggered whenever the map is drawn to the screen.

Drawing occurs with a change to the map’s position, zoom, pitch, or bearing,
a change to the map’s style,
a change to a GeoJSON source,
or the loading of a vector tile, GeoJSON file, glyph, or sprite.

#### Declaration

Swift
`case didRender = "render"`

- 

didResize

Triggered immediately after the map has been resized.

#### Declaration

Swift
`case didResize = "resize"`

- 

isRotating

Triggered repeatedly during a “drag to rotate” interaction.

#### Declaration

Swift
`case isRotating = "rotate"`

- 

rotateDidEnd

Triggered when a “drag to rotate” interaction ends.

#### Declaration

Swift
`case rotateDidEnd = "rotateend"`

- 

rotateDidStart

Triggered when a “drag to rotate” interaction starts.

#### Declaration

Swift
`case rotateDidStart = "rotatestart"`

- 

sourceDidUpdate

Triggered when one of the map’s sources loads or changes,
including if a tile belonging to a source loads or changes.

#### Declaration

Swift
`case sourceDidUpdate = "sourcedata"`

- 

sourceUpdateDidAbort

Triggered when a request for one of the map’s sources’ data is aborted.

#### Declaration

Swift
`case sourceUpdateDidAbort = "sourcedataabort"`

- 

sourceUpdateDidStart

Triggered when one of the map’s sources begins loading or changing asynchronously.

All sourceUpdateDidStart events are followed by a sourceDidUpdate, sourceUpdateDidAbort or error events.

#### Declaration

Swift
`case sourceUpdateDidStart = "sourcedataloading"`

- 

styleDidUpdate

Triggered when the map’s style loads or changes.

#### Declaration

Swift
`case styleDidUpdate = "styledata"`

- 

styleUpdateDidStart

Triggered when the map’s style begins loading or changing asynchronously.

All styleUpdateDidStart events are followed by a styleDidUpdate or error events.

#### Declaration

Swift
`case styleUpdateDidStart = "styledataloading"`

- 

styleImageIsMissing

Triggered when an icon or pattern needed by the style is missing.

#### Declaration

Swift
`case styleImageIsMissing = "styleimagemissing"`

- 

didTriggerTerrain

Triggered when a terrain event occurs within the map.

#### Declaration

Swift
`case didTriggerTerrain = "terrain"`

- 

terrainAnimationDidStart

The terrainAnimationDidStart event is triggered when the animation begins
transitioning between terrain and non-terrain states.

#### Declaration

Swift
`case terrainAnimationDidStart = "terrainAnimationStart"`

- 

terrainAnimationDidStop

The terrainAnimationDidStop event is triggered when the animation
between terrain and non-terrain states ends.

#### Declaration

Swift
`case terrainAnimationDidStop = "terrainAnimationStop"`

- 

touchDidCancel

Triggered when a touch is cancelled within the map.

#### Declaration

Swift
`case touchDidCancel = "touchcancel"`

- 

touchDidEnd

Triggered when a touch ends within the map.

#### Declaration

Swift
`case touchDidEnd = "touchend"`

- 

touchDidMove

Triggered when a touch moves within the map.

#### Declaration

Swift
`case touchDidMove = "touchmove"`

- 

touchDidStart

Triggered when a touch starts within the map.

#### Declaration

Swift
`case touchDidStart = "touchstart"`

- 

isZooming

Triggered repeatedly during an animated transition from one zoom level to another,
as the result of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case isZooming = "zoom"`

- 

zoomDidEnd

Triggered just after the map completes a transition from one zoom level to another,
as the result of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case zoomDidEnd = "zoomend"`

- 

zoomDidStart

Triggered just before the map begins a transition from one zoom level to another,
as the result of either user interaction or methods such as flyTo.

#### Declaration

Swift
`case zoomDidStart = "zoomstart"`

---

## File: Enums/MTEventLevel.html

---
layout: mobile_sdk
title: "MTEventLevel"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Controls which map events are forwarded from the map object."
id: mteventlevel
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTEventLevel

`public enum MTEventLevel : String, Codable, Sendable`

Controls which map events are forwarded from the map object.

- essential: Low-frequency lifecycle events only (ready, load, moveend, etc.) plus taps.

- cameraOnly: Forwards only camera events (move, zoom) in addition to minimal lifecycle.

- all: Default. Forwards all events including high-frequency move/zoom/touch/render
(use with caution on low-end devices).

- off: Minimal wiring to keep internal lifecycle (ready/load) functioning; all other events are suppressed.

- 

essential

Undocumented

#### Declaration

Swift
`case essential = "ESSENTIAL"`

- 

cameraOnly

Forwards only camera motion events (move, zoom) plus minimal lifecycle (ready/load is implicit).
Use this to support overlays that track camera without wiring all touch/render events.

#### Declaration

Swift
`case cameraOnly = "CAMERA_ONLY"`

- 

all

Undocumented

#### Declaration

Swift
`case all = "ALL"`

- 

off

Undocumented

#### Declaration

Swift
`case off = "OFF"`

---

## File: Enums/MTExpression.html

---
layout: mobile_sdk
title: "MTExpression"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper to construct common style expressions without raw strings."
id: mtexpression
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTExpression

`public enum MTExpression`

Helper to construct common style expressions without raw strings.

- 

get(_:)

[“get”, key]

#### Declaration

Swift
`public static func get(_ key: String) -> MTPropertyValue`

- 

get(_:)

[“get”, key]

#### Declaration

Swift
`public static func get(_ key: MTFeatureKey) -> MTPropertyValue`

- 

toString(_:)

[“to-string”, expr]

#### Declaration

Swift
`public static func toString(_ value: MTPropertyValue) -> MTPropertyValue`

- 

step(input:default:stops:)

step expression builder: [“step”, input, default, t1, v1, t2, v2, …]

#### Declaration

Swift
public static func step(
input: MTPropertyValue,
default defaultValue: MTPropertyValue,
stops: [(Double, MTPropertyValue)]
) -> MTPropertyValue

---

## File: Enums/MTFeatureKey.html

---
layout: mobile_sdk
title: "MTFeatureKey"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Commonly-used feature keys"
id: mtfeaturekey
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTFeatureKey

`public enum MTFeatureKey : String, Sendable`

Commonly-used feature keys

- 

pointCount

Undocumented

#### Declaration

Swift
`case pointCount = "point_count"`

- 

clusterId

Undocumented

#### Declaration

Swift
`case clusterId = "cluster_id"`

---

## File: Enums/MTFillExtrusionTranslateAnchor.html

---
layout: mobile_sdk
title: "MTFillExtrusionTranslateAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Controls the frame of reference for fill-extrusion translate."
id: mtfillextrusiontranslateanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTFillExtrusionTranslateAnchor

`public enum MTFillExtrusionTranslateAnchor : String`

Controls the frame of reference for fill-extrusion translate.

- 

map

The fill extrusion is translated relative to the map.

#### Declaration

Swift
`case map`

- 

viewport

The fill extrusion is translated relative to the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTFillTranslateAnchor.html

---
layout: mobile_sdk
title: "MTFillTranslateAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Enum controlling the frame of reference for fill translate."
id: mtfilltranslateanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTFillTranslateAnchor

`public enum MTFillTranslateAnchor : String`

Enum controlling the frame of reference for fill translate.

- 

map

The fill is translated relative to the map.

#### Declaration

Swift
`case map`

- 

viewport

The fill is translated relative to the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTFilter.html

---
layout: mobile_sdk
title: "MTFilter"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Helper to construct common filter expressions without raw strings."
id: mtfilter
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTFilter

`public enum MTFilter`

Helper to construct common filter expressions without raw strings.

- 

has(_:)

[“has”, key]

#### Declaration

Swift
`public static func has(_ key: String) -> MTPropertyValue`

- 

has(_:)

[“has”, key]

#### Declaration

Swift
`public static func has(_ key: MTFeatureKey) -> MTPropertyValue`

- 

not(_:)

[“!”, filter]

#### Declaration

Swift
`public static func not(_ filter: MTPropertyValue) -> MTPropertyValue`

- 

eq(_:_:)

[“==”, [“get”, key], value]

#### Declaration

Swift
`public static func eq(_ key: String, _ value: MTPropertyValue) -> MTPropertyValue`

- 

eq(_:_:)

[“==”, [“get”, key], value]

#### Declaration

Swift
`public static func eq(_ key: MTFeatureKey, _ value: MTPropertyValue) -> MTPropertyValue`

- 

all(_:)

[“all”, …filters]

#### Declaration

Swift
`public static func all(_ filters: [MTPropertyValue]) -> MTPropertyValue`

- 

any(_:)

[“any”, …filters]

#### Declaration

Swift
`public static func any(_ filters: [MTPropertyValue]) -> MTPropertyValue`

- 

clusters()

Convenience: filter for clusters (features having point_count)

#### Declaration

Swift
`static func clusters() -> MTPropertyValue`

- 

unclustered()

Convenience: filter for non-clustered points (![has point_count])

#### Declaration

Swift
`static func unclustered() -> MTPropertyValue`

---

## File: Enums/MTFitBoundsPadding.html

---
layout: mobile_sdk
title: "MTFitBoundsPadding"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Padding values accepted by MTFitBoundsOptions."
id: mtfitboundspadding
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTFitBoundsPadding

`public enum MTFitBoundsPadding : Sendable, Codable, Equatable`

Padding values accepted by `MTFitBoundsOptions`.

- 

uniform(_:)

Applies the same padding to all sides.

#### Declaration

Swift
`case uniform(Double)`

- 

directional(_:)

Applies directional padding values.

#### Declaration

Swift
`case directional(MTPaddingOptions)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Enums/MTGestureType.html

---
layout: mobile_sdk
title: "MTGestureType"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Gesture types available in the SDK."
id: mtgesturetype
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTGestureType

@MainActor
public enum MTGestureType

Gesture types available in the SDK.

- 

doubleTapZoomIn

Double tap zoom in.

#### Declaration

Swift
`case doubleTapZoomIn`

- 

dragPan

Drag and pan.

#### Declaration

Swift
`case dragPan`

- 

twoFingersDragPitch

Pitch shifting with two finger drag.

#### Declaration

Swift
`case twoFingersDragPitch`

- 

pinchRotateAndZoom

Pinching to rotate and zoom.

#### Declaration

Swift
`case pinchRotateAndZoom`

---

## File: Enums/MTHaloOption.html

---
layout: mobile_sdk
title: "MTHaloOption"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Option that can enable default halo or configure it."
id: mthalooption
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTHaloOption

`public enum MTHaloOption : Sendable, Codable`

Option that can enable default halo or configure it.

- 

enabled(_:)

Undocumented

#### Declaration

Swift
`case enabled(Bool)`

- 

config(_:)

Undocumented

#### Declaration

Swift
`case config(MTHalo)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Enums/MTHillshadeIlluminationAnchor.html

---
layout: mobile_sdk
title: "MTHillshadeIlluminationAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Direction of light source when map is rotated."
id: mthillshadeilluminationanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTHillshadeIlluminationAnchor

`public enum MTHillshadeIlluminationAnchor : String`

Direction of light source when map is rotated.

- 

map

The hillshade illumination is relative to the north direction.

#### Declaration

Swift
`case map`

- 

viewport

The hillshade illumination is relative to the top of the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTLanguage.html

---
layout: mobile_sdk
title: "MTLanguage"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Language of the map labels."
id: mtlanguage
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLanguage

`public enum MTLanguage : Sendable, Codable`

Language of the map labels.

- 

special(_:)

Custom language options.

#### Declaration

Swift
`case special(MTSpecialLanguage)`

- 

country(_:)

Country specific language.

#### Declaration

Swift
`case country(MTCountryLanguage)`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Enums/MTLayerType.html

---
layout: mobile_sdk
title: "MTLayerType"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Types of layers."
id: mtlayertype
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLayerType

`public enum MTLayerType : String, Codable`

Types of layers.

- 

fill

A filled polygon with an optional stroked border.

#### Declaration

Swift
`case fill`

- 

line

A stroked line.

#### Declaration

Swift
`case line`

- 

symbol

An icon or a text label.

#### Declaration

Swift
`case symbol`

- 

raster

Raster map textures such as satellite imagery.

#### Declaration

Swift
`case raster`

- 

circle

A filled circle.

#### Declaration

Swift
`case circle`

- 

fillExtrusion

An extruded (3D) polygon.

#### Declaration

Swift
`case fillExtrusion = "fill-extrusion"`

- 

heatmap

A heatmap.

#### Declaration

Swift
`case heatmap`

- 

hillshade

Client-side hillshading visualization based on DEM data.

#### Declaration

Swift
`case hillshade`

- 

background

The background color or pattern of the map.

#### Declaration

Swift
`case background`

---

## File: Enums/MTLayerVisibility.html

---
layout: mobile_sdk
title: "MTLayerVisibility"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Enum representing the visibility of the layer."
id: mtlayervisibility
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLayerVisibility

`public enum MTLayerVisibility : String`

Enum representing the visibility of the layer.

- 

visible

Layer is shown.

#### Declaration

Swift
`case visible`

- 

none

Layer is not shown.

#### Declaration

Swift
`case none`

---

## File: Enums/MTLightAnchor.html

---
layout: mobile_sdk
title: "MTLightAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Sets whether extruded geometries are lit relative to the map or viewport."
id: mtlightanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLightAnchor

`public enum MTLightAnchor : String, Sendable, Codable`

Sets whether extruded geometries are lit relative to the map or viewport.

- 

map

The position of the light source is aligned to the rotation of the map.

#### Declaration

Swift
`case map`

- 

viewport

The position of the light source is aligned to the rotation of the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTLineCap.html

---
layout: mobile_sdk
title: "MTLineCap"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The display of line endings."
id: mtlinecap
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLineCap

`public enum MTLineCap : String`

The display of line endings.

- 

butt

A cap with a squared-off end which is drawn to the exact endpoint of the line.

#### Declaration

Swift
`case butt`

- 

round

A cap with a rounded end which is drawn beyond the endpoint of the line
at a radius of one-half of the line’s width and centered on the endpoint of the line.

#### Declaration

Swift
`case round`

- 

square

A cap with a squared-off end which is drawn beyond the endpoint of the line
at a distance of one-half of the line’s width.

#### Declaration

Swift
`case square`

---

## File: Enums/MTLineJoin.html

---
layout: mobile_sdk
title: "MTLineJoin"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "The display of lines when joining."
id: mtlinejoin
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLineJoin

`public enum MTLineJoin : String`

The display of lines when joining.

- 

bevel

A join with a squared-off end which is drawn beyond the endpoint
of the line at a distance of one-half of the line’s width.

#### Declaration

Swift
`case bevel`

- 

round

A join with a rounded end which is drawn beyond the endpoint of the line
at a radius of one-half of the line’s width and centered on the endpoint of the line.

#### Declaration

Swift
`case round`

- 

miter

A join with a sharp, angled corner which is drawn with the outer
sides beyond the endpoint of the path until they meet.

#### Declaration

Swift
`case miter`

---

## File: Enums/MTLineTranslateAnchor.html

---
layout: mobile_sdk
title: "MTLineTranslateAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Controls the frame of reference for line translate."
id: mtlinetranslateanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLineTranslateAnchor

`public enum MTLineTranslateAnchor : String`

Controls the frame of reference for line translate.

- 

map

The line is translated relative to the map.

#### Declaration

Swift
`case map`

- 

viewport

The line is translated relative to the viewport.

#### Declaration

Swift
`case viewport`

---

## File: Enums/MTLocationError.html

---
layout: mobile_sdk
title: "MTLocationError"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Enum representing MTLocationManager errors."
id: mtlocationerror
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLocationError

`public enum MTLocationError : Error`

Enum representing MTLocationManager errors.

- 

permissionDenied

Location permission denied.

#### Declaration

Swift
`case permissionDenied`

---

## File: Enums/MTLogLevel.html

---
layout: mobile_sdk
title: "MTLogLevel"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "SDK log level."
id: mtloglevel
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLogLevel

`public enum MTLogLevel : Sendable, Equatable`

SDK log level.

- 

none

No logs will be printed.

#### Declaration

Swift
`case none`

- 

info

Only information logs will be printed.

#### Declaration

Swift
`case info`

- 

debug(verbose:)

All logs will be printed.

#### Declaration

Swift
`case debug(verbose: Bool = false)`

- 

==(_:_:)

#### Declaration

Swift
`public static func == (lhs: MTLogLevel, rhs: MTLogLevel) -> Bool`

- 

!=(_:_:)

Undocumented

#### Declaration

Swift
`public static func != (lhs: MTLogLevel, rhs: MTLogLevel) -> Bool`

---

## File: Enums/MTLogType.html

---
layout: mobile_sdk
title: "MTLogType"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Type of log messages in the SDK."
id: mtlogtype
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTLogType

`public enum MTLogType : Sendable`

Type of log messages in the SDK.

- 

info

Informational messages.

#### Declaration

Swift
`case info`

- 

warning

Warning messages.

#### Declaration

Swift
`case warning`

- 

error

SDK Errors.

#### Declaration

Swift
`case error`

- 

criticalError

Critical SDK errors.

#### Declaration

Swift
`case criticalError`

- 

event

Event messages.

#### Declaration

Swift
`case event`

---

## File: Enums/MTMapCorner.html

---
layout: mobile_sdk
title: "MTMapCorner"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents corners of the map."
id: mtmapcorner
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTMapCorner

`public enum MTMapCorner : String, Sendable, Codable`

Represents corners of the map.

- 

topLeft

Top left corner of the map.

#### Declaration

Swift
`case topLeft = "top-left"`

- 

topRight

Top right corner of the map.

#### Declaration

Swift
`case topRight = "top-right"`

- 

bottomLeft

Bottom left corner of the map.

#### Declaration

Swift
`case bottomLeft = "bottom-left"`

- 

bottomRight

Bottom right corner of the map.

#### Declaration

Swift
`case bottomRight = "bottom-right"`

---

## File: Enums/MTMapReferenceStyle.html

---
layout: mobile_sdk
title: "MTMapReferenceStyle"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Defines purpose and guidelines on what information is displayed."
id: mtmapreferencestyle
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTMapReferenceStyle

`public enum MTMapReferenceStyle : Identifiable, Hashable, Sendable`

Defines purpose and guidelines on what information is displayed.

- 

id

Unique id of the style.

#### Declaration

Swift
`public var id: String { get }`

- 

streets

The classic default style, perfect for urban areas.

#### Declaration

Swift
`case streets`

- 

satellite

High resolution satellite images.

#### Declaration

Swift
`case satellite`

- 

outdoor

A solid hiking companion, with peaks, parks, isolines and more.

#### Declaration

Swift
`case outdoor`

- 

winter

A map for developing skiing, snowboarding and other winter activities and adventures.

#### Declaration

Swift
`case winter`

- 

dataviz

A minimalist style for data visualization.

#### Declaration

Swift
`case dataviz`

- 

basic

A minimalist alternative to STREETS, with a touch of flat design.

#### Declaration

Swift
`case basic`

- 

bright

A minimalist style for high contrast navigation.

#### Declaration

Swift
`case bright`

- 

topo

Reference style for topographic study.

#### Declaration

Swift
`case topo`

- 

toner

Reference style for very high contrast stylish maps.

#### Declaration

Swift
`case toner`

- 

backdrop

Neutral greyscale style with hillshading suitable for colorful terrain-aware visualization.

#### Declaration

Swift
`case backdrop`

- 

openStreetMap

Reference style without any variants.

#### Declaration

Swift
`case openStreetMap`

- 

aquarelle

Watercolor map for creative use.

#### Declaration

Swift
`case aquarelle`

- 

landscape

Light terrain map for data overlays.

#### Declaration

Swift
`case landscape`

- 

ocean

Detailed map of the ocean seafloor and bathymetry.

#### Declaration

Swift
`case ocean`

- 

custom(_:)

Custom style from the URL.

Custom style does not have variants.

#### Declaration

Swift
`case custom(URL)`

- 

getVariants()

Returns all child variants.

#### Declaration

Swift
`public func getVariants() -> [MTMapStyleVariant]?`

- 

isCustom()

Returns boolean indicating whether style is custom or pre-made.

#### Declaration

Swift
`public func isCustom() -> Bool`

- 

getName()

Returns the reference style name.

#### Declaration

Swift
`public func getName() -> String`

- 

all()

Returns all pre-made styles.

#### Declaration

Swift
`public static func all() -> [MTMapReferenceStyle]`

---

## File: Enums/MTMapStyleVariant.html

---
layout: mobile_sdk
title: "MTMapStyleVariant"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Variants of the reference styles."
id: mtmapstylevariant
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTMapStyleVariant

`public enum MTMapStyleVariant : String, Sendable, CaseIterable, Identifiable`

Variants of the reference styles.

- 

id

Unique id of the style variant.

#### Declaration

Swift
`public var id: String { get }`

- 

defaultVariant

Default variant.

#### Declaration

Swift
`case defaultVariant = "default"`

- 

dark

Dark variant.

#### Declaration

Swift
`case dark`

- 

light

Light variant.

#### Declaration

Swift
`case light`

- 

pastel

Pastel variant.

#### Declaration

Swift
`case pastel`

- 

night

Night variant.

#### Declaration

Swift
`case night`

- 

shiny

Shiny variant.

#### Declaration

Swift
`case shiny`

- 

topographique

Topographique variant.

#### Declaration

Swift
`case topographique`

- 

lite

Lite variant.

#### Declaration

Swift
`case lite`

- 

lines

Lines variant.

#### Declaration

Swift
`case lines`

- 

background

Background variant

#### Declaration

Swift
`case background`

- 

vivid

Vivid variant

#### Declaration

Swift
`case vivid`

---

## File: Enums/MTMarkerPitchAlignment.html

---
layout: mobile_sdk
title: "MTMarkerPitchAlignment"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Alignment for marker pitch relative to map or viewport."
id: mtmarkerpitchalignment
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTMarkerPitchAlignment

`public enum MTMarkerPitchAlignment : String, Sendable, Codable`

Alignment for marker pitch relative to map or viewport.

- 

map

Aligns the marker with the plane of the map.

#### Declaration

Swift
`case map`

- 

viewport

Aligns the marker with the viewport plane.

#### Declaration

Swift
`case viewport`

- 

auto

Automatically matches the marker’s rotation alignment.

#### Declaration

Swift
`case auto`

---

## File: Enums/MTMarkerRotationAlignment.html

---
layout: mobile_sdk
title: "MTMarkerRotationAlignment"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Alignment for marker rotation relative to map or viewport."
id: mtmarkerrotationalignment
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTMarkerRotationAlignment

`public enum MTMarkerRotationAlignment : String, Sendable, Codable`

Alignment for marker rotation relative to map or viewport.

- 

map

Aligns the marker’s rotation with the map, reacting to map bearing.

#### Declaration

Swift
`case map`

- 

viewport

Aligns the marker’s rotation with the viewport, ignoring map bearing.

#### Declaration

Swift
`case viewport`

- 

auto

Alias for `.viewport`.

#### Declaration

Swift
`case auto`

---

## File: Enums/MTNumberOrPropertyValues.html

---
layout: mobile_sdk
title: "MTNumberOrPropertyValues"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Either a numeric value or property-mapped numeric values."
id: mtnumberorpropertyvalues
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTNumberOrPropertyValues

`public enum MTNumberOrPropertyValues : Codable, Sendable`

Either a numeric value or property-mapped numeric values.

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

propertyValues(_:)

Undocumented

#### Declaration

Swift
`case propertyValues(MTPropertyValues)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

---

## File: Enums/MTNumberOrZoomNumberValues.html

---
layout: mobile_sdk
title: "MTNumberOrZoomNumberValues"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Either a numeric value or zoom-ramped numeric values."
id: mtnumberorzoomnumbervalues
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTNumberOrZoomNumberValues

`public enum MTNumberOrZoomNumberValues : Codable, Sendable`

Either a numeric value or zoom-ramped numeric values.

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

ramp(_:)

Undocumented

#### Declaration

Swift
`case ramp(MTZoomNumberValues)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

---

## File: Enums/MTPerformancePresets.html

---
layout: mobile_sdk
title: "MTPerformancePresets"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Performance-oriented presets for MapTiler Swift SDK."
id: mtperformancepresets
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTPerformancePresets

`public enum MTPerformancePresets`

Performance-oriented presets for MapTiler Swift SDK.

- 

leanPerformance(base:)

Lean performance preset: prioritize responsiveness and bytes over fidelity.

Applied overrides (favor performance over fidelity):

pixelRatio = 1.0

- shouldRefreshExpiredTiles = false

- cancelPendingTileRequestsWhileZooming = true

- maxTileCacheZoomLevels = 4.0 (if unset)

- crossSourceCollisionsAreEnabled = false

- eventLevel = ESSENTIAL (keeps low-frequency events; per-frame events opt-in)

- highFrequencyEventThrottleMs = 150 (when ALL is enabled)

#### Declaration

Swift
`public static func leanPerformance(base: MTMapOptions = MTMapOptions()) -> MTMapOptions`

- 

balancedPerformance(base:)

Returns a new [MTMapOptions] based on [base] with balanced performance defaults.

Keeps crisper rendering by using a higher pixel ratio.

Applied overrides:

pixelRatio = base.pixelRatio ?: 1.5 (sharper than 1.0)

- shouldRefreshExpiredTiles = false

- cancelPendingTileRequestsWhileZooming = true

- maxTileCacheZoomLevels = 4.0 (if unset)

- crossSourceCollisionsAreEnabled = false

- eventLevel = ESSENTIAL (per-frame events opt-in)

- highFrequencyEventThrottleMs = 150 (when ALL is enabled)

#### Declaration

Swift
`public static func balancedPerformance(base: MTMapOptions = MTMapOptions()) -> MTMapOptions`

- 

highFidelity(base:)

Returns a new [MTMapOptions] based on [base] tuned for higher-end devices.

Focuses on visual fidelity while keeping sensible performance guardrails.

Applied overrides:

pixelRatio = base.pixelRatio ?: 2.0 (very crisp; test for memory on low-end)

- shouldRefreshExpiredTiles = true (prefer up-to-date tiles)

- cancelPendingTileRequestsWhileZooming = false (allow progressive detail during zoom)

- maxTileCacheZoomLevels = 6.0 (if unset) to reduce churn when navigating

- crossSourceCollisionsAreEnabled = base.crossSourceCollisionsAreEnabled ?: true

- eventLevel = ALL

- highFrequencyEventThrottleMs = 100 (slightly more responsive when ALL is enabled)

#### Declaration

Swift
`public static func highFidelity(base: MTMapOptions = MTMapOptions()) -> MTMapOptions`

---

## File: Enums/MTProjectionType.html

---
layout: mobile_sdk
title: "MTProjectionType"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Type of projection the map uses."
id: mtprojectiontype
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTProjectionType

`public enum MTProjectionType : String, Sendable, Codable`

Type of projection the map uses.

- 

mercator

Mercator projection.

#### Declaration

Swift
`case mercator`

- 

globe

Globe projection.

#### Declaration

Swift
`case globe`

---

## File: Enums/MTPropertyValue.html

---
layout: mobile_sdk
title: "MTPropertyValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A typed value container"
id: mtpropertyvalue
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTPropertyValue

`public enum MTPropertyValue : Sendable`

A typed value container

- 

string(_:)

Undocumented

#### Declaration

Swift
`case string(String)`

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

bool(_:)

Undocumented

#### Declaration

Swift
`case bool(Bool)`

- 

array(_:)

Undocumented

#### Declaration

Swift
`case array([MTPropertyValue])`

- 

rawExpression(_:)

Undocumented

#### Declaration

Swift
`case rawExpression(String)`

- 

color(_:)

Undocumented

#### Declaration

Swift
`case color(UIColor)`

---

## File: Enums/MTRadiusOption.html

---
layout: mobile_sdk
title: "MTRadiusOption"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Heatmap radius can be a number, zoom-ramped numbers, or property-mapped numbers."
id: mtradiusoption
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTRadiusOption

`public enum MTRadiusOption : Codable, Sendable`

Heatmap radius can be a number, zoom-ramped numbers, or property-mapped numbers.

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

zoom(_:)

Undocumented

#### Declaration

Swift
`case zoom(MTZoomNumberValues)`

- 

property(_:)

Undocumented

#### Declaration

Swift
`case property(MTPropertyValues)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

---

## File: Enums/MTRasterDEMEncoding.html

---
layout: mobile_sdk
title: "MTRasterDEMEncoding"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Encoding used by the Raster DEM source."
id: mtrasterdemencoding
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTRasterDEMEncoding

`public enum MTRasterDEMEncoding : String, Sendable`

Encoding used by the Raster DEM source.

- 

terrarium

Terrarium format PNG tiles.

#### Declaration

Swift
`case terrarium`

- 

mapbox

Terrain RGB tiles (Mapbox/MapTiler Terrain RGB).

#### Declaration

Swift
`case mapbox`

---

## File: Enums/MTRasterResampling.html

---
layout: mobile_sdk
title: "MTRasterResampling"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Resampling/interpolation method to use for overscaling."
id: mtrasterresampling
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTRasterResampling

`public enum MTRasterResampling : String, Codable, Sendable`

Resampling/interpolation method to use for overscaling.

- 

linear

(Bi)linear filtering for smooth but slightly blurry overscaling.

#### Declaration

Swift
`case linear`

- 

nearest

Nearest neighbor filtering for sharp but pixelated overscaling.

#### Declaration

Swift
`case nearest`

---

## File: Enums/MTSkyColorValue.html

---
layout: mobile_sdk
title: "MTSkyColorValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents a color or expression for the sky configuration."
id: mtskycolorvalue
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSkyColorValue

`public enum MTSkyColorValue : Sendable, Codable, Equatable`

Represents a color or expression for the sky configuration.

- 

color(_:)

Undocumented

#### Declaration

Swift
`case color(MTColor)`

- 

expression(_:)

Undocumented

#### Declaration

Swift
`case expression([MTSkyExpression])`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

color(_:)

Convenience to wrap a UIKit color.

#### Declaration

Swift
`public static func color(_ color: UIColor) -> MTSkyColorValue`

---

## File: Enums/MTSkyExpression.html

---
layout: mobile_sdk
title: "MTSkyExpression"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Expression element used to build MapTiler style expressions for sky values."
id: mtskyexpression
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSkyExpression

`public enum MTSkyExpression : Sendable, Codable, Equatable`

Expression element used to build MapTiler style expressions for sky values.

- 

string(_:)

Undocumented

#### Declaration

Swift
`case string(String)`

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

array(_:)

Undocumented

#### Declaration

Swift
`case array([MTSkyExpression])`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Enums/MTSkyNumberValue.html

---
layout: mobile_sdk
title: "MTSkyNumberValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents a numeric value or expression for the sky configuration."
id: mtskynumbervalue
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSkyNumberValue

`public enum MTSkyNumberValue : Sendable, Codable, Equatable`

Represents a numeric value or expression for the sky configuration.

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

expression(_:)

Undocumented

#### Declaration

Swift
`case expression([MTSkyExpression])`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

- 

clamped()

Clamps numeric values to the valid [0, 1] range.

#### Declaration

Swift
`public func clamped() -> MTSkyNumberValue`

---

## File: Enums/MTSourceType.html

---
layout: mobile_sdk
title: "MTSourceType"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Types of sources."
id: mtsourcetype
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSourceType

`public enum MTSourceType : String, Codable`

Types of sources.

Sources state which data the map should display.

- 

vector

Vector tile source.

#### Declaration

Swift
`case vector`

- 

raster

Raster tile source.

#### Declaration

Swift
`case raster`

- 

rasterDEM

Raster DEM source.

#### Declaration

Swift
`case rasterDEM = "raster-dem"`

- 

geojson

GeoJSON source.

#### Declaration

Swift
`case geojson`

- 

image

Image source.

#### Declaration

Swift
`case image`

- 

video

Video source.

#### Declaration

Swift
`case video`

---

## File: Enums/MTSpaceOption.html

---
layout: mobile_sdk
title: "MTSpaceOption"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Option that can enable default space or configure it."
id: mtspaceoption
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSpaceOption

`public enum MTSpaceOption : Sendable, Codable`

Option that can enable default space or configure it.

- 

enabled(_:)

Undocumented

#### Declaration

Swift
`case enabled(Bool)`

- 

config(_:)

Undocumented

#### Declaration

Swift
`case config(MTSpace)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: Encoder) throws`

---

## File: Enums/MTSpacePreset.html

---
layout: mobile_sdk
title: "MTSpacePreset"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Predefined cubemap presets for space backgrounds."
id: mtspacepreset
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSpacePreset

`public enum MTSpacePreset : String, Sendable, Codable, CaseIterable`

Predefined cubemap presets for space backgrounds.

- 

space

Dark blue hsl(210, 100%, 4%) background and white stars (transparent background image).
Space color changes the background color, stars always stay white.

#### Declaration

Swift
`case space`

- 

stars

(default): Black background (image mask), space color changes the stars color, background always stays black.

#### Declaration

Swift
`case stars`

- 

milkyway

Black half-transparent background with standard milkyway and stars.
Space color changes the stars and milkyway color, background always stays black.

#### Declaration

Swift
`case milkyway`

- 

milkywaySubtle

Black half-transparent background with subtle milkyway and less stars.
Space color changes the stars and milkyway color, background always stays black.
Black half-transparent background with standard milkyway and stars.
Space color changes the stars and milkyway color, background always stays black.

#### Declaration

Swift
`case milkywaySubtle = "milkyway-subtle"`

- 

milkywayBright

Black half-transparent background with bright milkyway and more stars.
Space color changes the stars and milkyway color, background always stays black.

#### Declaration

Swift
`case milkywayBright = "milkyway-bright"`

- 

milkywayColored

Full background image with natural space colors. Space color doesn’t change anything (non transparent image).

#### Declaration

Swift
`case milkywayColored = "milkyway-colored"`

---

## File: Enums/MTSpecialLanguage.html

---
layout: mobile_sdk
title: "MTSpecialLanguage"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Custom language options."
id: mtspeciallanguage
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSpecialLanguage

`public enum MTSpecialLanguage : String, Sendable, Codable`

Custom language options.

- 

auto

The default language of the device.

#### Declaration

Swift
`case auto`

- 

international

The international name. This option is equivalent to OSM’s name int_name.

#### Declaration

Swift
`case international`

- 

latin

The default fallback language in the Latin charset.

#### Declaration

Swift
`case latin`

- 

local

The local language for each country.

#### Declaration

Swift
`case local`

- 

nonLatin

The default fallback language in the non-Latin charset.

#### Declaration

Swift
`case nonLatin`

- 

style

The language defined by the style.

#### Declaration

Swift
`case style`

- 

visitor

Preferred language from the user settings and “default name”

This mode is useful when a user needs to access both local names and English names,
for example, when traveling abroad where signs are likely to be available only in the local language

#### Declaration

Swift
`case visitor`

- 

visitorEnglish

English and “default name”

This mode is useful when a user needs to access both local names and English names,
for example, when traveling abroad where signs are likely to be available only in the local language

#### Declaration

Swift
`case visitorEnglish`

---

## File: Enums/MTStringOrZoomStringValues.html

---
layout: mobile_sdk
title: "MTStringOrZoomStringValues"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Either a string value or zoom-ramped string values."
id: mtstringorzoomstringvalues
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTStringOrZoomStringValues

`public enum MTStringOrZoomStringValues : Codable, Sendable`

Either a string value or zoom-ramped string values.

- 

string(_:)

Undocumented

#### Declaration

Swift
`case string(String)`

- 

ramp(_:)

Undocumented

#### Declaration

Swift
`case ramp(MTZoomStringValues)`

- 

uiColor(_:)

Undocumented

#### Declaration

Swift
`case uiColor(UIColor)`

- 

init(from:)

#### Declaration

Swift
`public init(from decoder: any Decoder) throws`

- 

encode(to:)

#### Declaration

Swift
`public func encode(to encoder: any Encoder) throws`

Union helper types for encoding mixed-value options

- 

init(_:)

Undocumented

#### Declaration

Swift
`init(_ color: UIColor)`

---

## File: Enums/MTStyleError.html

---
layout: mobile_sdk
title: "MTStyleError"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Represents the exceptions raised by the MTStyle object."
id: mtstyleerror
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTStyleError

`public enum MTStyleError : Error`

Represents the exceptions raised by the MTStyle object.

- 

sourceAlreadyExists

Source with the same id already added to the map.

#### Declaration

Swift
`case sourceAlreadyExists`

- 

sourceNotFound

Source does not exist in the map.

#### Declaration

Swift
`case sourceNotFound`

- 

layerAlreadyExists

Layer with the same id already added to the map.

#### Declaration

Swift
`case layerAlreadyExists`

- 

layerNotFound

Layer does not exist in the map.

#### Declaration

Swift
`case layerNotFound`

---

## File: Enums/MTStyleValue.html

---
layout: mobile_sdk
title: "MTStyleValue"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A unified style value that may be a constant or an expression."
id: mtstylevalue
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTStyleValue

`public enum MTStyleValue : Sendable`

A unified style value that may be a constant or an expression.

- 

color(_:)

Undocumented

#### Declaration

Swift
`case color(UIColor)`

- 

number(_:)

Undocumented

#### Declaration

Swift
`case number(Double)`

- 

bool(_:)

Undocumented

#### Declaration

Swift
`case bool(Bool)`

- 

string(_:)

Undocumented

#### Declaration

Swift
`case string(String)`

- 

expression(_:)

Undocumented

#### Declaration

Swift
`case expression(MTPropertyValue)`

---

## File: Enums/MTSymbolLayoutProperty.html

---
layout: mobile_sdk
title: "MTSymbolLayoutProperty"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Typed keys for symbol layout properties."
id: mtsymbollayoutproperty
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSymbolLayoutProperty

`public enum MTSymbolLayoutProperty : String, Sendable`

Typed keys for symbol layout properties.

- 

textField

Undocumented

#### Declaration

Swift
`case textField = "text-field"`

- 

textSize

Undocumented

#### Declaration

Swift
`case textSize = "text-size"`

- 

textAllowOverlap

Undocumented

#### Declaration

Swift
`case textAllowOverlap = "text-allow-overlap"`

- 

textAnchor

Undocumented

#### Declaration

Swift
`case textAnchor = "text-anchor"`

- 

textFont

Undocumented

#### Declaration

Swift
`case textFont = "text-font"`

- 

visibility

Undocumented

#### Declaration

Swift
`case visibility`

- 

iconImage

Undocumented

#### Declaration

Swift
`case iconImage = "icon-image"`

---

## File: Enums/MTSymbolPaintProperty.html

---
layout: mobile_sdk
title: "MTSymbolPaintProperty"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Typed keys for symbol paint properties."
id: mtsymbolpaintproperty
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTSymbolPaintProperty

`public enum MTSymbolPaintProperty : String, Sendable`

Typed keys for symbol paint properties.

- 

textColor

Undocumented

#### Declaration

Swift
`case textColor = "text-color"`

---

## File: Enums/MTTextAnchor.html

---
layout: mobile_sdk
title: "MTTextAnchor"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Symbol text anchor positions."
id: mttextanchor
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTTextAnchor

`public enum MTTextAnchor : String, Sendable`

Symbol text anchor positions.

- 

center

Undocumented

#### Declaration

Swift
`case center`

- 

left

Undocumented

#### Declaration

Swift
`case left`

- 

right

Undocumented

#### Declaration

Swift
`case right`

- 

top

Undocumented

#### Declaration

Swift
`case top`

- 

bottom

Undocumented

#### Declaration

Swift
`case bottom`

- 

topLeft

Undocumented

#### Declaration

Swift
`case topLeft = "top-left"`

- 

topRight

Undocumented

#### Declaration

Swift
`case topRight = "top-right"`

- 

bottomLeft

Undocumented

#### Declaration

Swift
`case bottomLeft = "bottom-left"`

- 

bottomRight

Undocumented

#### Declaration

Swift
`case bottomRight = "bottom-right"`

---

## File: Enums/MTTextToken.html

---
layout: mobile_sdk
title: "MTTextToken"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Common text field tokens"
id: mttexttoken
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTTextToken

`public enum MTTextToken : String, Sendable`

Common text field tokens

- 

pointCountAbbreviated

Undocumented

#### Declaration

Swift
`case pointCountAbbreviated = "{point_count_abbreviated}"`

---

## File: Enums/MTTileScheme.html

---
layout: mobile_sdk
title: "MTTileScheme"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "A scheme used for tiles."
id: mttilescheme
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTTileScheme

`public enum MTTileScheme : String`

A scheme used for tiles.

- 

xyz

XYZ Format.

#### Declaration

Swift
`case xyz`

- 

tms

TMS Format.

#### Declaration

Swift
`case tms`

---

## File: Enums/MTUnit.html

---
layout: mobile_sdk
title: "MTUnit"
title_size: regular
category: mobile-sdk-ios
categories: mobile-sdk mobile-sdk-ios ios
group: API Reference
group_number: 999
description: "Units of measurement used in MTMapView object."
id: mtunit
breadcrumb: "Mobile SDK/iOS/Reference/Enums"
---

# MTUnit

`public enum MTUnit : String, Sendable`

Units of measurement used in MTMapView object.

- 

imperial

Imperical units.

#### Declaration

Swift
`case imperial`

- 

metric

Metric units.

#### Declaration

Swift
`case metric`

- 

nautical

Nautical units.

#### Declaration

Swift
`case nautical`

---

