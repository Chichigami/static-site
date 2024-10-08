import re
import os
from block_markdown import *

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    if 'heading' not in [block_to_block_type (block) for block in blocks]:
        raise Exception('No h1 heading')
    for block in blocks:
        if re.match(r'^\s*#{1}\s(.*)', block):
            title = re.sub(r'^\s*#{1}\s*', '', block)
    return title
    

def generate_page(from_path, template_path, dest_path):
    """
    args: 3 different file paths
    read the markdown
    convert the markdown to an html string
    feed the html strings into the template
    generate a new file
    return: make a new file at the dest_path
    """
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown_file = open(from_path, 'r').read()
    html_string = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)

    template_file = open(template_path, 'r').read()
    template_file = template_file.replace('{{ Title }}', title)
    template_file = template_file.replace('{{ Content }}', html_string)

    open(f'{dest_path}'.replace('md', 'html'), 'w').write(template_file)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    paths_to_visit = [dir_path_content]
    while paths_to_visit:
        current_dir = paths_to_visit.pop()
        for file_or_dir in os.listdir(current_dir):
            current = os.path.join(current_dir, file_or_dir)
            if os.path.isdir(current):
                paths_to_visit.append(current)
                os.mkdir(os.path.join(dest_dir_path, file_or_dir))
            if os.path.splitext(file_or_dir)[1] == '.md':
                generate_page(current, template_path, f'{re.sub(dir_path_content, dest_dir_path, current)}')
            
