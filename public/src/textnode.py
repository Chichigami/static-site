from typing import Self


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text: str, text_type, url: str = None):
        self.text = text
        self.text_type = text_type #bold italics
        self.url = url #link or image

    def __eq__(self, other: Self) -> bool:
        return (self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type}, {self.url})"
    
    