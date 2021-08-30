Bootstrap-Flask
===============

`Bootstrap 4 <https://getbootstrap.com>`_ helper for Flask/Jinja2.


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

    $ git clone git@github.com:greyli/bootstrap-flask.git
    $ cd bootstrap-flask
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install ".[dev]"

Then run tests with tox:

.. code-block:: bash

    $ tox


Authors
-------

Maintainer: `Grey Li <http://greyli.com>`_

See also the list of
`contributors <https://github.com/greyli/bootstrap-flask/contributors>`_
who participated in this project.


License
-------

This project is licensed under the MIT License (see the
``LICENSE`` file for details).

Some macros were part of `Flask-Bootstrap <https://github.com/mbr/flask-bootstrap>`_ and were modified under the terms of its BSD License.
