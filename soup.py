from __future__ import print_function
import sys
if sys.version_info[0] == 3:
    PYTHON3 = True
else:
    PYTHON3 = False

if PYTHON3:
    from urllib.request import urlopen
    from collections import UserList
    string_representation = str
else:
    from urllib2 import urlopen
    from UserList import UserList
    string_representation = unicode

from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter

from bs4 import BeautifulSoup, Tag

requests = None
try:
    import requests
except ImportError:
    pass


SHOW_RENDERED_HTML = False
SHOW_RENDERED_CSS = False
SHOW_RENDERED_JS = False
BS_PARSER = 'html.parser'


def configure_ipython_beautifulsoup(show_html=False,
                                    show_css=False,
                                    show_js=False,
                                    parser=None):
    """
    Configure rendering settings for ipython-beautifulsoup extension

    Args:
        show_html: whether to show actual HTML before the prettified copy
        show_css: whether to remove <style> and <link> blocks from actual HTML
        show_js: whether to remove <script> blocks from actual HTML
        parser: what parser BeautifulSoup should use by default

    .. warning:: By nature of including external HTML, JS, and CSS,
       this extension is inherently unsafe. These configurable options
       only apply to <script> and <link> and <style> tags.

       The most safe option is to set all of these options to False
       (the default).

    """
    global SHOW_RENDERED_HTML
    global SHOW_RENDERED_CSS
    global SHOW_RENDERED_JS
    global BS_PARSER

    SHOW_RENDERED_HTML = show_html
    SHOW_RENDERED_CSS = show_css
    SHOW_RENDERED_JS = show_js

    if parser:
        BS_PARSER = parser


def cleaned_beautifulsoup_copy(soup, parser=None):
    # Allow for overriding the default parser for a particular request.
    if not parser:
        parser = BS_PARSER

    copy = BeautifulSoup(string_representation(soup), parser)
    if SHOW_RENDERED_JS is not True:
        for node in copy('script'):
            node.extract()

    if SHOW_RENDERED_CSS is not True:
        for node in copy('style') + copy('link'):
            node.extract()

    return copy


def render(self, parser=None):
    def __render(self, parser=None):
        if SHOW_RENDERED_HTML:
            yield string_representation(cleaned_beautifulsoup_copy(self,
                                                                   parser))
            yield u"<hr/>"

        yield string_representation(highlight(
            self.prettify(),
            HtmlLexer(),
            HtmlFormatter(noclasses=True),
            ))
        yield u"<hr/>"

    return u''.join(__render(self, parser))


class BeautifulSoupList(UserList):
    def _repr_html_(self, parser=None):
        def __repr_html(self, parser=None):
            # string addition is slow (and makes copies)
            yield u"<table>"
            yield u"<tr><th>Index</th><th>Render</th><th>source</th></tr>"
            for num, item in enumerate(self):
                yield u"<tr>"
                yield u"<td>"
                yield str(num)
                yield u"</td>"
                yield u"<td>"
                yield string_representation(cleaned_beautifulsoup_copy(item,
                                                                       parser))
                yield u"</td>"
                yield u"<td>"
                yield highlight(
                    item.prettify(),
                    HtmlLexer(),
                    HtmlFormatter(noclasses=True),
                )
                yield u"</td>"
                yield u"</tr>"
            yield u"</table>"
        return u''.join(__repr_html(self, parser))

    def __getslice__(self, *args, **kwargs):
        return BeautifulSoupList(
            super(BeautifulSoupList, self).__getslice__(*args, **kwargs))


def wrap_findall(function):
    def findall_wrapper(*args, **kwargs):
        return BeautifulSoupList(function(*args, **kwargs))
    return findall_wrapper


def p(url, parser=None):
    # Allow for overriding the default parser for a particular request.
    if not parser:
        parser = BS_PARSER

    if requests is not None:
        return BeautifulSoup(requests.get(url).content, parser)
    return BeautifulSoup(urlopen(url).read(), parser)


def monkey_patch_beautiful_soup():
    BeautifulSoup._repr_html_ = render
    Tag._repr_html_ = render
    BeautifulSoup.find_all = wrap_findall(BeautifulSoup.find_all)
    Tag.find_all = wrap_findall(Tag.find_all)

    return BeautifulSoup, Tag


def load_ipython_extension(ipython):
    print("Monkey patch BeautifulSoup with custom rendering")
    monkey_patch_beautiful_soup()

    to_push = ["BeautifulSoup", "urlopen", "p",
               "configure_ipython_beautifulsoup"]

    print("See `configure_ipython_beautifulsoup?` for configuration"
          " information")

    print("Push 'BeautifulSoup' from 'bs4' into current context")

    print("Push 'urlopen' from '%s' into current context" %
        ("urllib.request" if PYTHON3 else "urllib2"))
    print("Push 'p' shortcut into current context")

    try:
        import requests
        requests  # pyflakes
        print("Push 'requests' into current context")
        to_push.append('requests')
    except ImportError:
        pass

    ipython.push(to_push)
