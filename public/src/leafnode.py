from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    #A leafnode is a type of HTMLNode that represents a single HTML tag with no children
    #example: <p> This is a paragraph text.</p>
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.children = None #not allowed to have children
        self.props = props

    def to_html(self):
        #if self.value is None then raise ValueError
        #if self.tag is None then return value raw text
        #render html tag
        #LeafNode("p", "This is a paragraph of text.") -> <p>This is a paragraph of text.</p>
        #LeafNode("a", "Click me!", {"href": "https://www.google.com"}) -> <a href="https://www.google.com">Click me!</a>

        if self.value == None:
            raise ValueError("All leafnodes must have a value")
        if self.tag == None:
            return self.value
        #if there are no links
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>'