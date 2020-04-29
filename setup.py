# -*- coding: utf-8 -*-
"""
    Bootstrap-Flask
    ~~~~~~~~~~~~~~
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
from os import path
from codecs import open
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='Bootstrap-Flask',
    version='1.3.1',
    url='https://github.com/greyli/bootstrap-flask',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Bootstrap helper for Flask/Jinja2.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['flask_bootstrap'],
    zip_safe=False,
    include_package_data=True,
    test_suite='test_bootstrap_flask',
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
        'Development Status :: 3 - Alpha',
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
