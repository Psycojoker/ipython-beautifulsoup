IPython-BeautifulSoup
=====================

IPython-BeautifulSoup is an IPython extension for displaying BeautifulSoup HTML/XML objects as prettified and syntax highlighted HTML blocks in IPython notebook and qtconsole.

Syntax highlighting is accomplished with [`Pygments`](http://pygments.org/).

![teaser](teaser.png)

Install
=======

Simply run:

    pip install "ipython-beautifulSoup[bs4]"

For BeautifulSoup 3 instead of BeautifulSoup 4, change `bs4` to `bs3`.

Installing IPython Notebook
---------------------------

See the [IPython installation docs](http://ipython.org/ipython-doc/stable/install/index.html) for details.

To install IPython notebook or qtconsole as well, append `notebook` and/or `qtconsole` to the extras specifier after "bs4" separated by a ",", like this:

    pip install "ipython-beautifulsoup[bs4,notebook,qtconsole]"

On Ubuntu LTS, if you want to install **IPython notebook**, you'll need to do this before:

    sudo apt-get install python-dev g++

(use `python3-dev` if you're using Python 3)

For the **qtconsole** do this (if you do this in a virtualenv) (WARNING: it's slow):

    sudo apt-get install make cmake qt4-qmake libqt4-dev
    pip install pyside

Usage
=====

In IPython notebook or qtconsole, run:

```ipython
%load_ext soup
```

This will push a series of callables into your current context, as well as a monkey-patched BeautifulSoup and requests.

You can now use BeautifulSoup like you would if it was imported from the corresponding module.

There is great chances that you'll want to configure the output by using `configure_ipython_beautifulsoup`, for example like this (just after the `%load_ext`):

    configure_ipython_beautifulsoup(show_html=True, show_css=True, show_js=False)

To see `configure_ipython_beautifulsoup` documentation just do (in any interface of IPython):

    configure_ipython_beautifulsoup?

This also loads a shortcut function called `p` (for <b>P</b>arse) defined as follows:

```python
def p(url):
    if requests is not None:
        return BeautifulSoup(requests.get(url).contents)
    return BeautifulSoup(urlopen(url).read())
```

A note on security
==================

> **WARNING**
>
> By nature of including external HTML, JS, and CSS, this extension is inherently unsafe if you choose to render the html by setting show\_html to True when calling **`configure_ipython_beautifulsoup`**.
>
> By default, `<script>`, `<link>`, and `<style>` tags are removed but this isn't a 100% guarantee that this is secure if you choose to render the html, use at your own risk.

The safest option is to set all options of `configure_ipython_beautifulsoup` to `False` (the default).

Screenshots
===========

IPython Notebook
----------------

`.find`:

![.find](1.png)

`.find_all`:

![.find_all](2.png)

Contributors
============

In chronological order:

-   [Astalaseven](https://github.com/Astalaseven) - pull request: [#1](https://github.com/Psycojoker/ipython-beautifulsoup/pull/1)
-   [westurner](https://github.com/westurner) - pull request: [#3](https://github.com/Psycojoker/ipython-beautifulsoup/pull/3)
-   [MattDMo](https://github.com/MattDMo) - pull request: [#5](https://github.com/Psycojoker/ipython-beautifulsoup/pull/5)

Don't hesitate to add yourself.

