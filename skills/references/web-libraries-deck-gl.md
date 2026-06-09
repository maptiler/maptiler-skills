# Source: https://docs.maptiler.com/deck-gl/index/

# 

[Deck.gl](https://deck.gl/) is a framework powered by WebGL for visual exploratory data analysis of large datasets.

Within Deck.gl, you have the option to incorporate MapTiler SDK either in interleaved mode (rendering directly into MapTiler SDK WebGL context) or reverse-controlled mode (renders deck.gl above the MapTiler SDK container and blocks any interaction to the base map).

Deck.gl is **not a map library**. Instead, it is a high-performance data visualization framework designed to works standalone without a base map. Deck.gl integrates with mapping libraries such as MapTiler SDK, MapLibre, etc.

## Get started

This is the easiest and fastest way to use your MapTiler maps in Deck.gl in interleaved mode. For reverse-controlled mode see: [How to use Vector Tiles in Deck.gl](./examples/get-started/)

Deck.gl allows a great diversification of visualizations. Like the one shown in the following example, where the `ArcLayer` is used to represent raised arc linking source and destination coordinate pair and `ScatterplotLayer` is used to show affected area. Simply use the code below the map.

<iframe style="height: 400px; width: 100%" src="?key="></iframe>



<div class="tab-content cdn-steps">
<pre data-src="/deck-gl/examples/interleaved/code1/index.html"></pre>
</div>

<div class="tab-content bundler-steps">
  <div class="my-1">
    <pre data-src="/deck-gl/examples/interleaved/npm/install.sh"></pre>
  </div>

  <div class='border rounded-3 my-1 accordion-item' id='main-code' aria-expanded='true'>
    <div class='bg-lighter rounded-3'>
      <a role='button' data-bs-toggle='collapse' data-bs-target='#main-js' aria-expanded='true' aria-controls='main-js'>
        <div class="d-flex justify-content-between align-items-center px-2 py-1">
          <div class="h6 m-0 text-secondary">main.js</div>
          <span class="collapse-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use>
            </svg>
          </span>
        </div>
      </a>
    </div>
    <div id='main-js' aria-labelledby='main-js' data-parent='#accordion'>
      <div class='card-body px-1'>
        <pre data-src="/deck-gl/examples/interleaved/npm/main.js"></pre>
      </div>
    </div>
  </div>

  <div class='border rounded-3 my-1 accordion-item' id='index-code' aria-expanded='false'>
    <div class='bg-lighter rounded-3'>
      <a role='button' data-bs-toggle='collapse' data-bs-target='#index-html' aria-expanded='false' aria-controls='index-html' class='collapsed'>
        <div class="d-flex justify-content-between align-items-center px-2 py-1">
          <div class="h6 m-0 text-secondary">index.html</div>
          <span class="collapse-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use>
            </svg>
          </span>
        </div>
      </a>
    </div>
    <div id='index-html' class='collapse' aria-labelledby='index-html' data-parent='#accordion'>
      <div class='card-body px-1'>
        <pre data-src="/deck-gl/examples/interleaved/npm/index.html"></pre>
      </div>
    </div>
  </div>
  
  <div class='border rounded-3 my-1 accordion-item' id='style-code' aria-expanded='false'>
    <div class='bg-lighter rounded-3'>
      <a role='button' data-bs-toggle='collapse' data-bs-target='#style-css' aria-expanded='false' aria-controls='style-css' class='collapsed'>
        <div class="d-flex justify-content-between align-items-center px-2 py-1">
          <div class="h6 m-0 text-secondary">style.css</div>
          <span class="collapse-arrow">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <use href="/styles/style/icon/icon.svg#keyboard_arrow_down"></use>
            </svg>
          </span>
        </div>
      </a>
    </div>
    <div id='style-css' class='collapse' aria-labelledby='style-css' data-parent='#accordion'>
      <div class='card-body px-1'>
        <pre data-src="/deck-gl/examples/interleaved/npm/style.css"></pre>
      </div>
    </div>
  </div>
</div>
