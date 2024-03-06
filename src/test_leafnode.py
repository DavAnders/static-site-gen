import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_render_as_text(self):
        leaf_node = LeafNode(None, "This is some raw text.")
        self.assertEqual(leaf_node.to_html(), "This is some raw text.")

    def test_render_with_tag_and_value(self):
        leaf_p = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_p.to_html(), "<p>This is a paragraph of text.</p>")

    def test_render_with_tag_value_and_props(self):
        leaf_a = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
        self.assertEqual(leaf_a.to_html(), '<a href="https://www.boot.dev">Click me!</a>')

    def test_render_with_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode("div", None)

    def test_render_with_missing_tag(self):
        leaf_node = LeafNode(None, "Raw text with no tag.")
        self.assertEqual(leaf_node.to_html(), "Raw text with no tag.")

if __name__ == "__main__":
    unittest.main()