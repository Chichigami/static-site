import re
from block_markdown import *

def extract_title(markdown):
    checker = re.findall(r'^\s*#\s*(.*)', markdown)
    if not checker:
        raise Exception('does not contain a h1 title')
    return checker[0]
    

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_file = open(from_path, 'r')
    temple_file = open(template_path, 'r')
    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_to_blocks(markdown_file))
    