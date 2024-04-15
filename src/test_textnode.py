import unittest
from textnode import (
    TextNode,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_text,
    text_type_link,
    text_type_image
)
from leafnode import LeafNode

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

    def test_text_node_to_html_node_raw(self):
        node = TextNode("This is a text node", text_type_text)
        leafNode = LeafNode(None, "This is a text node")
        self.assertEqual(node.text_node_to_html_node().value, leafNode.value)
        self.assertEqual(node.text_node_to_html_node().tag, leafNode.tag)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", text_type_bold)
        leafNode = LeafNode("b", "This is a text node")
        self.assertEqual(node.text_node_to_html_node().value, leafNode.value)
        self.assertEqual(node.text_node_to_html_node().tag, leafNode.tag)
    def test_text_node_to_html_node_img(self):
         node = TextNode("this is an image", text_type_image, "url link goes here")
         leafNode = LeafNode("img", "", {"src": "url link goes here", "alt": "this is an image"})
         self.assertEqual(node.text_node_to_html_node().value, leafNode.value)
         self.assertEqual(node.text_node_to_html_node().tag, leafNode.tag)
         self.assertEqual(node.text_node_to_html_node().props["src"], leafNode.props["src"])

    def test_text_node_to_html_node_link(self):
         node = TextNode("this is a link", text_type_link, "url link goes here")
         leafNode = LeafNode("a", "this is a link", {"href": "url link goes here"})
         self.assertEqual(node.text_node_to_html_node().value, leafNode.value)
         self.assertEqual(node.text_node_to_html_node().tag, leafNode.tag)
         self.assertEqual(node.text_node_to_html_node().props["href"], leafNode.props["href"])

    def test_text_node_to_html_node_no_type_found(self):
         node = TextNode("This will raise an error", "emoji")
         self.assertRaises(ValueError, node.text_node_to_html_node)




if __name__ == "__main__":
    unittest.main()