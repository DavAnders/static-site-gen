import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "bold")
        self.assertNotEqual(node1, node2)

    def test_not_eq_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("Test node", "plain", "https://boot.dev")
        expected_repr = "TextNode('Test node', 'plain', 'https://boot.dev')"
        self.assertEqual(repr(node), expected_repr)
    
    def test_eq_with_and_without_url(self):
        node_with_url = TextNode("Some text", "link", "https://boot.dev")
        node_without_url = TextNode("Some text", "link")
        # Check if nodes are considered equal despite one having a URL and the other not
        self.assertEqual(node_with_url, node_without_url)


if __name__ == "__main__":
    unittest.main()
