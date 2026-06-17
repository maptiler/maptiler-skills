# MapTiler Planet Lite

Source: https://docs.maptiler.com/schema/planet-lite/

Tileset containing general layers with topographic information for an attribtution free map.

MapTiler Planet Lite
  is a tileset containing general layers containing topographic information for a copyright-free map
  of the entire world up to zoom 10.

## Layers

### aerodrome_label

Aeroports.

### Fields

#### name

Name of the aerodrome.

#### class

Distinguish between more and less important aerodromes.

Possible values:

- `spaceport`
- `regional`
- `military`
- `national`
- `international`


#### iata

3-character code issued by the IATA.

### boundary

Contains administrative boundaries as linestrings.

### Fields

#### admin_level

Admin_level indicating the level of importance of this boundary.

Possible values:

- `2`
- `4`
- `6`


#### adm0_l

State name on the left of the border. For country boundaries only (`admin_level = 2`) from z4.

#### adm0_r

State name on the right of the border. For country boundaries only (`admin_level = 2`) from z4.

#### disputed

Mark with `1` if the border is disputed.

Possible values:

- `0`
- `1`


#### disputed_name

Field containing name of the disputed area. For country boundaries only (`admin_level = 2`).

#### maritime

Mark with 1 if it is a maritime border.

Possible values:

- `0`
- `1`

### globallandcover

Landcover with generalized polygons up to zoom 10 with classes - crop, grass, scrub, tree, forest, snow.

### Fields

#### class

An attribute o assign natural colors for globallandcover.

Possible values:

- `crop`
- `grass`
- `scrub`
- `tree`
- `forest`
- `snow`

### landcover

Landcover is used to describe the physical material at the surface of the earth.

### Fields

#### class

Use the **class** to assign natural colors for **landcover**.

Possible values:

- `ice`


#### subclass

Use **subclass** to do more precise styling.

Possible values:

- `glacier`
- `ice_shelf`

### landuse

Landuse is used to describe use of land by humans.

### Fields

#### class

Use the **class** to assign special colors to areas.

Possible values:

- `residential`

### mountain_peak

Natural peaks.

### Fields

#### name

Name of the peak.

#### class



Possible values:

- `mountain`


#### ele

Elevation (`ele`) in meters.

#### ele_ft

Elevation (`ele`) in feets.

#### customary_ft

Value 1 for peaks in location where feet is used as customary unit (USA).

Possible values:

- `1`


#### rank

Rank of the peak within one tile (starting at 1 that is the most important peak).

### park

National Park units in the United States only.

### Fields

#### class



Possible values:

- `national_park`
- `nature_reserve`
- `protected_area`


#### name

Name of the park (point features only).

#### rank

Rank of the park within one tile, starting at 1 that is the most important park (point features only).

### place

The place layer consists out of continents, countries, states and cities.

### Fields

#### id

ID of the place name. When available, the ID is Wikidata ID, then GeoNames, or generic.

#### name

The name of the unit.

#### capital

The **capital** field marks the place is a capital of.

Possible values:

- `2`
- `4`


#### class

Distinguish between continents, countries, states and
places like settlements or smaller entities.
Use **class** to separately style the different places and build
a text hierarchy according to their importance.

Possible values:

- `continent`
- `country`
- `state`
- `province`
- `city`


#### iso_a2

Two-letter country code ISO alpha-2.

#### rank

Countries, states and the most important cities all have a
**rank** to boost their importance on the map.

### poi

Points of interests containing `port` and `cape` tags.

### Fields

#### name

The name value of the POI.

#### class



Possible values:

- `harbor`
- `natural`


#### rank

Values of importance.

### transportation

Transportation contains roads, railways and shipping lines.
It contains all roads from motorways to primary, secondary and
tertiary. Roads Styling the roads is the most essential part of the map.

### Fields

#### class

Distinguish between more and less important roads or railways and roads under construction.

Possible values:

- `ferry`
- `motorway`
- `primary`
- `secondary`
- `tertiary`
- `minor`
- `track`
- `motorway_construction`
- `rail`


#### network

See more info about [`us-*`](https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_States),
[`ca-transcanada`](https://en.wikipedia.org/wiki/Trans-Canada_Highway),
or [`gb-*`](https://wiki.openstreetmap.org/wiki/United_Kingdom_Tagging_Guidelines#UK_roads).

Possible values:

- `ca-transcanada`
- `gb-motorway`
- `gb-trunk`
- `us-highway`
- `us-interstate`
- `us-state`

### transportation_name

This is the layer for labelling the highways. Only highways that are named `name=*` and are long enough
to place text upon appear. The roads are stitched together if they contain the same name
to have better label placement than having many small linestrings.
For motorways you should use the `ref` field to label them while for other roads you should use `name`.

### Fields

#### name

The name of the highway or road.

#### ref

Name value of the motorway or its network.

#### ref_length

Length of the `ref` field. Useful for having a shield icon as background for labeling motorways.

#### network

See more info about [`us-*`](https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_States),
[`ca-transcanada`](https://en.wikipedia.org/wiki/Trans-Canada_Highway),
or [`gb-*`](https://wiki.openstreetmap.org/wiki/United_Kingdom_Tagging_Guidelines#UK_roads).

Possible values:

- `ca-transcanada`
- `gb-motorway`
- `gb-trunk`
- `us-highway`
- `us-interstate`
- `us-state`
- `road`


#### class

Distinguish between more and less important roads and roads under construction.

Possible values:

- `motorway`
- `primary`
- `secondary`
- `tertiary`
- `minor`
- `track`
- `motorway_construction`
- `rail`
- `ferry`


#### route_1

1st route concurrency.

#### route_2

2nd route concurrency.

#### route_3

3rd route concurrency.

#### route_4

4th route concurrency.

Possible values:

- `E442`
- `E70`
- `E761`
- `E85`

### water

Water polygons representing oceans and lakes.

### Fields

#### id

ID of the lake. When available, the ID is Wikidata ID (e.g. Lake Geneva - Q6403)

#### class

All water polygons.

Possible values:

- `ocean`
- `lake`

### waterway

Waterways.

### Fields

#### name

Name of the waterway.

#### class



Possible values:

- `canal`
- `river`


#### intermittent

Mark with `1` if it is an intermittent waterway.

Possible values:

- `0`
- `1`

### water_name

Labelling of water bodies. See possible values in class.

### Fields

#### name

Name of the water body.

#### class

Distinguish between `lake`, `ocean`, `sea` and others .

Possible values:

- `lake`
- `bay`
- `channel`
- `fjord`
- `gulf`
- `inlet`
- `lagoon`
- `ocean`
- `reef`
- `river`
- `sea`
- `sound`
- `strait`

