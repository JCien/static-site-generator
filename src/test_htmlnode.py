import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode("a", "value the text inside a paragraph", {"href": "https://www.google.com", "target": "_blank"})
        repr(node)
    
    def test_props(self):
        node = HTMLNode("a", "value the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        node.props_to_html()

if __name__ == "__main__":
    unittest.main()