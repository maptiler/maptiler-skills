# NL Cartiqo

Source: https://docs.maptiler.com/schema/nl-cartiqo/

Tileset containing open source geo data of the Netherlands.

Cartiqo is a Vector Tile product based on open source geo data of the Netherlands.
It provides a full and detailed map of the Netherlands customizable to your own likes.

## Layers

### agricultural

All fields for agricultural purposes, including pastures, greenhouses, arboriculture and fallow.

Together with the layers `natural`, `infrastructure` and `builtup` it covers the total surface of the Netherlands from zoom level 13 and higher.

### Fields

#### originalID

#### type

The main type of the feature.

Possible values:

- `agriculture`
- `arboriculture`
- `pasture`
- `greenhouse`
- `fallow`

#### subtype

Possible values:

- `agriculture`
  - `orchard`
  - `fruit`
- `arboriculture`
  - `nursery`
- `pasture`
- `greenhouse`
- `fallow`

### boundaries

Administrative boundaries of countries, provinces and municipalities. Will be expanded with regions and neighborhoods in the next editions.

### Fields

#### originalID

#### name

#### type

The main type of the feature.

Possible values:

- `country`
- `province`
- `municipality`

#### subtype

Possible values:

- `country`
  - `foreign`
  - `domestic`
- `province`
- `municipality`

### waterline

Contains all the urban areas and buildings. 
On lower zoom levels a city is represented as an urban area and on higher zoom levels the areas will be split up into 
building blocks and later by buildings and even more detail, entrances, walls and covers.
Together with the layers `natural`, `agriculture` and `infrastructure` 
it covers the total surface of the Netherlands from zoom level 13 and higher.

### Fields

#### originalID

#### name

#### type

The main type of the feature.

Possible values:

- `area`
- `building`
- `wall`

#### subtype

Possible values:

- `area`
  - ` `
  - `courtyard`
  - `industrial`
  - `residential`
  - `graveyard`
- `building`
  - ` `
  - `industry`
  - `main`
  - `barn`
  - `entrance`
  - `waterbassin`
  - `cover`
  - `pitch`
  - `berth`
- `wall`

### infrastructure

This is NOT the road infrastructure. But physical areas, human-made which are not natural or vegetation covered.
Mostly asphalt or stone coverages, often found inside urban areas. Areas supporting the road infrastructure.
Together with the layers `agriculture`, `natural` and `builtup` it covers the total surface of the Netherlands from zoom level 13 and higher.

### Fields

#### originalID

#### name

#### type

The main type of the feature.

Possible values:

- `parking`
- `road`
- `railway`
- `jetty`
- `tunnel`
- `bridge`
- `runway`
- `pavement`

#### subtype

Possible values:

- `parking`
- `road`
  - `motorway`
  - `transit`
  - `bike`
  - `driveway`
  - `bridle_Way`
  - `crossing`
  - `secondary`
  - `highway`
  - `local`
  - `path`
- `railway`
  - `track_surface`
  - `platform`
- `jetty`
- `tunnel`
- `bridge`
- `runway`
- `pavement`

### labels

Names of areas, usually displayed only as a label (not an icon). Larger areas with natural names of undefined borders and administrative areas.
Also including address numbers at zoom level 16.

### Fields

#### originalID

#### name

#### type

Possible values:

- `place` - Place names of inhabited places like cities, large towns, small towns and hamlets in the Netherlands. Also including urban district names as used by inhabitants (different form administrative districts).
- `admin` - Administrative names from administrative areas according to the CBS. Placed as a point inside the area.
- `water` - Relevant water names of physical areas. (not harbors)
- `nature` - Relevant nature area names. Only large nature areas. (not gardens and dog parks)
- `adress` - Address numbers and letters, available at zoom level 16.
- `junction`
- `milestone`
- `street`


#### subtype

Possible values:

- `place`
  - `urban_district`
  - `settlement`
- `admin`
  - `country`
  - `province`
  - `municipality`
  - `district`
  - `neighborhood`
- `water`
- `nature`
- `address`
- `junction`
- `milestone`
- `street`

#### hierarchy

Place label hierarchy. Based on capitals, population size, category and geometry type. e.g. polygons have a higher hierarchy then points.
For a detailed overview see the document [Label_hierarchy.ods](https://github.com/webmapper/cartiqo-documentation/blob/master/Label_hierarchy.ods)

Possible values:

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

#### rotation

Rotation of address numbers in degrees. Only for type == address.
Possible values from -90 to 90.

### natural

Contains all nature polygons like nature areas, grass fields and forest areas. 
It describes the physical material of the land surface.
Together with the layers `agriculture`, `infrastructure` and `builtup` 
it covers the total surface of the Netherlands from zoom level 13 and higher.
### Fields

#### originalID

#### type

The main type of the feature.

Possible values:

- `high` - is all natural vegetation like trees and forest areas. Including tree lines.
- `low` - covers all natural vegetation defined as grass, heather and shrubs.
- `bare` - are features describing natural areas without vegetation like sand areas: dunes and sand and rock plains.

#### subtype

The subtype of the feature describes the type in even more detail and can be used to make more distinction in the map styling.

Possible values:

- `high`
  - `mixed` 
  - `deciduous`
  - `coniferous`
- `low`
  - `heath`
  - `grass`
  - `shrubs`
- `bare`
  - `sand`
  - `rock`
  - `dune`

### obstructions

### Fields

#### originalID

#### type

The main type of the feature.

- `fence`
- `hedge`
- `railing`
- `wall`

### pois

Points of interest which usually are visualized with an icon. Human-made functionality or human agreements that define a distinct place of reference.

### Fields

#### originalID

#### name

#### type

Possible values:

- `food_drink` - All food and drink occasions.
- `public_building` - A public building with general purposes.
- `public_space` - Public areas which are not buildings but fields or areas with a functionality. Like a harbour, industry, dog park or playground. Nature areas which describe physical areas are not in this layer but in Labels. POIs describe an area with a human decided function assigned.
- `public_transport` - Public transport stops.
- `commercial` - Commercial shops other then food and drink.

#### subtype

Possible values:

- `food_drink`
  - `drink`
  - `food`
- `public_building`
  - `culture`
  - `education`
  - `healthcare`
  - `public_building`
- `public_space`
  - `industry`
  - `green`
  - `parking`
  - `sport`
  - `water`
- `public_transport`
  - `airport`
  - `bus_stop`
  - `ferry_terminal`
  - `metro_entrance`
  - `train_station`
  - `tram_stop`
- `commercial`
  - `groceries`
  - `convenience`
  - `fuel`

#### subsubtype

The `subsubtype` of a POI feature is the original description from source data the POI is derived from. (mainly OSM)

#### hierarchy

The label hierarchy or size/importance per POI category.
Top10NL data is considered priority. Then Polygon sources and larger areas. Then POINTS
Most features must contain a name to be considered in the data. Except for the Parking places. Which are hierarchical ordered according to having a name or not.
Parks are also hierarchical ordered to name and area size.
See [POIs_decision.ods for](https://github.com/webmapper/cartiqo-documentation/blob/master/POIs_decision.ods) a complete overview of the decisions made.

Possible values:

- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `10`

### railways

### Fields

#### originalID

#### type

The main type of the feature.

Possible values:

- `rail`
- `tram`
- `metro`
- `industrial`
- `touristic`
- `light_rail`

#### tunnel

If line feature is tunnel or not.

Possible values:

- `true`
- `false`

### roads

### Fields

#### originalID

#### name

#### type

The main type of the feature.

Possible values:

- `highway`
- `motorway`
- `main`
- `secondary`
- `local`
- `bike`
- `path`
- `ferry`

#### tunnel

If line feature is tunnel or not.

Possible values:

- `true`
- `false`

#### oneway

Possible values:

- `-1`
- `0`
- `1`

#### road_number

Dutch road number classification if available. Like A roads and N road numbers. These roads often contain a name and a number, so this can be used for double labeling.

### water

Contains all water area polygons like oceans, sea, lakes and rivers. 
On lower zoom levels it contains all oceans from the Natural Earth data set. 
At higher zoom levels it contains all water bodies from The Netherlands. 
Including the Wadden.

### Fields

#### originalID

#### name

#### type

The main type of the feature.

Possible values:

- `sea`
- `tidal_flat`
- `lake`
- `water_way`

### waterline

Water streams in Dutch geo data sources are sometimes drawn as a Polygon and sometimes as a Line. 
Therefore a separate layer for water lines is provided. 
Note! a water body or stream is not defined by the geometry. 
Water streams can be drawn as a line or a polygon. 
Water bodies are often given as polygons but also larger rivers are given as polygons. 
No explicit reasons can be found for this difference. 
Mostly water drawn as lines are smaller water streams like ditches between fields.

### Fields

#### originalID

#### name

#### type

The type of water line is the width given by the source data.

Possible values:

- `3m`
- `6m`
- `12m`
- `50m`
- `125m`

