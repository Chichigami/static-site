import os, re
from shutil import rmtree, copytree, copy2
from generate_page import generate_pages_recursive


def main():
    try:
        if os.path.exists('public/'): #always removes the public folder before regenerating
            rmtree('public/')
        os.mkdir('public/')
        copytree("static", "public", dirs_exist_ok=True)
    except Exception as e:
        print(f"Failed to copy tree: {e}")

    generate_pages_recursive('content/', 'templates/template.html', 'public/')

if __name__ == "__main__":
    main()