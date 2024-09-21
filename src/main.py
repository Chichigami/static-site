import os, re
from shutil import rmtree, copy2
from generate_page import generate_pages_recursive


def main():
    #delete files in destination
    #recursively copies everything from start to destination
    ## for file/dir in start
    ## if dir & dir doesn't exist then make dir
    ## if file exists don't copy
    ## else copy file
    if os.path.exists('public/'): #always removes the public folder
        rmtree('public/')
    os.mkdir('public/')
    paths_to_visit = ['static/']
    while paths_to_visit:
        dirs = paths_to_visit.pop()
        for dir in os.listdir(dirs):
            if os.path.isdir(f"{dirs}/{dir}"):
                paths_to_visit.append(os.path.join(dirs, dir))
                os.mkdir(f'{re.sub(r'^(static/)', 'public/', dirs)}/{dir}')
            else:
                copy2(f'{dirs}/{dir}', f'{re.sub(r'^(static/)', 'public/', dirs)}/{dir}')

    generate_pages_recursive('content/', 'template.html', 'public/')
    

if __name__ == "__main__":
    main()