from UserList import UserList
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup, Tag


def render(self):
    to_return = str(self)
    to_return += "<hr/>"
    to_return += highlight(self.prettify(), HtmlLexer(), HtmlFormatter(noclasses=True)).encode("Utf-8")
    return to_return


class BeautifulSoupList(UserList):
    def _repr_html_(self):
        to_return = "<table>"
        to_return += "<tr><th>Index</th><th>Render</th><th>source</th></tr>"
        for num, item in enumerate(self):
            to_return += "<tr>"
            to_return += "<td>" + str(num) + "</td>"
            to_return += "<td>" + str(item) + "</td>"
            to_return += "<td>" + highlight(item.prettify(), HtmlLexer(), HtmlFormatter(noclasses=True)).encode("Utf-8") + "</td></tr>"
            to_return += "</tr>"

        return to_return + "</table>"

    def __getslice__(self, *args, **kwargs):
        return BeautifulSoupList(super(BeautifulSoupList, self).__getslice__(*args, **kwargs))


def wrap_findAll(function):
    def findAll_wrapper(*args, **kwargs):
        return BeautifulSoupList(function(*args, **kwargs))
    return findAll_wrapper


def load_ipython_extension(ipython):
    print "Monkey patch BeautifulSoup with custom rendering"
    BeautifulSoup._repr_html_ = render
    BeautifulSoup.findAll = wrap_findAll(BeautifulSoup.findAll)

    Tag._repr_html_ = render
    Tag.findAll = wrap_findAll(Tag.findAll)
    from urllib2 import urlopen
    print "Push 'BeautifulSoup' of 'BeautifulSoup' into current context"
    print "Push 'urlopen' of 'urllib2' into current context"
    ipython.push(["BeautifulSoup", "urlopen"])
