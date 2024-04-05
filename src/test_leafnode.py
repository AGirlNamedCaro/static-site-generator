import unittest

from leafnode import (
    LeafNode
)

node = LeafNode('p', 'here is the value of the paragraph')

class TestLeafNode(unittest.TestCase):
    def test_to_HTML_no_value(self):
        node = LeafNode('p', None)
        self.assertRaises(ValueError, node.to_HTML)

    def test_to_HTML_with_value(self):
        self.assertEqual(node.to_HTML(), '<p>here is the value of the paragraph</p>')
    def test_to_HTML_with_no_tag(self):
        node = LeafNode(None, "insert value here")
        self.assertEqual(node.to_HTML(), 'insert value here')
    def test_to_HTML_with_props(self):
        node = LeafNode('a', "Google", {"href": 'https://www.google.ca', "target": '_blank'} )
        self.assertEqual(node.to_HTML(), '<a href="https://www.google.ca" target="_blank">Google</a>' )

if __name__ == "__main__":
    unittest.main()
