import unittest
from markdown_blocks import markdown_to_blocks
from markdown_blocks import (
    block_type_code,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
    block_type_heading,
    block_type_paragraph,
    block_to_block_type
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_string = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(markdown_string)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    def test_block_to_block_type(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "###### heading numero 6"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```code goes here ```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> Wisdom  \n> another piece of wisdom"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = '* unordered list item 1\n * item 2 '
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. don't pick up the phone, you know he's only calling because he's drunk and alone\n 2. Don't let him in, you'll have to kick him out again"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    