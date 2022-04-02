# netlify-cms-widget-country-select

[Check out a demo!](https://netlify-cms-widget-country-select.netlify.com/demo)

A select widget for netlify-cms providing all countries of the world as options.

## Install

As an npm package:

```shell
npm install --save netlify-cms-widget-country-select
```

```js
import { CountrySelectControl } from 'netlify-cms-widget-country-select'

CMS.registerWidget('country-select', CountrySelectControl)
```

Via `script` tag:

```html
<script src="https://unpkg.com/netlify-cms-widget-country-select@^1.0.0"></script>

<script>
  CMS.registerWidget('country-select', window.countrySelectControl, window.countrySelectPreview)
</script>
```

## How to use

Add to your Netlify CMS configuration:

```yaml
    fields:
      - { name: 'country', label: 'Country', widget: country-select }
```

## Support

For help with this widget, open an [issue](https://github.com/<user>/<repo>) or ask the Netlify CMS community in [Gitter](https://gitter.im/netlify/netlifycms).
