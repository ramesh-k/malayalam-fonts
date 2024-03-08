# Nupuram Color

Version: `1.000-alpha.16`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/Nupuram).

## Font Files

* [Nupuram-Color.colrv1.woff2](Nupuram-Color.colrv1.woff2)

## Variation axes

| Axis       | Tag    | Range        | Default | Description                                                     |
| ---------- | ------ | ------------ | ------- | --------------------------------------------------------------- |
| Weight  | `wght` | 100 to 900       | 400       | Thin to Black. Can be defined with usual font-weight property. 

---

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import the `Nupuram Color` font like this:

```javascript
import "malayalam-fonts/fonts/Nupuram-Color/main.css";
```
`Nupuram Color` font gives 18 predefined pallettes that can be selected by users. Or a user can specify the colors in a CSS file, CSS Module, or CSS-in-JS.

This color font uses 3 colors for its shadow-ish look. They are Dark, Light, Base colors. Base is the facing color, Light is the central glowing area color. Dark is the color for the shadow part. The colors are used to create a gradient internally.
The following CSS customizes the pallette:

```css

body {
  font-family: 'Nupuram Color';
  font-size: 48px;
  font-variation-settings: "wght" 400; /* Custom axis settings */
  font-palette: --custom;
}

@font-palette-values --custom  {
  font-family: 'Nupuram Color';
  /* Change this to a value between 0 and 18 to chose a supplied palette. */
  base-palette: 0;
  /* Or provide the colors directly to override palette */
  override-colors: 0 #FFD700, 1 #FFD700, 2 #1E0303;
}

```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Nupuram Color` font, copy the code into the `<head>` of your html :

````css
<style>

@import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Nupuram-Color/main.min.css');

html {
	font-family: 'Nupuram Color';
	font-size: 48px;
	font-variation-settings: "wght" 400;	/* Custom axis settings */
	font-palette: --custom;
}

@font-palette-values --custom {
	font-family: 'Nupuram Color';
	/* Change this to a value between 0 and 18 to chose a supplied palette. */
	base-palette: 0;
	/* Or provide the colors directly to override palette */
	override-colors: 0 #FFD700, 1 #FFD700, 2 #1E0303;
}

</style>
````
---
## License

See [OFL.txt](OFL.txt)