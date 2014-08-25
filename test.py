import unittest
from soup import BeautifulSoup, render, monkey_patch_beautiful_soup
import sys

if sys.version_info[0] == 3:
    PYTHON3 = True
else:
    PYTHON3 = False



class TestIPythonBeautifulSoup(unittest.TestCase):
    global PYTHON3
    @staticmethod
    def read_test_file(filename):
        import codecs
        contents = None
        with codecs.open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
        return contents

    def test_beautifulsoup__repr_html(self):
        contents = self.read_test_file('test.html')
        BeautifulSoup._repr_html_ = render
        soup = BeautifulSoup(contents)
        output = soup._repr_html_()
        self.assertTrue(output)
        if PYTHON3:
            self.assertTrue(isinstance(output, str))
        else:
            self.assertTrue(isinstance(output, unicode))

    def test_monkey_patch_beautiful_soup(self):
        BeautifulSoup_, Tag_ = monkey_patch_beautiful_soup()
        self.assertTrue(BeautifulSoup_)
        self.assertTrue(Tag_)
        self.assertTrue(hasattr(BeautifulSoup_, '_repr_html_'))
        self.assertTrue(hasattr(BeautifulSoup_, '_repr_html_'))

        contents = self.read_test_file('test.html')
        soup = BeautifulSoup_(contents)
        self.assertTrue(hasattr(soup, '_repr_html_'))
        output = soup._repr_html_()
        self.assertTrue(output)
        if PYTHON3:
            self.assertTrue(isinstance(output, str))
        else:
            self.assertTrue(isinstance(output, unicode))

        divs = soup.findAll('div')
        for tag in divs:
            self.assertTrue(hasattr(soup, '_repr_html_'))
            output = tag._repr_html()
            self.assertTrue(output)
        if PYTHON3:
            self.assertTrue(isinstance(output, str))
        else:
            self.assertTrue(isinstance(output, unicode))


if __name__ == '__main__':
    sys.exit(unittest.main())
