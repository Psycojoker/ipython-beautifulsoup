#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

import os.path
README_PATH = os.path.join(os.path.dirname(__file__), 'README.rst')
README_TEXT = None
with open(README_PATH, 'r') as f:
    README_TEXT = f.read()

setup(
    name='ipython-beautifulsoup',
    version='0.1.1',
    description='custom rendering of beautifulsoup object \
    in ipython notebook and qtconsole',
    author='Laurent Peuch',
    long_description=README_TEXT,
    author_email='cortex@worlddomination.be',
    url='https://github.com/Psycojoker/ipython-beautifulsoup',
    install_requires=['pygments', 'ipython'],
    extras_require={
        "notebook": ["ipython[notebook]", "pyzmq", "jinja2", "tornado"],
        "qtconsole": ["ipython[qtconsole]"],
        "bs3": ["BeautifulSoup"],
        "bs4": ["BeautifulSoup4"],
    },
    py_modules=['soup'],
    license='MIT',
    scripts=[],
    keywords='ipython beautifulsoup parsing scraping',
    )
