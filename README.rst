IPython-BeautifulSoup
=====================

IPython-BeautifulSoup is an IPython extension for displaying
BeautifulSoup HTML/XML objects as prettified and syntax highlighted HTML
blocks in IPython notebook and qtconsole.

Syntax highlighting is accomplished with Pygments.

.. figure:: teaser.png
   :align: center
   :alt: teaser



Install
=======

Simply run:

::

    pip install "ipython-beautifulSoup[bs4]"

For BeautifulSoup 3 instead of BeautifulSoup 4, change ``bs4`` to
``bs3``.

Installing IPython Notebook
-----------------------------
See http://ipython.org/ipython-doc/stable/install/index.html

To install IPython notebook or qtconsole as well, append ``notebook``
and/or ``qtconsole`` to the extras specifier after "bs4" separated by a
",", like this:

::

    pip install "ipython-beautifulSoup[bs4,notebook,qtconsole]"

On Ubuntu LTS, if you want to install **IPython notebook**, you'll need
to do this before:

::

    sudo apt-get install python-dev g++

For the **qtconsole** do this (if you do this in a virtualenv) (WARNING:
it's slow):

::

    sudo apt-get install make cmake qt4-qmake libqt4-dev
    pip install pyside


Usage
=====

In IPython notebook or qtconsole, do:

::

    %load_ext soup

This will push a series of callables into your current context,
as well as a monkey-patched BeautifulSoup and requests.

You can now use BeautifulSoup like you would if it was imported from the
corresponding module.

This also loads a shortcut function called ``p`` (for
**p** arse) defined as follows:

::

    def p(url):
        if requests is not None:
            return BeautifulSoup(requests.get(url).contents)
        return BeautifulSoup(urlopen(url).read())


Screenshots
===========

IPython Notebook
------------------

``.find``:

.. figure:: 1.png
   :align: center
   :alt: 1


``.findAll``:

.. figure:: 2.png
   :align: center
   :alt: 2

