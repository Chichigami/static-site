import unittest

from extract_markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_default(self):
        md =    """
                # Hello World
                """
        actual = extract_title(md)
        expected = 'Hello World'
        self.assertEqual(actual, expected)
    
    def test_trailing_and_leading_whitespace(self):
        md =    """
                    #    Hello World
                """
        actual = extract_title(md)
        expected = 'Hello World'
        self.assertEqual(actual, expected)
    
    def test_no_header(self):
        md =    """
                Hello World
                """
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()