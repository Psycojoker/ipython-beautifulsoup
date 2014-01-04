IPython-BeautifulSoup
=====================

IPython-BeautifulSoup is an IPython extension that provide a custom rendering of
BeautifulSoup objects in iPython notebook and qtconsole.

A BeautifulSoup object will now display a rendered version of the selected html
and a prettify and syntax highlighted version of the selected html using
pygments.

![teaser](teaser.png)

Install
=======

Simply run:

    pip install "ipython-beautifulSoup[bs4]"

If you want BeautifulSoup 3 instead of BeautifulSoup 4, change "bs4" by "bs3". If you want the notebook or the qtconsole to be installed, just add "notebook" or "qtconsole" after "bs4" separated by a "," like this:

    pip install "ipython-beautifulSoup[bs4,notebook,qtconsole]"

On Ubuntu LTS, if you want to install the **notebook**, you'll need to do this before:

    sudo apt-get install python-dev g++

For the **qtconsole** do this (if you do this in a virtualenv) (WARNING: it's slow):

    sudo apt-get install make cmake qt4-qmake libqt4-dev
    pip install pyside

Usage
=====

In IPython notebook or qtconsole, do:

    %load_ext soup

This will push a series of callable into your current context, including
BeautifulSoup. You can now use BeautifulSoup like you would do if it was
imported from the corresponding module.

This also load a shortcut for the lazy people called *p* (for **p**arse) which
is defined this way:

```python
def p(url):
    return BeautifulSoup(urlopen(url).read())
```

Screenshots
===========

On a single .find:

![1](1.png)

On a .findAll:

![2](2.png)
