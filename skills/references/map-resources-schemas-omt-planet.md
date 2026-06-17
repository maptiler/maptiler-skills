# OpenMapTiles Planet

Source: https://docs.maptiler.com/schema/omt-planet/

Tileset containing general layers with topographic information from OSM data.

OpenMapTiles Planet
  is a tileset containing general layers with topographic information based on OSM Data.
  It is built to use as a general context of a map for daily life or as a base of visualization for your data.

## Layers

### aerodrome_label

[Aerodrome labels](https://wiki.openstreetmap.org/wiki/Tag:aeroway%3Daerodrome)

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the aerodrome.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### class

Distinguish between more and less important aerodromes.
Class is derived from the value of
[`aerodrome`](https://wiki.openstreetmap.org/wiki/Proposed_features/Aerodrome)
and `aerodrome:type` tags.

Possible values:

- `international`
- `public`
- `regional`
- `military`
- `private`
- `other`


#### iata

3-character code issued by the IATA.

#### icao

4-letter code issued by the ICAO.

#### ele

Elevation (`ele`) in meters.

#### ele_ft

Elevation (`ele`) in feets.

### aeroway

Aeroway polygons based of OpenStreetMap [aeroways](https://wiki.openstreetmap.org/wiki/Aeroways).
Airport buildings are contained in the **building** layer but all
other airport related polygons can be found in the **aeroway** layer.

### Fields

#### ref

The OSM [`ref`](https://wiki.openstreetmap.org/wiki/Key:ref) tag of the runway/taxiway.

#### class

The original value of
[`aeroway`](https://wiki.openstreetmap.org/wiki/Key:aeroway) or
`area:aeroway` tag.

Possible values:

- `aerodrome`
- `heliport`
- `runway`
- `helipad`
- `taxiway`
- `apron`
- `gate`

### boundary

Contains administrative boundaries as linestrings.
Until z4 [Natural Earth data](https://www.naturalearthdata.com/downloads/) is used after which
OSM boundaries ([`boundary=administrative`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative))
are present from z5 to z14 (also for maritime boundaries with `admin_level <= 2` at z4).
OSM data contains several [`admin_level`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#admin_level)
but for most styles it makes sense to just style `admin_level=2` and `admin_level=4`.

### Fields

#### admin_level

OSM [admin_level](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#admin_level)
indicating the level of importance of this boundary.
The `admin_level` corresponds to the lowest `admin_level`
the line participates in.
At low zoom levels the Natural Earth boundaries are mapped to the equivalent admin levels.

#### adm0_l

State name on the left of the border. For country boundaries only (`admin_level = 2`).

#### adm0_r

State name on the right of the border. For country boundaries only (`admin_level = 2`).

#### disputed

Mark with `1` if the border is disputed.

Possible values:

- `0`
- `1`


#### disputed_name

Field containing name of the disputed area (extracted from border relation in OSM, without spaces).
For country boundaries only (`admin_level = 2`).
Value examples from Asian OSM pbf extract

Possible values:

- `AbuMusaIsland`
- `BaraHotiiValleys`
- `ChineseClaim`
- `Crimea`
- `Demchok`
- `Dokdo`
- `IndianClaim-North`
- `IndianClaimwesternKashmir`
- `PakistaniClaim`
- `SamduValleys`
- `TirpaniValleys`


#### claimed_by

ISO2 code of country, which wants to see the boundary line.
For country boundaries only (`admin_level = 2`).

#### maritime

Mark with `1` if it is a maritime border.

Possible values:

- `0`
- `1`

### building

All [OSM Buildings](https://wiki.openstreetmap.org/wiki/Buildings). All building tags are imported ([`building=*`](https://wiki.openstreetmap.org/wiki/Key:building)).
Only buildings with tag location:underground are excluded.

### Fields

#### render_height

An approximated height from levels and height of the building or building:part.

#### render_min_height

An approximated height from minimum levels or minimum height of the bottom of the building or building:part.

#### colour

Colour

#### hide_3d

If True, building (part) should not be rendered in 3D. Currently, [building outlines](https://wiki.openstreetmap.org/wiki/Simple_3D_buildings) are marked as hide_3d.

### housenumber

Everything in OpenStreetMap which contains a `addr:housenumber` tag useful for labelling housenumbers on a map.
This adds significant size to *z14*. For buildings the centroid of the building is used as housenumber.

### Fields

#### housenumber

Value of the [`addr:housenumber`](https://wiki.openstreetmap.org/wiki/Key:addr) tag.

### landcover

Landcover is used to describe the physical material at the surface of the earth. At lower zoom levels this is
from Natural Earth data for glaciers and ice shelves and at higher zoom levels the landcover is [implied by OSM tags](https://wiki.openstreetmap.org/wiki/Landcover). The most common use case for this layer
  is to style wood (`class=wood`) and grass (`class=grass`) areas.

### Fields

#### class

Use the **class** to assign natural colors for **landcover**.

Possible values:

- `farmland`
- `ice`
- `wood`
- `rock`
- `grass`
- `wetland`
- `sand`


#### subclass

Use **subclass** to do more precise styling.
Original value of either the
[`natural`](https://wiki.openstreetmap.org/wiki/Key:natural),
[`landuse`](https://wiki.openstreetmap.org/wiki/Key:landuse),
[`leisure`](https://wiki.openstreetmap.org/wiki/Key:leisure),
or [`wetland`](https://wiki.openstreetmap.org/wiki/Key:wetland) tag.

Possible values:

- `allotments`
- `bare_rock`
- `beach`
- `bog`
- `dune`
- `scrub`
- `shrubbery`
- `farm`
- `farmland`
- `fell`
- `forest`
- `garden`
- `glacier`
- `grass`
- `grassland`
- `golf_course`
- `heath`
- `mangrove`
- `marsh`
- `meadow`
- `orchard`
- `park`
- `plant_nursery`
- `recreation_ground`
- `reedbed`
- `saltern`
- `saltmarsh`
- `sand`
- `scree`
- `swamp`
- `tidalflat`
- `tundra`
- `village_green`
- `vineyard`
- `wet_meadow`
- `wetland`
- `wood`

### landuse

Landuse is used to describe use of land by humans. At lower zoom levels this is
from Natural Earth data for residential (urban) areas and at higher zoom levels mostly OSM `landuse` tags.

### Fields

#### class

Use the **class** to assign special colors to areas.
Original value of either the
[`landuse`](https://wiki.openstreetmap.org/wiki/Key:landuse),
[`amenity`](https://wiki.openstreetmap.org/wiki/Key:amenity),
[`leisure`](https://wiki.openstreetmap.org/wiki/Key:leisure),
[`tourism`](https://wiki.openstreetmap.org/wiki/Key:tourism),
[`place`](https://wiki.openstreetmap.org/wiki/Key:place)
or [`waterway`](https://wiki.openstreetmap.org/wiki/Key:waterway) tag.

Possible values:

- `railway`
- `cemetery`
- `military`
- `residential`
- `commercial`
- `industrial`
- `garages`
- `retail`
- `bus_station`
- `school`
- `university`
- `kindergarten`
- `college`
- `library`
- `hospital`
- `stadium`
- `pitch`
- `playground`
- `track`
- `theme_park`
- `zoo`
- `suburb`
- `quarter`
- `neighbourhood`
- `dam`
- `quarry`

### mountain_peak

[Natural peaks](https://wiki.openstreetmap.org/wiki/Tag:natural%3Dpeak)

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the peak.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### class

Use the **class** to differentiate between natural objects.

Possible values:

- `peak`
- `volcano`
- `saddle`
- `ridge`
- `cliff`
- `arete`


#### ele

Elevation (`ele`) in meters.

#### ele_ft

Elevation (`ele`) in feet.

#### customary_ft

Value 1 for peaks in location where feet is used as customary unit (USA).

Possible values:

- `1`
- `None`


#### rank

Rank of the peak within one tile (starting at 1 that is the most important peak).

### park

The park layer contains parks from OpenStreetMap tagged with
[`boundary=national_park`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dnational_park),
[`boundary=protected_area`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dprotected_area),
or [`leisure=nature_reserve`](https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dnature_reserve).

### Fields

#### class

Use the **class** to differentiate between different parks.
The class for `boundary=protected_area` parks is the lower-case of the
[`protection_title`](https://wiki.openstreetmap.org/wiki/key:protection_title)
value with blanks replaced by `_`.
`national_park` is the class of `protection_title=National Park` and `boundary=national_park`.
`nature_reserve` is the class of `protection_title=Nature Reserve` and `leisure=nature_reserve`.
The class for other [`protection_title`](https://wiki.openstreetmap.org/wiki/key:protection_title) 
values is similarly assigned.

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the park (point features only).

#### name_en

English name `name:en` if available, otherwise `name` (point features only).

#### name_de

German name `name:de` if available, otherwise `name` or `name:en` (point features only).

#### rank

Rank of the park within one tile, starting at 1 that is the most important park (point features only).

### place

The place layer consists out of [countries](https://wiki.openstreetmap.org/wiki/Tag:place%3Dcountry),
[states](https://wiki.openstreetmap.org/wiki/Tag:place%3Dstate), [cities](https://wiki.openstreetmap.org/wiki/Key:place)
and [islands](https://wiki.openstreetmap.org/wiki/Tag:place%3Disland).
Apart from the roads this is also one of the more important layers to create a beautiful map.
We suggest you use different font styles and sizes to create a text hierarchy.

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the POI.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### capital

The **capital** field marks the
[`admin_level`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#admin_level)
of the boundary the place is a capital of.

Possible values:

- `2`
- `3`
- `4`
- `5`
- `6`


#### class

Original value of the
[`place`](https://wiki.openstreetmap.org/wiki/Key:place) tag.
Distinguish between continents, countries, states, islands and
places like settlements or smaller entities.
Use **class** to separately style the different places and build
a text hierarchy according to their importance.

Possible values:

- `continent`
- `country`
- `state`
- `province`
- `city`
- `town`
- `village`
- `hamlet`
- `suburb`
- `quarter`
- `neighbourhood`
- `isolated_dwelling`
- `island`


#### iso_a2

Two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). Available only for `class=country`.
Original value of the
[`country_code_iso3166_1_alpha_2`](https://wiki.openstreetmap.org/wiki/Tag:place%3Dcountry) tag.

#### rank

Countries, states and the most important cities all have a
**rank** to boost their importance on the map.
The **rank** field for countries and states ranges from
`1` to `6` while the **rank** field for cities ranges from
`1` to `10` for the most important cities
and continues from `10` serially based on the
local importance of the city (derived from population and city class).
You can use the **rank** to limit density of labels or improve
the text hierarchy.
The rank value is a combination of the Natural Earth
`scalerank`, `labelrank` and `datarank` values for countries
and states and for cities consists out of a shifted
Natural Earth `scalerank` combined with a local rank
within a grid for cities that do not have a Natural Earth `scalerank`.

### poi

[Points of interests](https://wiki.openstreetmap.org/wiki/Points_of_interest) containing
a of a variety of OpenStreetMap tags. Mostly contains amenities, sport, shop and tourist POIs.

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the POI.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### class

More general classes of POIs. If there is no more general `class` for the `subclass`
this field will contain the same value as `subclass`.
But for example for schools you only need to style the class `school` to filter the subclasses `school`
and `kindergarten`. Or use the class `shop` to style all shops.

Possible values:

- `shop`
- `town_hall`
- `golf`
- `fast_food`
- `park`
- `bus`
- `railway`
- `aerialway`
- `entrance`
- `campsite`
- `laundry`
- `grocery`
- `library`
- `college`
- `lodging`
- `ice_cream`
- `post`
- `cafe`
- `school`
- `alcohol_shop`
- `bar`
- `harbor`
- `car`
- `hospital`
- `cemetery`
- `attraction`
- `beer`
- `music`
- `stadium`
- `art_gallery`
- `clothing_store`
- `swimming`
- `castle`
- `atm`


#### subclass

Original value of either the
[`amenity`](https://wiki.openstreetmap.org/wiki/Key:amenity),
[`barrier`](https://wiki.openstreetmap.org/wiki/Key:barrier),
[`historic`](https://wiki.openstreetmap.org/wiki/Key:historic),
[`information`](https://wiki.openstreetmap.org/wiki/Key:information),
[`landuse`](https://wiki.openstreetmap.org/wiki/Key:landuse),
[`leisure`](https://wiki.openstreetmap.org/wiki/Key:leisure),
[`railway`](https://wiki.openstreetmap.org/wiki/Key:railway),
[`shop`](https://wiki.openstreetmap.org/wiki/Key:shop),
[`sport`](https://wiki.openstreetmap.org/wiki/Key:sport),
[`station`](https://wiki.openstreetmap.org/wiki/Key:station),
[`religion`](https://wiki.openstreetmap.org/wiki/Key:religion),
[`tourism`](https://wiki.openstreetmap.org/wiki/Key:tourism),
[`aerialway`](https://wiki.openstreetmap.org/wiki/Key:aerialway),
[`building`](https://wiki.openstreetmap.org/wiki/Key:building),
[`highway`](https://wiki.openstreetmap.org/wiki/Key:highway),
[`office`](https://wiki.openstreetmap.org/wiki/Key:office)
or [`waterway`](https://wiki.openstreetmap.org/wiki/Key:waterway)
tag.  Use this to do more precise styling.

#### rank

The POIs are ranked ascending according to their importance within a grid. The `rank` value shows the
local relative importance of a POI within it's cell in the grid. This can be used to reduce label density at *z14*.
Since all POIs already need to be contained at *z14* you can use `less than rank=10` epxression to limit
POIs. At some point like *z17* you can show all POIs.

#### agg_stop

Experimental feature! Indicates main platform of public transport
stops (buses, trams, and subways). Grouping of platforms is
implemented using
[`uic_ref`](https://wiki.openstreetmap.org/wiki/Key:uic_ref) tag that
 is not used worldwide.

Possible values:

- `1`


#### level

Original value of [`level`](https://wiki.openstreetmap.org/wiki/Key:level) tag.

#### layer

Original value of [`layer`](https://wiki.openstreetmap.org/wiki/Key:layer) tag.

#### indoor

Original value of [`indoor`](https://wiki.openstreetmap.org/wiki/Key:indoor) tag.

Possible values:

- `1`

### transportation

**transportation** contains roads, railways, aerial ways, and shipping
 lines.
This layer is directly derived from the OSM road hierarchy.
At lower zoom levels major highways from Natural Earth are used.
It contains all roads from motorways to primary, secondary and
tertiary roads to residential roads and
foot paths. Styling the roads is the most essential part of the map.
The `transportation` layer also contains polygons for features like plazas.

### Fields

#### class

Distinguish between more and less important roads or railways and roads under construction.
Class is derived from the value of the
[`highway`](https://wiki.openstreetmap.org/wiki/Key:highway),
[`construction`](https://wiki.openstreetmap.org/wiki/Key:construction),
[`railway`](https://wiki.openstreetmap.org/wiki/Key:railway),
[`aerialway`](https://wiki.openstreetmap.org/wiki/Key:aerialway),
[`route`](https://wiki.openstreetmap.org/wiki/Key:route) tag (for
shipping ways),
[`busway`](https://wiki.openstreetmap.org/wiki/Key:busway), or
[`man_made`](https://wiki.openstreetmap.org/wiki/Key:man_made).

Possible values:

- `motorway`
- `trunk`
- `primary`
- `secondary`
- `tertiary`
- `minor`
- `path`
- `service`
- `track`
- `raceway`
- `busway`
- `bus_guideway`
- `ferry`
- `motorway_construction`
- `trunk_construction`
- `primary_construction`
- `secondary_construction`
- `tertiary_construction`
- `minor_construction`
- `path_construction`
- `service_construction`
- `track_construction`
- `raceway_construction`


#### subclass

Distinguish more specific classes of railway and path:
Subclass is value of the
[`railway`](https://wiki.openstreetmap.org/wiki/Key:railway),
[`highway`](https://wiki.openstreetmap.org/wiki/Key:highway) (for paths), or
[`public_transport`](https://wiki.openstreetmap.org/wiki/Key:public_transport) (for platforms) tag.

Possible values:

- `rail`
- `narrow_gauge`
- `preserved`
- `funicular`
- `subway`
- `light_rail`
- `monorail`
- `tram`
- `pedestrian`
- `path`
- `footway`
- `cycleway`
- `steps`
- `bridleway`
- `corridor`
- `platform`
- `ferry (DEPRECATED - use class)`


#### network

The network type derived mainly from [`network`](https://wiki.openstreetmap.org/wiki/Key:network) tag of the road.
See more info about [`us-*`](https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_States),
[`ca-transcanada`](https://en.wikipedia.org/wiki/Trans-Canada_Highway),
or [`gb-*`](https://wiki.openstreetmap.org/wiki/United_Kingdom_Tagging_Guidelines#UK_roads).

#### brunnel

Mark whether way is a tunnel or bridge.

Possible values:

- `bridge`
- `tunnel`
- `ford`


#### oneway

Mark with `1` whether way is a oneway in the direction of the way,
with `-1` whether way is a oneway in the opposite direction of the way
or not a oneway with `0`.

Possible values:

- `1`
- `-1`


#### ramp

Mark with `1` whether way is a ramp (link or steps)
or not with `0`.

Possible values:

- `1`


#### service

Original value of the [`service`](https://wiki.openstreetmap.org/wiki/Key:service) tag.

Possible values:

- `spur`
- `yard`
- `siding`
- `crossover`
- `driveway`
- `alley`
- `parking_aisle`


#### access

Access restrictions on this road.  Supported values of the
[`access`](https://wiki.openstreetmap.org/wiki/Key:access) tag are `no` and `private`,
which resolve to `no`.

Possible values:

- `False`


#### toll

Whether this is a toll road, based on the [`toll`](https://wiki.openstreetmap.org/wiki/Key:toll) tag.

Possible values:

- `0`
- `1`


#### expressway

Whether this is an expressway, based on the [`expressway`](https://wiki.openstreetmap.org/wiki/Key:expressway) tag.

Possible values:

- `1`


#### layer

Original value of the [`layer`](https://wiki.openstreetmap.org/wiki/Key:layer) tag.

#### level

Experimental feature! Filled only for steps and footways. Original
value of the [`level`](https://wiki.openstreetmap.org/wiki/Key:level) tag.

#### indoor

Experimental feature! Filled only for steps and footways. Original
value of the [`indoor`](https://wiki.openstreetmap.org/wiki/Key:indoor) tag.

Possible values:

- `1`


#### bicycle

Original value of the [`bicycle`](https://wiki.openstreetmap.org/wiki/Key:bicycle) tag (highways only).

#### foot

Original value of the [`foot`](https://wiki.openstreetmap.org/wiki/Key:foot) tag (highways only).

#### horse

Original value of the [`horse`](https://wiki.openstreetmap.org/wiki/Key:horse) tag (highways only).

#### mtb_scale

Original value of the [`mtb:scale`](https://wiki.openstreetmap.org/wiki/Key:mtb:scale) tag (highways only).

#### surface

Values of [`surface`](https://wiki.openstreetmap.org/wiki/Key:surface) tag devided into 2 groups `paved` (paved, asphalt, cobblestone, concrete, concrete:lanes, concrete:plates, metal, paving_stones, sett, unhewn_cobblestone, wood) and `unpaved` (unpaved, compacted, dirt, earth, fine_gravel, grass, grass_paver, gravel, gravel_turf, ground, ice, mud, pebblestone, salt, sand, snow, woodchips).

Possible values:

- `paved`
- `unpaved`

### transportation_name

This is the layer for labelling the highways. Only highways that are named `name=*` and are long enough
to place text upon appear. The OSM roads are stitched together if they contain the same name
to have better label placement than having many small linestrings.
For motorways you should use the `ref` field to label them while for other roads you should use `name`.

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Highways#Names_and_references) value of the highway.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### ref

The OSM [`ref`](https://wiki.openstreetmap.org/wiki/Key:ref) tag of the motorway or its network.

#### ref_length

Length of the `ref` field. Useful for having a shield icon as background for labeling motorways.

#### network

The network type derived mainly from [`network`](https://wiki.openstreetmap.org/wiki/Key:network) tag of the road.
See more info about [`us-*`](https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_States),
[`ca-transcanada`](https://en.wikipedia.org/wiki/Trans-Canada_Highway),
or [`gb-*`](https://wiki.openstreetmap.org/wiki/United_Kingdom_Tagging_Guidelines#UK_roads).

Possible values:

- `us-interstate`
- `us-highway`
- `us-state`
- `ca-transcanada`
- `gb-motorway`
- `gb-trunk`
- `road (default)`


#### class

Distinguish between more and less important roads and roads under construction.

Possible values:

- `motorway`
- `trunk`
- `primary`
- `secondary`
- `tertiary`
- `minor`
- `service`
- `track`
- `path`
- `raceway`
- `motorway_construction`
- `trunk_construction`
- `primary_construction`
- `secondary_construction`
- `tertiary_construction`
- `minor_construction`
- `service_construction`
- `track_construction`
- `path_construction`
- `raceway_construction`
- `rail`
- `transit`
- `motorway_junction`


#### subclass

Distinguish more specific classes of path:
Subclass is value of the
[`highway`](https://wiki.openstreetmap.org/wiki/Key:highway) (for paths),
and "junction" for [`motorway junctions`](https://wiki.openstreetmap.org/wiki/Tag:highway=motorway_junction).

Possible values:

- `pedestrian`
- `path`
- `footway`
- `cycleway`
- `steps`
- `bridleway`
- `corridor`
- `platform`
- `junction`


#### brunnel

Mark whether way is a bridge, a tunnel or a ford.

Possible values:

- `bridge`
- `tunnel`
- `ford`


#### level

Experimental feature! Filled only for steps and footways. Original
value of [`level`](https://wiki.openstreetmap.org/wiki/Key:level) tag.

#### layer

Experimental feature! Filled only for steps and footways. Original
value of [`layer`](https://wiki.openstreetmap.org/wiki/Key:layer) tag.

#### indoor

Experimental feature! Filled only for steps and footways. Original
value of [`indoor`](https://wiki.openstreetmap.org/wiki/Key:indoor) tag.

Possible values:

- `1`


#### route_1

1st route concurrency.

#### route_2

2nd route concurrency.

#### route_3

3rd route concurrency.

#### route_4

4th route concurrency.

#### route_5

5th route concurrency.

#### route_6

6th route concurrency.

### water

Water polygons representing oceans and lakes. Covered watered areas are excluded (`covered=yes`).
On low zoom levels all water originates from Natural Earth. To get a more correct display of the south pole you should also
style the covering ice shelves over the water.
On higher zoom levels water polygons from [OpenStreetMapData](https://osmdata.openstreetmap.de/) are used.
The polygons are split into many smaller polygons to improve rendering performance.
This however can lead to less rendering options in clients since these boundaries show up. So you might not be
able to use border styling for ocean water features.

### Fields

#### id

From zoom 6 are taken OSM IDs. Up to zoom 5 there are used Natural Earth lakes, where are propagated the OSM IDs insted of Natural Earth IDs.
For smaller area then planet, NE lakes keep their Natural Earth IDs.

#### class

All water polygons from [OpenStreetMapData](https://osmdata.openstreetmap.de/) have the class `ocean`.
Water bodies with the [`water=river`](https://wiki.openstreetmap.org/wiki/Tag:water=river) tag are classified as river.  Wet and dry docks
tagged [`waterway=dock`](https://wiki.openstreetmap.org/wiki/Tag:waterway=dock) are classified as a `dock`. 
Swimming pools tagged [`leisure=swimming_pool`](https://wiki.openstreetmap.org/wiki/Tag:leisure=swimming_pool) are classified as a `swimming_pool`
All other water bodies are classified as `lake`.

Possible values:

- `dock`
- `river`
- `lake`
- `ocean`
- `swimming_pool`


#### intermittent

Mark with `1` if it is an [intermittent](https://wiki.openstreetmap.org/wiki/Key:intermittent) water polygon.

Possible values:

- `0`
- `1`


#### brunnel

Identifies the type of crossing as either a bridge or a tunnel.

Possible values:

- `bridge`
- `tunnel`

### waterway

OpenStreetMap [waterways](https://wiki.openstreetmap.org/wiki/Waterways) for higher zoom levels (z9 and more)
and Natural Earth rivers and lake centerlines for low zoom levels (z3 - z8).
Linestrings without a name or which are too short are filtered
out at low zoom levels.
Till z11 there is `river` class only, in z12 there is also `canal` generated,
starting z13 there is no generalization according to `class` field applied.
Waterways do not have a `subclass` field.

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the waterway.
The `name` field may be empty for NaturalEarth data or at lower zoom levels.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### class

The original value of the [`waterway`](https://wiki.openstreetmap.org/wiki/Key:waterway) tag.

Possible values:

- `stream`
- `river`
- `canal`
- `drain`
- `ditch`


#### brunnel

Mark whether way is a tunnel or bridge.

Possible values:

- `bridge`
- `tunnel`


#### intermittent

Mark with `1` if it is an [intermittent](https://wiki.openstreetmap.org/wiki/Key:intermittent) waterway.

Possible values:

- `0`
- `1`

### water_name

Lake center lines for labelling lake bodies.
This is based of the [osm-lakelines](https://github.com/openmaptiles/osm-lakelines) project
which derives nice centerlines from OSM water bodies. Only the most important lakes contain labels.

### Fields

#### name

The OSM [`name`](https://wiki.openstreetmap.org/wiki/Key:name) value of the water body.

#### name_en

English name `name:en` if available, otherwise `name`.

#### name_de

German name `name:de` if available, otherwise `name` or `name:en`.

#### class

Distinguish between `lake`, `ocean` and `sea`.

Possible values:

- `lake`
- `sea`
- `ocean`


#### intermittent

Mark with `1` if it is an [intermittent](https://wiki.openstreetmap.org/wiki/Key:intermittent) lake.

Possible values:

- `0`
- `1`

