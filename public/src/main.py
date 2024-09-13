from node_conversions import *
import re


def main():
    text = "```hello world```"
    if re.match(r'^`{3}.*?', text) and re.match(r'.*?`{3}$', text):
        print("true")

if __name__ == "__main__":
    main()