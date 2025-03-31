import os, re, sys
from shutil import rmtree, copytree, copy2
from generate_page import generate_pages_recursive


def main():
    BASEPATH = sys.argv[1] if len(sys.argv) > 1 else "/"
    try:
        if os.path.exists('docs/'): #always removes the public folder before regenerating
            rmtree('docs/')
        os.mkdir('docs/')
        copytree("static", "docs", dirs_exist_ok=True)
    except Exception as e:
        print(f"Failed to copy tree: {e}")

    generate_pages_recursive('content/', 'templates/template.html', 'docs/', BASEPATH)
    print(BASEPATH)
if __name__ == "__main__":
    main()