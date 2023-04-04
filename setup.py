"""
Bootstrap-Flask
---------------

Bootstrap-Flask is a collection of Jinja macros for Bootstrap 4 & 5 and Flask.
It helps you to render Flask-related objects and data to Bootstrap HTML more easily.

If you come from Flask-Bootstrap, check out
[this tutorial](https://bootstrap-flask.readthedocs.io/en/stable/migrate/)
on how to migrate to this extension.

Go to [GitHub page](https://github.com/helloflask/bootstrap-flask), which you
can check for more details.
"""
from setuptools import setup

setup(
    name='Bootstrap-Flask',
    version='2.3.0dev',
    url='https://github.com/helloflask/bootstrap-flask',
    project_urls={
        'Documentation': 'https://bootstrap-flask.readthedocs.io/en/stable/',
        'Funding': 'https://opencollective.com/bootstrap-flask',
        'Changes': 'https://bootstrap-flask.readthedocs.io/en/stable/changelog/',
        'Source Code': 'https://github.com/helloflask/bootstrap-flask/',
        'Issue Tracker': 'https://github.com/helloflask/bootstrap-flask/issues/',
        'Discussions': 'https://github.com/helloflask/bootstrap-flask/discussions/'
    },
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
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
