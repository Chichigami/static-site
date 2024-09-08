from typing import Self

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type #bold italics
        self.url = url #link or image

    def __eq__(self, other: Self) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"   