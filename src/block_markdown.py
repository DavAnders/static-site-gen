import re
from htmlnode import HTMLNode, LeafNode, ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            html_nodes.append(markdown_to_html_heading(block))
        elif block_type == block_type_code:
            html_nodes.append(markdown_to_html_code(block))
        elif block_type == block_type_quote:
            html_nodes.append(markdown_to_html_quote(block))
        elif block_type == block_type_unordered_list:
            html_nodes.append(markdown_to_html_list(block, ordered=False))
        elif block_type == block_type_ordered_list:
            html_nodes.append(markdown_to_html_list(block, ordered=True))
        elif block_type == block_type_paragraph:
            html_nodes.append(markdown_to_html_paragraph(block))
    return ParentNode(tag='div', children=html_nodes)


def translate_inline_styles(markdown):
    # Translate images ![alt text](url)
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2">', markdown)
    
    # Translate links [link text](url)
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    
    # Translate bold **text**
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown)
    
    # Translate italic *text*
    markdown = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown)

    return markdown

def markdown_to_html_list(block, ordered=False):
    children = []
    items = block.split('\n')
    for item in items:
        # remove the list markers depending on ordered or unordered
        if ordered:
            item_content = re.sub(r"^\d+\.\s", "", item)
        else:
            item_content = re.sub(r"^\*\s|\-\s", "", item)
        html_content = translate_inline_styles(item_content)
        child = LeafNode('li', html_content)
        children.append(child)
    tag = 'ol' if ordered else 'ul'
    return ParentNode(tag, children=children)

def markdown_to_html_quote(block):
    lines = block.split('\n')
    # each line, removing '>' and leading/trailing whitespace
    quote_lines = [line.lstrip("> ").rstrip() for line in lines]
    # combine lines back into a single string
    content = ' '.join(quote_lines)
    html_content = translate_inline_styles(content)
    return LeafNode("blockquote", html_content)

def markdown_to_html_paragraph(block):
    html_content = translate_inline_styles(block)
    return LeafNode("p", html_content)

def markdown_to_html_code(block):
    # Regex pattern to match code blocks delimited by triple backticks
    pattern = r'^```(.*?)```$'
    match = re.match(pattern, block, re.DOTALL)
    if match:
        # Extract the content within the backticks, ignoring any leading/trailing whitespace
        content = match.group(1).strip()
        code_node = LeafNode(tag='code', value=content)
        return ParentNode(tag='pre', children=[code_node])
    else:
        raise ValueError("No code block found.")

def markdown_to_html_heading(block):
    # Regex to capture the heading level and text allowing for extra spaces
    match = re.match(r"^(#+)\s*(.*)$", block)
    if match:
        level = len(match.group(1))  # Number of '#' characters
        content = match.group(2).strip()  # Heading text, stripping leading/trailing spaces
        html_content = translate_inline_styles(content)
        return LeafNode(tag=f'h{level}', value=html_content)

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        stripped_block = block.strip() # remove leading or trailing whitespace
        if stripped_block: # if it is not an empty string
            cleaned_blocks.append(stripped_block)

    return cleaned_blocks

def block_to_block_type(block):
    if re.match(r"^\#{1,6}\s", block):
        return block_type_heading
    elif block.startswith("```") and block.endswith("```"):
        return block_type_code
    elif block.startswith(">"):
        return block_type_quote
    elif block.strip().startswith(("* ", "- ")):
        return block_type_unordered_list
    elif re.match(r"^\d+\.\s", block):
        return block_type_ordered_list
    else:
        return block_type_paragraph