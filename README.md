# MapTiler — Agent Skill

Expert coding skill for building location-aware applications across the full MapTiler platform. It gives AI coding agents the context to generate correct, production-ready code using MapTiler Cloud APIs, the MapTiler SDK, MapTiler GeoSplats SDK
mobile SDKs, and on-premise tools.

Built on the Agent Skills open standard, so the same skill works across Claude Code, Gemini CLI, Cursor, Windsurf, and other compatible AI agents.

## What it does

A skill is on-demand expertise: the agent loads it only when your request matches the skill's description, then follows its instructions instead of guessing. When you ask for maps, geocoding, weather, elevation, vector tiles, or any geospatial feature, this skill makes the agent:

*   **Generate platform-correct code** for web (MapTiler SDK JS, Leaflet, OpenLayers), frameworks (React, Svelte, Vue, Angular, Cesium, deck.gl), mobile (iOS Swift, Android Kotlin, Flutter, React Native), and on-premise (MapTiler Server, MapTiler Engine).
*   **Call the right Cloud REST API** (geocoding, weather, static maps, elevation, tiles, coordinates, IP geolocation, admin/tilesets) with correct endpoints and auth patterns.
*   **Apply modern v4 styles automatically**, upgrading deprecated `*-v2` / `*-v3` style IDs wherever they appear.
*   **Use pinned, current versions** for every SDK, CDN script, and dependency, with no unresolved template placeholders.
*   **Cross-reference vector tile schemas** (Planet v4, Buildings, Contours, Outdoor, Ocean, Landcover, Landform, Cadastre) before inventing source-layer names, paint expressions, or filter keys.
*   **Handle framework lifecycle correctly** — WebGL cleanup, stale-closure prevention in React, isolated reactivity, ES module vs UMD CDN selection.

## How skills, plugins, and agents fit together

It helps to keep three layers separate, because the install steps below differ by layer:

1.  **The skill** is the portable content: a `SKILL.md` plus a `references/` folder. This is what every agent actually reads, and it's identical across tools.
2.  **The plugin** is a Claude Code–specific wrapper for distributing the skill through a marketplace. Other tools don't use it.
3.  **The agent** (Claude Code, Gemini CLI, Cursor, Windsurf…) is the tool that loads the skill from its own skills directory.

So there are two ways to install: through the Claude Code plugin marketplace (Claude Code only), or by copying the skill folder into any agent's skills directory (works everywhere).

What triggers a skill is the same in every tool: the description field in the `SKILL.md` frontmatter. The agent matches your request against that description to decide whether to activate the skill, so installation alone isn't enough — the skill also has to be registered and triggered.

## Installation

### Claude Code — as a plugin

Add the marketplace, install the plugin, then reload so the skill registers:

```bash
/plugin marketplace add maptiler/agent-skills
/plugin install maptiler@agent-skills
/reload-plugins
```



### Gemini CLI

Install straight from the repository with a single command:

#### Windows (PowerShell)

```powershell
git clone https://github.com/maptiler/agent-skills.git; mkdir "$HOME\.gemini\skills\maptiler" -Force; cp -Recurse agent-skills\skills\* "$HOME\.gemini\skills\maptiler\"; rm -Recurse -Force agent-skills
```

#### Linux & macOS (bash)

```bash
git clone https://github.com/maptiler/agent-skills.git && mkdir -p ~/.gemini/skills/maptiler && cp -r agent-skills/skills/* ~/.gemini/skills/maptiler/ && rm -rf agent-skills
```

Or copy it in manually:

```bash
# Global (every project)
cp -r skills/maptiler ~/.gemini/skills/

# Project (run /trust in the session afterward, then restart)
mkdir -p .gemini/skills && cp -r skills/maptiler .gemini/skills/
```

### Cursor

Project-scoped only. Copy the skill folder into the project's skills directory:

```bash
mkdir -p .cursor/skills && cp -r skills/maptiler .cursor/skills/
```

### Windsurf

Project-scoped, read by the Cascade agent. Copy the skill folder in:

```bash
mkdir -p .windsurf/skills && cp -r skills/maptiler .windsurf/skills/
```

> [!NOTE]
> Claude Code–specific frontmatter fields (such as `allowed-tools`) are ignored by Windsurf without causing errors.

### Other agents

Any tool that supports the Agent Skills standard can use this skill. Place the `maptiler` folder (containing `SKILL.md` and `references/`) wherever that agent looks for skill definitions.

---

## Repository layout

```
.claude-plugin/
  marketplace.json    — Claude Code marketplace manifest
  plugin.json         — Claude Code plugin manifest
skills/
  maptiler/
    SKILL.md          — Skill entry point (always loaded when triggered)
    references/
      INDEX.md                          — Curated catalog of high-value docs
      versions.md                       — Pinned versions of every library & dependency
      cloud-api-*.md                    — Cloud REST APIs (geocoding, weather, static, …)
      cloud-admin-api-*.md              — Admin API (tilesets, uploads, analytics, keys)
      sdk-js-*.md                       — MapTiler SDK JS core
      web-libraries-*.md                — React, Vue, Svelte, Angular, Leaflet, OL, Cesium, deck.gl
      mobile-sdks-*.md                  — iOS, Android, Flutter, React Native
      on-prem-*.md                      — Self-hosted Server & Tile Engine CLI
      map-resources-schemas-*.md        — Vector tile schemas (Planet v4, Buildings, …)
      map-resources-specifications-*.md — MapLibre style spec (layers, sources, expressions)
      examples-*.md                     — Runnable per-platform examples
      complex-dds-expressions-guide.md  — Data-driven styling deep dive
README.md             — This file
```

For the Claude Code plugin to expose the skill, `SKILL.md` must live at `skills/maptiler/SKILL.md` — not at the repository root, and not inside `.claude-plugin/`. Only the manifests go in `.claude-plugin/`.

---

## Platform Coverage & File Prefix Conventions

To avoid cross-platform contamination when searching, use these filename prefix filters in the `references/` directory:

| Target Platform | File Name Prefix |
| :--- | :--- |
| **Web** (Core JS SDK) | `sdk-js-*`, `examples-sdk-js-*` |
| **Web Frameworks** (React, Svelte, Vue, Angular) | `web-libraries-*`, `examples-react-*`, `examples-svelte-*`, `examples-vuejs-*`, `examples-angular-*` |
| **Web Mapping Engines** (Leaflet, OpenLayers, Cesium, deck.gl) | `examples-leaflet-*`, `examples-openlayers-*`, `examples-cesium-*`, `web-libraries-deck-gl*` |
| **Android** (Kotlin/Java) | `mobile-sdks-android-*`, `examples-android-*` |
| **iOS** (Swift) | `mobile-sdks-ios-*`, `examples-ios-*` |
| **Cross-Platform Mobile** (Flutter, React Native) | `mobile-sdks-flutter-*`, `mobile-sdks-react-native-*` |
| **Cloud REST APIs** | `cloud-api-*`, `cloud-admin-api-*` |
| **On-Premise Infrastructure** | `on-prem-*` |
| **Vector Tile Schemas** | `map-resources-schemas-*` |
| **MapLibre Style Spec** | `map-resources-specifications-*` |

---

## Prerequisites

*   A MapTiler API key from [cloud.maptiler.com](https://cloud.maptiler.com).

## Links

*   [MapTiler Cloud Console](https://cloud.maptiler.com)
*   MapTiler SDK JS · [Docs](https://docs.maptiler.com/sdk-js/) · [GitHub](https://github.com/maptiler/maptiler-sdk-js) · [NPM](https://www.npmjs.com/package/@maptiler/sdk)
*   [MapTiler GeoSplats SDK](https://docs.maptiler.com/geosplats-sdk/)
*   [MapTiler iOS SDK](https://docs.maptiler.com/mobile-sdk/ios/)
*   [Android SDK](https://docs.maptiler.com/mobile-sdk/android/)
*   [MapTiler Server](https://docs.maptiler.com/guides/on-prem/server/)
*   [MapTiler Engine](https://docs.maptiler.com/guides/on-prem/engine/)

---

## License

MIT

