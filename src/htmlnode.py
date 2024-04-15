class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_HTML(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_HTML(self):
        if self.props is None:
            return ""
        prop_array = []
        for prop in self.props:
            prop_array.append(f' {prop}="{self.props[prop]}"')
        return  "".join(prop_array)