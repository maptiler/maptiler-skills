# France Cadastre

Source: https://docs.maptiler.com/schema/fr-cadastre/

Tileset containing cadastral layers, parcel information, buildings, etc.

France Cadastral is a tileset containing real estate cadastre information for France.
Design of tileset containing the most useful information like parcel, buildings and their numbers, or addresses.
Tileset provides the most precise geometry (low scale mapping) with additional information for interconnecting
with authorities.

Nevertheless, this Tileset cannot be used for any legal action and in any legal 
case please contact the competent authority.

## Layers

### batiments

Polygons of the buildings.

### Fields

#### commune

Commune code.

#### created

Date of data creation.

#### nom

Name of the building.

#### type

Type of the building. `01` for `bâtiment dur` , `02` for `bâtiment léger`.

Possible values:

- `01`
- `02`

#### updated

Date of data update.

### parcelles

The main part of the cadastral map defines areas and owners.

### Fields

#### id

Parcel ID defined by the responsible party.

#### numero

A parcel name is often just a number defined by the responsible party.

#### arpente

Marks whether the parcel has been surveyed.  
Possible values:

- `false`
- `true`

#### commune

Commune code.

#### created

Date of data creation.

#### prefixe

Prefix

#### section

Section ID.

#### updated

Date of data update.

#### contenance

Parcel area.

### sections

Sections.

### Fields

#### id

Section ID defined by the responsible party.

#### code

Code.

#### commune

Commune code.

#### created

Date of data creation.

#### prefixe

Prefix code.

#### updated

Date of data update.

