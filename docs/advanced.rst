Advanced Usage
===============

.. _button_customizatoin:

Form Button Customization
--------------------------

Button Style
~~~~~~~~~~~~

When you use form related macros, you have a couple ways to style buttons. Before we start to dive into the solutions, let's
review some Bootstrap basics: In Bootstrap 4, you have 9 normal button style and 8 outline button style, so you have 17 button
style classes below:

- btn-primary
- btn-secondary
- btn-success
- btn-danger
- btn-warning
- btn-info
- btn-light
- btn-dark
- btn-link
- btn-outline-primary
- btn-outline-secondary
- btn-outline-success
- btn-outline-danger
- btn-outline-warning
- btn-outline-info
- btn-outline-light
- btn-outline-dark

Remove the ``btn-`` prefix, you will get what we (actually, I) called "Bootstrap button style name":

- primary
- secondary
- success
- danger
- warning
- info
- light
- dark
- link
- outline-primary
- outline-secondary
- outline-success
- outline-danger
- outline-warning
- outline-info
- outline-light
- outline-dark

You will use these names in Bootstrap-Flask. First, you configuration variables ``BOOTSTRAP_BTN_STYLE`` to set a global form button style:

.. code-block:: python

    from flask import Flask
    from flask_bootstrap import Bootstrap

    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'  # default to 'secondary'


Or you can use ``button_style`` parameter when using ``render_form``, ``render_field`` and ``render_form_row``, this parameter will overwrite
``BOOTSTRAP_BTN_STYLE``:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form, button_style='success') }}

Similarly, you can use this way to control the button size. In Bootstrap 4, buttons can have 4 sizes:

- btn-sm
- btn-md (the default size)
- btn-lg
- btn-block

So, the size names used in Bootstrap-Flask will be:

- sm
- md (the default size)
- lg
- block

Now you can use a configuration variable called ``BOOTSTRAP_BTN_STYLE`` to set global form button size:

.. code-block:: python

    from flask import Flask
    from flask_bootstrap import Bootstrap

    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'  # default to 'md'

there also a parameter called ``button_size`` in form related macros (it will overwrite ``BOOTSTRAP_BTN_SIZE``):

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form, button_size='lg') }}

if you need a **block level small** button (``btn btn-sm btn-block``), you can just do something hacky like this:

.. code-block:: python

    app.config['BOOTSTRAP_BTN_SIZE'] = 'sm btn-block'

What if I have three buttons in one form, and I want they have different styles and sizes? The answer is ``button_map`` parameter in form related macros.
``button_map`` is a dictionary that mapping button field name to Bootstrap button style names. For example, ``{'submit': 'success'}``.
Here is a more complicate example:

.. code-block:: jinja

    {% from 'bootstrap/form.html' import render_form %}

    {{ render_form(form, button_map={'submit': 'success', 'cancel': 'secondary', 'delete': 'danger'}) }}

It will overwrite ``button_style`` and ``BOOTSTRAP_BTN_STYLE``.


.. _bootswatch_theme:

Bootswatch Themes
-----------------

`Bootswatch <https://bootswatch.com>`_ is a collection of free and open source themes for Bootstrap. If you are using ``bootstrap.load_css()`` to include
Bootstrap resources. Then you can set Bootswatch theme with configuration variable ``BOOTSTRAP_BOOTSWATCH_THEME``.

The available theme names are: 'cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'litera',
'lumen', 'lux', 'materia', 'minty', 'pulse', 'sandstone', 'simplex', 'sketchy', 'slate',
'solar', 'spacelab', 'superhero', 'united', 'yeti'.

Here is an example to use ``lumen`` theme:

.. code-block:: python

    app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'

You can find these themes on `https://bootswatch.com <https://bootswatch.com>`_.
