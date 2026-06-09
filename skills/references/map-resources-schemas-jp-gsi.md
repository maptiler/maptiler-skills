# JP GSI

Source: https://docs.maptiler.com/schema/jp-gsi/

Tileset containing vector tiles of Japan provided by the Geospatial Information Authority of Japan.

JP GSI is a tileset that contains vector tiles provided by the Geospatial Information Authority of Japan.

## Layers

### AdmArea

Layer containing Administrative Area (AdmArea).

### Block

`AdmArea`

### Geometry

`Polygon`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `1104` (Towns/Villages and Wards of Designated Cities)
- `1103` (Counties/Cities and Wards of Tokyo)
- `1188`
- `1199`

### AdmBdry

Layer containing Administrative Boundary Line (AdmBdry).

### Block

`AdmBdry`

### Geometry

`LineString`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `1221` (25000 Municipal Boundary)
- `1212` (Regional Boundary)
- `1211` (25000 Prefectural and Hokkaido Regional Bureau Boundary)

### Anno

Layer containing Annotation (Anno).

### Block

`Anno`

### Geometry

`Point`, `LineString`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Min value:
- `110` (Municipality)

Max value:
- `8105` (Radio Tower)

#### vt_text

Type: `string`

#### vt_arrng

Type: `number`

Values:
- `1` (Horizontal Text)
- `2` (Vertical Text)
- `0`
- `3` (Horizontal Free Text)
- `4` (Vertical Free Text)
- `-2147483648`

#### vt_arrngagl

Type: `number`

Min value:
- `-356`

Max value:
- `375`

#### vt_dsppos

Type: `string`

Values:
- `RC`
- `CT`
- `LC`
- `CB`
- `LT`
- `RB`
- `RT`
- `CC`
- `LB`

#### vt_flag17

Type: `number`

Values:
- `0` (Display Zoom Level 16)
- `1` (Display Both Zoom Levels 16,17)
- `2` (Display Zoom Level 17)

### BldA

Layer containing Building (BldA).

### Block

`BldA`

### Geometry

`Polygon`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `3102` (Solid Building)
- `3101` (Ordinary Building)
- `3111` (Ordinary Roofed Structure without Walls)
- `3112` (Solid Roofed Structure without Walls)
- `3103` (High-rise Building)

#### vt_lvorder

Type: `number`

Values:
- `0`
- `4`
- `1`
- `2`
- `3`
- `6`
- `20`
- `10`

### Cntr

Layer containing Contour Line (Cntr).

### Block

`Cntr`

### Geometry

`LineString`

### Min zoom

`8`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `7351` (Contour Line Normal Part)
- `7353` (Contour Line Depression Part)
- `7352` (25000 Contour Line Numeric Value)

#### vt_alti

Type: `number`

Min value:
- `-150`

Max value:
- `3770`

### Cstline

Layer containing Coastline (Cstline).

### Block

`Cstline`

### Geometry

`LineString`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5101` (Coastline Normal Part)
- `5103` (Coastline Contacting Levee etc.)

### Isbt

Layer containing Depth Contour (Isbt).

### Block

`Isbt`

### Geometry

`LineString`

### Min zoom

`11`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `7371` (Depth Contour Normal Part (Lake/Pond))
- `7372` (25000 Depth Contour Numeric Value (Lake/Pond))
- `7373` (Depth Contour Cliff Part (Lake/Pond))

#### vt_depth

Type: `number`

Min value:
- `0`

Max value:
- `420`

### PwrTrnsmL

Layer containing Power Transmission Line (PwrTrnsmL).

### Block

`PwrTrnsmL`

### Geometry

`LineString`

### Min zoom

`14`

### Max zoom

`16`

### Fields

#### vt_code

Type: `number`

Values:
- `8202` (Power Transmission Line)

### RailCL

Layer containing Railway Centerline (RailCL).

### Block

`RailCL`

### Geometry

`LineString`

### Min zoom

`4`

### Max zoom

`16`

### Fields

#### vt_code

Type: `number`

Values:
- `8201` (Railway Centerline)

#### vt_railstate

Type: `string`

Values:
- `通常部` (Normal Part)
- `トンネル ` (Tunnel)
- `トンネル` (Tunnel)
- `橋・高架` (Bridge/Elevated)
- `雪覆い` (Snow Shelter)
- `地下` (Underground)
- `運休中` (Suspended)

#### vt_rtcode

Type: `string`

Values:
- `新幹線` (Shinkansen)
- `主要鉄道` (Major Railway)
- `JR`
- `JR以外` (Other than JR)
- `索道` (Cableway)
- `路面` (Tram)
- `地下鉄` (Subway)
- `特殊鉄道` (Special Railway)
- `側線` (Sidetrack)

#### vt_sngldbl

Type: `string`

Values:
- `複線以上` (Double Track or More)
- `単線` (Single Track)
- `側線` (Sidetrack)
- `駅部分` (Station Part)
- `非表示` (Hidden)

#### vt_lvorder

Type: `number`

Values:
- `1`
- `2`
- `0`
- `3`
- `5`
- `4`
- `6`

#### vt_flag17

Type: `number`

Values:
- `0` (Display Zoom Level 16)
- `1` (Display Both Zoom Levels 16,17)

### RailTrCL

Layer containing Track Centerline (RailTrCL).

### Block

`RailTrCL`

### Geometry

`LineString`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `2821` (Cableway Normal Part)
- `2811` (Special Railway Normal Part)
- `2812` (Special Railway Shielded)
- `2813` (Special Railway Bridge/Elevated)
- `2814` (Special Railway Tunnel)
- `2801` (Ordinary Railway Normal Part)
- `2802` (Ordinary Railway Shielded)
- `2804` (Ordinary Railway Tunnel)
- `2803` (Ordinary Railway Bridge/Elevated)
- `2841` (Sidetrack Normal Part)
- `2843` (Sidetrack Bridge/Elevated)
- `2842` (Sidetrack Shielded)
- `2822` (Cableway Shielded)
- `2831` (Tram Normal Part)
- `2832` (Tram Shielded)
- `2833` (Tram Bridge/Elevated)
- `2834` (Tram Tunnel)
- `2806` (Ordinary Railway Suspended)
- `2824` (Cableway Tunnel)
- `2823`
- `2836` (Tram Suspended)
- `2844` (Sidetrack Tunnel)

#### vt_drworder

Type: `number`

Values:
- `0`
- `1`
- `2`

### RdCL

Layer containing Road Centerline (RdCL).

### Block

`RdCL`

### Geometry

`LineString`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `2701` (Road Centerline Normal Part)
- `2704` (Road Centerline Tunnel)
- `2703` (Road Centerline Bridge/Elevated)
- `2711` (2-Lane Road Centerline Normal Part)
- `2721` (2-Lane Road Centerline Normal Part)
- `2713` (2-Lane Road Centerline Bridge/Elevated)
- `2731` (Footpath Normal Part)
- `2723` (2-Lane Road Centerline Bridge/Elevated)
- `2714` (2-Lane Road Centerline Tunnel)
- `2724` (2-Lane Road Centerline Tunnel)
- `2702` (Road Centerline Snow Shelter)
- `2712` (2-Lane Road Centerline Snow Shelter)
- `2722` (2-Lane Road Centerline Snow Shelter)
- `2732` (Footpath Snow Shelter)

#### vt_rdctg

Type: `string`

Values:
- `高速自動車国道等` (National Expressway, etc.)
- `主要道路` (Major Road)
- `国道` (National Highway)
- `不明` (Unknown)
- `都道府県道` (Prefectural Road)
- `市区町村道等` (Municipal Road, etc.)
- `その他` (Other)

#### vt_drworder

Type: `number`

Values:
- `4`
- `2`
- `3`
- `44`
- `49`
- `48`
- `40`
- `24`
- `47`
- `29`
- `28`
- `26`
- `46`
- `27`
- `43`
- `23`
- `54`
- `45`
- `55`
- `41`
- `25`
- `51`
- `21`
- `42`
- `50`
- `53`
- `22`
- `52`
- `20`
- `34`
- `35`
- `33`
- `31`
- `32`

#### vt_tollsect

Type: `string`

Values:
- `不明` (Unknown)
- `無料` (Free)
- `有料` (Toll)
- `暫定無料` (Provisionally Free)

#### vt_motorway

Type: `number`

Values:
- `9` (Unknown)
- `0` (Other than Expressway)
- `1` (Expressway)

#### vt_lvorder

Type: `number`

Values:
- `0`
- `1`
- `2`
- `3`
- `4`

#### vt_rnkwidth

Type: `string`

Values:
- `3m未満` (Under 3m)
- `5.5m-13m未満` (5.5m to under 13m)
- `3m-5.5m未満` (3m to under 5.5m)
- `13m-19.5m未満` (13m to under 19.5m)
- `19.5m以上` (19.5m or more)
- `不明` (Unknown)

#### vt_width

Type: `number`

Min value:
- `131`

Max value:
- `7992`

#### vt_flag17

Type: `number`

Values:
- `0` (Display Zoom Level 16)
- `1` (Display Both Zoom Levels 16,17)

### RdCompt

Layer containing Road Configuration Line (RdCompt).

### Block

`RdCompt`

### Geometry

`LineString`

### Min zoom

`17`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `2401` (Road in Tunnel)
- `2411` (Median Normal Part)

### RdEdg

Layer containing Road Edge (RdEdg).

### Block

`RdEdg`

### Geometry

`LineString`

### Min zoom

`17`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `2201` (Road Edge Normal Part)
- `2221` (Road Edge Normal Part)
- `2223` (Road Edge Bridge/Elevated)
- `2203` (Road Edge Bridge/Elevated)
- `2204` (Road Edge Tunnel Entrance Line)
- `2224` (Road Edge Tunnel Entrance Line)

#### vt_drworder

Type: `number`

Values:
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`

### RvrCL

Layer containing River Centerline (RvrCL).

### Block

`RvrCL`

### Geometry

`LineString`

### Min zoom

`8`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5301` (Single River Normal Part)
- `5322` (Artificial Waterway Underground)
- `5302` (Single River Dry Riverbed)
- `5321` (Artificial Waterway Space)
- `5331` (Irrigation Canal)

### SpcfArea

Layer containing Specific Area Boundary (SpcfArea).

### Block

`SpcfArea`

### Geometry

`LineString`

### Min zoom

`11`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `6101` (Specific Area Boundary)

### StrctArea

Layer containing Structure Area (StrctArea).

### Block

`StrctArea`

### Geometry

`Polygon`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `4302` (Tank)
- `4301` (Huge Structure)

### StrctLine

Layer containing Structure Line (StrctLine).

### Block

`StrctLine`

### Geometry

`LineString`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `4202` (Mine/Tunnel Entrance)
- `4201` (Tall Tower)

### TpgphArea

Layer containing Topographic Notation Area (TpgphArea).

### Block

`TpgphArea`

### Geometry

`Polygon`

### Min zoom

`8`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `7401` (Wetland)
- `7403` (Gravel Area (When Boundary is Clear))
- `7402` (Perennial Snow)

#### vt_flag17

Type: `number`

Values:
- `1` (Display Both Zoom Levels 16,17)
- `0` (Display Zoom Level 16)

### TpgphLine

Layer containing Topographic Notation Line (TpgphLine).

### Block

`TpgphLine`

### Geometry

`LineString`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `7532` (Depression Direction Line Small Depression (Arrow))
- `7531` (Depression Direction Line Large Depression (Protrusion))
- `7509` (Earth Cliff (Unknown))
- `7501` (Earth Cliff Concrete/Solid Stone Masonry Slope)
- `7502` (Earth Cliff Concrete/Not Solid Stone Masonry Slope)
- `7511` (Rock Cliff)
- `7521` (Gully (Upper Part))
- `7551` (Tidal Flat Boundary)
- `7512` (Rock)
- `7541` (Rock Awash)
- `7572` (Water Depression Direction Line)
- `7571` (Steep Lake Bottom Slope)
- `7561` (Dry River Waterline)

### WA

Layer containing Water Area (WA).

### Block

`WA`

### Geometry

`Polygon`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5242` (Lake/Pond Boundary Line (Lake/Pond Side))
- `5101` (Coastline Normal Part)
- `5231` (Lake/Pond Normal Part)
- `5190`
- `5201` (River Normal Part)
- `5203` (River Contacting Levee etc.)
- `5202` (River Contacting Rock etc.)
- `5103` (Coastline Contacting Levee etc.)
- `5102` (Coastline Contacting Rock etc.)
- `5100` (Sea)
- `5200` (River/Lake/Pond)

### WL

Layer containing Waterline (WL).

### Block

`WL`

### Geometry

`LineString`

### Min zoom

`16`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5201` (River Normal Part)
- `5203` (River Contacting Levee etc.)
- `5231` (Lake/Marsh Normal Part)
- `5233` (Lake/Marsh Contacting Levee etc.)

### WRltLine

Layer containing Water Notation Line (WRltLine).

### Block

`WRltLine`

### Geometry

`LineString`, `Polygon`, `Point`

### Min zoom

`4`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5902` (Water/Maritime Traffic Route Trajectory)
- `5901` (Water/Maritime Traffic Vessel)
- `5911` (Flow Direction)

#### vt_angle

Type: `number`

Min value:
- `0`

Max value:
- `360`

### WStrA

Layer containing Water Structure Area (WStrA).

### Block

`WStrA`

### Geometry

`Polygon`

### Min zoom

`8`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5411` (Pier (Iron, Concrete))
- `5401` (Dam)

### WStrL

Layer containing Water Structure Line (WStrL).

### Block

`WStrL`

### Geometry

`LineString`

### Min zoom

`14`

### Max zoom

`17`

### Fields

#### vt_code

Type: `number`

Values:
- `5515` (Sluice Gate)
- `5521` (Waterfall)
- `5501` (Dam)
- `5532` (Permeable Breakwater)
- `5511` (Pier (Iron, Concrete))
- `5514` (Weir)

#### vt_flag17

Type: `number`

Values:
- `1` (Display Both Zoom Levels 16,17)
- `0` (Display Zoom Level 16)
- `2` (Display Zoom Level 17)

