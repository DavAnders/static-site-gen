import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_single_level_nesting(self):
        # Test single level nesting of ParentNode
        parent_node = ParentNode("div", [
            LeafNode("p", "Paragraph 1"),
            LeafNode("p", "Paragraph 2")
        ])
        expected_html = '<div><p>Paragraph 1</p><p>Paragraph 2</p></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_multiple_levels_nesting(self):
        # Test multiple levels of nesting
        parent_node = ParentNode("div", [
            ParentNode("section", [
                LeafNode("p", "Paragraph 1"),
                LeafNode("p", "Paragraph 2")
            ]),
            ParentNode("section", [
                LeafNode("p", "Paragraph 3"),
                LeafNode("p", "Paragraph 4")
            ])
        ])
        expected_html = '<div><section><p>Paragraph 1</p><p>Paragraph 2</p></section><section><p>Paragraph 3</p><p>Paragraph 4</p></section></div>'
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_nested_parent_node(self):
        # Test nesting ParentNode inside another ParentNode
        inner_parent = ParentNode("div", [
            LeafNode("p", "Inner Paragraph 1"),
            LeafNode("p", "Inner Paragraph 2")
        ])
        outer_parent = ParentNode("div", [inner_parent])
        expected_html = '<div><div><p>Inner Paragraph 1</p><p>Inner Paragraph 2</p></div></div>'
        self.assertEqual(outer_parent.to_html(), expected_html)

    def test_empty_children(self):
        # Test creating ParentNode with empty children
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_missing_tag(self):
        # Test creating ParentNode without a tag
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "Paragraph")])

    def test_missing_child(self):
        # Test creating ParentNode without any children
        with self.assertRaises(ValueError):
            ParentNode("div", None)

if __name__ == "__main__":
    unittest.main()