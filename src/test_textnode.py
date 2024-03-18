import unittest
from textnode import (
    TextNode,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

node = TextNode("This is a text node", text_type_bold)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node2 = TextNode("This is a text node", text_type_code)
        self.assertNotEqual(node, node2)
    
    def test_eq_false2(self):
        node2 = node2 = TextNode("This is a text node2", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node_url = TextNode("This is a text node", text_type_italic, "https://here-is-some-url.com")
        node_url2 = TextNode("This is a text node", text_type_italic, "https://here-is-some-url.com")
        self.assertEqual(node_url, node_url2)
        
    def test_not_eq_url(self):
        node2 = TextNode("This is a text node", "bold", 'https://here-is-some-url.com')
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        self.assertEqual("TextNode(This is a text node, bold, None)", repr(node))

if __name__ == "__main__":
    unittest.main()