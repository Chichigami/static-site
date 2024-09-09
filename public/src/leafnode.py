from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    #A leafnode is a type of HTMLNode that represents a single HTML tag with no children
    #example: <p> This is a paragraph text.</p>
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)