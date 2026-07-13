## 🎨 7. User Interface & Widgets Specification

The Marine Biologist Expert agent mainly communicates using natural language and direct markdown links. However, to enhance the visual experience, we can configure a custom widget representing a NOAA Resource Card.

### Widget 1: `noaa_resource_card`
*   **Type:** Info Card / Container
*   **Theme Token Default:** `blue`
*   **Layout JSON Structure:**
```json
// app/ui/widgets/noaa_resource_card.json
{
  "type": "container",
  "props": {
    "className": "flex flex-col gap-3 p-4 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800"
  },
  "children": [
    {
      "type": "text",
      "props": {
        "text": "National Oceanic and Atmospheric Administration (NOAA)",
        "className": "text-lg font-bold text-blue-600 dark:text-blue-400"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "NOAA is an agency that enriches life through science. Our reach goes from the surface of the sun to the depths of the ocean floor as we work to keep citizens informed of the changing environment around them.",
        "className": "text-sm text-slate-600 dark:text-slate-300"
      }
    },
    {
      "type": "text",
      "props": {
        "text": "[Visit Official NOAA Website](https://www.noaa.gov)",
        "className": "text-sm font-semibold text-blue-500 hover:underline"
      }
    }
  ]
}
```
