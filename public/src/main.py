from node_conversions import *
import re


def main():
    block1 =  "```\n" \
            "def hello_world():\n" \
            "   print('hello world')\n" \
            "```"
    block2 = "> some profound quote\n" \
            "> -author"
    print(re.sub(r'^>\s', '', block2, flags=re.MULTILINE))

if __name__ == "__main__":
    main()