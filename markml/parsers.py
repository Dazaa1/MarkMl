import re
from .enums import Headings, Patterns

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


def list_parser(pattern, text):
    p = re.compile(pattern, flags=re.MULTILINE)
    return p.sub(r'<li>\1</li>', text)

def bold_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<strong>\1</strong>', text)

def italic_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<em>\1</em>', text)

def strikethrough_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<del>\1</del>', text)

def underline_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<u>\1</u>', text)

def url_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<a href="\2">\1</a>', text)

def image_parser(pattern, text):
    p = re.compile(pattern)
    return p.sub(r'<img src="\2" alt="\1">', text)