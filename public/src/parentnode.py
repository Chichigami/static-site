from htmlnode import HTMLNode
from leafnode import LeafNode
from typing import Self, Type

class ParentNode(HTMLNode):
    #child of HTMLNode class
    #no value
    #children is a must
    def __init__(self, tag: str, children, props: dict = None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self) -> str:
        #if no tag then raise ValueError
        #if no children raise ValueError
        #return html str including children recursively 
        if self.tag is None:
            raise ValueError("ParentNode with no tag")
        if self.children is None:
            raise ValueError("ParentNode can't parent without a child")
        
        child_string = ''
        for child in self.children:
            child_string += child.to_html()

        if self.props is None:
            return f'<{self.tag}>{child_string}</{self.tag}>'
        else:
            return f'<{self.tag} {self.props_to_html()}>{child_string}</{self.tag}>'