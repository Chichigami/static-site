import unittest

from node_conversions import *
from block_markdown import *
from textnode import *
from htmlnode import LeafNode

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

if __name__ == "__main__":
    unittest.main()