import unittest

from node_conversions import *
from textnode import *
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
        node = TextNode("foo", text_type_text, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode(None, "foo")
        self.assertEqual(actual, expected)
        
    def test_bold(self):
        node = TextNode("foo", text_type_bold, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("b", "foo")
        self.assertEqual(actual, expected)
        
    def test_italic(self):
        node = TextNode("foo", text_type_italic, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("i", "foo")
        self.assertEqual(actual, expected)
    
    def test_code(self):
        node = TextNode("foo", text_type_code, "bar")
        actual = text_node_to_html_node(node)
        expected = LeafNode("code", "foo")
        self.assertEqual(actual, expected)
    
    def test_link(self):
        node = TextNode("Click me!", text_type_link, "https://www.google.com")
        actual = text_node_to_html_node(node)
        expected = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(actual, expected)
    
    def test_image(self):
        node = TextNode("foo", text_type_image, "https://www.someurl.com/")
        actual = text_node_to_html_node(node)
        expected = LeafNode("img", "", {"src": "https://www.someurl.com/", "alt": "foo"})
        self.assertEqual(actual, expected)

class TestSplitTextNode(unittest.TestCase):
    def test_default(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_back_to_back(self):
        node = TextNode("This is text with a `code block``code block2` word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode("", text_type_text),
                    TextNode("code block2", text_type_code),
                    TextNode(" word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_every_other(self):
        node = TextNode("foo `code block` bar `code block2` foobar", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("foo ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" bar ", text_type_text),
                    TextNode("code block2", text_type_code),
                    TextNode(" foobar", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_default_with_bold(self):
        node = TextNode("foo `code block` bar **bold** foobar", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("foo ", text_type_text),
                    TextNode("code block", text_type_code),
                    TextNode(" bar **bold** foobar", text_type_text),
                    ]
        self.assertEqual(actual, expected)

    def test_plain(self):
        node = TextNode("This is text with a word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
                    TextNode("This is text with a word", text_type_text),
                    ]
        self.assertEqual(actual, expected)

# class TestSplitTextNodeLinks(unittest.TestCase):
#     def test_default(self):
#         node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type_text,)
#         actual = split_nodes_link(node)
#         expected = [
#                     TextNode("This is text with a link ", text_type_text),
#                     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#                     TextNode(" and ", text_type_text),
#                     TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
#                     ]
#         self.assertEqual(actual, expected)

class TestSplitTextNodeImages(unittest.TestCase):
    def test_default(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", text_type_text,)
        actual = split_nodes_image([node])
        expected = [
                    TextNode("This is text with a link ", text_type_text),
                    TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                    TextNode(" and ", text_type_text),
                    TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
                    ]
        self.assertEqual(actual, expected)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()