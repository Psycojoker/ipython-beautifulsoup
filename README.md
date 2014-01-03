IPython-BeautifulSoup
=====================

IPython-BeautifulSoup is an IPython extension that provide a custom rendring of
BeautifulSoup objects in ipython notebook and qtconsole.

A BeautifulSoup object will now display a rendered version of the selected html
and and prettyfy and syntaxe highlighted version of the selected html using
pygments.

Usage
=====

In IPython notebook or qtconsole, do:

    %load_ext soup

This will push a series of callable into your current context, including
BeautifulSoup. You can now use BeautifulSoup like you would do if it was
imported from the corresponding module.

This also load a shortcut for the lazy people called *p* (for **p**arse) which is defined this
way:

```python
def p(url):
    return BeautifulSoup(urlopen(url).read()
```

Screenshots
===========

On a single .find:

![1](1.png)

On a .findAll:

![2](2.png)
