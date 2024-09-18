import re
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    if not re.search(r'^\s*#\s*', markdown):
        raise Exception('no h1 header')
    return re.sub(r'^\s*#\s*', '', markdown)

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_file = open(from_path, 'r')
    temple_file = open(template_path, 'r')
    html_string = markdown_to_html_node(markdown_file).to_html()
    
    title = extract_title(markdown_file)