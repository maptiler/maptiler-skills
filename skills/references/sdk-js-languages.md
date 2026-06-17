# Source: https://docs.maptiler.com/sdk-js/api/languages/

#  

<p id="github-link">
  <span>
  
  <a class="text-secondary mb-2" href="https://github.com/maptiler/maptiler-sdk-js/blob/main/src/language.ts" target="_blank"
  rel="noopener noreferrer"> src/language.ts</a>
  </span>
</p>

The MapTiler SDK JS has a built-in list of compatible languages, which can be used as shorthand for the [ISO language codes](https://en.wikipedia.org/wiki/ISO_639-1) used to define the language of the map labels. The language generally depends on the map's style.

The MapTiler SDK JS also provides seamless support for **right-to-left languages**. Arabic, Hebrew, and other right-to-left languages are fully supported by default. No extra plugins are needed.

Check out the [complete list of supported languages](https://github.com/maptiler/maptiler-client-js/blob/main/src/language.ts). In addition to the built-in ISO languages, there are these special cases for supported languages:

- `Language.AUTO`: uses the default language of the browser
- `Language.LATIN`: uses the default fallback language in the Latin charset
- `Language.LOCAL`: uses the local language for each country
- `Language.NON_LATIN`: uses the default fallback language in the non-Latin charset
- `Language.STYLE`: uses the language defined by the style

  > [!WARNING]
  > `Language.STYLE` is the default state. Once you switch the language from `STYLE`, you **cannot switch it back**.

- `Language.STYLE_LOCK`: keep the language from the style and prevent any further updates

  > [!WARNING]
  > `Language.STYLE_LOCK` should **only** be used in the **constructor**.

- `Language.VISITOR`: uses the preferred language from the user settings and the "default name". This mode is useful when a user needs to access both local names and English names, for example, when traveling abroad where signs are likely to be available only in the local language.
- `Language.VISITOR_ENGLISH`: uses English and the "default name". This mode is useful when a user needs to access both local names and English names, for example, when traveling abroad where signs are likely to be available only in the local language.

> [!INFO]
> The "default name" is equivalent to OSM's `{name}`, which is either the most globally recognized name or the local name.

## Related examples

- [How to change the default map labels language](/sdk-js/examples/language-map/)
- [How to change the map labels language based on visitor's location](/sdk-js/examples/ip-map-language/)
- [Change a map's language](/sdk-js/examples/language-switch/)
- [Display and style rich text labels](/sdk-js/examples/display-and-style-rich-text-labels/)
