# RIT Rachana

Version: `1.4.7`

To learn about this font, please visit the [source](https://gitlab.com/rit-fonts/RIT-Rachana).

## Font Files

* [RIT-Rachana-Regular.woff2](RIT-Rachana-Regular.woff2)
* [RIT-Rachana-Italic.woff2](RIT-Rachana-Italic.woff2)
* [RIT-Rachana-Bold.woff2](RIT-Rachana-Bold.woff2)
* [RIT-Rachana-BoldItalic.woff2](RIT-Rachana-BoldItalic.woff2)

## Supported variants

* Weights: Normal (400), Bold (700)
* Styles: Normal, Italic

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `RIT Rachana` font like this:

```javascript
import "malayalam-fonts/fonts/RIT-Rachana/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: "RIT Rachana";
  font-weight : normal;
  font-style  : normal;
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `RIT Rachana` font, copy the code into the `<head>` of your html :

```css
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/RIT-Rachana/main.min.css');
   html {
   font-family : 'RIT Rachana';
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
/* Oldstyle figures */
font-feature-settings: "onum" 1;
```

---
## License

See [LICENSE.txt](LICENSE.txt)