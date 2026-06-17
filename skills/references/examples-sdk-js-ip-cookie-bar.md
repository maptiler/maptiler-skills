# Source: https://docs.maptiler.com/sdk-js/examples/ip-cookie-bar/

# Display the cookies bar according to the visitor's location

In this tutorial, we will demonstrate the process of presenting the cookies consent bar based on the location of the visitor. This can be achieved by utilizing the [MapTiler Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"}.

By following the steps outlined in this tutorial, you will be able to implement a solution that dynamically displays the cookie's consent bar according to the visitor's specific location. The MapTiler Geolocation API provides the necessary functionality to determine the visitor's location accurately, allowing you to tailor the display of the cookies consent bar accordingly. By incorporating this feature into your website, you can ensure compliance with relevant regulations and enhance the user experience for visitors from different locations.

<div class="tab-common-content" markdown="1">

1. Call [MapTiler's Geolocation API](https://docs.maptiler.com/cloud/api/geolocation/){:target="_blank" rel="noopener"} to get information about the visitor's location based on the IP address.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="24-27"><code class="language-js"><!--

(async () => {

const result = await maptilersdk.geolocation.info();

})();

--></code></pre>

1. Get the user's location country code.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="26"><code class="language-js"><!--

(async () => {

const result = await maptilersdk.geolocation.info();

const {country_code} = result;

})();

--></code></pre>

1. Include the cookie consent bar JavaScript and CSS files in the `<head>` of your HTML file. To display the cookie consent bar, we will use a third-party library (you can use any library you like or implement your own). In the example, we are using [Osano Cookie Consent](https://www.osano.com/cookieconsent){:target="_blank" rel="noopener"}.

<pre><code class="language-html"><!--

<script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js"></script>

<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css" />

--></code></pre>

1. Initialize the cookie consent bar using the user's country code.

<pre class="line-numbers" data-start="24" data-line-offset="23" data-line="27-46"><code class="language-js"><!--

(async () => {

const result = await maptilersdk.geolocation.info();

const {country_code} = result;

window.cookieconsent.initialise({

cookie: {

domain: "YOUR_DOMAIN"

},

palette:{

popup: {background: "#EFF3FB", text:"#333359", link: "#3170FE"},

button: {background: "#3170FE"},

},

theme: "classic",

type: "opt-out",

revokable:true,

content: {

href: "https://YOUR_DOMAIN/privacy-policy/"

},

law: {

regionalLaw: false,

countryCode: country_code

},

legal: country_code

});

})();

--></code></pre>

</div>

<div class="tab-content cdn-steps" markdown="1">

</div>

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
container: 'map', // container's id or the HTML element to render the map
      style: maptilersdk.MapStyle.STREETS,
      center: [151.21395, -33.86828], // starting position [lng, lat]
      zoom: 12.18, // starting zoom
    });
    (async () => {
      const result = await maptilersdk.geolocation.info();
      let {country_code} = result;
      country_code = 'ES';
      window.cookieconsent.initialise({
        cookie: {
          domain: "www.maptiler.com"
        },
        palette:{
          popup: {background: "#EFF3FB", text:"#333359", link: "#3170FE"},
          button: {background: "#3170FE"},
        },
        theme: "classic",
        type: "opt-out",
        revokable:true,
        content: {
          href: "https://www.maptiler.com/privacy-policy/"
        },
        law: {
          regionalLaw: false,
          countryCode: country_code
        },
        legal: country_code
      });
    })();
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Display the cookies bar according to the visitor's location</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/cookieconsent@3/build/cookieconsent.min.css" rel="stylesheet" />
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
            center: [151.21395, -33.86828],
            zoom: 12.18
        });

        container: 'map', // container's id or the HTML element to render the map
              style: maptilersdk.MapStyle.STREETS,
              center: [151.21395, -33.86828], // starting position [lng, lat]
              zoom: 12.18, // starting zoom
            });
            (async () => {
              const result = await maptilersdk.geolocation.info();
              let {country_code} = result;
              country_code = 'ES';
              window.cookieconsent.initialise({
                cookie: {
                  domain: "www.maptiler.com"
                },
                palette:{
                  popup: {background: "#EFF3FB", text:"#333359", link: "#3170FE"},
                  button: {background: "#3170FE"},
                },
                theme: "classic",
                type: "opt-out",
                revokable:true,
                content: {
                  href: "https://www.maptiler.com/privacy-policy/"
                },
                law: {
                  regionalLaw: false,
                  countryCode: country_code
                },
                legal: country_code
              });
            })();
    </script>
</body>
</html>
```
