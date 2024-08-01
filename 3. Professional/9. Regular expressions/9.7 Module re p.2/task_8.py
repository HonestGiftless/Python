# HTML 🌶️🌶️
import re
import sys

def extract_tags(html):
    tag_pattern = re.compile(r'<(\w+)(\s+[^>]+)?>')
    attr_pattern = re.compile(r'([\w-]+)="[^"]*"')

    tags = tag_pattern.findall(html)
    result = {}

    for tag, attrs in tags:
        if tag not in result:
            result[tag] = set()
        if attrs:
            attributes = attr_pattern.findall(attrs)
            for attr in attributes:
                result[tag].add(attr)
    
    output = []
    for tag in sorted(result.keys()):
        attr_list = ", ".join(sorted(result[tag]))
        output.append(f"{tag}: {attr_list}")
    
    return "\n".join(output)

def main():
    html_input = sys.stdin.read()
    result = extract_tags(html_input)
    print(result)

if __name__ == "__main__":
    main()