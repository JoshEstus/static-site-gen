import shutil
import os

from textnode import TextNode, TextType

def main():
    copy_static_to_public()



def copy_static_to_public():
    public_path = "./public/"
    static_path = "./static/"
    if os.path.exists(public_path):
        print("Removing public...")
        shutil.rmtree("./public/")
    else:
        print("public folder does not exist, making dir...")
        os.mkdir(public_path)

    print("Copying static to public...")
    shutil.copytree(static_path, public_path)


main()