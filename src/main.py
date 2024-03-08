from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil

def copy_directory_contents(src, dest):
    # check if destination exists, create if not
    if not os.path.exists(dest):
        os.mkdir(dest)
    elif os.path.isdir(dest):
        # if destination exists and is directory, clear contents for IDEMPOTENCY!
        shutil.rmtree(dest)
        os.mkdir(dest)
    # list contents of the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item) # path to item in source directory
        dest_path = os.path.join(dest, item) # path to where item should go in destination
        # if item is a file copy it to destination
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} to {dest_path}")
        # if the item is a directory recursively copy its contents
        elif os.path.isdir(src_path):
            copy_directory_contents(src_path, dest_path)
            print(f"Copied directory: {src_path} to {dest_path}")


def main():
    src_directory = "static"  # Source directory
    dest_directory = "public"  # Destination directory

    # Ensure the destination directory (public) is cleared before copying
    if os.path.exists(dest_directory) and os.path.isdir(dest_directory):
        shutil.rmtree(dest_directory)
    print("Starting to copy...")
    copy_directory_contents(src_directory, dest_directory)
    print("Copy operation completed.")

if __name__ == "__main__":
    main()