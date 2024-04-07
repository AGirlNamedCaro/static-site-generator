from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_HTML(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: Tag required")
        elif self.children is None:
            raise ValueError("Invalid HTML: Children required")
        children_html = ""
        for child in self.children:
            children_html += child.to_HTML()
        return f"<{self.tag}{self.props_to_HTML()}>{children_html}</{self.tag}>"





