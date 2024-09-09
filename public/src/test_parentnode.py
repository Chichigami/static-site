import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):
    def test_default(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"), 
                LeafNode(None, "Normal text"), 
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
             ],
             )
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        actual = node.to_html()
        self.assertEqual(actual, expected)

    def test_parent_in_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"), 
                LeafNode(None, "Normal text"), 
                LeafNode("i", "italic text"),
                ParentNode("p",
                           [
                            LeafNode("b", "Bold text"), 
                            LeafNode(None, "Normal text"), 
                            LeafNode("i", "italic text"),
                            LeafNode(None, "Normal text"),
                            ],
                )
            ],
            )
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>'
        actual = node.to_html()
        self.assertEqual(actual, expected)
    
    def test_default_with_props(self):
        node = ParentNode(
            "a",
            [
                LeafNode("b", "Bold text"), 
                LeafNode(None, "Normal text"), 
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
             ],
             {"href": "https://www.google.com"}
             )
        expected = '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>'
        actual = node.to_html()
        self.assertEqual(actual, expected)

    def test_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_empty_children(self):
        node = ParentNode("p", LeafNode(), )
        with self.assertRaises(TypeError):
            node.to_html()


    def test_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"),LeafNode(None, "Normal text"),])
        with self.assertRaises(ValueError):
            node.to_html()
    
if __name__ == "__main__":
    unittest.main()