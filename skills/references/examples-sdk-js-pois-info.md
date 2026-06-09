# Source: https://docs.maptiler.com/sdk-js/examples/pois-info/

# Offset the vanishing point using padding

Get POI information from MapTiler, OpenStreetMap (OSM), and Wikidata data by clicking on the map.

<sup>Click on any POI on the map to get the information.</sup>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
const marker = new maptilersdk.Marker();

    function toggleSidebar(id) {
        const elem = document.getElementById(id);
        const classes = elem.className.split(' ');
        const collapsed = classes.indexOf('collapsed') !== -1;

        const padding = {};

        if (collapsed) {
            // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
            classes.splice(classes.indexOf('collapsed'), 1);

            padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
            map.easeTo({
                padding: padding,
                duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
            });
        } else {
            padding[id] = 0;
            // Add the 'collapsed' class to the class list of the element
            classes.push('collapsed');

            map.easeTo({
                padding: padding,
                duration: 1000
            });
        }

        // Update the class list on the element
        elem.className = classes.join(' ');
    }

    function showSidebar(id) {
      const elem = document.getElementById(id);
      const classes = elem.className.split(' ');
      const collapsed = classes.indexOf('collapsed') !== -1;
      const padding = {};
      if (collapsed) {
        // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
        classes.splice(classes.indexOf('collapsed'), 1);

        padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
        map.easeTo({
          padding: padding,
          duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
        });
        // Update the class list on the element
        elem.className = classes.join(' ');
      }
    }

    map.on('load', function () {
      toggleSidebar('left');
      map.on('click', async function(e) {
        const features = map.queryRenderedFeatures(e.point, {
          layers: ['Public', 'Sport', 'Tourism', 'Culture', 'Education', 'Shopping', 'Food', 
          'Transport', 'Park', 'Healthcare', 'Station']
        });
        if (features.length > 0) {
          getInfoFromLngLat(e.lngLat, features[0]);
        }
      });
    });

    async function getInfoFromLngLat(lngLat, feature) {
      marker.setLngLat(lngLat).addTo(map);
      const osmInfo = await getOMSInfo(feature.id);
      const wikidata = await getWikidata(osmInfo?.tags);
      showPoiInfo(feature, osmInfo, wikidata);
    }

    async function getOMSInfo(id) {
      const query = queryString.stringify({
          data: `[out:json][timeout:25];
            node(${id/10});
            out tags;`
        });
      const response = await fetch(`https://overpass-api.de/api/interpreter?${query}`, {
        redirect: 'follow',
        headers: {
          accept: 'application/json'
        },
      });
      const info = await response.json();
      return info?.elements[0] ? info.elements[0] : null;
    }

    function getWikidataId(tags) {
      if (!tags) return null;
      const regexWikidata = /(\w*:)?wikidata/;
      const key = Object.keys(tags).find(key => key.match(regexWikidata));
      return tags[key] ? tags[key] : null;
    }

    function getWikidataImageHash(name) {
      const imageHash = md5(name);
      return imageHash;
    }

    function getWikidataImagePath(image_name) {
      const name = image_name.replace(/\s+/g, '_');
      const hash = getWikidataImageHash(name);
      return `https://upload.wikimedia.org/wikipedia/commons/${hash.substring(0,1)}/${hash.substring(0,2)}/${name}`;
    }

    async function getWikidata(tags) {
      const id = getWikidataId(tags);
      if (!id) return null;
      const response = await fetch(`https://www.wikidata.org/wiki/Special:EntityData/${id}.json?flavor=simple`);
      const info = await response.json();
      let image;
      if (info.entities[id].claims.P154) {
        image = getWikidataImagePath(info.entities[id].claims.P154[0].mainsnak.datavalue.value);
      }else if (info.entities[id].claims.P18) {
        image = getWikidataImagePath(info.entities[id].claims.P18[0].mainsnak.datavalue.value);
      }

      return image ? {...info.entities[id], ...{image}} : info.entities[id];
    }

    function showPoiInfo(feature, osmInfo, wikidata) {
      const textHtml = [];
      if (wikidata?.image) {
        textHtml.push(`<img src="${wikidata?.image}" />`);
      }
      textHtml.push(`<h1>${feature.properties.name}</h1>`);
      if (feature.properties.class !== feature.properties.subclass) {
        textHtml.push(`<h4>${feature.properties.class} (<small>${feature.properties.subclass}</small>)</h4>`);
      } else {
        textHtml.push(`<h4>${feature.properties.class}</h4>`);
      }
      if (osmInfo && osmInfo?.tags) {
        const {opening_hours, "contact:website": contact_website, website, ...tags } = osmInfo.tags;
        if (contact_website || website) {
          let web = website ?? contact_website;
          textHtml.push(`<div><a href="${web}">${web}</a></div>`);
        }
        if (opening_hours) {
          textHtml.push(`<h3>Opening hours</h3>`);
          osmInfo?.tags?.opening_hours.split(",").forEach(element => {
            textHtml.push(`<div>${element.trim()}</div>`);
          });
        }
        if (tags) {
          textHtml.push(`<h3>Details</h3>`);
          textHtml.push(`<div class="details-info">`);
          Object.keys(tags).forEach(element => {
            if (element.includes("email")) {
              textHtml.push(`<div><label>${element}:</label><a href="mailto: ${tags[element]}">${tags[element]}</a></div>`);
            } else if (element.includes("website")) {
              textHtml.push(`<div><label>${element}:</label><a href="${tags[element]}">${tags[element]}</a></div>`);
            } else if (element.includes("wikidata")) {
              textHtml.push(`<div><label>${element}:</label><a href="https://www.wikidata.org/wiki/${tags[element]}">${tags[element]}</a></div>`);
            } else if (element.includes("wikipedia")) {
              const [lang, term] = tags[element].split(":");
              textHtml.push(`<div><label>${element}:</label><a href="https://${lang}.wikipedia.org/wiki/${term}">${tags[element]}</a></div>`);
            } else {
              textHtml.push(`<div><label>${element}:</label>${tags[element]}</div>`);
            }
          });
          textHtml.push(`</div>`);
        }
      }
      document.querySelector(".sidebar-content-info").innerHTML = textHtml.join("");
      showSidebar('left');
    }

    document.querySelector(".sidebar-toggle").addEventListener('click', function() {
      toggleSidebar('left');
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Offset the vanishing point using padding</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/blueimp-md5/2.19.0/js/md5.min.js"></script>
    <style>
        body { margin: 0; padding: 0; }
        #map { position: absolute; top: 0; bottom: 0; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        maptilersdk.config.apiKey = 'YOUR_MAPTILER_API_KEY';

        const map = new maptilersdk.Map({
            container: 'map',
            style: maptilersdk.MapStyle.STREETS,
            center: [0, 0],
            zoom: 16
        });

        const marker = new maptilersdk.Marker();

            function toggleSidebar(id) {
                const elem = document.getElementById(id);
                const classes = elem.className.split(' ');
                const collapsed = classes.indexOf('collapsed') !== -1;

                const padding = {};

                if (collapsed) {
                    // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
                    classes.splice(classes.indexOf('collapsed'), 1);

                    padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
                    map.easeTo({
                        padding: padding,
                        duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
                    });
                } else {
                    padding[id] = 0;
                    // Add the 'collapsed' class to the class list of the element
                    classes.push('collapsed');

                    map.easeTo({
                        padding: padding,
                        duration: 1000
                    });
                }

                // Update the class list on the element
                elem.className = classes.join(' ');
            }

            function showSidebar(id) {
              const elem = document.getElementById(id);
              const classes = elem.className.split(' ');
              const collapsed = classes.indexOf('collapsed') !== -1;
              const padding = {};
              if (collapsed) {
                // Remove the 'collapsed' class from the class list of the element, this sets it back to the expanded state.
                classes.splice(classes.indexOf('collapsed'), 1);

                padding[id] = 300; // In px, matches the width of the sidebars set in .sidebar CSS class
                map.easeTo({
                  padding: padding,
                  duration: 1000 // In ms, CSS transition duration property for the sidebar matches this value
                });
                // Update the class list on the element
                elem.className = classes.join(' ');
              }
            }

            map.on('load', function () {
              toggleSidebar('left');
              map.on('click', async function(e) {
                const features = map.queryRenderedFeatures(e.point, {
                  layers: ['Public', 'Sport', 'Tourism', 'Culture', 'Education', 'Shopping', 'Food', 
                  'Transport', 'Park', 'Healthcare', 'Station']
                });
                if (features.length > 0) {
                  getInfoFromLngLat(e.lngLat, features[0]);
                }
              });
            });

            async function getInfoFromLngLat(lngLat, feature) {
              marker.setLngLat(lngLat).addTo(map);
              const osmInfo = await getOMSInfo(feature.id);
              const wikidata = await getWikidata(osmInfo?.tags);
              showPoiInfo(feature, osmInfo, wikidata);
            }

            async function getOMSInfo(id) {
              const query = queryString.stringify({
                  data: `[out:json][timeout:25];
                    node(${id/10});
                    out tags;`
                });
              const response = await fetch(`https://overpass-api.de/api/interpreter?${query}`, {
                redirect: 'follow',
                headers: {
                  accept: 'application/json'
                },
              });
              const info = await response.json();
              return info?.elements[0] ? info.elements[0] : null;
            }

            function getWikidataId(tags) {
              if (!tags) return null;
              const regexWikidata = /(\w*:)?wikidata/;
              const key = Object.keys(tags).find(key => key.match(regexWikidata));
              return tags[key] ? tags[key] : null;
            }

            function getWikidataImageHash(name) {
              const imageHash = md5(name);
              return imageHash;
            }

            function getWikidataImagePath(image_name) {
              const name = image_name.replace(/\s+/g, '_');
              const hash = getWikidataImageHash(name);
              return `https://upload.wikimedia.org/wikipedia/commons/${hash.substring(0,1)}/${hash.substring(0,2)}/${name}`;
            }

            async function getWikidata(tags) {
              const id = getWikidataId(tags);
              if (!id) return null;
              const response = await fetch(`https://www.wikidata.org/wiki/Special:EntityData/${id}.json?flavor=simple`);
              const info = await response.json();
              let image;
              if (info.entities[id].claims.P154) {
                image = getWikidataImagePath(info.entities[id].claims.P154[0].mainsnak.datavalue.value);
              }else if (info.entities[id].claims.P18) {
                image = getWikidataImagePath(info.entities[id].claims.P18[0].mainsnak.datavalue.value);
              }

              return image ? {...info.entities[id], ...{image}} : info.entities[id];
            }

            function showPoiInfo(feature, osmInfo, wikidata) {
              const textHtml = [];
              if (wikidata?.image) {
                textHtml.push(`<img src="${wikidata?.image}" />`);
              }
              textHtml.push(`<h1>${feature.properties.name}</h1>`);
              if (feature.properties.class !== feature.properties.subclass) {
                textHtml.push(`<h4>${feature.properties.class} (<small>${feature.properties.subclass}</small>)</h4>`);
              } else {
                textHtml.push(`<h4>${feature.properties.class}</h4>`);
              }
              if (osmInfo && osmInfo?.tags) {
                const {opening_hours, "contact:website": contact_website, website, ...tags } = osmInfo.tags;
                if (contact_website || website) {
                  let web = website ?? contact_website;
                  textHtml.push(`<div><a href="${web}">${web}</a></div>`);
                }
                if (opening_hours) {
                  textHtml.push(`<h3>Opening hours</h3>`);
                  osmInfo?.tags?.opening_hours.split(",").forEach(element => {
                    textHtml.push(`<div>${element.trim()}</div>`);
                  });
                }
                if (tags) {
                  textHtml.push(`<h3>Details</h3>`);
                  textHtml.push(`<div class="details-info">`);
                  Object.keys(tags).forEach(element => {
                    if (element.includes("email")) {
                      textHtml.push(`<div><label>${element}:</label><a href="mailto: ${tags[element]}">${tags[element]}</a></div>`);
                    } else if (element.includes("website")) {
                      textHtml.push(`<div><label>${element}:</label><a href="${tags[element]}">${tags[element]}</a></div>`);
                    } else if (element.includes("wikidata")) {
                      textHtml.push(`<div><label>${element}:</label><a href="https://www.wikidata.org/wiki/${tags[element]}">${tags[element]}</a></div>`);
                    } else if (element.includes("wikipedia")) {
                      const [lang, term] = tags[element].split(":");
                      textHtml.push(`<div><label>${element}:</label><a href="https://${lang}.wikipedia.org/wiki/${term}">${tags[element]}</a></div>`);
                    } else {
                      textHtml.push(`<div><label>${element}:</label>${tags[element]}</div>`);
                    }
                  });
                  textHtml.push(`</div>`);
                }
              }
              document.querySelector(".sidebar-content-info").innerHTML = textHtml.join("");
              showSidebar('left');
            }

            document.querySelector(".sidebar-toggle").addEventListener('click', function() {
              toggleSidebar('left');
            });
    </script>
</body>
</html>
```
