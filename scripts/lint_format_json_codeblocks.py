# Vibe coded by github copilot, agent gpt-4.1 28.11.2025
# This script formats JSON and XML code blocks in Markdown files.
# It can process a single file, all files in a default 'content' folder,
# or all files in a specified folder.

import sys
import re
import json
from pathlib import Path
from xml.dom import Node
from xml.dom.minidom import parseString


FORMATTERS = {}
MAX_CODE_BLOCK_LINE_LENGTH = 95
XML_FRAGMENT_WRAPPER = '__code_block_xml_fragment__'
XML_NAME_PREFIX_PATTERN = re.compile(r'(?<!xmlns:)\b([A-Za-z_][\w.-]*):[A-Za-z_][\w.-]*')
XML_ATTRIBUTE_PATTERN = re.compile(r'\s+([^\s=]+)="([^"]*)"')


def formatter(language):
    def register(func):
        FORMATTERS[language] = func
        return func
    return register


@formatter('json')
def format_json_block(block):
    obj = json.loads(block.strip())
    return json.dumps(obj, indent=2, ensure_ascii=False)


def remove_whitespace_text_nodes(node):
    for child in list(node.childNodes):
        if child.nodeType == Node.TEXT_NODE and child.data.strip() == '':
            node.removeChild(child)
            child.unlink()
        else:
            remove_whitespace_text_nodes(child)


@formatter('xml')
def format_xml_block(block):
    block_stripped = block.strip()
    has_xml_declaration = block_stripped.startswith('<?xml')

    try:
        dom = parseString(block_stripped)
    except Exception:
        dom = parse_xml_fragment(block_stripped)

    remove_whitespace_text_nodes(dom)
    lines = formatted_xml_lines(dom)

    if not has_xml_declaration and lines and lines[0].startswith('<?xml'):
        lines = lines[1:]

    return '\n'.join(wrap_xml_lines(lines))


def parse_xml_fragment(block):
    namespace_attributes = ' '.join(
        f'xmlns:{prefix}="urn:markdown-code-block-prefix:{prefix}"'
        for prefix in sorted(detect_xml_prefixes(block))
    )
    if namespace_attributes:
        namespace_attributes = ' ' + namespace_attributes

    wrapped_block = (
        f'<{XML_FRAGMENT_WRAPPER}{namespace_attributes}>'
        f'{block}'
        f'</{XML_FRAGMENT_WRAPPER}>'
    )
    return parseString(wrapped_block)


def detect_xml_prefixes(block):
    return {
        match.group(1)
        for match in XML_NAME_PREFIX_PATTERN.finditer(block)
        if match.group(1).lower() not in ('xml', 'xmlns')
    }


def formatted_xml_lines(dom):
    root = dom.documentElement

    if root.tagName == XML_FRAGMENT_WRAPPER:
        lines = []
        for child in root.childNodes:
            lines.extend(pretty_xml_lines(child))
        return lines

    return pretty_xml_lines(dom)


def pretty_xml_lines(node):
    formatted = node.toprettyxml(indent='  ', newl='\n')
    return [line for line in formatted.splitlines() if line.strip()]


def wrap_xml_lines(lines):
    wrapped_lines = []
    for line in lines:
        wrapped_lines.extend(wrap_xml_line(line))
    return wrapped_lines


def wrap_xml_line(line):
    if len(line) <= MAX_CODE_BLOCK_LINE_LENGTH:
        return [line]

    stripped = line.lstrip(' ')
    indent = line[:len(line) - len(stripped)]

    if not stripped.startswith('<') or stripped.startswith(('</', '<?', '<!')):
        return [line]

    tag_match = re.match(r'<([^\s>/]+)(.*?)(/?>)(.*)$', stripped)
    if not tag_match:
        return [line]

    tag_name, attributes_text, tag_close, trailing_text = tag_match.groups()
    attributes = XML_ATTRIBUTE_PATTERN.findall(attributes_text)
    if not attributes:
        return [line]

    return wrap_xml_attributes(
        indent,
        tag_name,
        [f'{name}="{value}"' for name, value in attributes],
        tag_close + trailing_text
    )


def wrap_xml_attributes(indent, tag_name, attributes, closing):
    lines = [f'{indent}<{tag_name}']
    continuation_indent = indent + '  '

    for attribute in attributes:
        candidate = f'{lines[-1]} {attribute}'
        if len(candidate) <= MAX_CODE_BLOCK_LINE_LENGTH:
            lines[-1] = candidate
        else:
            lines.append(f'{continuation_indent}{attribute}')

    closing_candidate = f'{lines[-1]}{closing}'
    if len(closing_candidate) <= MAX_CODE_BLOCK_LINE_LENGTH:
        lines[-1] = closing_candidate
    else:
        lines.append(f'{continuation_indent}{closing}')

    return lines


def format_code_blocks(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(
        r'^[ \t]*```(?P<language>json|xml)(?P<attributes>[^\n]*)\n'
        r'(?P<block>.*?)'
        r'^[ \t]*```[ \t]*$',
        re.DOTALL | re.IGNORECASE | re.MULTILINE
    )
    results = {
        language: {'seen': 0, 'changed': 0, 'unchanged': 0, 'invalid': 0, 'warnings': []}
        for language in FORMATTERS
    }

    def replacer(match):
        language = match.group('language').lower()
        block = match.group('block')
        formatter_func = FORMATTERS[language]
        results[language]['seen'] += 1
        block_number = results[language]['seen']

        try:
            formatted = formatter_func(block)
            replacement = f"```{match.group('language')}{match.group('attributes')}\n{formatted}\n```"
            if replacement == match.group(0):
                results[language]['unchanged'] += 1
            else:
                results[language]['changed'] += 1
            return replacement
        except Exception as error:
            results[language]['invalid'] += 1
            if language == 'xml':
                results[language]['warnings'].append(
                    f"Warning: {md_path}: XML block {block_number} left unchanged: {error}"
                )
            return match.group(0)  # Leave as-is

    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

    summaries = []
    for language in sorted(results):
        changed = results[language]['changed']
        unchanged = results[language]['unchanged']
        invalid = results[language]['invalid']
        if changed or unchanged or invalid:
            summaries.append(
                f"{language}: {changed} changed, {unchanged} unchanged, {invalid} invalid"
            )

    if summaries:
        print(f"{md_path}: " + '; '.join(summaries))
        for language in sorted(results):
            for warning in results[language]['warnings']:
                print(warning)
    else:
        print(f"{md_path}: No JSON or XML code blocks found.")

def lint_folder(folder_path):
    folder = Path(folder_path)
    md_files = list(folder.rglob('*.md'))
    if not md_files:
        print(f"No Markdown files found in {folder_path}")
        return
    for md_file in md_files:
        format_code_blocks(md_file)

if __name__ == "__main__":
    # If a single markdown file is given, lint just that file
    if len(sys.argv) == 2 and sys.argv[1].endswith('.md'):
        format_code_blocks(sys.argv[1])

    # If '--all' is given, lint all markdown files in the default 'content' folder
    elif len(sys.argv) == 2 and sys.argv[1] == '--all':
        lint_folder('../content')

    # If '--folder <folder>' is given, lint all markdown files in the specified folder
    elif len(sys.argv) == 3 and sys.argv[1] == '--folder':
        lint_folder(sys.argv[2])

    # If '--folder' is given without a folder name, default to 'content'
    elif len(sys.argv) == 2 and sys.argv[1] == '--folder':
        lint_folder('../content')

    # Otherwise, print usage instructions
    else:
        print("Usage:")
        print("  python lint_format_json_codeblocks.py <markdown-file>")
        print("  python lint_format_json_codeblocks.py --all")
        print("  python lint_format_json_codeblocks.py --folder <folder>")
        sys.exit(1)
