from enum import Enum

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
    STRIKETHROUGH = r'~~(.*?)~~'
    UNDERLINE = r'__(.*?)__'
    URL = r'\[(.*?)\]\((.*?)\)'
    IMAGE = r'!\[(.*?)\]\((.*?)\)'