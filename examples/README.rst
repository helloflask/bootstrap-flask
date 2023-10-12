Run the demo application
========================

Type these commands in the terminal:

.. code-block:: bash

    $ git clone https://github.com/helloflask/bootstrap-flask.git
    $ cd bootstrap-flask/examples
    $ pip install -r requirements.txt

Then based on the Bootstrap version you want to use to run the application.

Bootstrap 4:

.. code-block:: bash

    $ python bootstrap4/app.py

Bootstrap 5:

.. code-block:: bash

    $ python bootstrap5/app.py

Now go to http://localhost:5000.

Live demos for the example application: https://bootstrap-flask-example.azurewebsites.net/


Overview of icons
-----------------

The example applications contain a page called icons which gives an overview
of all icons supported by this version of Bootstrap-Flask. This overview can be
used for testing purposes but is also offline documentation on the icons
available.

When Bootstrap-Flask updates the icon file, the overview page can be upgraded
with:


.. code-block:: bash

    $ python3 update-icons.py

