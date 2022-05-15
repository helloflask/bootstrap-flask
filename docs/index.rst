Bootstrap-Flask
===============

Bootstrap-Flask is a collection of Jinja macros for Bootstrap and Flask. It helps you to
render Flask-related data and objects to Bootstrap markup HTML more easily.


Contents
--------

.. toctree::
   :maxdepth: 2

   basic
   macros
   migrate
   advanced
   examples


API Reference
-------------

If you are looking for information on a specific function, class or
method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Changelog
---------

.. toctree::
   :maxdepth: 2

   changelog


Development
-----------

We welcome all kinds of contributions. You can build the development environment
locally with the following commands:

.. code-block:: bash

    $ git clone git@github.com:helloflask/bootstrap-flask.git
    $ cd bootstrap-flask
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install -e .
    $ pip install -r requirements/dev.txt

Run the tests with pytest:

.. code-block:: bash

    $ pytest

Or run the full checks with tox:

.. code-block:: bash

    $ tox


Authors
-------

Maintainers:

- `Grey Li <https://github.com/greyli>`_
- `Pander <https://github.com/PanderMusubi>`_

See also the list of
`contributors <https://github.com/helloflask/bootstrap-flask/contributors>`_
who participated in this project.


License
-------

This project is licensed under the MIT License (see the ``LICENSE`` file for
details). Some macros were part of Flask-Bootstrap and were modified under
the terms of its BSD License.
