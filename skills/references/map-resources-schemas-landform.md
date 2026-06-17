# MapTiler Landform

Source: https://docs.maptiler.com/schema/landform/

A global vector tileset representing prominent topographic features.

MapTiler Landform is a tileset that contains prominent topographic features—such as mountain peaks, volcanoes,
  saddles, cliffs, and ridgelines. Features with elevations include values in both metres and feet.

## Layers

### cliff

Lines representing vertical or near-vertical natural drop in terrain topography.

### cliff_label

Lines with names representing vertical or near-vertical natural drop in terrain topography.

### Fields

#### name
Name of the cliff. Language-specific values are in `name:xx`.

Examples:
- `White Cliffs of Dover`
- `Pålstovebrotet`

### peak

Points representing the tops (summits) of hills or mountains.
### Fields

#### customary_units

Indicates the customary unit used to display a peak elevation in its country. 

Values:
- `m`
- `ft`

#### ele

Elevation in meters.

Min/max values: 
- `-1090`
- `8849`

#### ele_ft

Elevation in feet.

Min/max value:
- `-3576`
- `29032`

#### iso_a2

Two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

Examples:

- `CH`
- `JP`
- `US`

#### name

Name of the peak. Language-specific values are in `name:xx`.

Examples:

- `Dufourspitze`
- `Mount Rainier`
- `御嶽山`


#### rank

Importance of the peak. Higher peaks and peaks with name have lower rank.

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
- `worldview:ch=recognized` -> `name=Denali`
- `worldview:us=recognized` -> `name=Mount McKinley`

### ridge

Lines representing a hill or mountain landform with a continuous elevated crest.

### Fields

#### class
Distinguishes between a `ridge` and an `arête`. The term `arête` refers specifically to a sharp, narrow, rocky ridge.

Values:
- `arete`
- `ridge`

### ridge_label

Lines with names representing a hill or mountain landform with a continuous elevated crest.

### Fields

#### class
Distinguishes between a `ridge` and an `arête`. The term `arête` refers specifically to a sharp, narrow, rocky ridge.

Values:
- `arete`
- `ridge`


#### name
Name of the ridge. Language-specific values are in `name:xx`.

Examples:
- `Tschingelgrat`
- `Filo Noroeste`
- `Kozí chrbát`

### saddle

Points representing the lowest point along a ridge or between two mountain tops.

### Fields

#### class
Distinguishes between a `mountain_pass`, which is the highest point of a road, railway, or path crossing a mountain 
crest, and a `saddle`, which refers to a topographic depression between two peaks.

Values:
- `mountain_pass`
- `saddle`

#### customary_units

Indicates the customary unit used to display a peak elevation in its country. 

Values:
- `m`
- `ft`

#### ele

Elevation in meters.

Min/max values: 
- `-670`
- `7907`

#### ele_ft

Elevation in feet.

Min/max values:
- `-2198`
- `25942`

#### iso_a2

Two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

Examples:

- `CH`
- `JP`
- `US`

#### name

Name of the saddle. Language-specific values are in `name:xx`.

Examples:

- `Col du Grand Saint-Bernard`
- `Newfound Gap`
- `Thorong La`


#### rank

Importance of the saddle. Higher saddles and saddles with name have lower rank.

### volcano

Points representing tops (summits) of a volcano.

### Fields

#### customary_units

Indicates the customary unit used to display a peak elevation in its country. 

Values:
- `m`
- `ft`

#### ele

Elevation in meters.

Min/max value: 
- `-3800`
- `6891`

#### ele_ft

Elevation in feet.

Min/max value:
- `-12467`
- `22608`

#### iso_a2

Two-letter country code [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

Examples:

- `CH`
- `JP`
- `US`

#### name

Name of the peak. Language-specific values are in `name:xx`.

Examples:

- `Etna`
- `Mount Saint Helens`
- `富士山`


#### rank

Importance of the volcano. Higher volcanoes and volcanoes with name have lower rank. 

#### status

Status of the volcano.

Values:

- `active`
- `dormant`
- `extinct`
- `inactive`
- `unknown`

#### Submarine

Indicates whether the volcano is located underwater.

Values:

- `true`
- `false`

