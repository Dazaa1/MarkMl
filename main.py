import sys
import os
import re
from enum import Enum
import textwrap

class Headings(Enum):
    ONE = r'^#\s+(.+)$'
    TWO = r'^##\s+(.+)$'
    THREE = r'^###\s+(.+)$'
    FOUR = r'^####\s+(.+)$'
    FIVE = r'^#####\s+(.+)$'
    SIX = r'^######\s+(.+)$'

class Patterns(Enum):
    LIST = r'^-\s+(.+)$'
    BOLD = r'\*\*(.*?)\*\*'
    ITALIC = r'\*(.*?)\*'

def get_markdown(content):
    if not content:
        return []
    results = []
    # Simplified check for .md files
    if content[0].endswith(".md"):
        results.append(content[0])
    
    results.extend(get_markdown(content[1:]))
    return results

def headings_parser(pattern, text):
    p = re.compile(pattern, flags=re.MULTILINE)
    match pattern:
        case Headings.ONE.value:
            return p.sub(r'<h1>\1</h1>', text)
        case Headings.TWO.value:
            return p.sub(r'<h2>\1</h2>', text)
        case Headings.THREE.value:
            return p.sub(r'<h3>\1</h3>', text)
        case Headings.FOUR.value:
            return p.sub(r'<h4>\1</h4>', text)
        case Headings.FIVE.value:
            return p.sub(r'<h5>\1</h5>', text)
        case Headings.SIX.value:
            return p.sub(r'<h6>\1</h6>', text)
    return text

def main():
    text = textwrap.dedent("""\
    # Welcome to my SSG
    ### List Overview
    Lists are essential for keeping your thoughts organized:

    - Hello world.
    """)

    parsed_text = text
    for heading in Headings:
        parsed_text = headings_parser(heading.value, parsed_text)

    if os.path.exists("content"):
        content = os.listdir("content")
        print("Markdown files found:", get_markdown(content))
    else:
        print("Note: 'content' directory not found.")

    print("\n--- Parsed HTML Output ---")
    print(parsed_text)

    if len(sys.argv) < 3:
        print("\nUsage: ./main.py <source> <destination>")
    else:
        print("\nHello from funcstatic!")

if __name__ == "__main__":
    main()