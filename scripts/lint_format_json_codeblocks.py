# Vibe coded by github copilot, agent gpt-4.1 28.11.2025
# This script formats JSON code blocks in Markdown files.
# It can process a single file, all files in a default 'content' folder,
# or all files in a specified folder.

import sys
import re
import json
from pathlib import Path

def format_json_blocks(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find ```json code blocks
    pattern = re.compile(r'```json\s*\n(.*?)\n```', re.DOTALL)
    invalid_blocks = []
    def replacer(match):
        block = match.group(1)
        try:
            # Remove leading/trailing whitespace
            block_stripped = block.strip()
            # Parse and pretty-print
            obj = json.loads(block_stripped)
            formatted = json.dumps(obj, indent=2, ensure_ascii=False)
            return f'```json\n{formatted}\n```'
        except Exception as e:
            invalid_blocks.append(block)
            return match.group(0)  # Leave as-is

    new_content = pattern.sub(replacer, content)

    # Write back to file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    if invalid_blocks:
        print(f"{md_path}: Found {len(invalid_blocks)} invalid JSON code blocks. They were left unchanged.")
    else:
        print(f"{md_path}: All JSON code blocks formatted successfully.")

def lint_folder(folder_path):
    folder = Path(folder_path)
    md_files = list(folder.rglob('*.md'))
    if not md_files:
        print(f"No Markdown files found in {folder_path}")
        return
    for md_file in md_files:
        format_json_blocks(md_file)

if __name__ == "__main__":
    # If a single markdown file is given, lint just that file
    if len(sys.argv) == 2 and sys.argv[1].endswith('.md'):
        format_json_blocks(sys.argv[1])

    # If '--all' is given, lint all markdown files in the default 'content' folder
    elif len(sys.argv) == 2 and sys.argv[1] == '--all':
        lint_folder('content')

    # If '--folder <folder>' is given, lint all markdown files in the specified folder
    elif len(sys.argv) == 3 and sys.argv[1] == '--folder':
        lint_folder(sys.argv[2])

    # If '--folder' is given without a folder name, default to 'content'
    elif len(sys.argv) == 2 and sys.argv[1] == '--folder':
        lint_folder('content')

    # Otherwise, print usage instructions
    else:
        print("Usage:")
        print("  python lint_format_json_codeblocks.py <markdown-file>")
        print("  python lint_format_json_codeblocks.py --all")
        print("  python lint_format_json_codeblocks.py --folder <folder>")
        sys.exit(1)