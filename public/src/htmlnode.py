from typing import Self

class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: Self = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return None
        result = ""
        for key, value in self.props.items():
            result += f'{key}="{value}" '
        return result.rstrip(' ')
    
    def __eq__(self, other: Self) -> bool:
        return (isinstance(self, type(other))
                and self.tag == other.tag 
                and self.value == other.value 
                and self.children == other.children 
                and self.props == other.props)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    #A leafnode is a type of HTMLNode that represents a single HTML tag with no children
    #example: <p> This is a paragraph text.</p>
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        #if self.value is None then raise ValueError
        #if self.tag is None then return value raw text
        #render html tag
        #LeafNode("p", "This is a paragraph of text.") -> <p>This is a paragraph of text.</p>
        #LeafNode("a", "Click me!", {"href": "https://www.google.com"}) -> <a href="https://www.google.com">Click me!</a>

        if self.value is None:
            raise ValueError("All leafnodes must have a value")
        if self.tag is None:
            return self.value
        #if there are no links
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>'
    
    def __eq__(self, other: Self) -> bool:
        return super().__eq__(other)

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
        