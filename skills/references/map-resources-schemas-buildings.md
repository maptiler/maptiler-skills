# MapTiler Buildings

Source: https://docs.maptiler.com/schema/buildings/

Tileset providing an additional building-related layers with enhanced details, including building entrances, names, and classification attributes.

The MapTiler Buildings tileset provides additional building-related layers with enhanced detail
  (e.g. entrances, names, classification attributes).
  It is intended for use with MapTiler Planet v4,
  and together they offer rich building context for everyday mapping applications.

## Layers

### building

Layer containing polygons of building or building part footprints with additional attributes.


### Block

`builtup`

### Fields

#### class & subclass

Classification categories. Corresponds to `class & subclass` in the [building_label](#building_label) layer.

Values:


**agricultural**


- `agricultural`
- `barn`
- `cowshed`
- `farm`
- `farm_auxiliary`
- `glasshouse`
- `greenhouse`
- `silo`
- `stable`
- `sty`



**civic**


- `civic`
- `fire_station`
- `government`
- `public`



**commercial**


- `commercial`
- `hotel`
- `kiosk`
- `office`
- `retail`
- `supermarket`
- `warehouse`



**education**


- `college`
- `kindergarten`
- `school`
- `university`



**entertainment**


- `grandstand`
- `pavilion`
- `sports_centre`
- `sports_hall`
- `stadium`



**industrial**


- `factory`
- `industrial`
- `manufacture`



**medical**


- `hospital`



**military**


- `bunker`
- `military`



**outbuilding**


- `allotment_house`
- `carport`
- `outbuilding`
- `roof`
- `shed`



**religious**


- `cathedral`
- `chapel`
- `church`
- `monastery`
- `mosque`
- `presbytery`
- `religious`
- `shrine`
- `synagogue`
- `temple`
- `wayside_shrine`



**residential**


- `apartments`
- `bungalow`
- `cabin`
- `detached`
- `dormitory`
- `dwelling_house`
- `garage`
- `garages`
- `ger`
- `house`
- `houseboat`
- `hut`
- `residential`
- `semi`
- `semidetached_house`
- `static_caravan`
- `stilt_house`
- `terrace`
- `trullo`



**service**


- `beach_hut`
- `boathouse`
- `digester`
- `guardhouse`
- `service`
- `slurry_tank`
- `storage_tank`
- `toilets`
- `transformer_tower`



**transportation**


- `hangar`
- `parking`
- `train_station`
- `transportation`


#### facade_color

Hexadecimal color code representing the building façade.

Examples:
- `#778899`
- `#947A58`
- `#FF0000`

#### height

Approximate height (in meters), derived from building levels or height attributes (or building part).

Min value:
- `1`

Max value:
- `850`

#### height_min

Approximate base height (in meters), derived from minimum levels or minimum height attributes of the building or its parts.

Min value:
- `0`

Max value:
- `583`

#### roof_color

Hexadecimal color code of building roof.

Examples:
- `#008000`
- `#778899`
- `#8B4513`

#### roof_shape

Shape of the roof.

Values:
- `dome`
- `flat`
- `gabled`
- `gambrel`
- `half_hipped`
- `hipped`
- `mansard`
- `onion`
- `pyramidal`
- `round`
- `saltbox`
- `sawtooth`
- `skillion`
- `spherical`

#### underground

Indicates whether the building is underground.

Values:
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`true` (from z14+)

### building_entrance

Layer containing points of building entrances.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### building_label

Layer containing point labels for named buildings.


### Block

`builtup`

### Fields

#### class & subclass

Classification categories. Corresponds to `class & subclass` in the [building](#building) layer.

Values:


**agricultural**


- `agricultural`
- `barn`
- `cowshed`
- `farm`
- `farm_auxiliary`
- `glasshouse`
- `greenhouse`
- `silo`
- `stable`
- `sty`



**civic**


- `civic`
- `fire_station`
- `government`
- `public`



**commercial**


- `commercial`
- `hotel`
- `kiosk`
- `office`
- `retail`
- `supermarket`
- `warehouse`



**education**


- `college`
- `kindergarten`
- `school`
- `university`



**entertainment**


- `grandstand`
- `pavilion`
- `sports_centre`
- `sports_hall`
- `stadium`



**industrial**


- `factory`
- `industrial`
- `manufacture`



**medical**


- `hospital`



**military**


- `bunker`
- `military`



**outbuilding**


- `allotment_house`
- `carport`
- `outbuilding`
- `roof`
- `shed`



**religious**


- `cathedral`
- `chapel`
- `church`
- `monastery`
- `mosque`
- `presbytery`
- `religious`
- `shrine`
- `synagogue`
- `temple`
- `wayside_shrine`



**residential**


- `apartments`
- `bungalow`
- `cabin`
- `detached`
- `dormitory`
- `dwelling_house`
- `garage`
- `garages`
- `ger`
- `house`
- `houseboat`
- `hut`
- `residential`
- `semi`
- `semidetached_house`
- `static_caravan`
- `stilt_house`
- `terrace`
- `trullo`



**service**


- `beach_hut`
- `boathouse`
- `digester`
- `guardhouse`
- `service`
- `slurry_tank`
- `storage_tank`
- `toilets`
- `transformer_tower`



**transportation**


- `hangar`
- `parking`
- `train_station`
- `transportation`


#### name

Primary (local or official) name of the building.

Examples:
- `Casa Milà`
- `Empire State Building`
- `برج خليف`

#### name:{code}

Localized name of the building in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the building. Lower values indicate greater importance.

Min value:
- `1`

Max value:
- `6893`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### languages

List of possible languages available in Buildings tileset.

Read more in the article about [Change language in a map](/guides/map-design/change-language-in-a-map).

### Fields

#### name:{code}

Localized name of the feature in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents ISO 639 language code.

Values:

- `am` (Amharic)
- `ar` (Arabic)
- `az` (Azerbaijani)
- `be` (Belorussian)
- `bg` (Bulgarian)
- `bn` (Bengali)
- `br` (Breton)
- `bs` (Bosnian)
- `ca` (Catalan)
- `co` (Corsican)
- `cs` (Czech)
- `cy` (Welsh)
- `da` (Danish)
- `de` (German)
- `el` (Greek)
- `en` (English)
- `eo` (Esperanto)
- `es` (Spanish)
- `et` (Estonian)
- `eu` (Basque)
- `fa` (Persian)
- `fi` (Finnish)
- `fr` (French)
- `fy` (Western Frisian)
- `ga` (Irish)
- `gd` (Scottish Gaelic)
- `he` (Hebrew)
- `hi` (Hindi)
- `hr` (Croatian)
- `hu` (Hungarian)
- `hy` (Armenian)
- `id` (Indonesian)
- `is` (Icelandic)
- `it` (Italian)
- `ja` (Japanese)
- `ja_kana` (Japanese Kana form)
- `ja_rm` (romanization of Japanese)
- `ja-Latn` (romanisation of Japanese since 2018)
- `ja-Hira` (Japanese Hiragana form)
- `ka` (Georgian)
- `kk` (Kazakh)
- `kn` (Kannada)
- `ko` (Korean)
- `ko-Latn` (romanization of Korean)
- `ku` (Kurdish)
- `la` (Latin)
- `lb` (Luxembourgish)
- `lt` (Lithuanian)
- `lv` (Latvian)
- `mk` (Macedonian)
- `mt` (Maltese)
- `ml` (Malayalam)
- `nb` (Norwegian Bokmål)
- `nl` (Dutch)
- `nn` (Norwegian Nynorsk)
- `no` (Norwegian)
- `oc` (Occitan (post 1500))
- `pa` (Punjabi)
- `pnb` (Western Punjabi)
- `pl` (Polish)
- `pt` (Portuguese)
- `rm` (Romansh)
- `ro` (Romania)
- `ru` (Russian)
- `sk` (Slovak)
- `sl` (Slovene)
- `sq` (Albanian)
- `sr` (Serbian, Cyrillic)
- `sr-Latn` (Serbian)
- `sv` (Swedish)
- `ta` (Tamil)
- `te` (Telugu)
- `th` (Thai)
- `tr` (Turkish)
- `uk` (Ukrainian)
- `ur` (Urdu)
- `vi` (Vietnamese)
- `zh` (Chinese)
- `zh-Hant` (Traditional Chinese)
- `zh-Hans` (Simplified Chinese)

