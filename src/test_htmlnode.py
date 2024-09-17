import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_prop_None(self):
        node = HTMLNode()
        actual = node.props_to_html()
        expected = None
        self.assertEqual(actual, expected)
    
    def test_prop_to_html(self):
        node = HTMLNode("tag", "value", None, {"href": "https://www.google.com", "target": "_blank",})
        expected = 'href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(actual, expected)
    
    def test_repr(self):
        child = HTMLNode("a", "this has a href", None, {"href": "https://www.someurl.com/", "target": "hello world",})
        node = HTMLNode("tag", "value", child, {"href": "https://www.google.com", "target": "_blank",})
        expected = "HTMLNode(tag, value, HTMLNode(a, this has a href, None, {'href': 'https://www.someurl.com/', 'target': 'hello world'}), {'href': 'https://www.google.com', 'target': '_blank'})"
        actual = repr(node)
        self.assertEqual(actual, expected)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    

if __name__ == "__main__":
    unittest.main()