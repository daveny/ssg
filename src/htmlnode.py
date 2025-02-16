class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        return " " + " ".join(f"{k}=\"{v}\"" for k, v in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag, self.value, self.children, self.props) == (other.tag, other.value, other.children, self.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}>{self.value}<\\{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag, self.value, self.props) == (other.tag, other.value, other.props)