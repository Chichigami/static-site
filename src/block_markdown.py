import re
from textnode import *
from htmlnode import LeafNode, ParentNode
from node_conversions import text_node_to_html_node, text_to_textnodes
from typing import List

import re
from typing import List

def markdown_to_blocks(document: str) -> List[str]:
    """
    Splits a Markdown document into blocks, preserving meaningful structure.

    Args:
        document (str): A string with multiple lines of text.
    
    Returns:
        List[str]: A list of strings where each element is a separate block.
    """
    # Use regex to split on two or more consecutive newlines
    blocks = re.split(r'\n\s*\n+', document.strip())

    return blocks

def block_to_block_type(single_block: str) -> str:
    """
    Determines the type of a Markdown block.
    
    Args:
        single_block (str): A block of text.
        
    Returns:
        str: The type of Markdown block (e.g., "heading", "quote", "paragraph").
    """
    sentences = single_block.split('\n')

    # Check if the entire block consists of blockquote lines
    if all(re.match(r'^>\s?', line) for line in sentences):
        return "quote"

    # Check if it's a fenced code block
    if re.match(r'^`{3}.*?', sentences[0]) and re.match(r'.*?`{3}$', sentences[-1]):
        return "code"

    validator = []
    for i, line in enumerate(sentences):
        match line:
            case heading if re.match(r'^#{1,6}\s+', line):
                validator.append("heading")
            case unorder if re.match(r'^\s*(\*|\-)\s', line):
                validator.append("unordered_list")
            case order if re.match(r'^\s*[0-9]+\.\s', line) and int(re.findall(r'[0-9]+', line)[0]) == i + 1:
                validator.append("ordered_list")
            case _:
                return "paragraph"

    return validator[0] if len(set(validator)) == 1 else "paragraph"


def markdown_to_html_node(document: str) -> ParentNode:
    """
    Converts a Markdown document into an HTML node structure.

    Args:
        document (str): The Markdown text.

    Returns:
        ParentNode: The root HTML node.
    """
    node_list = []
    for block in markdown_to_blocks(document):
        block_type = block_to_block_type(block)

        match block_type:
            case "heading":
                heading_count = block.split()[0].count('#')
                node_list.append(ParentNode(f'h{heading_count}', 
                                          text_to_children(re.sub(r'^#{1,6}\s', '', block, flags=re.MULTILINE))
                                          ))
            case "quote":
                # Remove the ">" from each line and join properly
                quote_text = "\n".join([re.sub(r'^>\s?', '', line) for line in block.split('\n')])
                node_list.append(ParentNode('blockquote', text_to_children(quote_text)))
            case "code":
                node_list.append(ParentNode('pre', 
                         [ParentNode('code', text_to_children(block[4:-3]))], 
                                  ))
            case "unordered_list":
                node_list.append(ParentNode('ul',
                                          [ParentNode('li', 
                                                    text_to_children(re.sub(r'^(\*|\-)\s', '', text))) for text in block.split('\n') if text.strip()
                                                    ]
                                          ))
            case "ordered_list":
                node_list.append(ParentNode('ol',
                                          [ParentNode('li',
                                                    text_to_children(re.sub(r'^[0-9]+\.\s', '', text))) for text in block.split('\n') if text.strip()
                                                    ], 
                             ))
            case "paragraph":
                node_list.append(ParentNode('p', text_to_children(block)))
            case _:
                raise Exception("markdown_to_html_gone_wrong")

    return ParentNode('div', node_list)


def text_to_children(texts: str) -> List[LeafNode]:
    children = []
    textnodes = text_to_textnodes(texts)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children