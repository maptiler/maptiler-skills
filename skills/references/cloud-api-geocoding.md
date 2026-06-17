# Geocoding API

The MapTiler **Search and geocoding API** makes it possible to search for any place on Earth and get accurate location data in return. This API supports forward geocoding (search by place name), reverse geocoding (search by coordinates), feature ID search, and batch geocoding.

URL: `https://docs.maptiler.com/cloud/api/geocoding/`

## Endpoints

### 1. Search by name (Forward)
`GET https://api.maptiler.com/geocoding/{query}.json`
- **Description:** Forward geocoding (search by place name). You can also use a bare POI category or mix it with a name to search for POIs of a desired category.
- **Path Parameters:** 
  - `query` (string, required) - Place name to search.

### 2. Search by coordinates (Reverse)
`GET https://api.maptiler.com/geocoding/{longitude},{latitude}.json`
- **Description:** Reverse geocoding (search by coordinates).
- **Path Parameters:**
  - `longitude` (number, required) - Longitude between -180 and 180.
  - `latitude` (number, required) - Latitude between -90 and 90.

### 3. Search by feature ID
`GET https://api.maptiler.com/geocoding/{id}.json`
- **Description:** Search feature by its ID (`id`) as returned in a forward or reverse geocoding response and return its full geometry. Note that the feature ID is not stable and it changes when the database is re-indexed.
- **Path Parameters:**
  - `id` (string, required) - Feature ID (e.g., `country.26561650`).

### 4. Batch geocoding
`GET https://api.maptiler.com/geocoding/{queries}.json`
- **Description:** Perform geocoding of more than one request in a single API call.
- **Path Parameters:**
  - `queries` (string, required) - Semicolon-separated list of queries. Semicolon `;` must be provided verbatim and not be URL-encoded. Each query may be forward, reverse or by feature ID. Maximum of 50 queries are supported. Example: `Paris;Berlin`.

---

## Query Parameters

The following query parameters can be appended to the API requests (along with your `?key=YOUR_MAPTILER_API_KEY`).

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `bbox` | `[w, s, e, n]` array | | A bounding box array to use for limiting search results. Only features inside the provided bounding box will be included. Example: `5.95,45.8,10.49,47.8`. |
| `proximity` | `[lon, lat]` array or `ip` | | A coordinate array to bias search results, or the string `ip` to do server-side IP based geolocation. Features closer to the proximity value will be given priority. |
| `language` | array of strings | | Prefer results in a specific language (ISO 639-1 code). E.g., `de,en`. If omitted, the `Accept-Language` HTTP header is analyzed. |
| `country` | array of strings | | Limit search to specific country/countries using ISO 3166-1 alpha-2 codes. E.g., `sk,cz`. |
| `limit` | integer (1-10) | `5` | Maximum number of results to return. For reverse geocoding with multiple types, this must not be set or must be set to `1`. |
| `types` | array of strings | | Filter types of which features to return (e.g., `address`, `poi`, `country`). In reverse geocoding, if just a single type is specified, multiple nearby features of that type can be returned. |
| `excludeTypes`| boolean | `false` | Set to `true` to use all available feature types *except* those specified in `types`. |
| `fuzzyMatch` | boolean | `true` | Set to `false` to disable fuzzy search. |
| `autocomplete`| boolean | `true` | Set to `true` to use autocomplete, `false` to disable autocomplete. |
| `worldview` | string | `default` | Disputed boundaries worldview alignment. Options: `default`, `auto` (determined by client location), `ch`, `us`. |

---

## Response Format

The API returns a **GeoJSON FeatureCollection** where every item is represented as a GeoJSON Feature.

### Success Response (200 OK)
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "country.26561650",
      "text": "Switzerland",
      "place_name": "Switzerland",
      "place_type": ["country"],
      "relevance": 1,
      "properties": {
        "ref": "ch",
        "country_code": "ch",
        "kind": "country"
      },
      "bbox": [5.9559, 45.818, 10.4921, 47.8084],
      "center": [8.2275, 46.8182],
      "geometry": {
        "type": "Point",
        "coordinates": [8.2275, 46.8182]
      }
    }
  ],
  "query": ["switzerland"],
  "attribution": "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e"
}
```

### Error Responses
- **`400`**: Query too long / Invalid parameters
- **`403`**: Forbidden (Invalid, missing, or restricted API key)

### Place Types & POI Categories
Available `types` to filter by include: `continental_marine`, `country`, `major_landform`, `region`, `subregion`, `county`, `joint_municipality`, `joint_submunicipality`, `municipality`, `municipal_district`, `locality`, `neighbourhood`, `place`, `postal_code`, `address`, `road`, `poi`.

If `poi` is queried or filtered, the `properties` object of the feature will also contain an array of `categories` (e.g. `["restaurant"]` or `["atm"]`).


### Complete List of POI Categories
Below is the exhaustive list of supported POI categories that can be queried or returned in the properties.categories array:

\accessories\, \adit\, \adult_gaming_centre\, \advertising_agency\, \aerodrome\, \aeroway\, \agrarian\, \agricultural_engines\, \aikido\, \airsoft\, \alcohol\, \allotments\, \alpine_hut\, \american_football\, \american_handball\, \amusement_arcade\, \animal_breeding\, \animal_shelter\, \anime\, \antiques\, \apartment\, \appliance\, \aquarium\, \arch\, \archaeological_site\, \archery\, \architect\, \archipelago\, \art\, \arts_centre\, \artwork\, \association\, \association_football\, \athletics\, \atm\, \attraction\, \atv\, \audiologist\, \australian_football\, \baby_goods\, \badminton\, \bag\, \bakery\, \balle_pelote\, \bandy\, \bank\, \bar\, \barbecue\, \bare_rock\, \barefoot\, \baseball\, \basin\, \basketball\, \bathing_place\, \bathroom_furnishing\, \batting_cage\, \bay\, \bbq\, \beach\, \beach_resort\, \beachvolleyball\, \beauty\, \bed\, \bed_and_breakfast\, \beekeeper\, \beverages\, \biathlon\, \bicycle\, \bicycle_parking\, \bicycle_rental\, \bicycle_repair\, \bicycle_repair_station\, \biergarten\, \billards\, \billiards\, \bird_hide\, \birds_nest\, \blacksmith\, \blowhole\, \bmx\, \boat\, \boat_repair\, \boatbuilder\, \bobsleigh\, \bookbinder\, \bookmaker\, \books\, \boules\, \boutique\, \bowling\, \bowling_alley\, \bowls\, \boxing\, \brewery\, \brewing_supplies\, \brothel\, \brownfield\, \builder\, \building_materials\, \bullfighting\, \bunker\, \bureau_de_change\, \bus_station\, \bus_stop\, \business_machines\, \butcher\, \cabinet_maker\, \cable_car\, \cafe\, \calisthenics\, \camera\, \camp_site\, \canadian_football\, \canal\, \candles\, \cannabis\, \canoe\, \canoe_hire\, \cape\, \car\, \car_parts\, \car_rental\, \car_repair\, \car_service\, \car_wash\, \caravan\, \caravan_site\, \carpenter\, \carpet\, \carpet_layer\, \casino\, \castle\, \catalogue\, \caterer\, \cathedral\, \cave_entrance\, \cemetery\, \ceramics\, \chair_lift\, \chalet\, \chandler\, \chapel\, \charging_station\, \charity\, \cheese\, \chemist\, \chess\, \childcare\, \chimney_sweeper\, \chocolate\, \church\, \cinema\, \city_gate\, \cleaning\, \cliff_diving\, \clinic\, \clock\, \clockmaker\, \clothes\, \coffee\, \collector\, \college\, \commercial\, \communication\, \community_centre\, \compressed_air\, \computer\, \confectionery\, \convenience\, \copyshop\, \cosmetics\, \country_store\, \courthouse\, \craft\, \cricket\, \cricket_nets\, \croquet\, \crossfit\, \curling\, \curtain\, \cycling\, \dairy\, \dance\, \dancing\, \dancing_school\, \darts\, \deli\, \delicatessen\, \dental_technician\, \dentist\, \dentures\, \department_store\, \device_charging_station\, \diplomatic\, \disc_golf\, \disc_golf_course\, \discount\, \distillery\, \diving\, \dock\, \doctors\, \dog_agility\, \dog_park\, \dog_racing\, \doityourself\, \doors\, \dormitory\, \drag_lift\, \dressmaker\, \dressing_room\, \drinking_water\, \driving_school\, \dry_cleaning\, \educational_institution\, \electrical\, \electrician\, \electronics\, \electronics_repair\, \electrotools\, \embassy\, \energy\, \equestrian\, \erotic\, \escape_game\, \esoteric\, \estate_agent\, \events_venue\, \fabric\, \farm\, \farmland\, \farmyard\, \fashion\, \fashion_accessories\, \fast_food\, \feeding_place\, \fell\, \fencing\, \ferry_terminal\, \field_hockey\, \financial\, \financial_advisor\, \fire_station\, \firearms\, \firepit\, \fireplace\, \fireworks\, \fish\, \fishing\, \fishmonger\, \fitness\, \fitness_centre\, \fitness_station\, \floorball\, \floorer\, \flooring\, \florist\, \food\, \food_court\, \football\, \footballgolf\, \forest\, \four_square\, \frame\, \free_flying\, \frozen_food\, \fuel\, \funeral_directors\, \funeral_hall\, \funnel_ball\, \furnace\, \furniture\, \futsal\, \gaelic_games\, \gaga\, \gallery\, \gambling\, \games\, \garages\, \garden\, \garden_centre\, \garden_furniture\, \garden_machinery\, \gardener\, \gas\, \gate\, \general\, \general_store\, \geyser\, \gift\, \glacier\, \glass\, \glaziery\, \golf\, \golf_course\, \gondola\, \gold_buyer\, \goods\, \grassland\, \grave_yard\, \greengrocer\, \grocery\, \groundskeeping\, \guest_house\, \guns\, \gymnastics\, \haberdashery\, \hackerspace\, \hairdresser\, \hairdresser_supply\, \halt\, \handball\, \handicraft\, \hangar\, \hardware\, \health\, \health_food\, \hearing_aids\, \heath\, \helipad\, \herbalist\, \hifi\, \hobby\, \hockey\, \honey\, \hookah\, \horse_racing\, \horse_riding\, \horseshoes\, \hospital\, \hostel\, \hot_spring\, \hot_tub\, \hotel\, \household\, \household_linen\, \houseware\, \hunting\, \hunting_stand\, \hvac\, \ice_cream\, \ice_hockey\, \ice_rink\, \ice_skating\, \ice_stock\, \industrial\, \information\, \insurance\, \interior_decoration\, \island\, \islet\, \jewelry\, \jeweller\, \joiner\, \judo\, \juice\, \junk_yard\, \karate\, \karting\, \key_cutter\, \kickboxing\, \kindergarten\, \kiosk\, \kitchen\, \kitchenware\, \kitesurfing\, \korfball\, \krachtbal\, \lacrosse\, \lamps\, \landfill\, \language_school\, \laser_tag\, \laundromat\, \laundry\, \lawyer\, \leather\, \library\, \lighthouse\, \lighting\, \local\, \locksmith\, \long_jump\, \lottery\, \magic_carpet\, \mall\, \manor\, \maps\, \marina\, \marine\, \marketplace\, \martial_arts\, \massage\, \maze\, \meadow\, \medical\, \medical_supply\, \memorial\, \military\, \military_surplus\, \mineshaft\, \miniature_golf\, \mixed_lift\, \mobile_home\, \mobile_phone\, \mobility_scooter\, \model\, \model_aerodrome\, \monastery\, \money_lender\, \money_transfer\, \monument\, \mosque\, \motel\, \motocross\, \motor\, \motorcycle\, \motorcycle_parking\, \motorcycle_parts\, \motorcycle_rental\, \motorcycle_repair\, \motorhome\, \motorsports\, \mountain_range\, \multi\, \museum\, \music\, \music_school\, \musical_instrument\, \national_park\, \natural\, \netball\, \new_age\, \newsagent\, \ngo\, \nightclub\, \nine_mens_morris\, \notary\, \nutrition_supplements\, \nuts\, \observatory\, \obstacle_course\, \ocean\, \office_supplies\, \optician\, \orchard\, \organic\, \orienteering\, \outdoor\, \outpost\, \paddle_tennis\, \padel\, \paint\, \paintball\, \painter\, \parachuting\, \paragliding\, \parcel_locker\, \park\, \parking\, \parking_entrance\, \parking_space\, \parkour\, \party\, \pasta\, \pastry\, \pawnbroker\, \peak\, \pelota\, \peninsula\, \perfume\, \perfumery\, \pest_control\, \pet\, \pet_grooming\, \petanque\, \pharmacy\, \photo\, \photo_studio\, \photographer\, \photographic_laboratory\, \photography\, \picnic_site\, \picnic_table\, \pickleball\, \piercing\, \pilates\, \pitch\, \place_of_mourning\, \place_of_worship\, \plain\, \planetarium\, \plant\, \plant_hire\, \plasterer\, \plateau\, \platter\, \playground\, \plumber\, \pole_dance\, \police\, \polo\, \post_box\, \post_office\, \pottery\, \power_tools\, \printer\, \printer_ink\, \printing\, \prison\, \protected_area\, \psychic\, \pub\, \public_bookcase\, \public_building\, \pyrotechnics\, \quarry\, \racquet\, \radiotechnics\, \railway\, \ranger_station\, \rc_car\, \recreation_ground\, \recycling\, \religion\, \rental\, \repair\, \reservoir\, \reservoir_covered\, \residential\, \resort\, \restaurant\, \retail\, \rice\, \ridge\, \river\, \rock\, \roller_hockey\, \roller_skating\, \roofer\, \rope_tow\, \rowing\, \rugby\, \rugby_league\, \rugby_union\, \ruins\, \running\, \saddle\, \saddler\, \safety_training\, \sailing\, \salad\, \salon\, \sand\, \sauna\, \scaffolder\, \school\, \scooter\, \scree\, \scrub\, \scuba_diving\, \sculptor\, \sea\, \seafood\, \second_hand\, \security\, \sewing\, \shed\, \shelter\, \ship_chandler\, \shoe_repair\, \shoemaker\, \shoes\, \shooting\, \shooting_ground\, \shooting_range\, \shop\, \shopping_centre\, \shower\, \shuffleboard\, \signmaker\, \sinkhole\, \skate\, \skateboard\, \skating\, \ski\, \ski_jumping\, \ski_rental\, \skiing\, \smoking_area\, \snack\, \snooker\, \snowmobile\, \soccer\, \social_centre\, \social_club\, \social_facility\, \softball\, \souvenir\, \spare_parts\, \speedway\, \spices\, \sport\, \sports\, \sports_centre\, \sports_hall\, \spring\, \squash\, \stadium\, \station\, \stationery\, \stonemason\, \storage_rental\, \strait\, \stream\, \street_vendor\, \streetball\, \stripclub\, \studio\, \subway_entrance\, \summer_camp\, \sumo\, \supermarket\, \surf\, \surfing\, \swimming\, \swimming_area\, \swimming_pool\, \synagogue\, \table_soccer\, \table_tennis\, \taekwondo\, \tailor\, \tanning_salon\, \tapas\, \tattoo\, \tax_advisor\, \taxi\, \tea\, \team_handball\, \telecommunication\, \telephone\, \telescope\, \temple\, \tennis\, \terminal\, \tetherball\, \theme_park\, \theatre\, \ticket\, \tiler\, \tiles\, \tinsmith\, \tobacco\, \toboggan\, \toilets\, \tomb\, \tool_hire\, \tools\, \touch_football\, \tourism\, \tower\, \townhall\, \toys\, \track\, \tractor\, \trade\, \traffic_park\, \trail_riding_station\, \trailer\, \tram_stop\, \trampoline\, \trampoline_park\, \travel_agency\, \tree\, \trolley_bay\, \trophy\, \truck\, \truck_repair\, \tyres\, \ultimate\, \ultralight_aviation\, \university\, \upholsterer\, \vacuum_cleaner\, \valley\, \variety_store\, \vehicle_inspection\, \vending_machine\, \veterinary\, \video\, \video_games\, \viewpoint\, \vineyard\, \volleyball\, \wakeboarding\, \wastewater_plant\, \watches\, \water\, \water_park\, \water_polo\, \water_point\, \water_ski\, \water_sports\, \water_tap\, \water_tower\, \water_well\, \waterfall\, \watering_place\, \watermill\, \waterway\, \weapons\, \weightlifting\, \welder\, \wellness\, \wetland\, \wholesale\, \wigs\, \wilderness_hut\, \wildlife_hide\, \window_blind\, \window_construction\, \windows\, \windsurfing\, \wine\, \wine_cellar\, \winery\, \winter_sports\, \wood\, \wool\, \workout\, \workshop\, \wrestling\, \yoga\, \zip_line\, \zoo\, \zurkhaneh_sport\
