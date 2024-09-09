import unittest
from node_conversions import text_node_to_html_node
from textnode import TextNode
from htmlnode import LeafNode

class TestNodeConversion(unittest.TestCase):
    def test_no_tag(self):
        node = TextNode("foo", None, "bar")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_not_possible_tag(self):
        node = TextNode("foo", "hello", "bar")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

    def test_text(self):
        node = TextNode("foo", "text", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode(None, "foo")
        self.assertEqual(actual, expected)
        
    def test_bold(self):
        node = TextNode("foo", "bold", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("b", "foo")
        self.assertEqual(actual, expected)
        
    def test_italic(self):
        node = TextNode("foo", "italic", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("i", "foo")
        self.assertEqual(actual, expected)
    
    def test_code(self):
        node = TextNode("foo", "code", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("code", "foo")
        self.assertEqual(actual, expected)
    
    def test_link(self):
        node = TextNode("foo", "link", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("a", "foo", {"href": "bar"})
        self.assertEqual(actual, expected)
    
    def test_image(self):
        node = TextNode("foo", "image", "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("img", "", {"src": "bar", "alt": "foo"})
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()