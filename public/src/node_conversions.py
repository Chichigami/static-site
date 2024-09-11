import re

from textnode import *
from htmlnode import *
from typing import List


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """
    text_type_text = "text" -> LeafNode with no tag, just a raw text value
    text_type_bold = "bold" -> LeafNode with a "b" tag and the text
    text_type_italic = "italic" -> "i" tag, text
    text_type_code = "code" -> "code" tag, text
    text_type_link = "link" -> "a" tag, anchor text, and "href" prop
    text_type_image = "image" -> "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
    """
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

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type) -> List[TextNode]:
    """
    string: This is text with a **bolded phrase** in the middle
    result:
    [
    TextNode("This is text with a ", "text"),
    TextNode("bolded phrase", "bold"),
    TextNode(" in the middle", "text"),
    ]
    advanced: This is an *italic and **bold** word*.
    only want to split text type textnodes
    if no closing delimiter then raise exception
    """
    list_of_textnodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            list_of_textnodes.extend(node)
        else:
            temp = node.text.split(delimiter)
            for i in range(0, len(temp)):
                if i % 2 == 0:
                    list_of_textnodes.append(TextNode(temp[i], text_type_text))
                else:
                    list_of_textnodes.append(TextNode(temp[i], text_type))
               
    return list_of_textnodes

def extract_markdown_images(text: str) -> List[tuple]:
    """
    Arg: string of text
    finds all markdown images
    return: list of tuple of string and url link
    """
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> List[tuple]:
    """
    Arg: string of text
    finds all markdown links
    return: list of tuple of string and url link
    """
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    """
    Args: List of TextNodes
    TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", text_type_text,)
    Return: List of TextNodes
    [
    TextNode("This is text with a link ", text_type_text),
    TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    TextNode(" and ", text_type_text),
    TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
    ]
    """
    list_of_textnodes = []
    for node in old_nodes:
        list_of_tuples = extract_markdown_images(node.text)
        other_stuff = re.replace(r"!\[(.*?)\]\((.*?)\)", node.text)
        print(other_stuff)
    return list_of_textnodes

def split_nodes_link(old_nodes: TextNode) -> List[TextNode]:
    """
    Args: List of TextNodes
    Return: List of Textnodes
    """
    return