from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    if text_type == 'text':
        # raw text value, no tag
        return LeafNode(None, text_node.text)
    elif text_type == 'bold':
        # convert to leaf with 'b' tag
        return LeafNode('b', text_node.text)
    elif text_type == 'italic':
        # convert to leaf with 'i' tag
        return LeafNode('i', text_node.text)
    elif text_type == 'code':
        # convert to leaf with 'code' tag
        return LeafNode('code', text_node.text)
    elif text_type == 'link':
        # convert to leaf with 'a' tag, 'href' prop
        props = {'href': text_node.url}
        return LeafNode('a', text_node.text, props)
    elif text_type == 'image':
        # convert to leaf with 'img' tag, 'src' and 'alt' props
        props = {'src': text_node.url, 'alt': text_node.text}
        return LeafNode('img', '', props)
    else:
        raise ValueError('Invalid text type {}'.format(text_type))

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        # Check if other is TextNode
        if isinstance(other, TextNode):
            # Compare properties
            return (self.text == other.text and
                    self.text_type == other.text_type)
        return NotImplemented
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"