import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_eq2(self):
        node = TextNode("Sample text", "underline", "https://www.google.com")
        node2 = TextNode("Sample text", "underline", "https://www.google.com")
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("Sample text", "italic", "https://www.google.com")
        node2 = TextNode("Sample text", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)
        
    def test_not_eq2(self):
        node = TextNode("Sample text", "italic")
        node2 = TextNode("Sample text", "bold")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("Sample text", "italic", "www.google.com")
        self.assertEqual(repr(node), "TextNode(Sample text, italic, www.google.com)")

if __name__ == "__main__":
    unittest.main()