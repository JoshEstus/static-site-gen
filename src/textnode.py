from enum import Enum

class TextType(Enum):
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    TEXT = "text"


class TextNode():

    def __init__(self, text, text_type, url = None):
        if not isinstance(text_type, TextType):
            raise TypeError(f"text_type must be an instance of TextType Enum, not {type(text_type)}")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
