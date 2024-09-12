import re

from textnode import *
from htmlnode import *
from typing import List

def markdown_to_blocks(document: str) -> List[str]:
    """
    arg: a string with multiple lines of text
    return: a list of strings where each element is it's own block
    """
    splitted = document.split('\n\n')
    blocks = []
    for sentence in splitted:
        if sentence: #checks if it's empty block
            blocks.append(sentence.strip())
    return blocks

def block_to_block_type(single_block: str) -> str:
    """
    arg: a block of string
    return: a str representing the text_type of block
    """
    validator = []
    for sentence in single_block.split("\n"):
        match sentence:
            case heading if sentence.startswith(r'#{1,6}\s'):
                validator.append("heading")
            case code if sentence.startswith(r'`{3}') and sentence.endswith('`{3}'):
                validator.append("code")
            case quote if sentence.startswith(r'>\s'):
                validator.append("quote")
            case unorder if sentence.startswith(r'(\*|\-)\s'):
                validator.append("unordered_list")
            case order if sentence.startswith(r'[0-9].\s'):
                validator.append("ordered_list")
            case _:
                validator.append("paragraph")
    print(validator)
    if len(set(validator)) != 1:
        return "paragraph"
    return validator[0]