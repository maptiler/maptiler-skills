# MapTiler Planet v4

Source: https://docs.maptiler.com/schema/planet-v4/

"Next generation global vector tileset for professional map designers."

MapTiler Planet v4 is the next generation of the global vector tileset, designed for both professional cartographers and map designers. It delivers an optimized schema hierarchy, higher detail across all zoom levels, and enhanced data consistency worldwide. It features points of interest, administrative areas, built-up regions with buildings, transportation networks, and water and natural features. The dataset is updated bi-weekly with rigorous quality control to ensure reliability and precision.

## Layers

### aerialway

Layer containing aerialway features.

### Block

`transit`

### Fields

#### access

Indicates whether the aerialway is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class

Classification category.

Values:
- `cable_car`
- `chair_lift`
- `drag_lift`
- `gondola`
- `goods`
- `j-bar`
- `magic_carpet`
- `mixed_lift`
- `platter`
- `rope_tow`
- `t-bar`
- `zip_line`

#### ref

Reference code of the aerialway.

Examples:
- `17`
- `B1`
- `K`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### aerialway_label

Layer containing line labels for named aerialway features.


### Block

`transit`

### Fields

#### access

Indicates whether the aerialway is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class

Classification category.

Values:
- `cable_car`
- `chair_lift`
- `drag_lift`
- `gondola`
- `goods`
- `j-bar`
- `magic_carpet`
- `mixed_lift`
- `platter`
- `rope_tow`
- `t-bar`
- `zip_line`

#### name

Primary (local or official) name of the aerialway.

Examples:
- `Base to Base`
- `Heavenly Gondola`
- `Panoramic Mont Blanc`

#### name:{code}

Localized name of the aerialway in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).


#### ref

Reference code of the aerialway.

Examples:
- `17`
- `B1`
- `K`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### archipelago_label

Layer containing line labels for named archipelagos.


### Block

`administrative`

### Fields

#### name

Primary (local or official) name of the archipelago.

Examples:
- `Canarias`
- `Hawaiian Islands`
- `Mariana Islands`

#### name:{code}

Localized name of the archipelago in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the archipelago. Lower values indicate greater importance.

Min value:
- `1`

Max value:
- `7`

#### worldview

Defines the geopolitical perspective from which a feature is represented.

| worldview | description                            |
|-----------|----------------------------------------|
| `ch`      | geopolitical world view of Switzerland |
| `us`      | geopolitical world view of USA         |


Values:
- `recognized`
- `unrecognized`

Examples:
- `worldview:ch=recognized` => `name=Falklands Islands`
- `worldview:ch=unrecognized` => `name=Malvinas`

### Min zoom:

`3`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### aviation

Layer containing polygons of aviation features.


### Block

`transit`

### Fields

#### access

Indicates whether the aviation facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for aviation facility with their subclass values.

Values:


**aerodrome**


- `airfield`
- `airstrip`
- `club`
- `gliding`
- `international`
- `military`
- `private`
- `public`
- `regional`



**apron**


- `international`
- `military`
- `private`
- `public`
- `regional`



**helipad**


- `military`
- `private`



**heliport**


- `military`
- `private`
- `public`
- `regional`



**landingpad**





**launch_complex**


- `military`



**launchpad**


- `military`



**runway**


- `airfield`
- `military`



**spaceport**


- `military`



**taxiway**




#### construction {#aviation-construction}

Indicates whether the aviation facility is under construction.

Values:
- `True`

#### faa

The Federal Aviation Administration location identifier.

Examples:
- `MHV`
- `TE43`
- `WS35`

#### iata

3-character code issued by the International Air Transport Association.

Examples:
- `LHD`
- `ORD`
- `ZWU`

#### icao

4-letter code issued by the International Civil Aviation Organization.

Examples:
- `HSSP`
- `YGHP`
- `YUOF`

#### ref

Reference code of the aviation facility.

Examples:
- `H1`
- `LSPV`
- `PJZ 12.0`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### aviation_line

Layer containing lines of aviation features.


### Block

`transit`

### Fields

#### access

Indicates whether the aviation facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for aviation facility with their subclass values.

Values:


**model_runway**


- `private`



**runway**


- `airfield`
- `military`
- `private`
- `public`
- `regional`



**taxiway**


- `military`


#### construction {#aviation_line-construction}

Indicates whether the aviation facility is under construction.

Values:
- `True`

#### faa

The Federal Aviation Administration location identifier.

Examples:
- `MHV`
- `TE43`
- `WS35`

#### iata

3-character code issued by the International Air Transport Association.

Examples:
- `LHD`
- `ORD`
- `ZWU`

#### icao

4-letter code issued by the International Civil Aviation Organization.

Examples:
- `HSSP`
- `YGHP`
- `YUOF`

#### ref

Reference code of the aviation facility.

Examples:
- `H1`
- `LSPV`
- `PJZ 12.0`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### bridge

Layer containing polygons of bridges.


### Block

`transit`

### Fields

#### class

Classification category.

Values:
- `wildlife_crossing`

#### construction {#bridge-construction}

Indicates whether the bridge is under construction.

Values:
- `True`

#### layer

Defines the relative order of bridges in relation to other features (e.g., roads)

Min value:
- `-2`

Max value:
- `10`

### Min zoom:

`8`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### bridge_label

Layer containing label points of bridges.


### Block

`transit`

### Fields

#### class

Classification category.

Values:
- `wildlife_crossing`

#### construction {#bridge-construction}

Indicates whether the bridge is under construction.

Values:
- `True`

#### layer

Defines the relative order of bridges in relation to other features (e.g., roads)

Min value:
- `-2`

Max value:
- `10`

#### name

Primary (local or official) name of the bridge.

Examples:
- `Øresundsbron`
- `Robert F. Kennedy Bridge`
- `Quaibrücke`

#### name:{code}

Localized name of the bridge in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### building

Layer containing polygons of building or building part footprints.


### Block

`builtup`

### Fields

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

#### underground

Indicates whether the building is underground.

Values:
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### building_number

Layer containing points representing building address labels.

### Block

`builtup`

### Fields

#### number

Address number.

Examples:
- `99`
- `4232b`
- `461/28`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### cemetery

Layer containing polygons of cemeteries and graveyards.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### city_label

Layer containing point labels for cities.


### Block

`administrative`

### Fields

#### capital

Numerical representation of an administrative unit from country to neighbourhood.

Values:
- `20`
- `30`
- `40`
- `50`
- `60`
- `61`
- `70`
- `80`
- `90`
- `100`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the city.

Examples:
- `Berlin`
- `Washington`
- `Zürich`

#### name:{code}

Localized name of the city in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the city. Lower values indicate greater importance.

Min value:
- `1`

Max value:
- `7`

### Min zoom:

`3`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### commercial

Layer containing polygons of commercial areas, used for services and trade (tertiary sector).


### Block

`builtup`

### Fields

#### class

Classification category.

Values:
- `commercial`
- `marketplace`
- `retail`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### construction

Layer containing polygons of areas under construction.


### Block

`builtup`

### Fields

#### class

Classification categories for the construction areas.

Values:
- `civic`
- `commercial`
- `education`
- `industrial`
- `leisure`
- `medical`
- `military`
- `other`
- `religious`
- `residential`
- `transportation`

### Min zoom:

`8`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### continent_label

Layer containing label points of each continent.


### Block

`administrative`

### Fields

#### name

Primary (local or official) name of the continent.

Examples:
- `ANTARCTICA`
- `ASIA`
- `EUROPE`

#### name:{code}

Localized name of the continent in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`0`

### Max zoom:

`3`

### Unique id

`True`

### country_border

Layer containing lines of country borders.


### Block

`administrative`

### Fields

#### admin_l

ISO 3166-1 Alpha-2 code of the country to the left of the border.

Examples:
- `CH`
- `CZ`
- `US`

#### admin_r

ISO 3166-1 Alpha-2 code of the country to the right of the border.

Examples:
- `AT`
- `CA`
- `DE`

#### maritime

Indicates whether the border is maritime.

Values:
- `False`
- `True`

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### country_border_disputed

Layer containing lines of disputed country borders.


### Block

`administrative`

### Fields

#### claimed_by

ISO 3166-1 Alpha-2 code of the country that claims the border.

#### disputed_by

ISO 3166-1 Alpha-2 code of the country that disputes the border.

#### disputed_name

Primary (local) name of the disputed border or area.

#### maritime

Indicates whether the border is maritime.

Values:
- `False`
- `True`

#### worldview

Defines the geopolitical perspective from which a feature is represented.

| worldview | description                            |
|-----------|----------------------------------------|
| `ch`      | geopolitical world view of Switzerland |
| `us`      | geopolitical world view of USA         |


Values:
- `disputed`
- `recognized`
- `unrecognized`

Examples:

| attribute       | value          |
|-----------------|----------------|
| `disputed_name` | `WesternSahara`|
| `claimed_by`    | `EH`           |
| `disputed_by`   | `MA`           |
| `worldview:ch`  | `disputed`     |
| `worldview:us`  | `unrecognized` |

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### country_disputed_label

Layer containing point labels of disputed country.


### Block

`administrative`

### Fields

#### name

Primary (local) name of the disputed country.

#### name:{code}

Primary (local) name of the disputed country in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### worldview

Defines the geopolitical perspective from which a feature is represented.

| worldview | description                            |
|-----------|----------------------------------------|
| `ch`      | geopolitical world view of Switzerland |
| `us`      | geopolitical world view of USA         |


Values:
- `disputed`
- `recognized`
- `unrecognized`

Examples:

| attribute      | value             |
|----------------|-------------------|
| `name`         | `الصحراء الغربية` |
| `name:en`      | `Western Sahara`  |
| `worldview:ch` | `recognized`      |
| `worldview:us` | `unrecognized`    |

### Min zoom:

`3`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### country_label

Layer containing point labels of each country.


### Block

`administrative`

### Fields

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the country.

Examples:
- `Deutschland`
- `Switzerland`
- `United States of America`

#### name:{code}

Localized name of the country in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the country. Lower values indicate greater importance.

Min value:
- `0`

Max value:
- `5`

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### dam

Layer containing polygons of dam structures built across a river or stream to impound the water.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### education

Layer containing polygons of educational facilities.


### Block

`builtup`

### Fields

#### class

Classification category.

Values:
- `college`
- `kindergarten`
- `library`
- `school`
- `university`

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### farmland

Layer containing polygons of agricultural and farmland areas.


### Block

`nature`

### Fields
Features of this layer have no attributes.

### Min zoom:

`8`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### ferry

Layer containing lines of ferry routes.


### Block

`transit`

### Fields

#### access

Indicates whether the ferry is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### ref

Reference code of the ferry route.

Examples:
- `38M`
- `Nav2`
- `US 10`

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### ferry_label

Layer containing line labels for named ferry routes.


### Block

`transit`

### Fields

#### access

Indicates whether the ferry is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### name

Primary (local or official) name of the ferry route.

Examples:
- `Alaska Marine Lines`
- `Huelva - Tenerife (Santa Cruz de Tenerife)`
- `Wellington - Picton (Bluebridge)`

#### name:{code}

Localized name of the ferry route in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### ref

Reference code of the ferry route.

Examples:
- `38M`
- `Nav2`
- `US 10`

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### forest

Layer containing polygons of generalized forested areas.
Unlike the `wood` layer, it provides simplified geometry suitable for large-scale maps.

### Block

`nature`

### Fields

Features of this layer have no attributes.

### Min zoom:

`0`

### Max zoom:

`9`

### Unique id

`False`

### grass

Layer containing polygons of grass and meadow areas.


### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `allotments`
- `fell`
- `garden`
- `golf_course`
- `grass`
- `grassland`
- `heath`
- `meadow`
- `park`
- `recreation_ground`
- `shrubbery`
- `tundra`
- `village_green`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### hospital

Layer containing polygons of hospital areas.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### ice

Layer containing polygons of glaciers, ice sheets and permanent snow.

### Block

`nature`

### Fields

Features of this layer have no attributes.

### Min zoom:

`0`

### Max zoom:

`15`

### Unique id

`False`

### industrial

Layer containing polygons of industrial and utility areas.


### Block

`builtup`

### Fields

#### class

Classification category.

Values:
- `brownfield`
- `industrial`
- `landfill`
- `plant`
- `quarry`
- `wastewater_plant`

### Min zoom:

`8`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### island_label

Layer containing point labels for named islands, islets or atolls.


### Block

`administrative`

### Fields

#### class

Classification category.

Values:
- `atoll`
- `island`
- `islet`

#### name

Primary (local or official) name of the island, islet or atoll.

Examples:
- `Grand Bahama`
- `Madeira`
- `Tasmania`

#### name:{code}

Localized name of the island, islet or atoll in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the island. Lower values indicate greater importance.

Min value:
- `5`

Max value:
- `14`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### leisure

Layer containing polygons of leisure, recreation and sport-related areas.


### Block

`builtup`

### Fields

#### class

Classification category.

Values:
- `dog_park`
- `pitch`
- `playground`
- `recreation_ground`
- `sports_centre`
- `stadium`
- `theme_park`
- `track`
- `winter_sports`
- `zoo`

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### military

Layer containing polygons of military or defense-related areas.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`8`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### parking

Layer containing polygons of parking areas and parking spaces.


### Block

`roads`

### Fields

#### access

Indicates whether the parking is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification category for parking with its subclass values.

Values:


**parking**


- `parking`
- `parking_space`


#### parking

Classification categories for the parking areas types.

Values:
- `carports`
- `garage`
- `garage_boxes`
- `half_on_kerb`
- `lane`
- `layby`
- `multi-storey`
- `on_kerb`
- `other`
- `parking`
- `rooftop`
- `sheds`
- `street_side`
- `surface`
- `underground`

#### parking_space

Classification categories for the parking spaces.

Values:
- `ambulance`
- `bicycle`
- `boat_trailer`
- `bus`
- `car_sharing`
- `caravan`
- `carpool`
- `charging`
- `coach`
- `compact`
- `delivery`
- `disabled`
- `doctor`
- `eletric_vehicle`
- `emergency`
- `family`
- `hgv`
- `minute`
- `motorcycle`
- `motorhome`
- `normal`
- `other`
- `parent`
- `pickup`
- `police`
- `reserved`
- `service`
- `taxi`
- `trailer`
- `truck`
- `visitor`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### pathway

Layer containing pathways.


### Block

`roads`

### Fields

#### access

Indicates whether the pathway is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the pathway is part of a bridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bridleway`
- `corridor`
- `cycleway`
- `footway`
- `path`
- `pedestrian`
- `platform`
- `steps`
- `track`

#### construction {#pathway-construction}

Indicates whether the pathway is under construction.

Values:
- `True`

#### indoor

Indicates whether the pathway is located inside a building.

Values:
- `True`

#### layer

Defines the relative order of pathway in relation to other features (e.g., roads)

Min value:
- `-10`

Max value:
- `10`

#### level

Defines the absolute vertical level (floor level) of the pathway.

Min value:
- `-19`

Max value:
- `56`

#### oneway

Indicates whether the pathway is a one-way.

Values:
- `True`

#### paved

Indicates whether the pathway is paved.

Values:
- `False`
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### pathway_label

Layer containing line labels for named pathways.


### Block

`roads`

### Fields

#### access

Indicates whether the pathway is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the pathway is part of a bridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bridleway`
- `corridor`
- `cycleway`
- `footway`
- `path`
- `pedestrian`
- `platform`
- `steps`
- `track`

#### construction {#pathway_label-construction}

Indicates whether the pathway is under construction.

Values:
- `True`

#### name

Primary (local or official) name of the pathway.

Examples:
- `Bremer Weg`
- `Lincoln Steps`
- `Lorzenweg`

#### name:{code}

Localized name of the pathway in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### unpaved

Indicates whether the pathway is unpaved.

Values:
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`true` (might change between zooms due to merging)

### pedestrian

Layer containing polygons of pedestrian areas.


### Block

`roads`

### Fields

#### access

Indicates whether the pedestrian area is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the pedestrian area is part of abridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bridleway`
- `corridor`
- `cycleway`
- `footway`
- `path`
- `pedestrian`
- `platform`
- `steps`
- `track`

#### construction {#pedestrian-construction}

Indicates whether the pedestrian area is under construction.

Values:
- `True`

#### indoor

Indicates whether the pedestrian area is located inside a building.

Values:
- `True`

#### layer

Defines the relative order of pedestrian areas in relation to other features (e.g., roads)

Min value:
- `1`

Max value:
- `9`

#### level

Defines the absolute vertical level (floor level) of the pathway.

Min value:
- `-6`

Max value:
- `5`

#### paved

Indicates whether the pedestrian area is paved.

Values:
- `False`
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### pedestrian_label

Layer containing point labels for named pedestrian areas.


### Block

`roads`

### Fields

#### access

Indicates whether the pedestrian area is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the pedestrian area is part of abridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bridleway`
- `corridor`
- `cycleway`
- `footway`
- `path`
- `pedestrian`
- `platform`
- `steps`
- `track`

#### construction {#pedestrian_label-construction}

Indicates whether the pedestrian area is under construction.

Values:
- `True`

#### name

Primary (local or official) name of the pedestrian area.

Examples:
- `Lincoln Plaza`
- `Pariser Platz`
- `Sechseläutenplatz`

#### name:{code}

Localized name of the pedestrian area in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### unpaved

Indicates whether the pedestrian area is unpaved.

Values:
- `True`

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`true` (might change between zooms due to merging)

### pier

Layer containing pier polygons.


### Block

`roads`

### Fields
Features of this layer have no attributes.

### Min zoom:

`9`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### place_label

Layer containing point labels of places (excluding `town` and `city`).


### Block

`administrative`

### Fields

#### class

Classification category.

Values:
- `hamlet`
- `isolated_dwelling`
- `neighbourhood`
- `quarter`
- `suburb`
- `village`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the place.

Examples:
- `Manhattan`
- `Neustadt`
- `銀座 (Ginza)`

#### name:{code}

Localized name of the place in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the place. Lower values indicate greater importance.

Min value:
- `1`

Max value:
- `40`

### Min zoom:

`9`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_accommodation

Layer containing points of interest related to accommodation.


### Block

`poi`

### Fields

#### access

Indicates whether the accommodation is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class

Classification category.

Values:
- `apartment`
- `bed_and_breakfast`
- `camp_site`
- `caravan_site`
- `chalet`
- `guest_house`
- `hostel`
- `hotel`
- `motel`

#### name

Primary (local or official) name of the accommodation.

Examples:
- `Alpenheim`
- `Campingpark`
- `Hotel Washington`

#### name:{code}

Localized name of the accommodation in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### stars

Quality classification of the accommodation.

Values:
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_culture

Layer containing points of interest related to culture.


### Block

`poi`

### Fields

#### access

Indicates whether the facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for cultural POIs with their subclass values.

Values:


**aqueduct**


- `aqueduct`



**archaeological_site**


- `agora`
- `amphitheatre`
- `aqueduct`
- `basilica`
- `baths`
- `bawn`
- `bigstone`
- `bridge`
- `broch`
- `building`
- `burial`
- `burial_ground`
- `burial_site`
- `cairn`
- `camp`
- `castle`
- `catacombs`
- `cave oppidum`
- `cemetery`
- `chapel`
- `church`
- `cistern`
- `city`
- `cliff_dwelling`
- `crannog`
- `dam`
- `desert_kite`
- `domus`
- `earthwork`
- `earthworks`
- `enclosure`
- `farm`
- `field_system`
- `fortification`
- `fulacht_fia`
- `gate`
- `geoglyph`
- `grave`
- `grave_field`
- `grave_yard`
- `harbour`
- `hilltop_enclosure`
- `house`
- `hut_circle`
- `industrial`
- `kiln`
- `kiva`
- `landwehr`
- `lime_kiln`
- `linear_earthwork`
- `lynchets`
- `megalith`
- `milestone`
- `military_trench`
- `mine`
- `mineral_extraction`
- `minilith`
- `moat`
- `monastery`
- `mound`
- `necropolis`
- `nuraghe`
- `other`
- `palace`
- `petroglyph`
- `pictographs`
- `place_of_worship`
- `pottery_kiln`
- `quarry`
- `regiones`
- `remains`
- `ridge_and_furrow`
- `road`
- `rock_art`
- `rock_painting`
- `rock_shelter`
- `roman_circus`
- `roman_fort`
- `roman_road`
- `roman_villa`
- `ruins`
- `sacrificial_site`
- `sanctuary`
- `settlement`
- `shell_midden`
- `souterrain`
- `standing_stone`
- `stone`
- `structure`
- `tell`
- `temple`
- `theatre`
- `threshing_floor`
- `tomb`
- `tower`
- `trap_pit`
- `tumulus`
- `unknown`
- `villa`
- `village`
- `wall`
- `watermill`
- `well`



**arts_centre**


- `arts_centre`



**artwork**


- `Butterfly_Sculpture`
- `aircraft`
- `anchor`
- `arch`
- `architecture`
- `azulejo`
- `bell`
- `bench`
- `board`
- `boat`
- `building`
- `bust`
- `carving`
- `city_entrance`
- `coat_of_arms`
- `column`
- `cross`
- `crossing`
- `drinking_water`
- `dwarf`
- `dwart`
- `falla`
- `figurine`
- `flacking`
- `fontaine Wallace`
- `fountain`
- `fresco`
- `garden`
- `graffiti`
- `inscription`
- `installation`
- `land_art`
- `literature`
- `memorial`
- `model`
- `monument`
- `mosaic`
- `mummy`
- `mural`
- `mural_painting`
- `obelisk`
- `ornamental_vase`
- `other`
- `painting`
- `photo`
- `photograph`
- `pinwheel`
- `placard`
- `plaque`
- `plate`
- `pochoir`
- `poem`
- `poster`
- `pottery`
- `print`
- `pylon`
- `relief`
- `religious`
- `rock`
- `scarecrow`
- `sculpture`
- `sculpture/fountain`
- `sculpture_group`
- `sgraffito`
- `sign`
- `sound_sculpture`
- `stained_glass`
- `star`
- `statue`
- `stele`
- `stone`
- `street_art`
- `szekely_gate`
- `tank`
- `tilework`
- `topiary`
- `totem_pole`
- `tower`
- `traffic_sign`
- `vase`
- `wood`
- `woodcarving`



**cemetery**


- `adventist`
- `african_methodist_episcopal`
- `african_methodist_episcopal_zion`
- `anabaptist`
- `ancestor`
- `anglican`
- `animist`
- `apostolic`
- `armenian_apostolic`
- `assemblies_of_god`
- `bahai`
- `baptist`
- `benzhu`
- `buddhist`
- `bulgarian_orthodox`
- `caodaism`
- `catholic`
- `chinese_folk`
- `christ_scientist`
- `christian`
- `church_of_christ`
- `church_of_scotland`
- `confucian`
- `congregational`
- `dutch_reformed`
- `episcopal`
- `ethiopian_orthodox`
- `evangelical`
- `evangelical_lutheran`
- `georgian_orthodox`
- `greek_catholic`
- `greek_orthodox`
- `hindu`
- `iglesia_ni_cristo`
- `jain`
- `jehovahs_witness`
- `jewish`
- `jodo_shinshu`
- `konkokyo`
- `landmark`
- `latter-day_saints`
- `latter_day_saints`
- `lutheran`
- `macedonian_orthodox`
- `mahayana`
- `matriz_africana`
- `mennonite`
- `methodist`
- `mormon`
- `multifaith`
- `muslim`
- `nazarene`
- `neo-pentecostal`
- `new_apostolic`
- `nichiren`
- `nondenominational`
- `old_believers`
- `orthodox`
- `pagan`
- `pentecostal`
- `place_of_worship`
- `presbyterian`
- `protestant`
- `quaker`
- `reformed`
- `roman_catholic`
- `romanian_orthodox`
- `russian_orthodox`
- `salvation_army`
- `scientologist`
- `serbian_orthodox`
- `seventh_day_adventist`
- `shamanic`
- `shia`
- `shingon_shu`
- `shinto`
- `sikh`
- `soto`
- `southern_baptist`
- `spiritist`
- `spiritualist`
- `sunni`
- `taoist`
- `tenrikyo`
- `thai_mahanikaya`
- `theravada`
- `tibetan`
- `ukrainian_greek_catholic`
- `ukrainian_orthodox`
- `unitarian_universalist`
- `united`
- `united_church_of_christ`
- `united_methodist`
- `united_reformed`
- `uniting`
- `unknown`
- `vietnamese_folk`
- `voodoo`
- `yazidi`
- `zoroastrian`
- `曹洞宗`



**cinema**


- `cinema`



**community_centre**


- `athlete`
- `bicycle_maintenance`
- `child`
- `chitalishte`
- `church_hall`
- `club`
- `club_home`
- `club_house`
- `community_hall`
- `cultural_centre`
- `disabled`
- `environment_centre`
- `events_centre`
- `events_place`
- `events_venue`
- `family`
- `family_centre`
- `home_club`
- `immigrant`
- `juvenile`
- `language_centre`
- `lgbtq`
- `maison de quartier`
- `man`
- `meeting_room`
- `men`
- `multigeneration`
- `neighbourhood`
- `open_for_all`
- `other`
- `parish_hall`
- `religious`
- `samba_school`
- `scout`
- `scout_centre`
- `senior`
- `senior_center`
- `senior_centre`
- `social_centre`
- `sport_centre`
- `student`
- `village_hall`
- `warm_hub`
- `woman`
- `women`
- `youth`
- `youth_centre`
- `youth_club`



**exhibition_centre**


- `exhibition_centre`



**gallery**


- `gallery`



**library**


- `library`



**monastery**


- `adventist`
- `african_methodist_episcopal`
- `african_methodist_episcopal_zion`
- `anabaptist`
- `ancestor`
- `anglican`
- `animist`
- `apostolic`
- `armenian_apostolic`
- `assemblies_of_god`
- `bahai`
- `baptist`
- `benzhu`
- `buddhist`
- `bulgarian_orthodox`
- `caodaism`
- `catholic`
- `chinese_folk`
- `christ_scientist`
- `christian`
- `church_of_christ`
- `church_of_scotland`
- `confucian`
- `congregational`
- `dutch_reformed`
- `episcopal`
- `ethiopian_orthodox`
- `evangelical`
- `evangelical_lutheran`
- `georgian_orthodox`
- `greek_catholic`
- `greek_orthodox`
- `hindu`
- `iglesia_ni_cristo`
- `jain`
- `jehovahs_witness`
- `jewish`
- `jodo_shinshu`
- `konkokyo`
- `landmark`
- `latter-day_saints`
- `latter_day_saints`
- `lutheran`
- `macedonian_orthodox`
- `mahayana`
- `matriz_africana`
- `mennonite`
- `methodist`
- `mormon`
- `multifaith`
- `muslim`
- `nazarene`
- `neo-pentecostal`
- `new_apostolic`
- `nichiren`
- `nondenominational`
- `old_believers`
- `orthodox`
- `pagan`
- `pentecostal`
- `place_of_worship`
- `presbyterian`
- `protestant`
- `quaker`
- `reformed`
- `roman_catholic`
- `romanian_orthodox`
- `russian_orthodox`
- `salvation_army`
- `scientologist`
- `serbian_orthodox`
- `seventh_day_adventist`
- `shamanic`
- `shia`
- `shingon_shu`
- `shinto`
- `sikh`
- `soto`
- `southern_baptist`
- `spiritist`
- `spiritualist`
- `sunni`
- `taoist`
- `tenrikyo`
- `thai_mahanikaya`
- `theravada`
- `tibetan`
- `ukrainian_greek_catholic`
- `ukrainian_orthodox`
- `unitarian_universalist`
- `united`
- `united_church_of_christ`
- `united_methodist`
- `united_reformed`
- `uniting`
- `unknown`
- `vietnamese_folk`
- `voodoo`
- `yazidi`
- `zoroastrian`
- `曹洞宗`



**monument**


- `monument`



**museum**


- `aerospace`
- `agriculture`
- `archaeological`
- `architecture`
- `art`
- `aviation`
- `car`
- `children`
- `craft`
- `ethnography`
- `food`
- `gallery`
- `geology`
- `history`
- `literature`
- `living_history`
- `local`
- `local_history`
- `maritime`
- `medicine`
- `military`
- `museum`
- `music`
- `nature`
- `open_air`
- `other`
- `person`
- `porcelain`
- `railway`
- `religious`
- `science`
- `speciality`
- `sport`
- `technology`
- `toys`
- `transport`
- `war`



**place_of_mourning**


- `place_of_mourning`



**place_of_worship**


- `adventist`
- `african_methodist_episcopal`
- `african_methodist_episcopal_zion`
- `anabaptist`
- `ancestor`
- `anglican`
- `animist`
- `apostolic`
- `armenian_apostolic`
- `assemblies_of_god`
- `bahai`
- `baptist`
- `benzhu`
- `buddhist`
- `bulgarian_orthodox`
- `caodaism`
- `catholic`
- `chinese_folk`
- `christ_scientist`
- `christian`
- `church_of_christ`
- `church_of_scotland`
- `confucian`
- `congregational`
- `dutch_reformed`
- `episcopal`
- `ethiopian_orthodox`
- `evangelical`
- `evangelical_lutheran`
- `georgian_orthodox`
- `greek_catholic`
- `greek_orthodox`
- `hindu`
- `iglesia_ni_cristo`
- `jain`
- `jehovahs_witness`
- `jewish`
- `jodo_shinshu`
- `konkokyo`
- `landmark`
- `latter-day_saints`
- `latter_day_saints`
- `lutheran`
- `macedonian_orthodox`
- `mahayana`
- `matriz_africana`
- `mennonite`
- `methodist`
- `mormon`
- `multifaith`
- `muslim`
- `nazarene`
- `neo-pentecostal`
- `new_apostolic`
- `nichiren`
- `nondenominational`
- `old_believers`
- `orthodox`
- `pagan`
- `pentecostal`
- `place_of_worship`
- `presbyterian`
- `protestant`
- `quaker`
- `reformed`
- `roman_catholic`
- `romanian_orthodox`
- `russian_orthodox`
- `salvation_army`
- `scientologist`
- `serbian_orthodox`
- `seventh_day_adventist`
- `shamanic`
- `shia`
- `shingon_shu`
- `shinto`
- `sikh`
- `soto`
- `southern_baptist`
- `spiritist`
- `spiritualist`
- `sunni`
- `taoist`
- `tenrikyo`
- `thai_mahanikaya`
- `theravada`
- `tibetan`
- `ukrainian_greek_catholic`
- `ukrainian_orthodox`
- `unitarian_universalist`
- `united`
- `united_church_of_christ`
- `united_methodist`
- `united_reformed`
- `uniting`
- `unknown`
- `vietnamese_folk`
- `voodoo`
- `yazidi`
- `zoroastrian`
- `曹洞宗`



**planetarium**


- `planetarium`



**public_bookcase**


- `building`
- `fridge`
- `glass_cabinet`
- `metal_cabinet`
- `movable_cabinet`
- `other`
- `phone_box`
- `reading_box`
- `sculpture`
- `shelf`
- `shelter`
- `wall_cabinet`
- `wooden_box`
- `wooden_cabinet`



**studio**


- `studio`



**theatre**


- `amphi`
- `ballet`
- `cabaret`
- `chamber_music`
- `circus`
- `comedy`
- `drama`
- `figure`
- `marionette`
- `music`
- `musical`
- `opera`
- `other`
- `philharmonic`
- `puppet`
- `stand_up_comedy`
- `variety`


#### name

Primary (local or official) name of the cultural POIs.

Examples:
- `Fördertechnik Museum`
- `Python Gallery`
- `The Metropolitan Museum of Art`

#### name:{code}

Localized name of the cultural POIs in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`13`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_education

Layer containing points of interest related to education.


### Block

`poi`

### Fields

#### access

Indicates whether the facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for educational POIs with their subclass values.

Values:


**childcare**


- `association`
- `barangay_government`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**college**


- `association`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**dancing_school**


- `association`
- `business`
- `community`
- `government`
- `private`
- `public`



**driving_school**


- `association`
- `business`
- `government`
- `military`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `school`



**kindergarten**


- `association`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**language_school**


- `association`
- `business`
- `community`
- `cooperative`
- `council`
- `government`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `religious`
- `school`
- `university`



**music_school**


- `association`
- `business`
- `community`
- `government`
- `ngo`
- `private`
- `private_individual`
- `private_non_profit`
- `public`
- `religious`
- `school`
- `university`



**prep_school**


- `business`
- `cooperative`
- `private`
- `private_for_profit`
- `public`
- `religious`



**research_institute**


- `association`
- `business`
- `charitable`
- `community`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**school**


- `association`
- `barangay_government`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**surf_school**


- `private`
- `private_for_profit`



**traffic_park**


- `government`
- `private`
- `private_non_profit`
- `public`



**university**


- `association`
- `business`
- `charitable`
- `community`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`


#### name

Primary (local or official) name of the facility.

Examples:
- `CERN - Site de Meyrin`
- `Harvard University`
- `Johann-Wolfgang-von-Goethe-Schule`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_food

Layer containing points of interest related to foods and beverages.


### Block

`poi`

### Fields

#### class

Classification category.

Values:
- `bar`
- `biergarten`
- `cafe`
- `canteen`
- `fast_food`
- `food_court`
- `ice_cream`
- `pub`
- `restaurant`

#### cuisine

Categories of types of foods and beverages.

Examples:
- `burger`
- `pizza`
- `regional`

#### name

Primary (local or official) name of the facility.

Examples:
- `Awesome Ice creem`
- `Best burger`
- `The best bar`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_healthcare

Layer containing points of interest related to health.


### Block

`poi`

### Fields

#### class & subclass

Classification categories for healthcare POIs with their subclass values.

Values:


**clinic**


- `association`
- `barangay_government`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**dentist**


- `business`
- `community`
- `cooperative`
- `government`
- `military`
- `private`
- `private_for_profit`
- `private_non_profit`
- `public`
- `university`



**doctors**


- `association`
- `business`
- `community`
- `cooperative`
- `government`
- `government_facility-public`
- `ngo`
- `private`
- `private_for_profit`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `university`



**hospital**


- `association`
- `business`
- `cbo`
- `charitable`
- `community`
- `cooperative`
- `council`
- `county_government`
- `government`
- `government_facility-public`
- `military`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`
- `school`
- `university`



**nursing_home**


- `business`
- `charitable`
- `government`
- `ngo`
- `private`
- `private_non_profit`
- `public`
- `religious`



**pharmacy**


- `barangay_government`
- `business`
- `charitable`
- `community`
- `government`
- `government_facility-public`
- `ngo`
- `private`
- `private_for_profit`
- `private_individual`
- `private_non_profit`
- `public`
- `public/government`
- `religious`



**veterinary**


- `business`
- `community`
- `government`
- `private`
- `private_for_profit`
- `public`
- `university`


#### healthcare

Healthcare category.

Examples:
- `clinic`
- `hospital`
- `pharmacy`

#### name

Primary (local or official) name of the facility.

Examples:
- `CVS Pharmacy`
- `Medic-Center Nürnberg`
- `Universitätsspital Zürich`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_public

Layer containing points of interest related to public facilities.


### Block

`poi`

### Fields

#### access

Indicates whether the facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for public POIs with their subclass values.

Values:


**adult**


- `adult_gaming_centre`
- `brothel`
- `casino`
- `gambling`
- `nightclub`
- `stripclub`



**animal**


- `animal_breeding`
- `animal_shelter`
- `dog_park`



**cemetery**


- `funeral_hall`



**emergency**


- `fire_station`
- `police`



**office**


- `accountant`
- `advertising_agency`
- `architect`
- `association`
- `bail_bond_agent`
- `charity`
- `company`
- `construction_company`
- `consulting`
- `cooperative`
- `courier`
- `coworking`
- `diplomatic`
- `educational_institution`
- `employment_agency`
- `energy_supplier`
- `engineer`
- `estate_agent`
- `financial`
- `financial_advisor`
- `forestry`
- `foundation`
- `geodesist`
- `government`
- `graphic_design`
- `guide`
- `harbour_master`
- `health_insurance`
- `insurance`
- `interior_design`
- `it`
- `lawyer`
- `logistics`
- `marketing`
- `moving_company`
- `newspaper`
- `ngo`
- `notary`
- `physician`
- `political_party`
- `private_investigator`
- `property_management`
- `publisher`
- `quango`
- `religion`
- `research`
- `security`
- `surveyor`
- `tax_advisor`
- `taxi`
- `telecommunication`
- `therapist`
- `translator`
- `travel_agent`
- `tutoring`
- `union`
- `university`
- `water_utility`
- `web_design`
- `wedding_planner`



**post**


- `parcel_locker`
- `post_box`
- `post_office`



**public**


- `bbq`
- `courthouse`
- `events_venue`
- `hackerspace`
- `marketplace`
- `park`
- `prison`
- `social_centre`
- `social_facility`
- `townhall`



**recreation**


- `amusement_arcade`
- `bathing_place`
- `dance`
- `dressing_room`
- `escape_game`
- `hot_tub`
- `recreation_ground`
- `sauna`
- `shelter`
- `smoking_area`
- `swimming_area`
- `swimming_pool`
- `tanning_salon`



**service**


- `atm`
- `bank`
- `bureau_de_change`
- `money_transfer`



**uncategorized**




#### name

Primary (local or official) name of the facility.

Examples:
- `Grillplatz`
- `Hauptpost`
- `Old City Hall`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_shopping

Layer containing points of interest related to shopping and craft facilities.


### Block

`poi`

### Fields

#### class & subclass

Classification categories for shopping POIs with their subclass values.

Values:


**arts**


- `art`
- `camera`
- `collector`
- `craft`
- `esoteric`
- `frame`
- `games`
- `model`
- `music`
- `musical_instrument`
- `new_age`
- `photo`
- `photo_studio`
- `photographer`
- `printing`
- `psychic`
- `trophy`
- `video`
- `video_games`



**beauty**


- `beauty`
- `chemist`
- `cosmetics`
- `dental_technician`
- `dentures`
- `erotic`
- `hairdresser`
- `hairdresser_supply`
- `hearing_aids`
- `herbalist`
- `jeweller`
- `massage`
- `medical`
- `medical_supply`
- `nutrition_supplements`
- `optician`
- `perfumery`
- `piercing`
- `tattoo`
- `wigs`



**books**


- `anime`
- `bookbinder`
- `books`



**clothes**


- `baby_goods`
- `bag`
- `boutique`
- `clothes`
- `dressmaker`
- `fabric`
- `fashion`
- `fashion_accessories`
- `jewelry`
- `leather`
- `sewing`
- `shoe_repair`
- `shoemaker`
- `shoes`
- `tailor`
- `watches`
- `wool`



**construction**


- `3d_printing`
- `backet_maker`
- `boatbuilder`
- `builder`
- `cabinet_maker`
- `clockmaker`
- `door_construction`
- `fence_maker`
- `metal_construction`
- `organ_builder`
- `sailmaker`
- `toolmaker`
- `watchmaker`
- `window_construction`



**craft**


- `agricultural_engines`
- `atelier`
- `beekeeper`
- `blacksmith`
- `carpenter`
- `carpet_layer`
- `cleaning`
- `embroiderer`
- `engraver`
- `floorer`
- `glassblower`
- `goldsmith`
- `handicraft`
- `hvac`
- `insulation`
- `joiner`
- `key_cutter`
- `luthier`
- `parquet_layer`
- `plasterer`
- `plumber`
- `restoration`
- `rigger`
- `roofer`
- `saddler`
- `scaffolder`
- `sculptor`
- `signmaker`
- `stanemanson`
- `stonemason`
- `sun_protection`
- `tatami`
- `tiler`
- `tinsmith`
- `turner`
- `upholsterer`
- `welder`



**discount**


- `charity`
- `second_hand`
- `variety_store`



**electronics**


- `computer`
- `electrician`
- `electronics`
- `electronics_repair`
- `hifi`
- `mobile_phone`
- `photographic_laboratory`
- `print_shop`
- `printer`
- `printer_ink`
- `printmaker`
- `radiotechnics`
- `telecommunication`
- `vacuum_cleaner`



**foods**


- `alcohol`
- `bakery`
- `bbq`
- `beverages`
- `brewery`
- `brewing_supplies`
- `butcher`
- `cafe`
- `caterer`
- `cheese`
- `chocolate`
- `coffee`
- `coffee_roaster`
- `confectionery`
- `convenience`
- `country_store`
- `dairy`
- `deli`
- `distillery`
- `farm`
- `food`
- `frozen_food`
- `greengrocer`
- `health_food`
- `honey`
- `ice_cream`
- `nuts`
- `pasta`
- `pastry`
- `rice`
- `seafood`
- `snack`
- `spices`
- `tea`
- `water`
- `wine`
- `winery`



**household**


- `agrarian`
- `appliance`
- `bathroom_furnishing`
- `building_materials`
- `business_machines`
- `chimney_sweeper`
- `doityourself`
- `electrical`
- `energy`
- `estate_agent`
- `fireplace`
- `florist`
- `garden_centre`
- `garden_furniture`
- `garden_machinery`
- `gardener`
- `gas`
- `glaziery`
- `groundskeeping`
- `haberdashery`
- `hardware`
- `hobby`
- `household`
- `houseware`
- `interior_decorator`
- `interior_work`
- `locksmith`
- `paint`
- `painter`
- `pottery`
- `power_tools`
- `repair`
- `security`
- `shed`
- `tool_hire`
- `tools`
- `trade`
- `wellness`
- `windows`



**interior**


- `antiques`
- `bed`
- `candles`
- `carpet`
- `curtain`
- `doors`
- `flooring`
- `furniture`
- `household_linen`
- `interior_decoration`
- `kitchen`
- `kitchenware`
- `lighting`
- `tiles`
- `window_blind`



**malls**


- `catalogue`
- `department_store`
- `general`
- `grocery`
- `kiosk`
- `mall`
- `shopping_centre`
- `supermarket`
- `wholesale`



**mixture**


- `bookmaker`
- `cannabis`
- `copyshop`
- `dry_cleaning`
- `e-cigarette`
- `funeral_directors`
- `gift`
- `gold_buyer`
- `gun`
- `hookah`
- `insurance`
- `laundry`
- `lottery`
- `maps`
- `money_lender`
- `newsagent`
- `outpost`
- `party`
- `pawnbroker`
- `pest_control`
- `pet`
- `pet_grooming`
- `pyrotechnics`
- `religion`
- `spare_parts`
- `stationery`
- `storage_rental`
- `ticket`
- `tobacco`
- `toys`
- `travel_agency`
- `trolley_bay`
- `vacant`
- `vending_machine`
- `weapons`
- `yes`



**outdoors**


- `equestrian`
- `fishing`
- `golf`
- `grinding_mill`
- `hunting`
- `military_surplus`
- `oil_mill`
- `outdoor`
- `sawmill`
- `scuba_diving`
- `skate`
- `ski`
- `sports`
- `surf`
- `swimming_pool`
- `water_sports`



**uncategorized**





**vehicles**


- `atv`
- `bicycle`
- `boat`
- `boat_repair`
- `car`
- `car_painter`
- `car_parts`
- `car_repair`
- `caravan`
- `chandler`
- `fuel`
- `jetski`
- `junk_yard`
- `mobile_home`
- `mobility_scooter`
- `motorcycle`
- `motorcycle_parts`
- `motorcycle_repair`
- `motorhome`
- `motorsports`
- `plant_hire`
- `rental`
- `repair`
- `scooter`
- `ship_chandler`
- `snowmobile`
- `tractor`
- `trailer`
- `truck`
- `truck_repair`
- `tyres`


#### name

Primary (local or official) name of the facility.

Examples:
- `The Computer`
- `The Map Shop`
- `The Tile Studio`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_sport

Layer containing points of interest related to sports.


### Block

`poi`

### Fields

#### access

Indicates whether the sport facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class

Classification category.

Examples:
- `basketball`
- `soccer`
- `tennis`

#### name

Primary (local or official) name of the sport facility.

Examples:
- `The basketball hall`
- `The best pitch`
- `The biggest stadium`

#### name:{code}

Localized name of the sport facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_station

Layer containing points of interest related to public transport stations.


### Block

`poi`

### Fields

#### agg_stop

Indicates whether station is a main platform of public transport stops (buses, trams, and subways).

Values:
- `True`

#### class & subclass

Classification categories of POI transport stations with their subclass values.

Values:


**aerialway**


- `station`





**aerodrome**


- `aerodrome`
- `airfield`
- `airstrip`
- `club`
- `gliding`
- `international`
- `military`
- `private`
- `public`
- `regional`





**aeroway**


- `gate`
- `hangar`
- `helipad`
- `heliport`
- `military`
- `private`
- `public`
- `regional`
- `terminal`





**bus**


- `bus_station`
- `bus_stop`





**entrance**


- `subway_entrance`
- `train_station_entrance`





**landingpad**


- `landingpad`





**launch_complex**


- `launch_complex`
- `military`





**marina**


- `ferry_terminal`
- `marina`





**railway**


- `halt`
- `station`
- `subway`
- `tram_stop`
- `yard`





**spaceport**


- `military`
- `spaceport`




#### construction {#poi_station-construction}

Indicates whether the station is under construction.

Values:
- `True`

#### customary_units

Indicates whether elevation units of station is customary to use.

Values:
- `ft`
- `m`

#### ele

Elevation in meters.

Min value:
- `-378`

Max value:
- `8376`

#### ele_ft

Elevation in feet.

Min value:
- `-1240`

Max value:
- `27480`

#### faa

The Federal Aviation Administration location identifier.

#### iata

3-character code issued by the International Air Transport Association.

Examples:
- `LHD`
- `ORD`
- `ZWU`

#### icao

4-letter code issued by the International Civil Aviation Organization.

Examples:
- `HSSP`
- `YGHP`
- `YUOF`

#### name

Primary (local or official) name of the station.

Examples:
- `Flughafen Zürich`
- `John F. Kennedy International Airport`
- `Letiště Václava Havla Praha`

#### name:{code}

Localized name of the station in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### network

Network name or abbreviation.

Examples:
- `BVG`
- `WMATA Metrobus`
- `ZVV`

#### ref

Reference code of the station.

Examples:
- `CGS`
- `EDOJ`
- `PRG`

### Min zoom:

`5`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_tourism

Layer containing points of interest related to tourism.


### Block

`poi`

### Fields

#### access

Indicates whether the tourist facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for tourist POIs with their subclass values.

Values:


**adit**


- `dugout`
- `ruins`
- `unknown`



**alpine_hut**


- `building`
- `hut`
- `ruins`
- `unknown`



**aquarium**


- `unknown`



**attraction**


- `unknown`



**beach_resort**


- `unknown`



**castle**


- `archaeological_site`
- `building`
- `castle`
- `castrum`
- `chefferie`
- `church`
- `citadel`
- `defensive`
- `farm`
- `fort`
- `fortification`
- `fortified_church`
- `fortress`
- `hall_house`
- `hillfort`
- `hunting`
- `kremlin`
- `maison`
- `manor`
- `mansion`
- `medieval`
- `monastery`
- `motte`
- `observation`
- `palace`
- `ruins`
- `school`
- `shiro`
- `stately`
- `temple`
- `tower`
- `towerhouse`
- `unknown`
- `wall`
- `watchtower`



**cave_entrance**


- `castle`
- `fortification`
- `house`
- `monastery`
- `ruins`
- `unknown`



**church**


- `abbey`
- `building`
- `chapel`
- `church`
- `fortified_church`
- `ruins`
- `towerhouse`
- `unknown`



**city_gate**


- `building`
- `defensive`
- `fortress`
- `palace`
- `ruins`
- `tower`
- `unknown`



**communications_tower**


- `unknown`



**information**


- `building`
- `defensive`
- `palace`
- `ruins`
- `theatre`
- `unknown`



**lighthouse**


- `ruins`
- `tower`
- `unknown`



**manor**


- `building`
- `castle`
- `defensive`
- `fortress`
- `house`
- `maison`
- `manor`
- `mansion`
- `palace`
- `ruins`
- `stately`
- `tower`
- `unknown`
- `watermill`



**memorial**


- `bunker`
- `church`
- `defensive`
- `house`
- `inscriptions_on_precipices`
- `palace`
- `ruins`
- `unknown`
- `village`



**mine_shaft**


- `ruins`
- `unknown`



**mineshaft**


- `industrial`
- `ruins`
- `unknown`



**observatory**


- `ruins`
- `unknown`



**resort**


- `ruins`
- `unknown`



**ruins**


- `Città`
- `Stove`
- `abbey`
- `airport`
- `aqueduct`
- `artificial`
- `barn`
- `barrack`
- `barracks`
- `baths`
- `blackhouse`
- `bridge`
- `buddhist_temple`
- `building`
- `building_wall`
- `buildingq`
- `bunker`
- `cabin`
- `castle`
- `cave_room`
- `chapel`
- `charcoal_pit`
- `chimney`
- `church`
- `city_wall`
- `citywalls`
- `closter`
- `column`
- `dam`
- `dugout`
- `enclosure`
- `factory`
- `farm`
- `farm_auxiliary`
- `farmhouse`
- `former oil exploration`
- `fort`
- `fortification`
- `fortress`
- `foundation`
- `fountain`
- `furnace`
- `gate`
- `graveyard`
- `guy_wire_anchor`
- `hamlet`
- `house`
- `hunting`
- `hut`
- `industrial`
- `inscriptions_on_precipices`
- `lime_kiln`
- `manor`
- `megalith`
- `military`
- `mill`
- `mine`
- `monastery`
- `monastry`
- `mosque`
- `odeon`
- `pagoda`
- `pier`
- `place_of_worship`
- `prasat`
- `public_building`
- `railroad`
- `remmants`
- `remnants`
- `residential`
- `ruins`
- `school`
- `shed`
- `stele`
- `stoa`
- `temple`
- `theatre`
- `tomb`
- `tower`
- `town`
- `track`
- `village`
- `wall`
- `warehouse`
- `water_tank`
- `watermill`
- `well`
- `windmill`



**telescope**


- `ruins`
- `unknown`



**theme_park**


- `birds`
- `enclosure`
- `ruins`
- `unknown`
- `wildlife_park`



**tomb**


- `building`
- `church`
- `ruins`
- `temple`
- `unknown`



**tower**


- `archaeological_site`
- `building`
- `castle`
- `church`
- `defensive`
- `fort`
- `fortress`
- `military`
- `pagoda`
- `ruins`
- `tower`
- `unknown`
- `watchtower`



**viewpoint**


- `bridge`
- `building`
- `castle`
- `defensive`
- `fortification`
- `fortress`
- `military`
- `ruins`
- `stately`
- `tower`
- `unknown`
- `wall`
- `watermill`



**water_tower**


- `industrial`
- `ruins`
- `tower`
- `unknown`



**water_well**


- `ruins`
- `tower`
- `unknown`



**watermill**


- `building`
- `farm`
- `industrial`
- `manor`
- `ruins`
- `unknown`
- `watermill`
- `windmill`



**wilderness_hut**


- `hut`
- `ruins`
- `unknown`



**windmill**


- `building`
- `ruins`
- `tower`
- `unknown`
- `windmill`



**wine_cellar**


- `unknown`



**zoo**


- `aviary`
- `birds`
- `butterfly`
- `enclosure`
- `falconry`
- `farm_park`
- `insectarium`
- `petting_zoo`
- `reptile`
- `safari_park`
- `small_animal`
- `unknown`
- `wildlife_park`


#### direction

Clockwise rotation in degrees representing the angle of the label (class=viewpoint), suitable for use with the `text-rotate` style property.

Min value:
- `0`

Max value:
- `360`

#### name

Primary (local or official) name of the facility.

Examples:
- `Brunnihütte SAC`
- `Playlands`
- `The Aquarium`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`12`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### poi_transport

Layer containing points of interest related to transportation.


### Block

`poi`

### Fields

#### access

Indicates whether the transportation facility is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for transportational POIs with their subclass values.

Values:


**bicycle**


- `bicycle_rental`
- `bicycle_repair_station`



**fuel**


- `charging_station`
- `compressed_air`
- `fuel`



**parking**


- `bicycle_parking`
- `motorcycle_parking`
- `parking`
- `parking_entrance`
- `parking_space`



**vehicle**


- `car_pooling`
- `car_rental`
- `car_sharing`
- `car_wash`
- `motorcycle_rental`
- `taxi`
- `vacuum_cleaner`
- `vehicle_inspection`


#### name

Primary (local or official) name of the facility.

Examples:
- `Parking Garage`
- `Parkplatz`
- `Seeplatz`

#### name:{code}

Localized name of the facility in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### parking

Classification categories for the parking areas types.

Values:
- `carports`
- `garage`
- `garage_boxes`
- `half_on_kerb`
- `lane`
- `layby`
- `multi-storey`
- `on_kerb`
- `other`
- `parking`
- `rooftop`
- `sheds`
- `street_side`
- `surface`
- `underground`

#### parking_space

Classification categories for the parking spaces.

Values:
- `ambulance`
- `bicycle`
- `boat_trailer`
- `bus`
- `car_sharing`
- `caravan`
- `carpool`
- `charging`
- `coach`
- `compact`
- `delivery`
- `disabled`
- `doctor`
- `eletric_vehicle`
- `emergency`
- `family`
- `hgv`
- `minute`
- `motorcycle`
- `motorhome`
- `normal`
- `other`
- `parent`
- `pickup`
- `police`
- `reserved`
- `service`
- `taxi`
- `trailer`
- `visitor`

#### ref

Reference code of the transportation facility.

Examples:
- `38`
- `A`
- `P2`

### Min zoom:

`13`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### protected_area

Layer containing polygons of protected or restricted natural areas, classified by protection type.


### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `habitat_species_management_area`
- `national_park`
- `natura_2000`
- `natural_monument_or_feature`
- `nature_reserve`
- `protected_area`
- `protected_area_with_sustainable_use_of_natural_resources`
- `protected_landscape_seascape`
- `strict_nature_reserve`
- `water_protection_area`
- `wilderness_area`

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### protected_area_major_label

Layer containing centerlines of major protected areas used for labeling.

### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `habitat_species_management_area`
- `national_park`
- `natura_2000`
- `natural_monument_or_feature`
- `nature_reserve`
- `protected_area`
- `protected_area_with_sustainable_use_of_natural_resources`
- `protected_landscape_seascape`
- `strict_nature_reserve`
- `water_protection_area`
- `wilderness_area`

#### name

Primary (local or official) name of the protected area.

Examples:
- `Parc naturel régional du Massif des Bauges`
- `Parque Marino Motu Motiro Hiva`
- `Te Papa-Kura-o-Taranaki`

#### name:{code}

Localized name of the protected area in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### protected_area_minor_label

Layer containing label points of minor or local named protected areas.


### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `habitat_species_management_area`
- `national_park`
- `natura_2000`
- `natural_monument_or_feature`
- `nature_reserve`
- `protected_area`
- `protected_area_with_sustainable_use_of_natural_resources`
- `protected_landscape_seascape`
- `strict_nature_reserve`
- `water_protection_area`
- `wilderness_area`

#### name

Primary (local or official) name of the protected area.

Examples:
- `Glenmore National Nature Reserve`
- `Naturschutzgebiet Aletschwald`
- `Taman Negara Pahang`

#### name:{code}

Localized name of the protected area in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).


### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### railway

Layer containing railways.


### Block

`transit`

### Fields

#### brunnel

Describes whether the railway is part of a bridge or tunnel.

Values:
- `bridge`
- `tunnel`

#### class

Classification category.

Values:
- `abandoned`
- `disused`
- `funicular`
- `light_rail`
- `miniature`
- `monorail`
- `narrow_gauge`
- `preserved`
- `rail`
- `tram`
- `turntable`

#### construction {#railway-construction}

Indicates whether the railway is under construction.

Values:
- `True`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### ref

Reference code of the railway route.

Examples:
- `205000`
- `720`
- `PW`

#### service

Describes the service of the railway.

Values:
- `crossover`
- `other`
- `siding`
- `slipway`
- `spur`
- `yard`

#### usage

Describes the usage of the railway.

Values:
- `branch`
- `crane`
- `freight`
- `industrial`
- `leisure`
- `main`
- `military`
- `other`
- `science`
- `test`
- `tourism`

### Min zoom:

`6`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### railway_label

Layer containing line labels for named railways.


### Block

`transit`

### Fields

#### brunnel

Describes whether the railway is part of a bridge or tunnel.

Values:
- `bridge`
- `tunnel`

#### class

Classification category.

Values:
- `abandoned`
- `disused`
- `funicular`
- `light_rail`
- `miniature`
- `monorail`
- `narrow_gauge`
- `preserved`
- `rail`
- `tram`
- `turntable`

#### construction {#railway_label-construction}

Indicates whether the railway is under construction.

Values:
- `True`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the railway.

Examples:
- `Hauensteinstrecke`
- `Metropolitan Subdivision`
- `Werrabahn`

#### name:{code}

Localized name of the railway in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### ref

Reference code of the railway route.

Examples:
- `205000`
- `720`
- `PW`

#### service

Describes the service of the railway.

Values:
- `crossover`
- `other`
- `siding`
- `slipway`
- `spur`
- `yard`

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### residential

Layer containing polygons of residential areas.


### Block

`builtup`

### Fields
Features of this layer have no attributes.

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### road

Layer containting roads.


### Block

`roads`

### Fields

#### access

Indicates whether the road is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the road is part of a bridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bus_guideway`
- `busway`
- `minor`
- `motorway`
- `primary`
- `raceway`
- `secondary`
- `service`
- `tertiary`
- `trunk`

#### construction {#road-construction}

Indicates whether the road is under construction.

Values:
- `True`

#### expressway

Indicates whether the road is an expressway (lower-standard motorway).

Values:
- `True`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### layer

Defines the relative order of roads in relation to other features (e.g., different road)

Min value:
- `-10`

Max value:
- `10`

#### network

Describes localized road system categories.

Values:
- `ca-provincial`
- `ca-provincial-arterial`
- `ca-transcanada`
- `gb-motorway`
- `gb-primary`
- `gb-trunk`
- `ie-motorway`
- `ie-national`
- `ie-regional`
- `us-highway`
- `us-interstate`
- `us-state`

#### oneway

Indicates whether the road is a one-way.

Values:
- `True`

#### paved

Indicates whether the road is paved.

Values:
- `False`
- `True`

#### ramp

Indicates whether the road is a ramp or a link to/from the road.

Values:
- `True`

#### service

Describes the service of the road.

Values:
- `alley`
- `drive-through`
- `driveway`
- `emergency_access`
- `parking_aisle`
- `slipway`

#### toll

Indicates whether the toll is payable on the road.

Values:
- `True`

### Min zoom:

`4`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### road_exit

Layer containing point labels of road exits.


### Block

`roads`

### Fields

#### class

Classification category.

Values:
- `minor`
- `motorway`
- `primary`
- `secondary`
- `tertiary`
- `trunk`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### layer

Defines the relative order of road exits in relation to other features (e.g., road)

Min value:
- `-1`

Max value:
- `5`

#### name

Primary (local or official) name of the road exit.

Examples:
- `Express Exit 62`
- `Siemensdamm`
- `Zürich Altstetten`

#### name:{code}

Localized name of the road exit in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### ref

Reference code of the road exit.

Examples:
- `2`
- `29A`
- `W8`

#### ref_length

Number of characters of the reference code

Min value:
- `1`

Max value:
- `8`

### Min zoom:

`10`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### road_label

Layer containing line labels for named roads.


### Block

`roads`

### Fields

#### access

Indicates whether the road is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### brunnel

Describes whether the road is part of a bridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `bus_guideway`
- `busway`
- `minor`
- `motorway`
- `primary`
- `raceway`
- `secondary`
- `service`
- `tertiary`
- `trunk`

#### construction {#road_label-construction}

Indicates whether the road is under construction.

Values:
- `True`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the road.

Examples:
- `Constitution Avenue Northwest`
- `Unter den Linden`
- `Zugerstrasse`

#### name:{code}

Localized name of the road in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### network

Describes localized road system categories.

Values:
- `ca-provincial`
- `ca-provincial-arterial`
- `ca-transcanada`
- `gb-motorway`
- `gb-primary`
- `gb-trunk`
- `ie-motorway`
- `ie-national`
- `ie-regional`
- `road`
- `us-highway`
- `us-interstate`
- `us-state`

#### ref

Reference code of the road.

Examples:
- `381`
- `B 2`
- `D1`

#### ref_length

Number of characters of the reference code.

Min value:
- `0`

Max value:
- `8`

#### route_1_colour

Colour of the 1st concurrency road.

Examples:
- `#001EFF`
- `#00FF00`
- `#19408B`

#### route_1_name

Name of the 1st concurrency road.

Examples:
- `A1`
- `California National Historic Trail Auto Tour Route`
- `European Road E 50 (Germany)`

#### route_1_network

Describes localized 1st concurrency road system categories.

Examples:
- `BAB`
- `CH:motorway`
- `US:I`

#### route_1_ref

Reference code of the 1st concurrency road.

Examples:
- `70`
- `A 8`
- `A1`

#### route_2_colour

Colour of the 2nd concurrency road.

Examples:
- `#00FF00`
- `#26762D`
- `#FFC300`

#### route_2_name

Name of the 2nd concurrency road.

Examples:
- `E 20 England`
- `European route E43`
- `Mountain Parkway`

#### route_2_network

Describes localized 2nd concurrency road system categories.

Examples:
- `US:NHT`
- `US:US`
- `e-road`

#### route_2_ref

Reference code of the 2nd concurrency road.

Examples:
- `40`
- `E 60`
- `M25`

#### route_3_colour

Colour of the 3rd concurrency road.

Examples:
- `#00CC00`
- `#00FF00`
- `#FF7F00`

#### route_3_name

Name of the 3rd concurrency road.

Examples:
- `E 16 Scotland`
- `European route E41`
- `Historic US 66 (MO)`

#### route_3_network

Describes localized 3rd concurrency road system categories.

Examples:
- `US:CKC`
- `US:US:Historic`
- `e-road`

#### route_3_ref

Reference code of the 3rd concurrency road.

Examples:
- `66`
- `E 50`
- `E-20`

#### route_4_colour

Colour of the 4th concurrency road.

Examples:
- `#008000`

#### route_4_name

Name of the 4th concurrency road.

Examples:
- `A4`
- `E 18 Ireland`
- `NHS High Priority Corridor 6`

#### route_4_network

Describes localized 4th concurrency road system categories.

Examples:
- `JP:national`
- `US:KS:Turnpike`
- `e-road`

#### route_4_ref

Reference code of the 4th concurrency road.

Examples:
- `18`
- `468`
- `E 18`

#### route_5_name

Name of the 5th concurrency road.

Examples:
- `Columbia River Highway`
- `NHS High Priority Corridor 2 (Avenue of the Saints)`
- `NHS High Priority Corridor 26`

#### route_5_network

Describes localized 5th concurrency road system categories.

Examples:
- `US:NHS High Priority Corridors`
- `US:NHT`
- `US:OR:Named`

#### route_5_ref

Reference code of the 5th concurrency road.

Examples:
- `1`
- `E 80`
- `R26`

#### route_6_name

Name of the 6th concurrency road.

Examples:
- `Georgia State Route 3`
- `NH83`
- `Texas State Highway Loop 7`

#### route_6_network

Describes localized 6th concurrency road system categories.

Examples:
- `US:OH`
- `e-road`
- `fi:national`

#### route_6_ref

Reference code of the 6th concurrency road.

Examples:
- `8`
- `E 80`
- `R101`

### Min zoom:

`6`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### rock

Layer containing polygons of rocky areas, bare rocks and scree.


### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `bare_rock`
- `rock`
- `scree`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### sand

Layer containing polygons of sandy terrains such as beaches and dunes.


### Block

`nature`

### Fields

#### class

Classification category.

Values:
- `beach`
- `dune`
- `sand`

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### ice

Layer containing polygons of scrub or bushland areas.

### Block

`nature`

### Fields

Features of this layer have no attributes.

### Min zoom:

`0`

### Max zoom:

`9`

### Unique id

`False`

### street_furniture

Layer containing points of street furniture like gates, crossings, street lamps.


### Block

`poi`

### Fields

#### access

Indicates whether the street furniture is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categoryies for the street furniture POI with their subclass values.

Values:


**access_control**


- `barrier_board`
- `block`
- `border_control`
- `bus_trap`
- `cattle_grid`
- `cycle_barrier`
- `debris`
- `door`
- `entrance`
- `full-height_turnstil`
- `horse_jump`
- `horse_stile`
- `kent_carriage_gap`
- `motorcycle_barrier`
- `sally_port`
- `spikes`
- `stile`
- `sump_buster`
- `tank_trap`
- `toll_booth`
- `turnstile`
- `wedge`



**barrier**


- `barricade`
- `barrier`
- `fallen_tree`
- `log`
- `rock`
- `tree`



**emergency**


- `access_point`
- `assembly_point`
- `defibrillator`
- `disaster_help_point`
- `drinking_water`
- `emergency`
- `fire_alarm_box`
- `fire_extinguisher`
- `fire_hydrant`
- `fire_service_inlet`
- `first_aid_kit`
- `life_ring`
- `mountain_rescue`
- `phone`
- `siren`
- `suction_point`
- `water_tank`



**gate**


- `bump_gate`
- `gate`
- `hampshire_gate`
- `kissing_gate`
- `lift_gate`
- `lych_gate`
- `slide_gate`
- `sliding_beam`
- `sliding_gate`
- `swing_gate`



**protection**


- `bar`
- `bollard`
- `chain`
- `collision_protection`
- `coupure`
- `height_restrictor`
- `jersey_barrier`
- `kerb`
- `rope`
- `step`
- `tyres`



**street**


- `bench`
- `clock`
- `crossing`
- `device_charging_station`
- `drinking_water`
- `fountain`
- `mini_roundabout`
- `planter`
- `recycling`
- `shower`
- `street_lamp`
- `telephone`
- `toilets`
- `traffic_signals`
- `turning_circle`
- `turning_loop`
- `waste_basket`
- `waste_disposal`
- `waste_transfer_station`
- `water_point`
- `water_tap`



**traffic_calming**


- `bump`
- `chicane`
- `choker`
- `cushion`
- `dip`
- `double_dip`
- `hump`
- `island`
- `mini_bumps`
- `painted_island`
- `rumble_strip`
- `table`
- `traffic_calming`


#### direction

Clockwise rotation in degrees representing the angle of the label (`class=street, subclass=crossing`), suitable for use with the `text-rotate` style property.

Min value:
- `-90`

Max value:
- `90`

#### lowered

Indicates whether the `class=protection, subclass=kerb` is lowered.

Values:
- `True`

#### name

Primary (local or official) name of the street furniture.

Examples:
- `Lampenhirsch`
- `Tor 101`
- `Wright Gate`

#### name:{code}

Localized name of the street furniture in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### ref

Reference code of the street furniture.

Examples:
- `3800`
- `C0918/GH02`
- `I-8705`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### sub_border

Layer containing lines of country subdivision borders.


### Block

`administrative`

### Fields

#### admin_level

Numerical representation of an administrative unit for country subdivisions.

Values:
- `30`
- `40`
- `50`
- `60`
- `61`
- `70`
- `80`
- `90`
- `100`
- `110`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### maritime

Indicates whether the border is maritime.

Values:
- `False`
- `True`

### Min zoom:

`2`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### town_label

Layer containing point labels for towns.


### Block

`administrative`

### Fields

#### capital

Numerical representation of an administrative unit from country to neighbourhood.

Values:
- `20`
- `30`
- `40`
- `50`
- `60`
- `61`
- `70`
- `80`
- `90`
- `100`

#### iso_a2

Country code in ISO 3166-1 Alpha-2 format.

Examples:
- `CH`
- `DE`
- `US`

#### name

Primary (local or official) name of the town.

Examples:
- `Schwetzingen`
- `Springfield`
- `Unterägeri`

#### name:{code}

Localized name of the town in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the town. Lower values indicate greater importance.

Min value:
- `1`

Max value:
- `11`

### Min zoom:

`6`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### traffic_control

Layer containing lines of traffic control features like barriers, kerbs, bumps.


### Block

`roads`

### Fields

#### access

Indicates whether the traffic control is publicly accessible.

Values:
- `conditional`
- `no`
- `yes`

#### class & subclass

Classification categories for the traffic control features with their subclass values.

Values:


**access_control**


- `block`
- `tank_trap`



**barrier**


- `barrier`
- `berm`
- `city_wall`
- `debris`
- `ditch`
- `fence`
- `hedge`
- `line`
- `log`
- `retaining_wall`
- `wall`



**protection**


- `cable_barrier`
- `chain`
- `guard_rail`
- `handrail`
- `jersey_barrier`
- `kerb`
- `rope`
- `tyres`



**traffic_calming**


- `bump`
- `chicane`
- `choker`
- `cushion`
- `dip`
- `double_dip`
- `hump`
- `island`
- `mini_bumps`
- `painted_island`
- `rumble_strip`
- `table`
- `traffic_calming`
- `traffic_island`


#### lowered

Indicates whether the `class=protection, subclass=kerb` is lowered.

Values:
- `True`

#### ref

Reference code of the traffic control.

Examples:
- `5617`
- `C 1`
- `D 27`

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### tree

Layer containing points of individual trees.


### Block

`nature`

### Fields

#### name

Primary (local or official) name of the tree (if available).

Examples:
- `General Sherman Tree`
- `Sagole Baobab`
- `Tāne Mahuta`

#### name:{code}

Localized name of the tree (if available) in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

### Min zoom:

`15`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### vegetation

Layer containing polygons of general vegetation areas.

### Block

`nature`

### Fields

Features of this layer have no attributes.

### Min zoom:

`0`

### Max zoom:

`9`

### Unique id

`False`

### water

Layer containing polygons of water bodies including seas, lakes, reservoirs or rivers.


### Block

`water`

### Fields

#### class & subclass

Classification category.

Values:


**canal**


- `canal`



**ditch**


- `ditch`



**dock**


- `dock`



**drain**


- `drain`



**lake**


- `lake`



**ocean**





**pond**


- `basin`
- `pond`
- `salt_pond`
- `wastewater`



**reef**


- `reef`



**reservoir**


- `reservoir`
- `reservoir_covered`



**river**


- `river`



**stream**


- `stream`



**swimming_pool**


- `swimming_pool`


#### covered

Indicates whether the water body is covered. (Most often covered reservoirs.)

Values:
- `True`

#### intermittent

Indicates whether the water body is intermittent.

Values:
- `True`

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`true` (excluding `ocean` class)

### waterway

Layer containing lines of linear water features such as rivers, streams and canals.


### Block

`nature`

### Fields

#### brunnel

Describes whether the waterway segment is part of a bridge, tunnel, or ford.

Values:
- `bridge`
- `ford`
- `tunnel`

#### class

Classification category.

Values:
- `canal`
- `ditch`
- `drain`
- `river`
- `stream`

#### intermittent

Indicates whether the waterway is intermittent.

Values:
- `True`

### Min zoom:

`9`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True` (might change between zooms due to merging)

### water_centroid

Layer containing point labels for named water bodies.

### Block

`water`

### Fields

#### area

Area of the water body in square kilometers, measured in the Web Mercator (EPSG:3857) projection.

Min value:
- `0`

Max value:
- `4254074`

#### class

Classification category.

Values:
- `bay`
- `canal`
- `ditch`
- `drain`
- `lagoon`
- `lake`
- `ocean`
- `pond`
- `reef`
- `reservoir`
- `river`
- `sea`
- `strait`
- `stream`

#### ipq

Isoperimetric quotient in percent, ratio of polygon area to the area of a circle with the same perimeter. A perfect circle has an IPQ of 100%.

Min value:
- `0`

Max value:
- `100`

#### length

Length of the corresponding water label line from `water_label` in kilometers, measured in the Web Mercator (EPSG:3857) projection.

Min value:
- `0`

Max value:
- `12942`

#### name

Primary (local or official) name of the water body.

Examples:
- `Atlantic Ocean`
- `Lake Superior`
- `Lé Léman`

#### name:{code}

Localized name of the water body in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).


#### rank

Importance of the water label. Lower values indicate greater importance.

Values:
- `1`
- `2`
- `3`
- `4`
- `10`

#### rotation

Clockwise rotation in degrees representing the tangent angle at the midpoint of the label line from `water_label`,
suitable for use with the `text-rotate` style property.

Min value:
- `-70`

Max value:
- `70`

#### worldview

Defines the geopolitical perspective from which a feature is represented.

| worldview |              description               |
|-----------|----------------------------------------|
| `ch`      | geopolitical world view of Switzerland |
| `us`      | geopolitical world view of USA         |

Values:
- `recognized`
- `unrecognized`

Examples:
- `worldview:ch=recognized` -> `name=Gulf of Mexico`
- `worldview:us=recognized` -> `name=Gulf of America`

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### water_label

Layer containing line labels for named water bodies.


### Block

`nature`

### Fields

#### area

Area of the water body in square kilometers, measured in the Web Mercator (EPSG:3857) projection.

Min value:
- `0`

Max value:
- `4254074`

#### class

Classification category.

Values:
- `bay`
- `canal`
- `ditch`
- `drain`
- `lagoon`
- `lake`
- `ocean`
- `pond`
- `reef`
- `reservoir`
- `river`
- `sea`
- `strait`
- `stream`

#### ipq

Isoperimetric quotient in percent, ratio of polygon area to the area of a circle with the same perimeter. A perfect circle has an IPQ of 100%.

Min value:
- `0`

Max value:
- `100`

#### length

Length of the water label line in kilometers, measured in the Web Mercator (EPSG:3857) projection.

Min value:
- `0`

Max value:
- `12942`

#### name

Primary (local or official) name of the water body.

Examples:
- `Atlantic Ocean`
- `Lake Superior`
- `Lé Léman`

#### name:{code}

Localized name of the water body in a specific language (when a translation exists that is different from the primary `name`).

`{code}` represents [ISO 639 language code](#languages).

#### rank

Importance of the water label. Lower values indicate greater importance.

Values:
- `1`
- `2`
- `3`
- `4`
- `10`

#### rotation

Clockwise rotation in degrees representing the tangent angle at the midpoint of the label line, suitable for use with the `text-rotate` style property.

Min value:
- `-70`

Max value:
- `70`

#### worldview

Defines the geopolitical perspective from which a feature is represented.

| worldview | description                            |
|-----------|----------------------------------------|
| `ch`      | geopolitical world view of Switzerland |
| `us`      | geopolitical world view of USA         |


Values:
- `recognized`
- `unrecognized`

Examples:
- `worldview:ch=recognized` -> `name=Gulf of Mexico`
- `worldview:us=recognized` -> `name=Gulf of America`


### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`True`

### wetland

Layer containing polygons of wetlands, marshes and tidal flats.


### Block

`nature`

### Fields
Features of this layer have no attributes.

### Min zoom:

`7`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### wood

Layer containing polygons of woodland and tree-covered areas.
Unlike `forest` layer, it provides high-detail geometry suitable for large-scale maps.


### Block

`nature`

### Fields
Features of this layer have no attributes.

### Min zoom:

`0`

### Max zoom:

`15` (possible overzooming up to `22`)

### Unique id

`False`

### languages

List of possible languages available in MapTiler Planet v4.

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

