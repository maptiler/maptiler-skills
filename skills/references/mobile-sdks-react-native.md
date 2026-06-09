# Source: https://docs.maptiler.com/react-native/maplibre-gl-js/get-started/

# 

<div class="mobile-viewer">
  <iframe style="height: 100%; width: 100%" src="?key=" scrolling="no"></iframe>
  <div class="mobile-case"></div>
</div>

In this tutorial, you’ll learn how to display a map on a mobile device using React Native and MapLibre GL JS. Together, we will make a simple mobile fullscreen map application as an example of how to use MapTiler maps together with React Native and MapLibre GL JS for your native app.

We have made this app using the [expo-dev-client](https://docs.expo.dev/development/getting-started/#installing--expo-dev-client--in-your-project){:target="\_blank" rel="noopener"} and the plugin
[MapLibre React Native](https://maplibre.org/maplibre-react-native/){:target="\_blank" rel="noopener"}.

## Installation and setting up

1. Clone the [Get started with React Native and MapLibre GL JS](https://github.com/maptiler/get-started-react-native-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

```sh
  git clone https://github.com/maptiler/get-started-react-native-maplibre-gl-js.git my-react-map
```

1. Navigate to the newly created project folder **my-react-map**

```sh
  cd my-react-map
```

1. Install dependencies

```sh
  npm install
```

1. Open the `App.js` file. 
   
   <pre class="line-numbers" data-start="6" data-line-offset="5" data-line="10"><code class="language-js"><!--
     export default function App() {
       MapLibreGL.setWellKnownTileServer(MapLibreGL.TileServers.MapLibre);
       MapLibreGL.setAccessToken(null);
   
       const MAPTILER_API_KEY = "YOUR_MAPTILER_API_KEY_HERE";
   
       return (
         <View style={styles.page}>
           <View style={styles.container}>
             <MapLibreGL.MapView
               style={styles.map}
               styleURL={`https://api.maptiler.com/maps/streets-v4/style.json?key=${MAPTILER_API_KEY}`}
               logoEnabled={false}
               attributionPosition=>
               <MapLibreGL.Camera
                 defaultSettings=
               />
             </MapLibreGL.MapView>
           </View>
         </View>
       );
     }
   --></code></pre>

   

1. Build your project

   **Android**

   ```sh
     # Build your native Android project
     npx expo run:android
   ```

   **iOS**

   ```sh
     # Build your native iOS project
     npx expo run:ios
   ```

   > [!WARNING]
   > - `expo run:ios` requires Xcode (macOS only) installed on your computer. See the [setup guide](https://reactnative.dev/docs/environment-setup).
   > - `expo run:android` requires Android Studio and the Android SDK to be installed. See the [setup guide](https://reactnative.dev/docs/environment-setup).

1. You will find your app on your virtual device (Emulator) or physical device.

## Learn more

- [Expo Development builds](https://docs.expo.dev/development/getting-started/#installing--expo-dev-client--in-your-project){:target="\_blank" rel="noopener"}
- [Adding custom native code](https://docs.expo.dev/workflow/customizing/#generate-native-projects-with-prebuild){:target="\_blank" rel="noopener"}
- [MapLibre React Native documentation](https://maplibre.org/maplibre-react-native/docs/setup/getting-started){:target="\_blank" rel="noopener"}
