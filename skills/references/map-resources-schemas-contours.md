# MapTiler Contours

Source: https://docs.maptiler.com/schema/contours/

Tileset containing isolines of equal elevation.

MapTiler Contours is a tileset that contains contour lines with height in both meters and feet and additional information
  for index line and glacier styling.

## Layers

### contour

Contour lines with height in meters and additional information for index line and glacier styling.

### Fields

#### height

Elevation in meters (10 m resolution globally, 5 m resolution in specific areas - please see the [`high-res section`](https://docs.maptiler.com/schema/contours/#high-res)).

#### nth_line

Specifies the order of a contour line. Convenient for index line marking.

Possible values:
- `0`
- `1`
- `2`
- `5`
- `10`

Example:

For contour lines at zoom level 14 and higher
in areas with high-resolution data (5 m resolution), 
the following contour lines with `height` and `nth_line` attributes are available:

| height (m) |   | nth_line  |
|------------|---|-----------|
| 1200       |   | 10        |
| 1205       |   | 0         |
| 1210       |   | 1         |
| 1215       |   | 0         |
| 1220       |   | 2         |
| 1225       |   | 0         |
| 1230       |   | 1         |
| 1235       |   | 0         |
| 1240       |   | 2         |
| 1245       |   | 0         |
| 1250       |   | 5         |
| 1255       |   | 0         |
| 1260       |   | 2         |
| 1265       |   | 0         |
| 1270       |   | 1         |
| 1275       |   | 0         |
| 1280       |   | 2         |
| 1285       |   | 0         |
| 1290       |   | 1         |
| 1295       |   | 0         |
| 1300       |   | 10        |


#### glacier

Marks whether a line intersects a glacier.

### contour_ft

Contour lines with height in feet and additional information for index line and glacier styling.

### Fields

#### height

Elevation in feet.

#### nth_line

Specifies the order of a contour line. Convenient for index line marking.

Possible values:
- `1`
- `2`
- `5`
- `10`

Example:

For contour lines at zoom level 14 and higher
in areas with high-resolution data, 
the following contour lines with `height` and `nth_line` attributes are available:

| height (ft) |   | nth_line  |
|-------------|---|-----------|
| 4000        |   | 10        |
| 4010        |   | 1         |
| 4020        |   | 2         |
| 4030        |   | 1         |
| 4040        |   | 2         |
| 4050        |   | 5         |
| 4060        |   | 2         |
| 4070        |   | 1         |
| 4080        |   | 2         |
| 4090        |   | 1         |
| 4100        |   | 10        |
| 4110        |   | 1         |
| 4120        |   | 2         |
| 4130        |   | 1         |
| 4140        |   | 2         |
| 4150        |   | 5         |
| 4160        |   | 2         |
| 4170        |   | 1         |
| 4180        |   | 2         |
| 4190        |   | 1         |
| 4200        |   | 10        |


#### glacier

Marks whether a line intersects a glacier.

### high-res

List of areas with high resolution data.

### 5 m

- Czech Republic

More to come.

### 10 m

- Planet (global coverage)

