"""
Bootstrap-Flask
---------------

Bootstrap-Flask is a collection of Jinja macros for Bootstrap 4 & 5 and Flask.
It helps you to render Flask-related objects and data to Bootstrap HTML more easily.

If you come from Flask-Bootstrap, check out
[this tutorial](https://bootstrap-flask.readthedocs.io/en/latest/migrate.html)
on how to migrate to this extension.

Go to [GitHub page](https://github.com/greyli/bootstrap-flask), which you
can check for more details.
"""
from setuptools import setup

setup(
    name='Bootstrap-Flask',
    version='2.0.0',
    url='https://github.com/greyli/bootstrap-flask',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Bootstrap 4 & 5 helper for your Flask projects.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_bootstrap'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'Flask',
        'WTForms'
    ],
    keywords='flask extension development',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
