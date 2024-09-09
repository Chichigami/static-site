import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = '<p>This is a paragraph of text.</p>'
        actual = node.to_html()
        self.assertEqual(actual, expected)
    
    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        actual = node.to_html()
        self.assertEqual(actual, expected)

    def test_empty_leafnode(self):
        with self.assertRaises(TypeError):
            LeafNode()

    def test_value_none(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = LeafNode(None, "foo", {"href": "https://www.someurl.com"})
        expected = 'foo'
        actual = node.to_html()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()