'''Generate example page with overview of all icons.'''

from lxml import etree

def parse(filename):
    '''Parse SVG file containing icons.'''
    symbols = set()
    data = etree.parse(filename)
    svg = data.getroot()
    for symbol in svg:
        symbols.add(symbol.attrib['id'])
    return sorted(symbols)

def generate(version):
    '''Write the HTML template file.'''
    head = f'''<!-- DO NOT EDIT! Use generate.py for updating this file. -->
{{% extends 'base.html' %}}
{{% from 'bootstrap{version}/utils.html' import render_icon %}}

{{% block content %}}
<h2>Icons</h2>
<p>These are all the icons which are currently supported by Bootstrap-Flask.</p>
<ul class="row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list">
'''
    names = parse(f'../flask_bootstrap/static/bootstrap{version}/icons/bootstrap-icons.svg')
    with open(f'bootstrap{version}/templates/icons.html', 'w') as file:  # pylint:disable=unspecified-encoding
        file.write(head)
        for name in sorted(names):
            item=f'''<li class="col mb-4" data-tags="numbers" data-categories="typography">
<a class="d-block text-dark text-decoration-none" href="https://icons.getbootstrap.com/icons/{name}/">
<div class="p-3 py-4 mb-2 bg-light text-center rounded">
{{{{ render_icon('{name}', 32) }}}}
<use xlink:href="bootstrap-icons.svg#{name}" />
</svg>
</div>
</a>
<div class="name text-muted text-decoration-none text-center pt-1">{name}</div>
</li>
'''
            file.write(item)
        tail = '''</ul>
{% endblock %}
'''
        file.write(tail)

for value in (4, 5):
    generate(value)
