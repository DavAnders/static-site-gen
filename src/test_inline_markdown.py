import unittest
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code
from inline_markdown import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiters(self):
        nodes = [TextNode("Just some text", text_type_text)]
        self.assertEqual(split_nodes_delimiter(nodes, "**", text_type_bold), nodes)

    def test_single_delimiter_pair(self):
        nodes = [TextNode("This is **bold** text", text_type_text)]
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text", text_type_text),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", text_type_bold), expected)

    def test_multiple_delimiter_pairs(self):
        nodes = [TextNode("This **is** some **bold** text", text_type_text)]
        expected = [
            TextNode("This ", text_type_text),
            TextNode("is", text_type_bold),
            TextNode(" some ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text", text_type_text),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", text_type_bold), expected)

    def test_unmatched_delimiters(self):
        nodes = [TextNode("This is **bold text", text_type_text)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", text_type_bold)


if __name__ == '__main__':
    unittest.main()
