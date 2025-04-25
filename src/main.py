import shutil
import os
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = "/"
    if len(sys.argv) == 2:
        basepath = sys.argv[1]

    copy_static_to_public(basepath)

def copy_static_to_public(basepath):
    if os.path.exists(dir_path_public):
        print("Deleting public directory...")
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


main()