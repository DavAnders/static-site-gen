from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_html_node
import os
import shutil
import re

def extract_title(markdown):
    match = re.search(r'^#\s(.+)', markdown, flags=re.MULTILINE)
    if match:
        # The group(1) holds the text of the h1 header
        return match.group(1)
    else:
        # If there is no match, raise an exception indicating there's no h1 header
        raise ValueError("No h1 header found in markdown")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        content = file.read()
    with open(template_path, 'r') as file:
        template = file.read()

    html_content = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # write final html to destination path
    with open(dest_path, 'w') as file:
        file.write(final_html)
    
    print("Page generated successfully.")

    

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
    content_path = "content/index.md"
    template_path = "template.html"
    destination_path = os.path.join(dest_directory, "index.html")

    # Ensure the destination directory (public) is cleared before copying
    if os.path.exists(dest_directory) and os.path.isdir(dest_directory):
        shutil.rmtree(dest_directory)
    print("Starting to copy...")
    copy_directory_contents(src_directory, dest_directory)
    print("Copy operation completed.")

    generate_page(content_path, template_path, destination_path)

if __name__ == "__main__":
    main()