import unittest
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
import re

class TestMarkdownSplitting(unittest.TestCase):

    def test_split_nodes_image(self):
        input_nodes = [
            TextNode("This is text with an ![image](https://google.com/image.png) and another ![second image](https://google.com/second.png)", text_type_text),
        ]
        expected_output = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://google.com/image.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://google.com/second.png"),
        ]
        self.assertEqual(split_nodes_image(input_nodes), expected_output)

    def test_split_nodes_link(self):
        input_nodes = [
            TextNode("This is text with a [link](https://boot.dev) and another [second link](https://boot.dev/second)", text_type_text),
        ]
        expected_output = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
            TextNode(" and another ", text_type_text),
            TextNode("second link", text_type_link, "https://boot.dev/second"),
        ]
        self.assertEqual(split_nodes_link(input_nodes), expected_output)

    # Tests for cases with no images/links
    def test_no_images(self):
        input_nodes = [TextNode("No images here!", text_type_text)]
        self.assertEqual(split_nodes_image(input_nodes), input_nodes)

    def test_no_links(self):
        input_nodes = [TextNode("No links here!", text_type_text)]
        self.assertEqual(split_nodes_link(input_nodes), input_nodes)

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
