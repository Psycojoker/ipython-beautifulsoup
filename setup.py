#!/usr/bin/python
# -*- coding:utf-8 -*-

import os.path
from setuptools import setup

README_PATH = os.path.join(os.path.dirname(__file__), 'README.rst')
README_TEXT = None
with open(README_PATH, 'r') as f:
    README_TEXT = f.read()

CHANGELOG_PATH = os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')
CHANGELOG_TEXT = None
with open(CHANGELOG_PATH, 'r') as f:
    CHANGELOG_TEXT = f.read()

setup(name='ipython-beautifulsoup',
      version='0.3',
      description='Custom rendering of beautifulsoup objects \
      in IPython notebook and qtconsole',
      author='Laurent Peuch',
      long_description=README_TEXT + "\n\n" + CHANGELOG_TEXT,
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/ipython-beautifulsoup',
      install_requires=['pygments', 'ipython', 'beautifulsoup4'],
      extras_require={
          "notebook": ["ipython[notebook]", "pyzmq", "jinja2", "tornado"],
          "qtconsole": ["ipython[qtconsole]"],
          "bs4": ["BeautifulSoup4"],
      },
      py_modules=['soup'],
      license='MIT',
      scripts=[],
      keywords='ipython beautifulsoup parsing scraping',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Framework :: IPython",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Topic :: Text Processing :: Markup :: HTML",
                   "Topic :: Text Processing :: Markup :: XML",
                   "Topic :: Text Processing :: Markup :: SGML",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                  ],
    )
