import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # Tests for HTMLNode
    
    def test_node(self):
        node = HTMLNode("a", "value the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        repr(node)
    
    def test_props(self):
        node = HTMLNode("a", "value the text inside a paragraph", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    # Tests for LeafNode

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

    # Tests for ParentNode

    def test_ParentNode(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(repr(node), 'ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)')

    def test_ParentNode_toHTML(self):
        node = ParentNode("a", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"href": "www.google.com"})
        self.assertEqual(node.to_html(), '<a href="www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>')

    def test_ParentNode_toHTML2(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode("a", "Linked text", {"href": "www.boot.dev", "target": "_blank"}),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(node.to_html(), '<p><b>Bold text</b><a href="www.boot.dev" target="_blank">Linked text</a><i>italic text</i>Normal text</p>')
        
    # Tests from Boot.dev
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()