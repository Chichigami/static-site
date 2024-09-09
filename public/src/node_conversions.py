from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    # text_type_text = "text" -> LeafNode with no tag, just a raw text value
    # text_type_bold = "bold" -> LeafNode with a "b" tag and the text
    # text_type_italic = "italic" -> "i" tag, text
    # text_type_code = "code" -> "code" tag, text
    # text_type_link = "link" -> "a" tag, anchor text, and "href" prop
    # text_type_image = "image" -> "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)

    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "" , {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("text_node_text_type doesn't match")
    