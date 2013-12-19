from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup, Tag

def render(self):
    return "<style>" + HtmlFormatter().get_style_defs('.highlight') + "</style>" + str(self) + "<hr/>" + highlight(self.prettify(), HtmlLexer(), HtmlFormatter()).encode("Utf-8")

BeautifulSoup._repr_html_ = render
Tag._repr_html_ = render
