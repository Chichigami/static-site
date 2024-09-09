from typing import Self

class TextNode():
    def __init__(self, text: str, text_type: str, url: str = None):
        self.text = text
        self.text_type = text_type #bold italics
        self.url = url #link or image

    def __eq__(self, other: Self) -> bool:
        return self.text is other.text and self.text_type is other.text_type and self.url is other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    