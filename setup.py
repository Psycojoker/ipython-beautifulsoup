#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='ipython-beautifulsoup',
      version='0.1',
      description='custom rendering of beautifulsoup object in ipython notebook and qtconsole',
      author='Laurent Peuch',
      #long_description='',
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
      license= 'MIT',
      scripts=[],
      keywords='ipython beautifulsoup parsing scraping',
     )
