# Malini

Version: `1.000-alpha.13`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/Malini).

## Font Files

* [Malini-VF.woff2](Malini-VF.woff2)

## Variation axes


| Axis       | Tag    | Range        | Default | Description                                                     |
| ---------- | ------ | ------------ | ------- | --------------------------------------------------------------- |
| Weight  | `wght` | 100 to 900       | 400       | Thin to Black. Can be defined with usual font-weight property.                      |
| Slant     | `slnt` | -12 to 0       | 0       | Upright (0°) to Slanted (about 12°)                                                |
| Width     | `wdth` | 75 to 125  | 100     | Condensed to Expanded. Can be defined with usual font-stretch property. |
| Optical Size     | `opsz` | 10 to 48  | 12     | Follows the font size to optimize the contrast and spacing |


---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `Malini` font like this:

```javascript
import "malayalam-fonts/fonts/Malini/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: 'Malini';
  font-size: 18px;
  font-variation-settings: 'wght' 200, 'wdth' 100, 'slnt' -10; /* Custom axis settings */
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Malini` font, copy the code into the `<head>` of your html :

```css
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Malini/main.min.css');
   html {
   font-family: 'Malini';
   font-size: 18px;
   font-variation-settings: 'wght' 200, 'wdth' 100, 'slnt' -10; /* Custom axis settings */
   }
</style>
```
Refer font face defined in [`CSS`](main.css) file.

---
### Choosing Font Feature with CSS

To select specific font features using CSS, you can utilise the `font-feature-settings` property. Follow these steps to apply different features to elements or classes within your html:

```css
/* Apply Style 1 */
font-feature-settings: "salt" 1;

/* Apply Style 2 */
font-feature-settings: "salt" 2;
```

---
## License

See [OFL.txt](OFL.txt)