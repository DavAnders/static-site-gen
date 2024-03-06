import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_no_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.example.com" target="_blank"')

    def test_initialization_without_tag(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_initialization_with_tag_and_value(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_initialization_with_children(self):
        child_node = HTMLNode(tag="li", value="Item 1")
        parent_node = HTMLNode(tag="ul", children=[child_node])
        self.assertEqual(parent_node.tag, "ul")
        self.assertEqual(parent_node.children, [child_node])
        self.assertIsNone(parent_node.value)
        self.assertIsNone(parent_node.props)

if __name__ == "__main__":
    unittest.main()
