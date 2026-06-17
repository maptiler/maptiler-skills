# UK OS Open Zoomstack

Source: https://docs.maptiler.com/schema/uk-openzoomstack/

Tileset containing data from Ordnance Survey's OS Open Zoomstack.

Ordnance Survey's OS Open Zoomstack is an open vector basemap showing coverage of Great Britain from a national level, right down to street detail.

## Layers

### airports

A centre point for all major airports including a name.

### Fields

#### name
Name of airport.

### boundaries

National boundary lines between England - Scotland and England - Wales.

### Fields

#### type

Type of boundary line.

Possible values:

- `National`

### buildings

Generalised building footprints at both local and district resolutions. The local
buildings have a unique identifier which can be used to style features distinctly.
The identifier will not be persistent between product versions and therefore there
will be no change history information for a feature.

### Fields

#### uuid

### contours

These contours lines have a 10-metre interval with an index every 50 metres. Each contour contains a value.

### Fields

#### type

Type of contour line.

Possible values:

- `Index`
- `Normal`

#### value

Contour line elevation.

### etl

Electricity Transmission Lines.

### foreshore

These polygons depict the part of the shore or beach which lies between the Mean Low Water Mark and Mean High Water Mark.

### greenspaces

Polygon features representing the extent of places such as parks and sports facilities that are likely to be accessible to the public.

### Fields
Type of greenspace.
#### type

Possible values:

- `Allotments Or Community Growing Spaces`
- `Bowling Green`
- `Cemetery`
- `Golf Course`
- `Other Sports Facility`
- `Play Space`
- `Playing Field`
- `Public Park Or Garden`
- `Religious Grounds`
- `Tennis Court`

### names

Use this point layer to render contextual labels on your map.
The `name1language` and `name2language` attributes let you select which names to display. For example, if
you want to show all the Welsh language names then you can use these attributes to filter them out and
These are the attribute values in the language fields:
- `cym` - name is in the Welsh language.
- `eng` - name is in the English language.
- `gla` - name is in the Scottish Gaelic language.
- `NULL` - language type is not set if there is only one name, or if there are two names, and the language of one or both of the names is not recorded as English, Welsh or Gaelic.


### Fields

#### type

Possible values:
- `Country`
- `Capital`
- `National Park`
- `City`
- `Town`
- `Village`
- `Hamlet`
- `Small Settlements`
- `Suburban Area`
- `Woodland`
- `Landform`
- `Landcover`
- `Water`
- `Greenspace`
- `Sites`
- `Motorway Junctions`

#### name1

Contains the accepted or English name.

#### name1language
Let you select which names to display. For example, if you want to show all the Welsh language names then you can use these attributes to filter them out and render them on your map.

Possible values:
- NULL
- `eng`

#### name2
Contains the Welsh, Gaelic or English name

#### name2language
Let you select which names to display. For example, if you want to show all the Welsh language names then you can use these attributes to filter them out and render them on your map.


Possible values:
- NULL
- `cym`
- `gla`

### national_parks

These polygons depict the extent of the 15 National Parks in Great Britain.

### rail

Lines representing the railway network. They are broken where they pass under bridges, buildings or other obstructing detail.

### Fields

#### type

Type of rail.

Possible values:
- `Multi Track`
- `type`
- `Single Track`
- `Narrow Gauge`
- `Tunnel`

### railwaystations

This layer contains a point for all stations and includes a name.

### Fields

#### type

Type of railway station

Possible values:
- `Light Rapid Transit Station`
- `Light Rapid Transit Station And London`
- `Underground Station`
- `Light Rapid Transit Station And Railway Station`
- `London Underground Station`
- `Railway Station`
- `Railway Station And London Underground Station`

#### name

Name of railway station

### roads

Lines representing the road network. A road is defined as a metalled way for vehicles.

### Fields

#### type

Type of road.

Possible values:
- `Motorway`
- `Primary`
- `A Road`
- `B Road`
- `roads`
- `Guided Busway`
- `Minor`
- `Local`
- `Restricted`
- `Tunnels`

#### name

Name of road

#### number

Number of road

#### level

Level of road.

Possible values:
- `0`
- `1`
- `2`

### sea

This layer depicts the sea around Great Britain.

### sites

Polygon features that represent the area or extent of certain types of function or activity.

### Fields

#### type

Type of site.

Possible values:
- `Air Transport`
- `Education`
- `Medical Care`
- `Road Transport`
- `Water Transport`

### surfacewater

These polygons represent inland water bodies that are sufficiently wide enough to be captured as an area.

### urban_areas

These are generalised polygons representing built-up areas for use at smaller scales.

### waterlines

Lines representing rivers, canals, drains and other linear bodies of water.

### Fields

#### type

Type of waterline.

Possible values:

- `National`
- `Regional`
- `District`
- `Local`
- `MHW`
- `MLW`

### woodland

The polygons represent areas of trees: coniferous, non-coniferous and mixed.

