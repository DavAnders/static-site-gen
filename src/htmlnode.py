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