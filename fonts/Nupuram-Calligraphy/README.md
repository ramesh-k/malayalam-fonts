# Nupuram Calligraphy

Version: `1.000-alpha.16`

To learn about this font, please visit the [source](https://gitlab.com/smc/fonts/Nupuram).

## Font Files

* [Nupuram-Calligraphy-VF.woff2](Nupuram-Calligraphy-VF.woff2)

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

In your main application file or website component, import the `Nupuram Calligraphy` font like this:

```javascript
import "malayalam-fonts/fonts/Nupuram-Calligraphy/main.css";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS.

```css
body {
  font-family: 'Nupuram Calligraphy';
  font-size: 32px;
  font-variation-settings: "wght" 400; /* Custom axis settings */
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `Nupuram Calligraphy` font, copy the code into the `<head>` of your html :

````
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts/Nupuram-Calligraphy/main.min.css');
   html {
   font-family: 'Nupuram Calligraphy';
   font-size: 32px;
   font-variation-settings: "wght" 400; /* Custom axis settings */
   }
</style>
````
---
## License

See [OFL.txt](OFL.txt)