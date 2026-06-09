# MapTiler Grid

Source: https://docs.maptiler.com/schema/grid/

Tileset contains graticule (parallels and meridians) and timezone layers

MapTiler Grid is a vector tileset providing global spatial reference layers, including international timezones,
  UTC offset boundaries, and a standardized WGS84 graticule.

## Layers

### dateline

Layer containing an established navigation boundary located near 180° longitude that serves as the globally recognized 
demarcation for the transition between calendar days.
### Fields

#### name
Name of the dateline.

Value:
- `International Date Line`

#### name:{code}

Localized name of the International Date Line in a specific language.

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### grid_wgs_84

Layer containing geographic lines - meridians and parallels - with 1 degree step, 
major circles of latitudes and prime meridians.

### Fields

#### class
Classification category to distinguish between meridians and parallels.

Values:
- `meridian`
- `parallel`

#### degree
Value of latitude (for parallels) or longitude (for meridians).

Min/max values: 
- `-180`
- `180`

#### latitude
Classification category to distinguish between northern and southern hemisphere.

Values:
- `North`
- `South`

#### longitude
Classification category to distinguish between western and eastern hemisphere.

Values:
- `West`
- `East`

#### name
Name of major circles of latitudes or prime meridians.

Values:
- `Antarctic Circle`
- `Arctic Circle`
- `Athens`
- `Bern`
- `Bogota`
- `Brussels`
- `Copenhagen`
- `Equator`
- `Ferro`
- `Greenwich`
- `Jakarta`
- `Lisbon`
- `Madrid`
- `Oslo`
- `Paris`
- `Rome`
- `Stockholm`
- `Tropic of Cancer`
- `Tropic of Capricorn`

#### name:{code}

Localized name of the major circles of latitudes or prime meridians in a specific language.

`{code}` represents [ISO 639 language code](#languages).


#### nth_line
Specifies the order of a geographic line.

Values:
- `1`
- `5`
- `15`
- `30`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### timezone

Layer containing timezone boundaries as polygons based on IANA timezone database.

## Fields

### abbr_sdt
Timezone abbreviation during standard time.

Values:

- `ACST`
- `AEST`
- `AKST`
- `AST`
- `AWST`
- `CAT`
- `CET`
- `CST`
- `ChST`
- `EAT`
- `EET`
- `EST`
- `GMT`
- `HKT`
- `HST`
- `IST`
- `JST`
- `KST`
- `MSK`
- `MST`
- `NST`
- `NZST`
- `PKT`
- `PST`
- `SAST`
- `SST`
- `UTC`
- `WAT`
- `WET`
- `WIB`
- `WIT`
- `WITA`

### abbr_dst

Timezone abbreviation during daylight saving time.

Values:

- `ACDT`
- `ADT`
- `AEDT`
- `AKDT`
- `BST`
- `CDT`
- `CEST`
- `EDT`
- `EEST`
- `HDT`
- `IDT`
- `IST`
- `MDT`
- `NDT`
- `NZDT`
- `PDT`
- `WEST`

### tz_id
Unique IANA timezone identifier.

Examples:
- `America/New_York`
- `Europe/London`


### utc_offset_sdt

UTC offset in hours during standard time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3`
- `-2.5`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+13`
- `+13.75`
- `+14`

### utc_offset_dst

UTC offset in hours during daylight saving time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3.5`
- `-3`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+12.75`
- `+13`
- `+14`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### timezone_label

Layer containing label points for timezone zones, suitable for placing timezone name labels on a map.

## Fields

### abbr_sdt
Timezone abbreviation during standard time.

Values:

- `ACST`
- `AEST`
- `AKST`
- `AST`
- `AWST`
- `CAT`
- `CET`
- `CST`
- `ChST`
- `EAT`
- `EET`
- `EST`
- `GMT`
- `HKT`
- `HST`
- `IST`
- `JST`
- `KST`
- `MSK`
- `MST`
- `NST`
- `NZST`
- `PKT`
- `PST`
- `SAST`
- `SST`
- `UTC`
- `WAT`
- `WET`
- `WIB`
- `WIT`
- `WITA`

### abbr_dst

Timezone abbreviation during daylight saving time.

Values:

- `ACDT`
- `ADT`
- `AEDT`
- `AKDT`
- `BST`
- `CDT`
- `CEST`
- `EDT`
- `EEST`
- `HDT`
- `IDT`
- `IST`
- `MDT`
- `NDT`
- `NZDT`
- `PDT`
- `WEST`

### tz_id
Unique IANA timezone identifier.

Examples:
- `America/New_York`
- `Europe/London`


### utc_offset_sdt

UTC offset in hours during standard time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3`
- `-2.5`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+13`
- `+13.75`
- `+14`

### utc_offset_dst

UTC offset in hours during daylight saving time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3.5`
- `-3`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+12.75`
- `+13`
- `+14`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### utc_offset_zone_dst

Layer containing polygons of UTC timezones based on daylight saving time offset.

## Fields

### utc_offset
UTC offset in hours.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3`
- `-2.5`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+13`
- `+13.75`
- `+14`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### utc_offset_zone_label

Layer containing polygons of UTC timezones based on standard time offset.

## Fields

### order
Order of the points for given zone from south to north. 

Values:
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `10`
- `11`
- `12`
- `13`
- `14`
- `15`
- `16`
- `17`
- `18`
- `19`
- `20`
- `21`
- `22`

### utc_offset_dst
UTC offset in hours for daylight saving time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3`
- `-2.5`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+13`
- `+13.75`
- `+14`

### utc_offset_sdt
UTC offset in hours for standard time.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3.5`
- `-3`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+12.75`
- `+13`
- `+14`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### utc_offset_zone_sdt

Layer containing polygons of UTC timezones based on standard time offset.

## Fields

### utc_offset
UTC offset in hours.

Values:
- `-12`
- `-11`
- `-10`
- `-9.5`
- `-9`
- `-8`
- `-7`
- `-6`
- `-5`
- `-4`
- `-3.5`
- `-3`
- `-2`
- `-1`
- `0`
- `+1`
- `+2`
- `+3`
- `+3.5`
- `+4`
- `+4.5`
- `+5`
- `+5.5`
- `+5.75`
- `+6`
- `+6.5`
- `+7`
- `+8`
- `+8.75`
- `+9`
- `+9.5`
- `+10`
- `+10.5`
- `+11`
- `+12`
- `+12.75`
- `+13`
- `+14`

### Min zoom:

`0`

### Max zoom:

`14` (possible overzooming up to `22`)

### Unique id

`True`

### languages

List of possible languages available in MapTiler Grid.

Read more in the article about [Change language in a map](/guides/map-design/change-language-in-a-map).

### Fields

#### name:{code}

Localized name of the feature in a specific language.

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

