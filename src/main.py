from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

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



def main():
    new_obj = TextNode('any', 'bold', 'https://www.boot.dev')
    print(new_obj) 

    leaf_p = LeafNode("p", "This is a paragraph of text.")
    leaf_a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf_p.to_html())
    print(leaf_a.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    test = node.to_html()
    print(test)

main()