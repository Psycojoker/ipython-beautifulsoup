from __future__ import print_function
from urllib2 import urlopen
from UserList import UserList
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter

bs4 = None
try:
    from bs4 import BeautifulSoup, Tag
    bs4 = True
except ImportError:
    from BeautifulSoup import BeautifulSoup, Tag

requests = None
try:
    import requests
except ImportError:
    pass

SHOW_RENDERED_HTML = False
SHOW_RENDERED_CSS = False
SHOW_RENDERED_JS = False


def configure_ipython_beautifulsoup(show_html=False,
                                    show_css=False,
                                    show_js=False):
    """
    Configure rendering settings for ipython-beautifulsoup extension

    Args:
        show_html: whether to show actual HTML before the prettified copy
        show_css: whether to remove <style> and <link> blocks from actual HTML
        show_js: whether to remove <script> blocks from actual HTML

    .. warning:: By nature of including external HTML, JS, and CSS,
       this extension is inherently unsafe. These configurable options
       only apply to <script> and <link> and <style> tags.

       The most safe option is to set all of these options to False
       (the default).

    """
    global SHOW_RENDERED_HTML
    global SHOW_RENDERED_CSS
    global SHOW_RENDERED_JS

    SHOW_RENDERED_HTML = show_html
    SHOW_RENDERED_CSS = show_css
    SHOW_RENDERED_JS = show_js


def cleaned_beautifulsoup_copy(soup):
    copy = BeautifulSoup(unicode(soup))
    if SHOW_RENDERED_JS is not True:
        for node in copy('script'):
            node.extract()

    if SHOW_RENDERED_CSS is not True:
        for node in copy('style') + copy('link'):
            node.extract()

    return copy


def render(self):
    def __render(self):
        if SHOW_RENDERED_HTML:
            yield unicode(cleaned_beautifulsoup_copy(self))
            yield u"<hr/>"

        yield unicode(highlight(
            self.prettify(),
            HtmlLexer(),
            HtmlFormatter(noclasses=True),
        ))
        yield u"<hr/>"

    return u''.join(__render(self))


class BeautifulSoupList(UserList):
    def _repr_html_(self):
        def __repr_html(self):
            # string addition is slow (and makes copies)
            yield u"<table>"
            yield u"<tr><th>Index</th><th>Render</th><th>source</th></tr>"
            for num, item in enumerate(self):
                yield u"<tr>"
                yield u"<td>"
                yield str(num)
                yield u"</td>"
                yield u"<td>"
                yield unicode(cleaned_beautifulsoup_copy(item))
                yield u"</td>"
                yield u"<td>"
                yield highlight(
                    item.prettify(),
                    HtmlLexer(),
                    HtmlFormatter(noclasses=True),
                )
                yield u"</td>"
                yield u"</tr>"
            yield "</table>"
        return u''.join(__repr_html(self))

    def __getslice__(self, *args, **kwargs):
        return BeautifulSoupList(
            super(BeautifulSoupList, self).__getslice__(*args, **kwargs))


def wrap_findall(function):
    def findall_wrapper(*args, **kwargs):
        return BeautifulSoupList(function(*args, **kwargs))
    return findall_wrapper


def p(url):
    if requests is not None:
        return BeautifulSoup(requests.get(url).content)
    return BeautifulSoup(urlopen(url).read())


def monkey_patch_beautiful_soup():
    BeautifulSoup._repr_html_ = render
    Tag._repr_html_ = render

    if bs4:
        BeautifulSoup.find_all = wrap_findall(BeautifulSoup.find_all)
        Tag.find_all = wrap_findall(Tag.find_all)
    else:
        BeautifulSoup.findAll = wrap_findall(BeautifulSoup.findAll)
        Tag.findAll = wrap_findall(Tag.findAll)

    return BeautifulSoup, Tag


def load_ipython_extension(ipython):
    print("Monkey patch BeautifulSoup with custom rendering")
    monkey_patch_beautiful_soup()

    to_push = ["BeautifulSoup", "urlopen", "p",
               "configure_ipython_beautifulsoup"]

    print("See `configure_ipython_beautifulsoup?` for configuration"
          " information")

    print("Push 'BeautifulSoup' of '%s' into current context" %
        ("bs4" if bs4 else "BeautifulSoup"))

    print("Push 'urlopen' of 'urllib2' into current context")
    print("Push 'p' shortcut into current context")

    try:
        import requests
        requests  # pyflakes
        print("Push 'requests' into current context")
        to_push.append('requests')
    except ImportError:
        pass

    ipython.push(to_push)
