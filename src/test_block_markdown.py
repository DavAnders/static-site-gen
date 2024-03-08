from block_markdown import markdown_to_blocks
import unittest

class TestMarkdownToBlocks(unittest.TestCase):

    def test_single_block(self):
        markdown = "This is a single block of text."
        expected = ["This is a single block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_blocks(self):
        markdown = """This is the first block.

This is the second block.

This is the third block."""
        expected = ["This is the first block.", "This is the second block.", "This is the third block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_with_whitespace(self):
        markdown = """
        
        This block has leading and trailing whitespace.
        
        
        """
        expected = ["This block has leading and trailing whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty_and_whitespace_blocks(self):
        markdown = """


        """
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_blocks_separated_by_various_newline_amounts(self):
        markdown = "Block one\n\n\nBlock two\n\n\n\nBlock three"
        expected = ["Block one", "Block two", "Block three"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_mixed_content_blocks(self):
        markdown = """# Heading

Paragraph with **bold** and *italic* text.

- List item 1
- List item 2

> Blockquote"""
        expected = [
            "# Heading",
            "Paragraph with **bold** and *italic* text.",
            "- List item 1\n- List item 2",
            "> Blockquote"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

if __name__ == '__main__':
    unittest.main()