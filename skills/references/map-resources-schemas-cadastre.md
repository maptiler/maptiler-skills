# MapTiler Cadastre

Source: https://docs.maptiler.com/schema/cadastre/

Tileset containing cadastral layers, parcel information, buildings, etc.

MapTiler Cadastre is a tileset containing real estate cadastre information. 
Design of tileset containing the most useful information 
(availability depends on country) like parcel, buildings and their numbers, 
land-use, or addresses. Tileset provides the most precise geometry 
(low scale mapping) with additional information for interconnecting 
with authorities.

Nevertheless, this Tileset cannot be used for any legal action and in any legal 
case please contact the competent authority.

## Layers

### address

---
category: schema-cadastre
title: address
etl_graph: /media/etl_address.png
mapping_graph: /media/mapping_address.png
sql_query: SELECT geometry, id, name, address, source FROM
  layer_address(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Building access name or number layer attributes."
---
Name or number that describes the building access.

### Fields

#### id

Building ID defined by the responsible party.

#### name

Housenumber.

#### address

Address of the building if it's provided.

#### source

Source of data from the responsible party.

### building

---
layout: simple-no-sidebar
category: schema-cadastre
title: building
etl_graph: /media/etl_building.png
mapping_graph: /media/mapping_building.png
sql_query: SELECT geometry, id, area, type, type_code, source, created, updated
  FROM layer_building(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Building polygon on the parcel layer attributes."
---
Polygon of the building that is on the parcel used.

### Fields

#### id

Building ID defined by the responsible party.

#### area

The indicative area of the polygon is in square meters. If it is not specified in the source data then it is computed in the original projection.

#### type

Usage of the parcel that is specified by the provider.

#### type_code

Code of the type defined by the responsible party.

#### source

Source of data from the responsible party.

#### created

Date of data creation.

#### updated

Date of data update.

### landuse

---
layout: simple-no-sidebar
category: schema-cadastre
title: landuse
etl_graph: /media/etl_landuse.png
mapping_graph: /media/mapping_landuse.png
sql_query: SELECT geometry, id, type, type_code, source, created, updated FROM
  layer_landuse(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Landuse and human usage layer attributes."
---
Landuse is used to describe use of land by humans.

### Fields

#### id

ID defined by the responsible party.

#### type

Usage of the area that is specified by the provider. In English.

Possible values:

- `building`
- `street`
- `pavement`
- `trafic_island`
- `train`
- `aerodrome`
- `water`
- `other_building`
- `field`
- `vines`
- `intensive_culture`
- `garden`
- `large_fen`
- `other_land`
- `water_standing`
- `water_flowing`
- `water_reed_belt`
- `forest`
- `pasture_dense`
- `pasture_open`
- `other_pasture`
- `rock`
- `glacier`
- `sand`
- `landfill`
- `other_barren_land`
- `wall`
- `underground_building`
- `other_part_of_the_building`
- `culverted_public_water_course`
- `important_staircase`
- `tunnel_underpass_gallery`
- `bridge_passerelle`
- `platform`
- `well`
- `reservoir`
- `pier`
- `shelter`
- `silo`
- `chimney`
- `monument`
- `antenna_pole`
- `observation_tower`
- `embankment`
- `sill`
- `avalanche_barrier`
- `massive_base`
- `ruin_archaeological_object`
- `landing_bridge`
- `single_rock`
- `narrow_stocked_area`
- `rivulet`
- `narrow_path`
- `high_voltage_line`
- `aerialway`
- `axis`
- `shrine_crucifix`
- `spring`
- `other`
- `pressure_line`
- `railway`
- `freight_cableway`
- `ferry`
- `cableway`
- `cave_entrance`
- `ski_lift`
- `noise_barrier`
- `loading_ramp`
- `driving_silo`
- `septic`
- `manure`
- `NULL`


#### type_code

Code of the type defined by the responsible party.

Possible values:

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
- `23`
- `24`
- `25`
- `26`
- `27`
- `28`
- `29`
- `30`
- `34`
- `39`
- `43`
- `44`
- `50`
- `51`
- `52`
- `53`
- `54`
- `55`
- `56`
- `57`
- `58`
- `46`
- `47`
- `48`
- `31`
- `32`
- `33`
- `35`
- `37`
- `40`
- `41`
- `42`
- `60`
- `61`
- `62`


#### source

Source of data from the responsible party.

#### created

Date of data creation.

#### updated

Date of data update.

### parcel

---
layout: simple-no-sidebar
category: schema-cadastre
title: parcel
etl_graph: /media/etl_parcel.png
sql_query: SELECT geometry, id, number, area, landuse, source, created, updated,
  zone FROM layer_parcel(ST_SetSRID('BOX3D(-20037508.34 -20037508.34,
  20037508.34 20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Cadastral map parcel areas and owners attributes."
---
The main part of the cadastral map defines areas and owners.

### Fields

#### id

Parcel ID defined by the responsible party.

#### number

A parcel name is often just a number defined by the responsible party.

#### area

Indicative area of the polygon in square meters. If it is not specified in source data than it is computed in the original projection.

#### landuse

Usage of the parcel that is specified by the provider (e.g. in Austria, Czechia).

#### source

Source of data from the responsible party.

#### created

Date of data creation.

#### updated

Date of data update.

#### zone

Referal of the area in the zone layer.

### parcel_name

---
layout: simple-no-sidebar
category: schema-cadastre
title: parcel_name
etl_graph: /media/etl_parcel_name.png
mapping_graph: /media/mapping_parcel_name.png
sql_query: SELECT geometry, number, rank FROM
  layer_parcel_name(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Parcel name or number layer attributes."
---
Name or number that describes the parcel.

### Fields

#### number

A parcel name is often just a number defined by the responsible party.

#### rank

The difference in parcel name number meaning.

Possible values:

- `1 - Parcel number`
- `2 - Permanent right`
- `3 - Building (object) parcel number`
- `4 - Name of the building`

### survey_point

---
layout: simple-no-sidebar
category: schema-cadastre
title: survey_point
etl_graph: /media/etl_survey_point.png
sql_query: SELECT geometry, number, category, mark, height, coord1, coord2,
  updated, created, source FROM
  layer_survey_point(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Fixed and border survey points layer attributes."
---
Fixed points and border points differentiate by category and marker type.
Some of the survey points include coordinates in the local reference system (e.g. for Switzerland it is LV95 EPSG:2056)
and height in meters.

### Fields

#### number

A point number (name) is often just a number defined by the responsible party.

#### category

Category of fix points.
LFP1 - Points of the National Survey LV95
LFP2 - Points of the cantonal triangulation
LFP3 - Points of the parcel survey
HFP1 - Points of the national levelling LN02
HFP2 - Points of the cantonal levelling
HFP3 - Points of communal levelling
border - Border points indicate the course of borders and boundaries.

Possible values:

- `LFP1`
- `LFP2`
- `LFP3`
- `HFP1`
- `HFP2`
- `HFP3`
- `border`


#### mark

Type of physical object.

#### height

Height of the point in meters and defined by the responsible party.

#### coord1

Coordinate the point in the local reference system and defined by the responsible party.

#### coord2

Coordinate the point in the local reference system and defined by the responsible party.

#### updated

Date of data update.

#### created

Date of data creation.

#### source

Source of data from the responsible party.

### zone

---
layout: simple-no-sidebar
category: schema-cadastre
title: zone
etl_graph: /media/etl_zone.png
sql_query: SELECT geometry, code, level, level_name, area, source FROM
  layer_zone(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 14)
indexed: false
description: "Cadastral territory zones layer attributes."
---
Often cadastral territories are defined by authority or admin level in the Country.

### Fields

#### code

Is defined by the responsible party.

#### level

The hierarchy level number of cadaster units in the country.

#### level_name

The local name of the level is defined and used by the responsible party.

#### source

Source of data from the responsible party.

#### area

The indicative area of the polygon is in square meters. If it is not specified in the source data then it is computed in the original projection.

