# Manjari

Version: `2.200`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/manjari).

## Font Files

* [Manjari-Regular.woff2](Manjari-Regular.woff2)
* [Manjari-Bold.woff2](Manjari-Bold.woff2)
* [Manjari-Thin.woff2](Manjari-Thin.woff2)

## Supported variants

* Weights: Normal (400), Bold (700), Thin (100)
* Styles: Normal

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `Manjari` font like this:

```javascript
import "malayalam-fonts/fonts/Manjari/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: "Manjari";
  font-weight : normal;
  font-style  : normal;
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Manjari` font, copy the code into the `<head>` of your html :

```css
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Manjari/main.min.css');
   html {
   font-family : 'Manjari';
   font-weight : normal;
   font-style  : normal;
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

/* Apply Tabular Figure */
font-feature-settings: "tnum" 1;

/* Apply Slashed Zero */
font-feature-settings: "zero" 1;

/* Apply Multiple features */
font-feature-settings: "tnum" 1, "zero" 1, "salt" 2;
```

---
## License

See [OFL.txt](OFL.txt)