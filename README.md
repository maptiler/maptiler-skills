<img src="./images/maptiler-logo.png" alt="Company Logo" height="32"/>

# MapTiler — Agent Skill

Expert coding skill for building location-aware applications across the full MapTiler platform. It gives AI coding agents the context to generate correct, production-ready code using MapTiler Cloud APIs, the MapTiler SDK, MapTiler GeoSplats SDK
mobile SDKs, and on-premise tools.

Built on the Agent Skills open standard, so the same skill works across Claude Code, Gemini CLI, Cursor, Windsurf, and other compatible AI agents.

---

🌐 [Website](https://www.maptiler.com/) &nbsp; 🔑 [Get API Key](https://cloud.maptiler.com/account/keys/)

---

<br>

<details> <summary><b>Table of Contents</b></summary>
<ul>
<li><a href="#what-it-does">What it does</a></li>
<li><a href="#how-skills-plugins-and-agents-fit-together">How skills, plugins, and agents fit together</a></li>
<li><a href="#-installation">Installation</a></li>
<li><a href="#-repository-layout">Repository layout</a></li>
<li><a href="#-platform-coverage--file-prefix-conventions">Platform Coverage & File Prefix Conventions</a></li>
<li><a href="#-prerequisites">Prerequisites</a></li>
<li><a href="#links">Links</a></li>
<li><a href="#-support">Support</a></li>
<li><a href="#-contributing">Contributing</a></li>
<li><a href="#-license">License</a></li>
</ul>
</details>

## What it does

A skill is on-demand expertise: the agent loads it only when your request matches the skill's description, then follows its instructions instead of guessing. When you ask for maps, geocoding, weather, elevation, vector tiles, or any geospatial feature, this skill makes the agent:

- **Generate platform-correct code** for web (MapTiler SDK JS, Leaflet, OpenLayers), frameworks (React, Svelte, Vue, Angular, Cesium, deck.gl), mobile (iOS Swift, Android Kotlin, Flutter, React Native), and on-premise (MapTiler Server, MapTiler Engine).
- **Call the right Cloud REST API** (geocoding, weather, static maps, elevation, tiles, coordinates, IP geolocation, admin/tilesets) with correct endpoints and auth patterns.
- **Apply modern v4 styles automatically**, upgrading deprecated `*-v2` / `*-v3` style IDs wherever they appear.
- **Use pinned, current versions** for every SDK, CDN script, and dependency, with no unresolved template placeholders.
- **Cross-reference vector tile schemas** (Planet v4, Buildings, Contours, Outdoor, Ocean, Landcover, Landform, Cadastre) before inventing source-layer names, paint expressions, or filter keys.
- **Handle framework lifecycle correctly** — WebGL cleanup, stale-closure prevention in React, isolated reactivity, ES module vs UMD CDN selection.

## How skills, plugins, and agents fit together

It helps to keep three layers separate, because the install steps below differ by layer:

1.  **The skill** is the portable content: a `SKILL.md` plus a `references/` folder. This is what every agent actually reads, and it's identical across tools.
2.  **The plugin** is a Claude Code–specific wrapper for distributing the skill through a marketplace. Other tools don't use it.
3.  **The agent** (Claude Code, Gemini CLI, Cursor, Windsurf…) is the tool that loads the skill from its own skills directory.

So there are three ways to install: with the [Skills CLI](https://github.com/vercel-labs/skills) (`npx skills add`, auto-detects your agent and works across dozens of them), through the Claude Code plugin marketplace (Claude Code only), or by copying the skill folder into any agent's skills directory (works everywhere).

What triggers a skill is the same in every tool: the description field in the `SKILL.md` frontmatter. The agent matches your request against that description to decide whether to activate the skill, so installation alone isn't enough — the skill also has to be registered and triggered.

<br>

## 📦 Installation

### Universal — via Skills CLI

Works with Claude Code, Gemini CLI, Cursor, Windsurf, and dozens of other agents. The [Skills CLI](https://github.com/vercel-labs/skills) auto-detects which agents you have installed and sets the skill up for each one, so you don't need to know the target directory yourself:

```bash
npx skills add maptiler/maptiler-skills
```
### Claude Code — as a plugin

Add the marketplace, install the plugin, then reload so the skill registers:

```bash
/plugin marketplace add maptiler/maptiler-skills
/plugin install maptiler@maptiler-skills
/reload-plugins
```

### Gemini CLI

Install straight from the repository with a single command:

#### Windows (PowerShell)

```powershell
git clone https://github.com/maptiler/maptiler-skills.git; mkdir "$HOME\.gemini\skills\maptiler" -Force; cp -Recurse maptiler-skills\skills\* "$HOME\.gemini\skills\maptiler\"; rm -Recurse -Force maptiler-skills
```

#### Linux & macOS (bash)

```bash
git clone https://github.com/maptiler/maptiler-skills.git && mkdir -p ~/.gemini/skills/maptiler && cp -r maptiler-skills/skills/* ~/.gemini/skills/maptiler/ && rm -rf maptiler-skills
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

Any tool that supports the Agent Skills standard can use this skill. The [Skills CLI](https://github.com/vercel-labs/skills) above already knows the skills directory for dozens of agents, so try `npx skills add maptiler/maptiler-skills` first. Otherwise, place the `maptiler` folder (containing `SKILL.md` and `references/`) wherever that agent looks for skill definitions.

<br>

---

<br>

## 📘 Repository layout

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

<br>

## 💡 Platform Coverage & File Prefix Conventions

To avoid cross-platform contamination when searching, use these filename prefix filters in the `references/` directory:

| Target Platform                                                | File Name Prefix                                                                                     |
| :------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Web** (Core JS SDK)                                          | `sdk-js-*`, `examples-sdk-js-*`                                                                      |
| **Web Frameworks** (React, Svelte, Vue, Angular)               | `web-libraries-*`, `examples-react-*`, `examples-svelte-*`, `examples-vuejs-*`, `examples-angular-*` |
| **Web Mapping Engines** (Leaflet, OpenLayers, Cesium, deck.gl) | `examples-leaflet-*`, `examples-openlayers-*`, `examples-cesium-*`, `web-libraries-deck-gl*`         |
| **Android** (Kotlin/Java)                                      | `mobile-sdks-android-*`, `examples-android-*`                                                        |
| **iOS** (Swift)                                                | `mobile-sdks-ios-*`, `examples-ios-*`                                                                |
| **Cross-Platform Mobile** (Flutter, React Native)              | `mobile-sdks-flutter-*`, `mobile-sdks-react-native-*`                                                |
| **Cloud REST APIs**                                            | `cloud-api-*`, `cloud-admin-api-*`                                                                   |
| **On-Premise Infrastructure**                                  | `on-prem-*`                                                                                          |
| **Vector Tile Schemas**                                        | `map-resources-schemas-*`                                                                            |
| **MapLibre Style Spec**                                        | `map-resources-specifications-*`                                                                     |

<br>

---

<br>

## 🚀 Prerequisites

- A MapTiler API key from [cloud.maptiler.com](https://cloud.maptiler.com).

<br>

## Links

- [MapTiler Cloud Console](https://cloud.maptiler.com)
- MapTiler SDK JS · [Docs](https://docs.maptiler.com/sdk-js/) · [GitHub](https://github.com/maptiler/maptiler-sdk-js) · [NPM](https://www.npmjs.com/package/@maptiler/sdk)
- [MapTiler GeoSplats SDK](https://docs.maptiler.com/geosplats-sdk/)
- [MapTiler iOS SDK](https://docs.maptiler.com/mobile-sdk/ios/)
- [Android SDK](https://docs.maptiler.com/mobile-sdk/android/)
- [MapTiler Server](https://docs.maptiler.com/guides/on-prem/server/)
- [MapTiler Engine](https://docs.maptiler.com/guides/on-prem/engine/)

---

<br>

## 💬 Support

- 📚 [Documentation](https://docs.maptiler.com/) - Comprehensive guides and API reference
- ✉️ [Contact us](https://maptiler.com/contact) - Get in touch or submit a request
- 🐦 [Twitter/X](https://twitter.com/maptiler) - Follow us for updates

<br>

---

<br>

## 🤝 Contributing

We love contributions from the community! Whether it's bug reports, feature requests, or pull requests, all contributions are welcome:

- Fork the repository and create your branch from `main`
- If you've added code, add tests that cover your changes
- Ensure your code follows our style guidelines
- Give your pull request a clear, descriptive summary
- Open a Pull Request with a comprehensive description

<br>

## 📄 License

This project is licensed under the MIT – see the [LICENSE](./LICENSE.md) file for details.

<br>

<p align="center" style="margin-top:20px;margin-bottom:20px;"> <a href="https://cloud.maptiler.com/account/keys/" style="display:inline-block;padding:12px 32px;background:#F2F6FF;color:#000;font-weight:bold;border-radius:6px;text-decoration:none;"> Get Your API Key <sup style="background-color:#0000ff;color:#fff;padding:2px 6px;font-size:12px;border-radius:3px;">FREE</sup><br /> <span style="font-size:90%;font-weight:400;">Start building with 100,000 free map loads per month ・ No credit card required.</span> </a> </p>

<br>

<p align="center"> 💜 Made with love by the <a href="https://www.maptiler.com/">MapTiler</a> team <br />
<p align="center">
  <a href="https://www.maptiler.com/">Website</a> •
  <a href="https://docs.maptiler.com/">Documentation</a> •
  <a href="https://github.com/maptiler/maptiler-skills">GitHub</a>
</p>
