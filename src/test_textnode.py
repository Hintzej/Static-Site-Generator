import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node but different", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, None)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_type_diff(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.google.com")
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "www.google.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()