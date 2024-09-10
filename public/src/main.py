from node_conversions import *


def main():
    test = extract_markdown_link("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
    print(test)

if __name__ == "__main__":
    main()