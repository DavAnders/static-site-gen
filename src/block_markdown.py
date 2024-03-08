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
            html_nodes.append(markdown_to_html_list(block))
        elif block_type == block_type_ordered_list:
            html_nodes.append(markdown_to_html_list(block))
        elif block_type == block_type_paragraph:
            html_nodes.append(markdown_to_html_paragraph(block))
    return ParentNode(tag='div', children=html_nodes)

def markdown_to_html_list(block, ordered=False):
    children = []
    items = block.split('\n')
    for item in items:
        if ordered:
            # replace number and period with nothing
            item_content = re.sub(r"^\d+\.\s", "", item)
            item_content = item.lstrip('* ').lstrip('- ')
        else:
            item_content = item.lstrip('* ').lstrip('- ')
        child = LeafNode('li', item_content)
        children.append(child)
    tag = 'ol' if ordered else 'ul'
    return ParentNode(tag, children=children)

def markdown_to_html_quote(block):
    content = block.lstrip(">")
    content = content.strip()
    return LeafNode("blockquote", content)

def markdown_to_html_paragraph(block):
    return LeafNode("p", block)

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
        return LeafNode(tag=f'h{level}', value=content)

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