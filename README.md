# Bootstrap-Flask

Bootstrap helper for Flask/Jinja2. Based on Flask-Bootstrap, but lighter and better.


## Installation

```
$ pip install bootstrap-flask
```

## Initialization

```
from flask_bootstrap import Bootstrap
from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap(app)
```

## Resources helpers

When development, Bootstrap-Flask provides two helper functions that can be used to generate
resources load code in template: `bootstrap.load_css()` and `bootstrap.load_js()`

Call it at your template, for example:
```html
<head>
{{ bootstrap.load_css() }}
</head>
<body>
...
{{ bootstrap.load_js() }}
</body>
```

## Macros

| Macro	| Templates Path | Description |
| ----- | -------------- | ----------- |
| render_field() | bootstrap/form.html | Redner a WTForms form field |
| render_form()	| bootstrap/form.html | Render a WTForms form |
| render_pager() | bootstrap/pagination.html | Render a basic pagination, only include previous and next button. |
| render_pagination() | bootstrap/pagination.html | Render a standard pagination |
| render_nav_item() | bootstrap/nav.html | Render a navigation item |
| render_breadcrumb_item() | bootstrap/nav.html | Render a breadcrumb item |
| render_static() | bootstrap/utils.html | Render a resource reference code (i.e. `<link>`, `<script>`) |

How to use these macors? It's quite simple, just import them from the
correspond path and then call them like any other macro:
```py
from 'bootstrap/form.html' import render_form

{{ render_form(form) }}
```

*API documentation will coming soon...*


## Changelog

### 0.1.0

Release date: 2018/6/11

Initialize release.

## License

This project is licensed under the MIT License (see the
`LICENSE` file for details).