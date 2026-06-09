# Source: https://docs.maptiler.com/sdk-js/examples/custom-style-layer/

# Add a custom style layer

Use a custom style layer to render custom WebGL content.

## Focused Code Snippet
Use this focused code snippet in your application logic to implement this feature:

```javascript
// create a custom style layer to implement the WebGL content
    const highlightLayer = {
        id: 'highlight',
        type: 'custom',

        // method called when the layer is added to the map
        // Search for StyleImageInterface in https://maplibre.org/maplibre-gl-js/docs/API/
        onAdd (map, gl) {
        // create GLSL source for vertex shader
            const vertexSource = `#version 300 es

            uniform mat4 u_matrix;
            in vec2 a_pos;
            void main() {
                gl_Position = u_matrix * vec4(a_pos, 0.0, 1.0);
            }`;

            // create GLSL source for fragment shader
            const fragmentSource = `#version 300 es

            out highp vec4 fragColor;
            void main() {
                fragColor = vec4(1.0, 0.0, 0.0, 0.5);
            }`;

            // create a vertex shader
            const vertexShader = gl.createShader(gl.VERTEX_SHADER);
            gl.shaderSource(vertexShader, vertexSource);
            gl.compileShader(vertexShader);

            // create a fragment shader
            const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
            gl.shaderSource(fragmentShader, fragmentSource);
            gl.compileShader(fragmentShader);

            // link the two shaders into a WebGL program
            this.program = gl.createProgram();
            gl.attachShader(this.program, vertexShader);
            gl.attachShader(this.program, fragmentShader);
            gl.linkProgram(this.program);

            this.aPos = gl.getAttribLocation(this.program, 'a_pos');

            // define vertices of the triangle to be rendered in the custom style layer
            const helsinki = maptilersdk.MercatorCoordinate.fromLngLat({
                lng: 25.004,
                lat: 60.239
            });
            const berlin = maptilersdk.MercatorCoordinate.fromLngLat({
                lng: 13.403,
                lat: 52.562
            });
            const kyiv = maptilersdk.MercatorCoordinate.fromLngLat({
                lng: 30.498,
                lat: 50.541
            });

            // create and initialize a WebGLBuffer to store vertex and color data
            this.buffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, this.buffer);
            gl.bufferData(
                gl.ARRAY_BUFFER,
                new Float32Array([
                    helsinki.x,
                    helsinki.y,
                    berlin.x,
                    berlin.y,
                    kyiv.x,
                    kyiv.y
                ]),
                gl.STATIC_DRAW
            );
        },

        // method fired on each animation frame
        render (gl, args) {
            gl.useProgram(this.program);
            gl.uniformMatrix4fv(
                gl.getUniformLocation(this.program, 'u_matrix'),
                false,
                args.defaultProjectionData.mainMatrix
            );
            gl.bindBuffer(gl.ARRAY_BUFFER, this.buffer);
            gl.enableVertexAttribArray(this.aPos);
            gl.vertexAttribPointer(this.aPos, 2, gl.FLOAT, false, 0, 0);
            gl.enable(gl.BLEND);
            gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 3);
        }
    };

    // add the custom style layer to the map
    map.on('load', () => {
        map.addLayer(highlightLayer, 'Building');
    });
```

## Runnable HTML Template
Below is the complete, runnable HTML file with all dependencies resolved. Use it as a clean template for your project:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add a custom style layer</title>
    <script src="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.umd.min.js"></script>
    <link href="https://cdn.maptiler.com/maptiler-sdk-js/v4.0.2/maptiler-sdk.css" rel="stylesheet" />
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
            center: [7.5, 58],
            zoom: 3
        });

        // create a custom style layer to implement the WebGL content
            const highlightLayer = {
                id: 'highlight',
                type: 'custom',

                // method called when the layer is added to the map
                // Search for StyleImageInterface in https://maplibre.org/maplibre-gl-js/docs/API/
                onAdd (map, gl) {
                // create GLSL source for vertex shader
                    const vertexSource = `#version 300 es

                    uniform mat4 u_matrix;
                    in vec2 a_pos;
                    void main() {
                        gl_Position = u_matrix * vec4(a_pos, 0.0, 1.0);
                    }`;

                    // create GLSL source for fragment shader
                    const fragmentSource = `#version 300 es

                    out highp vec4 fragColor;
                    void main() {
                        fragColor = vec4(1.0, 0.0, 0.0, 0.5);
                    }`;

                    // create a vertex shader
                    const vertexShader = gl.createShader(gl.VERTEX_SHADER);
                    gl.shaderSource(vertexShader, vertexSource);
                    gl.compileShader(vertexShader);

                    // create a fragment shader
                    const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
                    gl.shaderSource(fragmentShader, fragmentSource);
                    gl.compileShader(fragmentShader);

                    // link the two shaders into a WebGL program
                    this.program = gl.createProgram();
                    gl.attachShader(this.program, vertexShader);
                    gl.attachShader(this.program, fragmentShader);
                    gl.linkProgram(this.program);

                    this.aPos = gl.getAttribLocation(this.program, 'a_pos');

                    // define vertices of the triangle to be rendered in the custom style layer
                    const helsinki = maptilersdk.MercatorCoordinate.fromLngLat({
                        lng: 25.004,
                        lat: 60.239
                    });
                    const berlin = maptilersdk.MercatorCoordinate.fromLngLat({
                        lng: 13.403,
                        lat: 52.562
                    });
                    const kyiv = maptilersdk.MercatorCoordinate.fromLngLat({
                        lng: 30.498,
                        lat: 50.541
                    });

                    // create and initialize a WebGLBuffer to store vertex and color data
                    this.buffer = gl.createBuffer();
                    gl.bindBuffer(gl.ARRAY_BUFFER, this.buffer);
                    gl.bufferData(
                        gl.ARRAY_BUFFER,
                        new Float32Array([
                            helsinki.x,
                            helsinki.y,
                            berlin.x,
                            berlin.y,
                            kyiv.x,
                            kyiv.y
                        ]),
                        gl.STATIC_DRAW
                    );
                },

                // method fired on each animation frame
                render (gl, args) {
                    gl.useProgram(this.program);
                    gl.uniformMatrix4fv(
                        gl.getUniformLocation(this.program, 'u_matrix'),
                        false,
                        args.defaultProjectionData.mainMatrix
                    );
                    gl.bindBuffer(gl.ARRAY_BUFFER, this.buffer);
                    gl.enableVertexAttribArray(this.aPos);
                    gl.vertexAttribPointer(this.aPos, 2, gl.FLOAT, false, 0, 0);
                    gl.enable(gl.BLEND);
                    gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
                    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 3);
                }
            };

            // add the custom style layer to the map
            map.on('load', () => {
                map.addLayer(highlightLayer, 'Building');
            });
    </script>
</body>
</html>
```
