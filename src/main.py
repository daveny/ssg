from helpers import extract_markdown_images, split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

def main():
    # tn = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(repr(tn))

    # hn = HTMLNode("a", "http://index.hu", [HTMLNode("h1", "header value", None, None)], {"href": "https://www.google.com"})
    # print(repr(hn))

    # ln = LeafNode("p", "this is a text", {'class': 'test'})
    # print(repr(ln))

    # text_node = TextNode("Hello, world!", TextType.ITALIC)
    # html_node = text_node_to_html_node(text_node)
    # print(html_node.to_html())

    # text = "This is text with a `code block`"
    # blocks = split_nodes_delimiter(text, '`', TextType.CODE)
    # print(blocks)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    return 0

main()