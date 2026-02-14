import sys
from markml.utils import convert_markdown_to_html


def main():
    if len(sys.argv) < 3:
        print("\nUsage: ./main.py <source> <destination>")
    else:
        source = sys.argv[1]
        destination = sys.argv[2]
        convert_markdown_to_html(source, destination)
        print("\nHello from funcstatic!")

if __name__ == "__main__":
    main()