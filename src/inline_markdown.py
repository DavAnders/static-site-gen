from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
        else:
            text_remaining = node.text
            for alt_text, img_url in images:
                # split the text at the current image's markdown
                before_image, text_remaining = text_remaining.split(f"![{alt_text}]({img_url})", 1)
                if before_image:
                    new_nodes.append(TextNode(before_image, text_type_text))
                new_nodes.append(TextNode(alt_text, text_type_image, img_url))
            if text_remaining:
                new_nodes.append(TextNode(text_remaining, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        else:
            text_remaining = node.text
            for alt_text, link_url in links:
                before_link, text_remaining = text_remaining.split(f"[{alt_text}]({link_url})", 1)
                if before_link:
                    new_nodes.append(TextNode(before_link, text_type_text))
                new_nodes.append(TextNode(alt_text, text_type_link, link_url))
            if text_remaining:
                new_nodes.append(TextNode(text_remaining, text_type_text))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Invalid markdown, bold section not closed")
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, "text", node.url))
                else:
                    # odd parts are inside the delimiter
                    new_nodes.append(TextNode(part, text_type, node.url))
    return new_nodes