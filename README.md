# Malayalam Fonts
A collection of open source Malayalam web fonts.

## Fonts
| **Font Family** | **Version** |  |
|---|---|---|
| [Manjari](fonts/Manjari/) | 2.200 |
| [Chilanka](fonts/Chilanka/) | 1.7 |
| [Gayathri](fonts/Gayathri/) | 1.300 |
| [RIT Rachana](fonts/RIT-Rachana/) | 1.4.7 |
| [RIT Meera New](fonts/RIT-MeeraNew/) | 1.5.2 |
| [RIT Ezhuthu](fonts/RIT-Ezhuthu/) | 1.4 |
| [RIT TN Joy](fonts/RIT-TNJoy/) | 1.5 |
| [RIT Panmana](fonts/RIT-Panmana/) | 1.3 |
| [RIT Sundar](fonts/RIT-Sundar/) | 2.2 |
| [RIT Karuna](fonts/RIT-Karuna/) | 1.1 |
| [RIT Kutty](fonts/RIT-Kutty/) | 1.2 |
| [RIT Chingam](fonts/RIT-Chingam/) | 1.0 |

## Installation

```shell
npm install malayalam-fonts
```
## Usage

In your main application file or website component, import these fonts like this:

```javascript
import "malayalam-fonts";
```
You can specify the font name in a CSS file, CSS Module, or CSS-in-JS. Example:

```css
body {
  font-family: "RIT Meera New";
  font-weight : normal;
  font-style  : normal;
}
```
---

### Use these fonts directly from [jsDelivr CDN](https://www.jsdelivr.com/package/npm/malayalam-fonts)

[![](https://data.jsdelivr.com/v1/package/npm/malayalam-fonts/badge)](https://www.jsdelivr.com/package/npm/malayalam-fonts)

To embed `RIT Meera New` font, copy the code into the `<head>` of your html :

````
<style>
   @import url('https://cdn.jsdelivr.net/npm/malayalam-fonts@latest/fonts.min.css');
   html {
   font-family : 'RIT Meera New';
   font-weight : normal;
   font-style  : normal;
   }
</style>
````
---

The CSS file for each font and its usage-related information are contained in their respective font directories under [/fonts](fonts/).

----
[![npm](https://img.shields.io/npm/v/malayalam-fonts?color=red)](https://www.npmjs.com/package/malayalam-fonts)