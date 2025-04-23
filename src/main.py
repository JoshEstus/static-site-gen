from textnode import TextNode, TextType

def main():
    text = TextNode("Some text", TextType.Link, "https://www.google.com")
    print(text)


main()