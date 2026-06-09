# MapTiler Outdoor

Source: https://docs.maptiler.com/schema/outdoor/

Tileset containing general layers to maps for outdoor life.

MapTiler Outdoor 
is a tileset containing general layers 
to maps for outdoor life like hiking, cycling, cross-country 
skiing, and other related activities.

## Layers

### outdoor_poi

---
category: schema-outdoor
title: outdoor_poi
description: "Point features for outdoor tourism, campsites, and recreational amenities."
etl_graph: media/etl_outdoor_poi.png
mapping_graph: media/mapping_outdoor_poi.png
sql_query: SELECT osm_id, geometry, name, class, subclass FROM
  layer_outdoor_poi(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857 ), 14)
indexed: false
---
**outdoor_poi** (https://wiki.openstreetmap.org/wiki/Hiking) contains tourism information, camp sites, shelters, huts, springs, cave entrances, etc.

##### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the POI.

#### class

Selected values of the
[`information`](https://wiki.openstreetmap.org/wiki/Key:information),
[`tower:type`](https://wiki.openstreetmap.org/wiki/Key:tower:type),
[`shelter_type`](https://wiki.openstreetmap.org/wiki/Key:shelter_type),
[`tourism`](https://wiki.openstreetmap.org/wiki/Key:tourism),
[`amenity`](https://wiki.openstreetmap.org/wiki/Key:amenity),
[`leisure`](https://wiki.openstreetmap.org/wiki/Key:leisure),
[`fireplace`](https://wiki.openstreetmap.org/wiki/Key:fireplace),
[`natural`](https://wiki.openstreetmap.org/wiki/Key:natural),
[`waterway`](https://wiki.openstreetmap.org/wiki/Key:waterway),
[`historic`](https://wiki.openstreetmap.org/wiki/Key:historic),
[`castle_type`](https://wiki.openstreetmap.org/wiki/Key:castle_type),
[`sport`](https://wiki.openstreetmap.org/wiki/Key:sport),
[`man_made`](https://wiki.openstreetmap.org/wiki/Key:man_made) and
[`rental`](https://wiki.openstreetmap.org/wiki/Key:rental) tags.

Possible values:

- `board`
- `map`
- `info_office`
- `guidepost`
- `observation_tower`
- `shelter`
- `hut`
- `camp_site`
- `picnic_site`
- `viewpoint`
- `waterfall`
- `cave_entrance`
- `spring`
- `drinking_water`
- `bench`
- `fireplace`
- `mountain_rescue`
- `first_aid`
- `ski_school`
- `rental`
- `ice_rink`
- `ski_playground`
- `snow_cannon`
- `biathlon`
- `bobsleigh`
- `curling`
- `ice_hockey`
- `ice_skating`
- `skiing`
- `ski_jumping`
- `castle`
- `fortress`
- `ruins`
- `memorial`
- `monument`


#### subclass

Subclasses for shelters, huts, springs, rental and sport according to values of the
[`shelter_type`](https://wiki.openstreetmap.org/wiki/Key:shelter_type),
[`tourism`](https://wiki.openstreetmap.org/wiki/Key:tourism),
[`natural`](https://wiki.openstreetmap.org/wiki/Key:natural),
or [`rental`](https://wiki.openstreetmap.org/wiki/Key:rental) tag.

Possible values:

- `shelter_lean_to`
- `picnic_shelter`
- `rock_shelter`
- `weather_shelter`
- `basic_hut`
- `alpine_hut`
- `wilderness_hut`
- `spring`
- `mineral_spring`
- `ski`
- `sled`
- `skates`

### ski

---
category: schema-outdoor
title: ski
description: "Schema for ski pistes, lifts, and winter sport resort features."
etl_graph: media/etl_ski.png
mapping_graph: media/mapping_ski.png
sql_query: SELECT geometry, class, subclass, name, ref, difficulty, grooming,
  symbol, color FROM layer_ski(ST_SetSRID('BOX3D(-20037508.34 -20037508.34,
  20037508.34 20037508.34)'::box3d, 3857 ), 14)
indexed: false
---
**ski** contains ski + piste routes (line, polygon), lifts (line), avalanche protection features (line) and points of ski resorts, stations and pylons.

##### Fields

#### class

For point features there is choice of ski_resort, station or pylon. Class also distinguish lift and avalanche features from other winter sport categories, see values.

Possible values:

- `ski_resort`
- `station`
- `pylon`
- `lift`
- `avalanche`
- `downhill`
- `nordic`
- `skitour`
- `playground`
- `snow_park`
- `ski_jump`
- `ski_jump_landing`
- `hike`
- `sled`
- `sleigh`
- `ice_skate`
- `fatbike`
- `snowkite`
- `connection`
- `snowshoe`


#### subclass

Classification of class=lift and class=avalanche features.

Possible values:

- `avalanche_protection`
- `avalanche_dam`
- `fence`
- `net`
- `tunnel`
- `chair_lift`
- `drag_lift`
- `j-bar`
- `magic_carpet`
- `mixed_lift`
- `platter`
- `rope_tow`
- `t-bar`
- `funicular`
- `incline`


#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value.

#### ref

Original value of the [`ref`](https://wiki.openstreetmap.org/wiki/Key:ref) tag.

#### difficulty

Original value of the [`piste:difficulty`](https://wiki.openstreetmap.org/wiki/Key:piste:difficulty) tag.

Possible values:

- `novice`
- `easy`
- `intermediate`
- `advanced`
- `expert`
- `freeride`
- `extreme`


#### grooming

Original value of the [`piste:grooming`](https://wiki.openstreetmap.org/wiki/Key:piste:grooming) tag.

Possible values:

- `classic`
- `backcountry`
- `mogul`
- `skating`
- `scooter`


#### symbol

Original value of the [`osmc:symbol`](https://wiki.openstreetmap.org/wiki/Key:osmc:symbol) tag.

#### color

Derived from symbol (for nordic) or assigned according to [`piste:difficulty`](https://wiki.openstreetmap.org/wiki/Key:piste:difficulty) for downhill.

Possible values:

- `red`
- `blue`
- `green`
- `yellow`
- `brown`
- `orange`
- `purple`
- `black`
- `bunny hill`
- `green circle`
- `blue square`
- `black diamond`
- `double black diamond`
- `orange oval`
- `double-black`

### trail

---
category: schema-outdoor
title: trail
description: "Schema for hiking, cycling, and multi-modal outdoor trail routes."
etl_graph: media/etl_trail.png
mapping_graph: media/mapping_trail.png
sql_query: SELECT geometry, class, name, ref, operator, symbol, color, network,
  scale FROM layer_trail(ST_SetSRID('BOX3D(-20037508.34 -20037508.34,
  20037508.34 20037508.34)'::box3d, 3857 ), 14)
indexed: false
---
**trail** contains foot + hiking + bicycle + horse + wheelchair routes and via_ferrata.

##### Fields

#### class

Distinguish between route values.
Class is derived from the value of the
[`route`](https://wiki.openstreetmap.org/wiki/Relation:route) tag
and [`highway`](https://wiki.openstreetmap.org/wiki/Key:highway).

Possible values:

- `foot`
- `hiking`
- `via_ferrata`
- `bicycle`
- `horse`
- `wheelchair`


#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the trail.

#### ref

Original value of the [`ref`](https://wiki.openstreetmap.org/wiki/Key:ref) tag.

#### operator

Original value of the [`operator`](https://wiki.openstreetmap.org/wiki/Key:operator) tag.

#### symbol

Original value of the [`osmc:symbol`](https://wiki.openstreetmap.org/wiki/Key:osmc:symbol) tag.

#### color

Derived from symbol.

Possible values:

- `red`
- `blue`
- `green`
- `yellow`
- `brown`
- `orange`
- `purple`
- `black`


#### network

Original value of the [`network`](https://wiki.openstreetmap.org/wiki/Key:network) tag.

#### scale

Original value of the [`mtb:scale`](https://wiki.openstreetmap.org/wiki/Key:mtb:scale) tag for bicycle tracks,
value of the [`via_ferrata_scale`](https://wiki.openstreetmap.org/wiki/Key:via_ferrata_scale) tag for via_ferrata
value of the [`sac_scale`](https://wiki.openstreetmap.org/wiki/Key:sac_scale) tag for hiking trails.

