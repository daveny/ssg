import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "this is a text", None)
        node2 = LeafNode("p", "this is a text", None)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = LeafNode("p", "this is a text", None)
        node2 = LeafNode("p", "this is a different text", None)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = LeafNode("p", "this is a text", None)
        node2 = LeafNode("h1", "this is a text", None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = LeafNode("p", "this is a text", {"class": "test"})
        self.assertEqual(
            "LeafNode(p, this is a text, {'class': 'test'})", repr(node)
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
