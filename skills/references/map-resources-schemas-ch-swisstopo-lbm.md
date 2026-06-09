# CH Swisstopo LeichteBasiskarte

Source: https://docs.maptiler.com/schema/ch-swisstopo-lbm/

Tileset showcasing all SwissTopo layers.

CH Swisstopo Leichte Basiskarte tileset is a tileset showcasing all SwissTopo layers.

## Layers

### aerodrome_label

[Aerodrome labels](https://wiki.openstreetmap.org/wiki/Tag:aeroway%3Daerodrome)

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### class

Distinguish between more and less important aerodromes.

Possible values:

- `international`
- `helipad`
- `regional`
- `other`


#### ele

elevation in meters, measured in reference system LV95, srid 2056.

#### ele_ft

elevation in feet, measured in reference system LV95, srid 2056.

#### iata

iata-code

#### icao

icao-code

### aeroway

Airport buildings are contained in the **building** layer but all
other airport related polygons can be found in the **aeroway** layer.

### Fields

#### class

polygon of surfaces used for aerial operations

Possible values:

- `runway`
- `runway_grass`

### area_name

area_name layer for the LBM, contains points and lines for labelling areas.

### Fields

#### class

area names

Possible values:

- `place`


#### subclass

different classes of areas

Possible values:

- `massif`
- `glacier`


#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

### boundary

Contains administrative boundaries as linestrings.

### Fields

#### admin_level

[`admin_level`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#10_admin_level_values_for_specific_countries) indicating the level of importance of this boundary.
The `admin_level` corresponds to the lowest `admin_level` the line participates in.

#### adm4_l

the name of the administrative unit with admin_level = 4 to the left side of the boundary (canton name) or if it is an enclave (foreign territory) the name of the country. can be used to label boundaries.

#### adm4_r

the name of the administrative unit with admin_level = 4 to the right side of the boundary (canton name) or if it is an enclave (foreign territory) the name of the country. can be used to label boundaries.

#### disputed

wether the boundary is disputed or not

#### maritime

wether the boundary is in the sea or not

### building

buildings including roofs without sidewalls

### Fields

#### render_height

the average height of a building

#### render_min_height

the height of the bottom of the building

### building_ln

building_line layer for the LBM

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### class

Distinguish between classes of geometries.

Possible values:

- `horse_racing`
- `ski_jump`
- `toboggan`
- `track`
- `weir`

### construct

manmade structures not suitable for the layer building.

### Fields

#### class

use class to differentiate between different manmade structures.

Possible values:

- `dam`
- `lock`
- `platform`

### contour_line

contour lines

### Fields

#### class

use class attribute to assign differnt colors for contour_lines.

Possible values:

- `land`
- `ice`
- `scree`
- `water`


#### ele

elevation in meters, measured in reference system LV95, srid 2056.

#### ele_ft

elevation in feet, measured in reference system LV95, srid 2056.

### landcover

Landcover is used to describe the physical material at the surface of the earth.

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


#### subclass

Use **subclass** to do more precise styling.

Possible values:

- `allotments`
- `forest`
- `loose_forest`
- `glacier`
- `golf_course`
- `orchard`
- `park`
- `plant_nursery`
- `scrub`
- `swamp`
- `vineyard`
- `woody_plant`

### landuse

Landuse is used to describe use of land by humans.

### Fields

#### class

Use the **class** to assign special colors to areas.

Possible values:

- `cemetery`
- `landfill`
- `parking`
- `pitch`
- `quarry`

### mountain_peak

peaks or other topographical landmarks.

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### class

Use the **class** to differentiate between different topographic landmarks.

Possible values:

- `alpine_peak`
- `main_peak`
- `peak`
- `main_hill`
- `hill`
- `rocky_knoll`
- `mountain_pass`
- `saddle`


#### ele

elevation in meters, measured in reference system LV95, srid 2056.

#### ele_ft

elevation in feet, measured in reference system LV95, srid 2056.

#### rank

values of 1-5 according to relevance of a peak with more important peaks having lower rank values. can be used to adapt styling and filter mountain_peaks with lower values.

### park

The park layer contains parks from national park and protected areas. contains polygons for area and points for labelling

### Fields

#### class

Use the **class** to differentiate between different parks.

Possible values:

- `national_park`


#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

### place

used to label places.

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### capital

The **capital** field marks the
[`admin_level`](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#admin_level)
of the boundary the place is a capital of.

Possible values:

- `2`
- `4`


#### class

distinguish between different size and importance of labelled places.

Possible values:

- `country`
- `city`
- `town`
- `village`
- `hamlet`
- `isolated_dwelling`
- `neighbourhood`
- `suburb`
- `island`


#### iso_a2

Two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

#### code

Two-letter canton code.

#### population

Approximate number of inhabitants. Can be used to prioritize labelling. Data is not validated and may not be used for analysis!

#### rank

Use **rank** to boost importance of places on the map.
Important places have lowar ranks than less important ones.
The **rank** field for counries IS `1`. 
The **rank** field for cities ranges from `3` to `4`.
places gruadually rank higher serially based on the
local importance of the place with higher ranks being less important.
You can use the **rank** to limit density of labels or improve
the text hierarchy.

### poi

LBM POIs

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### class

More general classes of POIs. If there is no more general `class` for the `subclass`
this field will contain the same value as `subclass`.

Possible values:

- `aerialway`
- `allotments`
- `attraction`
- `boundary_stone`
- `building`
- `bus`
- `campsite`
- `castle`
- `cave`
- `cemetery`
- `college`
- `dam`
- `doline`
- `elevator`
- `ferry_terminal`
- `fuel`
- `funicular`
- `golf`
- `hospital`
- `lock`
- `lodging`
- `military`
- `monastery`
- `monument`
- `motorway`
- `park`
- `pitch`
- `place_of_worship`
- `power`
- `prison`
- `railway`
- `ruins`
- `school`
- `sports_centre`
- `spring`
- `stadium`
- `stone`
- `storage_tank`
- `survey_point`
- `swimming_pool`
- `tower`
- `wastewater_plant`
- `waterfall`
- `weir`
- `zoo`


#### subclass

More refined description.

Possible values:

- `aerialway_station`
- `allotments`
- `alpine_hut`
- `antenna_area`
- `attraction`
- `boundary_stone`
- `building`
- `bus_stop`
- `cable_car_station`
- `camp_site`
- `caravan_site`
- `car_ferry`
- `castle`
- `cave`
- `cemetery`
- `chair_lift_station`
- `christian`
- `church_tower`
- `college`
- `communications_tower`
- `dam`
- `driving_centre`
- `elevator`
- `entry_exit`
- `exit`
- `fairground`
- `ferry`
- `ferry_terminal`
- `funicular_stop`
- `golf_course`
- `gondola_station`
- `horse_racing`
- `hospital`
- `incineration_plant`
- `junction`
- `lock`
- `military`
- `monument`
- `observation_tower`
- `observatory`
- `park`
- `power_plant`
- `prison`
- `railway_station`
- `rest_area`
- `restaurant`
- `rest_stop`
- `ruins`
- `school`
- `shop`
- `sports_centre`
- `spring`
- `stadium`
- `stone_`
- `subway_stop`
- `survey_point`
- `surveying_pyramid`
- `swimming_pool`
- `tower`
- `toilets`
- `tram_stop`
- `university`
- `viewpoint`
- `wastewater_plant`
- `waterfall`
- `water_tank`
- `weir`
- `wilderness_hut`
- `wind_turbine`
- `zoo`


#### direction

can be used to orientate direction for waterfalls

### spot_elevation

spot elevation.

### Fields

#### class

class can be used to allow different styling of elevation points.

Possible values:

- `spot_elevation`
- `terrain_spot_elevation`
- `lake_elevation`
- `sinkhole`
- `sinkhole_rock`
- `sinkhole_scree`
- `sinkhole_ice`
- `sinkhole_water`
- `doline`


#### ele

elevation in meters, measured in reference system LV95, srid 2056.

#### ele_ft

elevation in feet, measured in reference system LV95, srid 2056.

#### lake_depth

the maximum depth of the lake in meters.

#### lake_depth_ft

the maximum depth of the lake in feet.

### transportation

**transportation** contains roads, railways, aerialways, and ferry lines.
It contains all roads from motorways to primary, secondary and
tertiary roads to residential roads and
foot paths. Styling the roads is the most essential part of the map.

### Fields

#### class

Distinguish between more and less important roads, railways, shipways and aerialways.

Possible values:

- `motorway`
- `trunk`
- `primary`
- `secondary`
- `tertiary`
- `minor`
- `path`
- `footway`
- `service`
- `track`
- `trail`
- `transit`
- `rail`
- `via_ferrata`
- `ferry`
- `car_ferry`
- `cable_car`
- `gondola`
- `chair_lift`


#### subclass

Distinguish more specific qualities.

Possible values:

- `avalanche_protector`
- `avalanche_protector_bridge`
- `covered_bridge`
- `steps`
- `tram`
- `subway`
- `funicular`
- `rail`
- `rack_rail`
- `narrow_gauge`


#### brunnel

Mark whether it is a bridge or tunnel or ford.

Possible values:

- `bridge`
- `tunnel`
- `ford`


#### ramp

Mark with `1` whether way is a ramp (link or steps)
or not with `0`.

Possible values:

- `0`
- `1`


#### oneway

Trafficways that are not oneway are marked with `0`, oneway trafficways are marked with `1` and duplicate road tunnel oneways may be marked with `2` for filtering at lower zoomlevels.

Possible values:

- `0`
- `1`
- `2`


#### layer

Used to describe vertical relationships between crossing or overlapping features.

Possible values:

- `-5`
- `-4`
- `-3`
- `-2`
- `-1`
- `1`
- `2`
- `3`
- `4`
- `5`


#### surface

Used to describe the surface type of roads.

Possible values:

- `paved`
- `unpaved`


#### sac_scale

Different kinds of hiking trails.

Possible values:

- `mountain_hiking`
- `hiking`
- `alpine_hiking`


#### service

Mark railways that are dead-ends.

Possible values:

- `siding`


#### is_route

Mark roads that are important routes (values 5-10) or main railways (value 99).

Possible values:

- `5`
- `6`
- `7`
- `8`
- `10`
- `99`

### transportation_name

Labeling geometry for transportation layer.

### Fields

#### class

Distinguish between more and less important roads or railways and roads.

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
- `trail`
- `transit`
- `rail`
- `via_ferrata`
- `ferry`
- `car_ferry`
- `cable_car`
- `gondola`
- `chair_lift`


#### subclass

Distinguish more specific qualities.

Possible values:

- `avalanche_protector_bridge`
- `covered_bridge`
- `steps`
- `tram`
- `subway`
- `funicular`
- `rail`
- `rack_rail`
- `narrow_gauge`


#### brunnel

Mark whether it is a bridge or tunnel or ford.

Possible values:

- `bridge`
- `tunnel`
- `ford`


#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### ref

Route number.

#### ref_length

Length of ref field.

#### layer

Used to describe vertical relationships between crossing or overlapping features.

Possible values:

- `-5`
- `-4`
- `-3`
- `-2`
- `-1`
- `1`
- `2`
- `3`
- `4`
- `5`


#### is_route

Mark roads that are important routes (values 5-10) or main railways (value 99).

Possible values:

- `5`
- `6`
- `7`
- `8`
- `10`
- `99`

### water

Water polygons representing rivers and lakes but also artificial constructions such as pools

### Fields

#### class

Water bodies are classified as `lake`, `river` or `pool`.

Possible values:

- `lake`
- `river`
- `pool`

### waterway

Lines of waterways or outlines of waterbodies. Underground waterways are not included.

### Fields

#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### class

stream/river are classified by [Strahler-order](https://en.wikipedia.org/wiki/Strahler_number). Upstream rivers are classified as streams, 
once they reach a certain Strahler number or if they intersect with a waterbody (polygon), they are classified as rivers.

Possible values:

- `stream`
- `river`
- `pressurised`
- `drain`


#### intermittent

Mark with `1` if it is an [intermittent](https://wiki.openstreetmap.org/wiki/Key:intermittent) waterway.

Possible values:

- `0`
- `1`


#### width

used to symbolize downstream rivers wider than upstream.

### water_name

The water_name layer contains points to label waterbodies.

### Fields

#### class

used to distinguish entire or parts of waterbodies.

Possible values:

- `lake`


#### name

common name

#### name:latin

common name, latin alphabet

#### name:de

german name, if unavailable uses default name

#### name:fr

french name, if unavailable uses default name

#### name:it

italien name, if unavailable uses default name

#### name:rm

romansh name, if unavailable uses default name

#### direction

direction of the lake to rotate label.

#### size

values 1 to 10, can be used for label size.

