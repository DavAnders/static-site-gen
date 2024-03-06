class TextNode:

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        # Check if other is TextNode
        if isinstance(other, TextNode):
            # Compare properties
            return (self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url)
        return NotImplemented
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"