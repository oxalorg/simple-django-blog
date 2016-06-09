import mistune
import unittest
from textwrap import dedent
from slugify import slugify


class Slugger():
    def slug(self, text):
        return slugify(text)


class Markdown2Html():
    def __init__(self):
        renderer = mistune.Renderer(hard_wrap=True)
        self.markdown = mistune.Markdown()

    def convert(self, md):
        return self.markdown(md)


class UtilTest(unittest.TestCase):
    def test_md2html(self):
        md = dedent("""\
        # Test
        **bold** *emphasized*
        ![](img-source.com)
        """)
        html = Markdown2Html().convert(md)
        self.assertEqual(
            html,
            '<h1>Test</h1>\n<p><strong>bold</strong> <em>emphasized</em>\n<img src="img-source.com" alt=""></p>\n')


if __name__ == '__main__':
    unittest.main()
