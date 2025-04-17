# Nupuram Arrows Color

Version: `1.000-beta.2`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/Nupuram).

## Font Files

* [Nupuram-Arrows-Color.colrv1.woff2](Nupuram-Arrows-Color.colrv1.woff2)

## Supported variants

* Weights: Normal (400)
* Styles: Normal

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `Nupuram Arrows Color` font like this:

```javascript
import "malayalam-fonts/fonts/Nupuram-Arrows-Color/main.css";
```
`Nupuram Arrows Color` font gives 18 predefined pallettes that can be selected by users. Or a user can specify the colors in a CSS file, CSS Module, or CSS-in-JS.

The following CSS customizes the pallette:

```css

body {
  font-family: 'Nupuram Arrows Color';
  font-size: 48px;
  font-palette: --custom;
}

@font-palette-values --custom  {
  font-family: 'Nupuram Arrows Color';
  /* Change this to a value between 0 and 18 to chose a supplied palette. */
  base-palette: 12;
  /* Or provide the colors directly to override palette */
  override-colors: 0 #FF0000, 1 #FFFFFF;
}

```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Nupuram Arrows Color` font, copy the code into the `<head>` of your html :

```css
<style>

@import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Nupuram-Arrows-Color/main.min.css');

html {
  font-family: 'Nupuram Arrows Color';
  font-size: 48px;
  font-palette: --custom;
}

@font-palette-values --custom  {
  font-family: 'Nupuram Arrows Color';
  /* Change this to a value between 0 and 18 to chose a supplied palette. */
  base-palette: 12;
  /* Or provide the colors directly to override palette */
  override-colors: 0 #FF0000, 1 #FFFFFF;
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