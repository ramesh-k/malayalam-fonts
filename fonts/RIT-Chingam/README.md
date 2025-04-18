# RIT Chingam

Version: `1.2.1`

To learn about this font, please visit the [source](https://gitlab.com/rit-fonts/chingam).

## Font Files

* [RITChingam.woff2](RITChingam.woff2)

## Supported variants

* Weights: Normal (400)
* Styles: Normal

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `RIT Chingam` font like this:

```javascript
import "malayalam-fonts/fonts/RIT-Chingam/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: "RIT Chingam";
  font-weight : normal;
  font-style  : normal;
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `RIT Chingam` font, copy the code into the `<head>` of your html :

```css
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/RIT-Chingam/main.min.css');
   html {
   font-family : 'RIT Chingam';
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
font-feature-settings: "ss01" 0;

/* Apply Style 2 */
font-feature-settings: "ss01" 1;
```

---
## License

See [LICENSE.txt](LICENSE.txt)