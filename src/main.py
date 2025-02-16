from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from htmlnode import LeafNode

def main():
    tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(repr(tn))

    hn = HTMLNode("a", "http://index.hu", [HTMLNode("h1", "header value", None, None)], {"href": "https://www.google.com"})
    print(repr(hn))

    ln = LeafNode("p", "this is a text", {'class': 'test'})
    print(repr(ln))

    return 0

main()