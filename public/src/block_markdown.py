import re

from textnode import *
from htmlnode import *
from typing import List

def markdown_to_blocks(document: str) -> List[str]:
    splitted = document.split('\n\n')
    blocks = []
    for sentence in splitted:
        blocks.append(sentence.lstrip())
    return blocks