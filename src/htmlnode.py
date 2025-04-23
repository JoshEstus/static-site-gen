class HTMLNode():

    def __init__(self, tag = None, value = None, children = None, props = None):
        """
            tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            children - A list of HTMLNode objects representing the children of this node
            props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        ret_str = ""
        for prop in self.props:
            ret_str += f' {prop}="{self.props[prop]}"'

        return ret_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"