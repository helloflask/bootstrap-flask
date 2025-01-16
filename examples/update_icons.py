"""Generaste example page with overview of all icons."""

from lxml import etree
import re

# pylint:disable=unspecified-encoding


def parse_svg(filename):
    """Parse SVG file containing icons."""
    symbols = set()
    data = etree.parse(filename)
    svg = data.getroot()
    for symbol in svg:
        symbols.add(symbol.attrib['id'])
    return sorted(symbols)


def parse_font(filename):
    """Parse font file containing icons."""
    symbols = set()
    with open(filename) as file:
        pattern = re.compile(r'\}\.bi-(.*?)::before\{')
        for line in file:
            if not line.startswith(' */@font-face{'):
                continue
            return sorted(set(pattern.findall(line)))


def generate_svg(version):
    """Write the HTML template file for SVG icons."""
    head = f'''{{% extends 'base.html' %}}
{{% from 'bootstrap{version}/utils.html' import render_icon %}}
<!-- DO NOT EDIT! Use update-icons.py for updating this file. -->

{{% block content %}}
<h2>Icons</h2>
<p>These are all SVG icons that are currently supported by Bootstrap-Flask.</p>
<ul class="row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list">
'''
    names = parse_svg(f'../flask_bootstrap/static/bootstrap{version}/icons/bootstrap-icons.svg')
    with open(f'bootstrap{version}/templates/icons.html', 'w') as file:  
        file.write(head)
        number = 0
        for name in sorted(names):
            item = f'''<li class="col mb-4">
<a class="d-block text-dark text-body-emphasis text-decoration-none" href="https://icons.getbootstrap.com/icons/{name}/">
<div class="px-3 py-4 mb-2 bg-light text-center rounded">
{{{{ render_icon('{name}', 32) }}}}
</div>
</a>
<div class="name text-body-secondary text-decoration-none text-center pt-1">{name}</div>
</li>
'''
            file.write(item)
            number += 1
        file.write('</ul>\n')
        file.write(f'<p>This is a total of {number} icons.</p>\n')
        file.write('{% endblock %}\n')
        print(f'Bootstrap{version} supports a total of {number} icons.')


def generate_font(version):
    """Write the HTML template file for font icons."""
    head = f'''{{% extends 'base.html' %}}
{{% from 'bootstrap{version}/utils.html' import render_icon_font %}}
<!-- DO NOT EDIT! Use update-icons.py for updating this file. -->

{{% block content %}}
<h2>Icons Font</h2>
<p>These all font icons that are currently supported by Bootstrap-Flask.</p>
<ul class="row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list">
'''
    names = parse_font(f'../flask_bootstrap/static/bootstrap{version}/font/bootstrap-icons.min.css')
    with open(f'bootstrap{version}/templates/icons_font.html', 'w') as file:  # pylint:disable=unspecified-encoding
        file.write(head)
        number = 0
        for name in sorted(names):
            item = f'''<li class="col mb-4">
<a class="d-block text-dark text-body-emphasis text-decoration-none" href="https://icons.getbootstrap.com/icons/{name}/">
<div class="px-3 py-4 mb-2 bg-light text-center rounded">
{{{{ render_icon_font('{name}', '32px') }}}}
</div>
</a>
<div class="name text-body-secondary text-decoration-none text-center pt-1">{name}</div>
</li>
'''
            file.write(item)
            number += 1
        file.write('</ul>\n')
        file.write(f'<p>This is a total of {number} icons.</p>\n')
        file.write('{% endblock %}\n')
        print(f'Bootstrap{version} supports a total of {number} icons.')


for value in (4, 5):
    generate_svg(value)
    generate_font(value)
