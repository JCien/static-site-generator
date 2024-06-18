import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode("a", "value the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        repr(node)
    
    def test_props(self):
        node = HTMLNode("a", "value the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_LeafNode(self):
        node = LeafNode("a", "Hello World!", {"href": "https://www.boot.dev", "target": "_blank"})
        repr(node.to_html())

    def test_LeafNode2(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_LeafNode_NoTag(self):
        node = LeafNode(None, "Testing no tag")
        self.assertEqual(node.to_html(), "Testing no tag")
    
    def test_LeafNode_NoValue(self):
        node = LeafNode("a", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
    unittest.main()