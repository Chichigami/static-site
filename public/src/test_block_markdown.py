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


if __name__ == "__main__":
    unittest.main()