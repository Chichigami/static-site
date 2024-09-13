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
    sentences = single_block.split('\n')
    if re.match(r'^`{3}.*?', sentences[0]) and re.match(r'.*?`{3}$', sentences[len(sentences)-1]):
        return "code"
    
    for i in range(0, len(sentences)):
        match sentences[i]:
            case heading if re.match(r'^#{1,6}\s*?', sentences[i]):
                validator.append("heading")
            case quote if re.match(r'^\s*>\s', sentences[i]):
                validator.append("quote")
            case unorder if re.match(r'^\s*(\*|\-)\s', sentences[i]):
                validator.append("unordered_list")
            case order if re.match(r'^\s*[0-9]+\.\s', sentences[i]) and int(re.findall(r'[0-9]+', sentences[i])[0]) == i+1: #if line starts w/ 'number. ' and that number == 1,2,...,n
                validator.append("ordered_list")
            case _: #if a line is ever not one of the types
                return "paragraph"

    if len(set(validator)) != 1: #if the list of types has more than 1 type then
        return "paragraph"
    return validator[0]