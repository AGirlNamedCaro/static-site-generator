import unittest

from htmlnode import (
    HTMLNode
)

node = HTMLNode('p', 'here is the value of the paragraph')

class TestHTMLNode(unittest.TestCase):
    def test_to_HTML(self):
        self.assertRaises(NotImplementedError, node.to_HTML)

    def test_props_to_HTML_with_props(self):
        node = HTMLNode("div", "Hello World!", None, {"href": "https://boot.dev", "target":"_blank"})
        self.assertEqual(node.props_to_HTML(), ' href="https://boot.dev" target="_blank"')
    
    def test_props_to_HTML_with_no_props(self):
        self.assertEqual(node.props_to_HTML(), "")
    



if __name__ == "__main__":
    unittest.main()
