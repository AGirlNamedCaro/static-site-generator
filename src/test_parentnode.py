import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
class TestParentNode(unittest.TestCase):

    def test_to_html_no_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],)
        self.assertRaises(ValueError, node.to_HTML)
    def test_to_html_no_children(self):
        node = ParentNode(
                'p',
                None)
        self.assertRaises(ValueError, node.to_HTML)
    def test_to_html_many_children(self):
        self.assertEqual(node.to_HTML(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", 'grandkid')
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_HTML(), "<div><span><b>grandkid</b></span></div>")


if __name__ == "__main__":
    unittest.main()