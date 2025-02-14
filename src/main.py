from textnode import TextNode
from textnode import TextType

def main():
    tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(repr(tn))

main()