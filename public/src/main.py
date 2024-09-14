from node_conversions import *
import re


def main():
    node = HTMLNode('div', None, 
                    HTMLNode('pre', None, 
                             HTMLNode('code', None, [
                                 HTMLNode(None, 'first code', None, None),
                                 HTMLNode(None, 'second code', None, None),
                                 HTMLNode(None, 'third code', None, None),
                             ], 
                                      None), None), None)
    text = '### hello world'
    count = text.split()[0].count('#')
    print(count)

if __name__ == "__main__":
    main()