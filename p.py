from UserList import UserList
from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup, Tag


def render(self):
    return "<style>" + HtmlFormatter().get_style_defs('.highlight') + "</style>" + str(self) + "<hr/>" + highlight(self.prettify(), HtmlLexer(), HtmlFormatter()).encode("Utf-8")


class BeautifulSoupList(UserList):
    def _repr_html_(self):
        to_return = "<style>" + HtmlFormatter().get_style_defs('.highlight') + "</style>"
        to_return += "<table>"
        for num, item in enumerate(self):
            to_return += "<tr><td>" + str(num) + "</td><td>" + str(item) + "</td><td>" + highlight(item.prettify(), HtmlLexer(), HtmlFormatter()).encode("Utf-8") + "</td></tr>"

        return to_return + "</table>"

def wrap_findAll(function):
    def findAll_wrapper(*args, **kwargs):
        return BeautifulSoupList(function(*args, **kwargs))
    return findAll_wrapper


BeautifulSoup._repr_html_ = render
BeautifulSoup.findAll = wrap_findAll(BeautifulSoup.findAll)

Tag._repr_html_ = render
Tag.findAll = wrap_findAll(Tag.findAll)
