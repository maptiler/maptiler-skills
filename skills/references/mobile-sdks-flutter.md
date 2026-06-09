# Source: https://docs.maptiler.com/flutter/maplibre-gl-js/get-started/

# 

<div class="mobile-viewer">
  <iframe style="height: 100%; width: 100%" src="?key=" scrolling="no"></iframe>
  <div class="mobile-case"></div>
</div>

In this tutorial, you’ll learn how to display a map on a mobile device using Flutter and MapLibre GL JS. Together, we will make a simple mobile fullscreen map application as an example of how to use MapTiler maps together with Flutter and MapLibre GL JS for your native app.

We have made this app using the [VS Code Flutter extension](https://docs.flutter.dev/get-started/editor?tab=vscode){:target="\_blank" rel="noopener"} and the plugin
[flutter-maplibre-gl](https://github.com/maplibre/flutter-maplibre-gl/tree/main){:target="\_blank" rel="noopener"}.

## Installation and setting up

1. [Install Flutter](https://docs.flutter.dev/get-started/install)

1. Clone the [Get started with Flutter and MapLibre GL JS](https://github.com/maptiler/get-started-flutter-maplibre-gl-js){:target="\_blank" rel="noopener"} repo

   ```sh
     git clone https://github.com/maptiler/get-started-flutter-maplibre-gl-js.git my-flutter-map
   ```

1. Navigate to the newly created project folder **my-flutter-map**

   ```sh
     cd my-flutter-map
   ```

1. Install dependencies

   ```sh
     flutter pub get
   ```

1. Open the `lib/map.dart` file. 
   <pre class="line-numbers" data-line="4"><code class="language-dart"><!--
     import 'package:flutter/material.dart';
     import 'package:maplibre_gl/maplibre_gl.dart';
   
     const apiKey = "YOUR_MAPTILER_API_KEY_HERE";
     const styleUrl = "https://api.maptiler.com/maps/streets-v4/style.json";
   
     class MapPage extends StatelessWidget {
       const MapPage({super.key});
   
       @override
       Widget build(BuildContext context) {
         return const Map();
       }
     }
   
     class Map extends StatefulWidget {
       const Map({super.key});
   
       @override
       State createState() => MapState();
     }
   
     class MapState extends State<Map> {
       @override
       Widget build(BuildContext context) {
         return Scaffold(
           body: MaplibreMap(
             styleString: "$styleUrl?key=$apiKey",
             myLocationEnabled: true,
             initialCameraPosition: const CameraPosition(target: LatLng(0.0, 0.0)),
             trackCameraPosition: true,
           ),
         );
       }
     }
   --></code></pre>

1. Build your project

   ```sh
     flutter run
   ```

1. You will find your app on your virtual device (Emulator) or physical device.

## Learn more

Here are a few resources to get you started if this is your first Flutter project:

- [Install Flutter](https://docs.flutter.dev/get-started/install)
- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

For help with [Flutter MapLibre](https://github.com/maplibre/flutter-maplibre-gl/) view the online documentation.
