from .enums import Headings, Patterns
from .parsers import headings_parser, list_parser, bold_parser, italic_parser, strikethrough_parser, underline_parser, url_parser, image_parser

def get_markdown(content):
    if not content:
        return []
    results = []
    # Simplified check for .md files
    if content[0].endswith(".md"):
        results.append(content[0])
    
    results.extend(get_markdown(content[1:]))
    return results

def markdown_to_html(markdown_text):
    parsed_text = markdown_text
    for heading in Headings:
        parsed_text = headings_parser(heading.value, parsed_text)
    parsed_text = list_parser(Patterns.LIST.value, parsed_text)
    parsed_text = bold_parser(Patterns.BOLD.value, parsed_text)
    parsed_text = italic_parser(Patterns.ITALIC.value, parsed_text)
    parsed_text = strikethrough_parser(Patterns.STRIKETHROUGH.value, parsed_text)
    parsed_text = underline_parser(Patterns.UNDERLINE.value, parsed_text)
    parsed_text = url_parser(Patterns.URL.value, parsed_text)
    parsed_text = image_parser(Patterns.IMAGE.value, parsed_text)
    return parsed_text

def convert_markdown_to_html(source, destination):
    with open(source, 'r') as src_file:
        markdown_content = src_file.read()

    html_content = markdown_to_html(markdown_content)

    with open(destination, 'w') as dest_file:
        dest_file.write(html_content)