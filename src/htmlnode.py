class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        # An HTMLNode without a tag will just render as raw text
        self.tag = tag
        # An HTMLNode without a value will be assumed to have children
        self.value = value
        # An HTMLNode without children will be assumed to have a value
        self.children = children
        # An HTMLNode without props simply won't have any attributes
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attrs = []
        for key, value in self.props.items():
            attrs.append(f'{key}="{value}"')
        return ' '.join(attrs)
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag=tag, value=value, props=props, children=None)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode requires a value")
        if self.tag is None:
            return self.value
        attrs = f' {self.props_to_html()}' if self.props else ''
        return f'<{self.tag}{attrs}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag.")
        if not children:
            raise ValueError("ParentNode requires at least one child")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        if not self.children:
            raise ValueError("ParentNode requires at least one child")
        children_html = ''.join(child.to_html() for child in self.children)
        return f'<{self.tag}>{children_html}</{self.tag}>'
