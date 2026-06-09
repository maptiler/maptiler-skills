# MapTiler Countries

Source: https://docs.maptiler.com/schema/countries/

Tileset containing boundaries and administrative units of world.

MapTiler Countries is a tileset that contains data about administrative divisions
  of a world based on countries and their territories.

List of features and IDs
Useful links with features for data joins.


  cdn.maptiler.com/data/countries/administrative-level-0.csv
  cdn.maptiler.com/data/countries/administrative-level-1.csv
  cdn.maptiler.com/data/countries/administrative-level-2.csv
  cdn.maptiler.com/data/countries/administrative-level-3.csv
  cdn.maptiler.com/data/countries/postal-level-0.csv
  cdn.maptiler.com/data/countries/postal-level-1-extra.csv
  cdn.maptiler.com/data/countries/postal-level-1.csv

## Layers

### administrative

---
category: schema-countries
title: administrative
etl_graph: /media/etl_administrative.png
sql_query: SELECT gid, geometry, level, iso_a2, code, name,
  NULLIF(tags->'name_int', '') AS "name_int", NULLIF(tags->'name:latin', '') AS
  "name:latin", NULLIF(tags->'name:nonlatin', '') AS "name:nonlatin", wikidata,
  area, continent, level_0, level_1, level_2, level_3 FROM
  layer_administrative(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857 ), 14)
description: "Schema definition for global administrative division data."
indexed: false
---
Contains data about administrative divisions of a world.

### Fields

#### gid

Unique ID for every administrative unit.

#### level

Hiearchy of administrative level (0 - country; 1 - state, kraj, federal state; 2 - county, ORP; 3 - municipalities; 4 - minor civil divisions).

#### iso_a2

ISO A2 code of the country.

#### code

Locally recognized code of the administrative unit.

#### name

Primary (local or official) name of the administrative unit.

#### name:{code}

Localized name of the administrative unit in a specific language.

`{code}` represents [ISO 639 language code](#languages).

#### wikidata

Wikidata ID of the administrative unit.

#### area

Area of the administrative unit (square kilometer).

#### continent

The name of the continent in which the country is located.

#### level_0

ISO A2 code of the country.

#### level_1

The name of the 1st hierarchy division of the administrative unit.

#### level_2

The name of the 2st hierarchy division of the administrative unit.

#### level_3

The name of the 3st hierarchy division of the administrative unit.

### Min zoom:

`0`

### Max zoom:

`11` (possible overzooming up to `22`)

### postal

---
layout: simple-no-sidebar
category: schema-countries
title: postal
etl_graph: /media/etl_postal.png
sql_query: SELECT gid, geometry, level, iso_a2, code, name, area, level_0,
  level_1, level_2 FROM layer_postal(ST_SetSRID('BOX3D(-20037508.34
  -20037508.34, 20037508.34 20037508.34)'::box3d, 3857 ), 14)
description: "Schema definition for administrative divisions at zip code level."
indexed: false
---
Contains data about administrative divisions at zip code level.

### Fields

#### gid

Unique ID for every administrative unit.

#### level

Hiearchy of administrative level (0 - grouped zip code; 1 - detailed zip codes).

#### iso_a2

ISO A2 code of the country.

#### code

Locally recognized code of the administrative unit.

#### name

Name of the administrative unit.

#### area

Area of the administrative unit (square kilometer).

#### level_0

ISO A2 code of the country.

#### level_1

The name of the 1st hierarchy division of the administrative unit.

#### level_2

The name of the 2st hierarchy division of the administrative unit.

### Min zoom:

`6`

### Max zoom:

`11` (possible overzooming up to `22`)

### languages

---
category: schema-countries
title: languages
description: "List of possible languages in MapTiler Countries tileset."
indexed: false
---
List of possible languages available in MapTiler Countries tileset.

Read more in the article about [Change language in a map](/guides/map-design/change-language-in-a-map).

### Fields

#### name_

Special forms of names are always included if there is a name.
These values are used in style as e.g. `{name_latin}` or `{name_int}`

Possible values:

- `latin` (Latin script of the name)
- `int` (International form of the name)

#### name:{code}

Localized name of the feature in a specific language.

`{code}` represents ISO 639 language code.

Possible `{code}` values:

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
- `ja-Hira` (Japanese Hiragana form)
- `ja_kana` (Japanese Kana form)
- `ja-Latn` (romanisation of Japanese since 2018)
- `ja_rm` (romanization of Japanese)
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
- `ml` (Malayalam)
- `mt` (Maltese)
- `nb` (Norwegian Bokmål)
- `nl` (Dutch)
- `nn` (Norwegian Nynorsk)
- `no` (Norwegian)
- `oc` (Occitan (post 1500))
- `pa` (Punjabi)
- `pl` (Polish)
- `pnb` (Western Punjabi)
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
- `zh-Hans` (Simplified Chinese)
- `zh-Hant` (Traditional Chinese)

