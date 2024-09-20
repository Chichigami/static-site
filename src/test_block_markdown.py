import unittest

from node_conversions import *
from block_markdown import *
from textnode import *
from htmlnode import *

class TestSplitBlockMarkdown(unittest.TestCase):
    def test_default(self):
        text =  "# This is a heading\n\n" \
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" \
                "* This is the first list item in a list block\n" \
                "* This is a list item\n" \
                "* This is another list item"
        actual = markdown_to_blocks(text)
        expected = ['# This is a heading',
                    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                    '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        self.assertEqual(actual, expected)

    def test_default_with_tabs_and_spaces(self):
        text =  "# This is a heading\n\n" \
                " This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" \
                " * This is the first list item in a list block\n" \
                "   * This is a list item\n" \
                "* This is another list item"
        actual = markdown_to_blocks(text)
        expected = ['# This is a heading',
                    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                    '* This is the first list item in a list block\n   * This is a list item\n* This is another list item']
        self.assertEqual(actual, expected)

class TestBlockIdentifier(unittest.TestCase):
    def test_default(self):
        text = '* This is the first list item in a list block\n   * This is a list item\n* This is another list item'
        actual = block_to_block_type(text)
        expected = 'unordered_list'
        self.assertEqual(actual, expected)

    def test_code_block(self):
        text = '```hello world\n foobar\n code block```'
        actual = block_to_block_type(text)
        expected = 'code'
        self.assertEqual(actual, expected)
    
    def test_quote_block(self):
        text =  "> hello\n" \
                "> world\n" \
                "> foo\n" \
                "> bar\n" \
                "> foobar "
        actual = block_to_block_type(text)
        expected = 'quote'
        self.assertEqual(actual, expected)

    def test_heading_block(self):
        text =  "# hello\n" \
                "## world\n" \
                "### foo\n" \
                "#### bar\n" \
                "##### foobar \n" \
                "###### six"
        actual = block_to_block_type(text)
        expected = 'heading'
        self.assertEqual(actual, expected)

    def test_unordered_block(self):
        text =  "- hello\n" \
                "* world\n" \
                "- foo\n" \
                "* bar\n" \
                "- foobar \n" \
                "* ten"
        actual = block_to_block_type(text)
        expected = 'unordered_list'
        self.assertEqual(actual, expected)

    def test_ordered_block(self):
        text =  "1. hello\n" \
                "2. world\n" \
                "3. foo\n" \
                "4. bar\n" \
                "5. foobar \n" \
                "6. ten"
        actual = block_to_block_type(text)
        expected = 'ordered_list'
        self.assertEqual(actual, expected)

    def test_out_of__order_ordered_block(self):
        text =  "1. hello\n" \
                "10. world\n" \
                "3. foo\n" \
                "4. bar\n" \
                "5. foobar \n" \
                "6. ten"
        actual = block_to_block_type(text)
        expected = 'paragraph'
        self.assertEqual(actual, expected)

    def test_out_mixed_blocks(self):
        text =  "> hello\n" \
                "* world\n" \
                "- foo\n" \
                "> bar\n" \
                "> foobar \n" \
                "> ten"
        actual = block_to_block_type(text)
        expected = 'paragraph'
        self.assertEqual(actual, expected)


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_code(self):
        text =  """
```
def hello_world():
    print("hello world")
```
"""
        actual = markdown_to_html_node(text).to_html()
        expected = '<div><pre><code>\ndef hello_world():\n    print("hello world")\n</code></pre></div>'
        self.assertEqual(actual, expected)
    
    def test_quotes(self):
        text =  """
> some profound provereb
> confucious says something idk
> -author's name
"""
        actual = markdown_to_html_node(text).to_html()
        expected = "<div><blockquote>some profound provereb\nconfucious says something idk\n-author's name</blockquote></div>"
        self.assertEqual(actual, expected)

    def test_ol(self):
        text =  """
1. some profound proverb
2. confucious says something idk
3. author's name
"""
        actual = markdown_to_html_node(text).to_html()
        expected = "<div><ol><li>1. some profound proverb</li><li>2. confucious says something idk</li><li>3. author's name</li></ol></div>"
        self.assertEqual(actual, expected)

    def test_giga_block(self):
        text =  """
## Big ass heading

> iOS 18 release
> -Gary Feng

```
code block
print('foobar')
```

1. buy new shaver

- Oranges

paragraph `code here as well?` here
"""
        actual = markdown_to_html_node(text).to_html()
        expected = \
        "<div><h2>Big ass heading</h2><blockquote>iOS 18 release\n-Gary Feng</blockquote><pre><code>\ncode block\nprint('foobar')\n</code></pre><ol><li>1. buy new shaver</li></ol><ul><li>Oranges</li></ul><p>paragraph <code>code here as well?</code> here</p></div>"
        self.assertEqual(actual, expected)

    def test_other(self):
        md = """
> block quote
> kekw

`code line`

```
code block
```

1. ol ol ol
2. abc

- ul ul ul
"""
        actual = markdown_to_html_node(md).to_html()
        expected = '<div><blockquote>block quote\nkekw</blockquote><p><code>code line</code></p><pre><code>\ncode block\n</code></pre><ol><li>1. ol ol ol</li><li>2. abc</li></ol><ul><li>ul ul ul</li></ul></div>'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()