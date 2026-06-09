# MapTiler Data-Driven Styling (DDS) Expressions

This cookbook contains production-ready MapTiler GL Style Spec expressions for advanced styling, category matching, zoom-dependent interpolation, and logical operations.

---

## 1. Zoom-Dependent Interpolation

Interpolation dynamically scales values (like line width or circle size) as the map zooms. This prevents visual clutter at low zooms while maintaining feature prominence at high zooms.

### Line Width Scaling (Exponential)
Smoothly scale road widths. Exponential interpolation allows roads to widen faster at high zoom levels.
```json
{
  "line-width": [
    "interpolate",
    ["exponential", 1.5],
    ["zoom"],
    4, 0.5,
    10, 2.0,
    18, 16.0
  ]
}
```

### Label Font-Size (Step-based)
Change text size in discrete intervals without smooth scaling:
```json
{
  "text-size": [
    "step",
    ["zoom"],
    10,      // Default value before zoom 6
    6, 12,   // Zoom >= 6, size 12
    12, 16,  // Zoom >= 12, size 16
    16, 22   // Zoom >= 16, size 22
  ]
}
```

---

## 2. Categorical Color Matching

The `match` expression is highly efficient for assigning colors or icon properties based on string properties (e.g. roads, boundaries, structures).

### Coloring Boundaries by ISO Code
Highlight specific countries (e.g. administrative boundary layers) by ISO 2-letter codes:
```json
{
  "fill-color": [
    "match",
    ["get", "iso_a2"],
    "US", "#3b82f6",  // Blue for United States
    "CA", "#ef4444",  // Red for Canada
    "MX", "#10b981",  // Green for Mexico
    "#94a3b8"         // Slate gray (default fallback)
  ]
}
```

---

## 3. Logical Evaluation & Multi-Property Filters

Evaluate features using logical operators (`all`, `any`, `none`, `case`, `has`, `!`).

### Conditional styling based on population and capital status
Style place names by evaluating if they are national capitals **and** have high population counts:
```json
{
  "text-color": [
    "case",
    [
      "all",
      ["==", ["get", "capital"], 1],
      [">=", ["get", "population"], 1000000]
    ],
    "#ef4444", // Red for large capitals
    "#0f172a"  // Dark blue-gray for regular cities
  ]
}
```

### Checking for Property Presence
Safely style features only if specific metadata properties exist:
```json
{
  "text-field": [
    "case",
    ["has", "name:en"],
    ["get", "name:en"], // Use English name if present
    ["get", "name"]     // Fallback to default local name
  ]
}
```

---

## 4. Interactive Hover & Focus States

Uses `feature-state` which is dynamically set at runtime on the client side via the SDK (`map.setFeatureState(...)`).

```json
{
  "fill-opacity": [
    "case",
    ["boolean", ["feature-state", "hover"], false],
    0.8, // Hover opacity
    0.3  // Standard opacity
  ],
  "fill-color": [
    "case",
    ["boolean", ["feature-state", "selected"], false],
    "#f59e0b", // Yellow for selected features
    "#3b82f6"  // Blue default
  ]
}
```
*Note: Feature-state works on feature IDs. Ensure vector tile features have unique integer `id` properties.*
