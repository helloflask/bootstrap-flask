# -*- coding: utf-8 -*-
"""
Bootstrap-Flask
---------------

[Bootstrap 4](https://getbootstrap.com) helper for Flask/Jinja2.

If you come from Flask-Bootstrap, check out [this tutorial](https://bootstrap-flask.readthedocs.io/en/latest/migrate.html) on how to migrate to this extension.

Go to [GitHub page](https://github.com/greyli/bootstrap-flask), which you
can check for more details.
"""
from setuptools import setup

setup(
    name='Bootstrap-Flask',
    version='1.7.1dev',
    url='https://github.com/greyli/bootstrap-flask',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Bootstrap helper for Flask/Jinja2.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_bootstrap'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'Flask'
    ],
    extras_require={
        'dev': [
            'coverage',
            'tox',
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ],
        'docs': [
            'sphinx',
            'pallets-sphinx-themes',
            'sphinxcontrib-log-cabinet',
        ]
    },
    keywords='flask extension development',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
