import unittest

from htmlnode import ParentNode


import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node1 = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        node2 = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        self.assertEqual(node1, node2)
    
    def test_eq_false(self):
        node1 = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        node2 = ParentNode("div", [LeafNode("p", "Hello")], {"class": "different"})
        self.assertNotEqual(node1, node2)
    
    def test_eq_false2(self):
        node1 = ParentNode("div", [LeafNode("p", "Hello")], {"class": "container"})
        node2 = ParentNode("div", [LeafNode("span", "Hello")], {"class": "container"})
        self.assertNotEqual(node1, node2)
    
    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "Hello", {"class": "text"})], {"class": "container"})
        self.assertEqual(repr(node), "ParentNode(div, children: [LeafNode(p, Hello, {'class': 'text'})], {'class': 'container'})")
    
    def test_to_html_no_children(self):
        node = ParentNode("div", [], {"class": "container"})
        with self.assertRaises(ValueError):
            node.to_html()
        
    def test_to_html_multiple_children(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello"),
            LeafNode("span", "World")
        ], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>Hello</p><span>World</span></div>')
        
if __name__ == "__main__":
    unittest.main()