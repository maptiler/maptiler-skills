# MapTiler Ocean

Source: https://docs.maptiler.com/schema/ocean/

"Tileset containing isolines and areas of equal depths of world oceans and seas."

MapTiler Ocean is a tileset that contains contour lines with minimum depth in meters, adjacent polygons with minimum depth
  for world oceans and seas.

## Layers

### contour

---
category: schema-ocean
title: contour
description: "Polygons mapping ocean and sea depths with depth values."
sql_query: SELECT depth, geometry FROM
  layer_bathymetry(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 12)
indexed: false
---
Contains polygons of ocean and sea depths.

### Fields

#### depth

Minimal depth value (a negative number).

Possible values:

- `0`
- `-12000`

### contour_line

---
category: schema-ocean
title: contour_line
description: "Lines mapping ocean and sea depths with depth values."
sql_query: SELECT depth, geometry FROM
  layer_contour_line(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 12)
indexed: false
---
Contains lines of ocean and sea depths.

### Fields

#### depth

Minimal depth value (a negative number).

Possible values:

- `0`
- `-12000`

### landform

---
category: schema-ocean
title: landform
description: "Topographic earth features including canyons, hills, and ocean ridges."
sql_query: SELECT geometry, name, class FROM
  layer_landform(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 12)
indexed: false
---
A landform is any topographic feature on the Earth, e.g., canyons, hills, or ridges.

### Fields

#### name

The name of landform entity.

#### class

The type of landform entity.

Possible values:

- `Bank`
- `Caldera`
- `Canyon`
- `Deep`
- `Guyot`
- `Hill`
- `Knoll`
- `Reef`
- `Ridge`
- `Seamount`
- `Shoal`
- `Valley`
- `Sea Valley`

### water_name

---
category: schema-ocean
title: water_name
description: "Named ocean and sea polygons for water body labeling."
sql_query: SELECT geometry, name, class FROM
  layer_water_name(ST_SetSRID('BOX3D(-20037508.34 -20037508.34, 20037508.34
  20037508.34)'::box3d, 3857), 12)
indexed: false
---
Ocean and sea names.

### Fields

#### name

The name value of the water body.

#### class

Distinguish between `ocean` and `sea`.

Possible values:

- `sea`
- `ocean`

