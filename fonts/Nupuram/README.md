# Nupuram

Version: `1.000-beta.2`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/Nupuram).

## Font Files

* [Nupuram-VF.woff2](Nupuram-VF.woff2)

## Variation axes


| Axis       | Tag    | Range        | Default | Description                                                     |
| ---------- | ------ | ------------ | ------- | --------------------------------------------------------------- |
| Weight  | `wght` | 100 to 900       | 400       | Thin to Black. Can be defined with usual font-weight property.                      |
| Slant     | `slnt` | -15 to 0       | 0       | Upright (0°) to Slanted (about 15°)                                                |
| Width     | `wdth` | 75 to 125  | 100     | Condensed to Expanded. Can be defined with usual font-stretch property. |
| Soft      | `SOFT` | 0 to 100     | 50       | Sharp to normal to SuperSoft terminals                           |

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `Nupuram` font like this:

```javascript
import "malayalam-fonts/fonts/Nupuram/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: 'Nupuram';
  font-size: 18px;
  font-variation-settings: 'wght' 200, 'wdth' 100, "soft" 50, 'slnt' -10; /* Custom axis settings */
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Nupuram` font, copy the code into the `<head>` of your html :

```css
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Nupuram/main.min.css');
   html {
   font-family: 'Nupuram';
   font-size: 18px;
   font-variation-settings: 'wght' 200, 'wdth' 100, "soft" 50, 'slnt' -10; /* Custom axis settings */
   }
</style>
```
Refer font face defined in [`CSS`](main.css) file.

---
### Choosing Font Feature with CSS

To select specific font features using CSS, you can utilise the `font-feature-settings` property. Follow these steps to apply different features to elements or classes within your html:

```css
/* Contextual alternates */
font-feature-settings: "calt" 1;
```

---
## License

See [OFL.txt](OFL.txt)