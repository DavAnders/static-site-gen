from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    new_obj = TextNode('any', 'bold', 'https://www.boot.dev')
    print(new_obj) 

    leaf_p = LeafNode("p", "This is a paragraph of text.")
    leaf_a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf_p.to_html())
    print(leaf_a.to_html())

main()