from inline_markdown import extract_markdown_links, extract_markdown_images
import unittest

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        # Test with a single image
        self.assertEqual(
            extract_markdown_images("This is an ![image](https://google.com/image.png) example."),
            [("image", "https://google.com/image.png")]
        )
        # Test with multiple images
        self.assertEqual(
            extract_markdown_images("Here's an ![image](https://boot.dev/image1.png) and another ![image](https://boot.dev/image2.png)."),
            [("image", "https://boot.dev/image1.png"), ("image", "https://boot.dev/image2.png")]
        )
        # Test with no images
        self.assertEqual(
            extract_markdown_images("This text has no images."),
            []
        )

    def test_extract_markdown_links(self):
        # Test with a single link
        self.assertEqual(
            extract_markdown_links("This is a [link](https://google.com) example."),
            [("link", "https://google.com")]
        )
        # Test with multiple links
        self.assertEqual(
            extract_markdown_links("Here's a [link](https://google.com/page1) and another [link](https://google.com/page2)."),
            [("link", "https://google.com/page1"), ("link", "https://google.com/page2")]
        )
        # Test with no links
        self.assertEqual(
            extract_markdown_links("This text has no links."),
            []
        )

if __name__ == '__main__':
    unittest.main()