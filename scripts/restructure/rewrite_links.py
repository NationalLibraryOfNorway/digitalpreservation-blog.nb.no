#!/usr/bin/env python3
"""Docs restructure helper (including the flattened Policies/Docs navigation).

Subcommands (run from the repository root):

  links    Rewrite internal doc links in content/ (.md and .json) according to
           mapping.tsv. Handles /docs/..., /nb/docs/... and
           https://digitalpreservation.no/(nb/)docs/... and keeps #fragments.
           Front matter is left alone, so aliases are never rewritten.
  aliases  For every page moved with `git mv` (staged renames), add the old URL
           to `aliases` in the new file. Drafts are skipped. Existing aliases
           are kept and the block is normalised to a YAML list.

Both subcommands are idempotent and can be re-run after a rebase.
Add --dry-run to print what would change without writing.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
MAPPING = Path(__file__).with_name("mapping.tsv")

# Extra aliases for URLs that are linked from published spec files but never existed.
EXTRA_ALIASES = {
    "content/docs/understanding/information-packages/_index": ["/docs/dps/sip/1.0/scope/"],
    "content/docs/reference/sip/mets/_index": ["/docs/dps/sip/1.0/mets/"],
    "content/docs/reference/sip/structure-requirements/_index": [
        "/docs/dps/sip/1.0/structure-requirements/"
    ],
}

PAGE_NAMES = {"_index.md", "_index.nb.md", "index.md", "index.nb.md"}


def load_mapping():
    rows = []
    for line in MAPPING.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        old, new = line.split("\t")
        rows.append((old.lower(), new))
    rows.sort(key=lambda r: len(r[0]), reverse=True)
    return rows


# Our own host, or no host at all (not preceded by a URL/word character).
LINK_RE = re.compile(
    r"(?:(?P<host>https?://digitalpreservation\.no)|(?<![\w.:/\-]))"
    r"(?P<lang>/nb)?(?P<path>/docs/[\w.\-/]*)"
)


def map_path(path, mapping):
    probe = path if path.endswith("/") else path + "/"
    low = probe.lower()
    for old, new in mapping:
        if low.startswith(old):
            rest = probe[len(old):].lower()
            result = new + rest
            if not path.endswith("/") and rest:
                result = result.rstrip("/")
            return result
    return None


def split_front_matter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            end += len("\n---")
            return text[:end], text[end:]
    return "", text


def rewrite_text(body, mapping):
    def repl(m):
        new = map_path(m.group("path"), mapping)
        if new is None:
            return m.group(0)
        return (m.group("host") or "") + (m.group("lang") or "") + new

    body = body.replace("](nb/docs/", "](/nb/docs/")  # pre-existing missing slash
    return LINK_RE.sub(repl, body)


def cmd_links(dry_run):
    mapping = load_mapping()
    changed = 0
    for f in sorted(list(CONTENT.rglob("*.md")) + list(CONTENT.rglob("*.json"))):
        text = f.read_text(encoding="utf-8")
        if f.suffix == ".md":
            fm, body = split_front_matter(text)
            new_text = fm + rewrite_text(body, mapping)
        else:
            new_text = rewrite_text(text, mapping)
        if new_text != text:
            changed += 1
            print(f"links: {f.relative_to(ROOT)}")
            if not dry_run:
                f.write_text(new_text, encoding="utf-8")
    print(f"{changed} file(s) {'would change' if dry_run else 'changed'}")


def staged_renames():
    out = subprocess.run(
        ["git", "diff", "--cached", "-M", "--name-status"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    for line in out.splitlines():
        parts = line.split("\t")
        if parts[0].startswith("R") and len(parts) == 3:
            yield parts[1], parts[2]


def url_for(rel_path):
    p = Path(rel_path)
    rel = p.parent.relative_to("content")
    return "/" + str(rel).lower() + "/"


ALIAS_LINE = re.compile(r"^aliases:\s*(.*)$", re.IGNORECASE)


def parse_aliases(lines, i):
    """Return (values, index after the aliases block)."""
    rest = ALIAS_LINE.match(lines[i]).group(1).strip()
    values = []
    j = i + 1
    if rest:
        values = re.findall(r'"([^"]+)"|\'([^\']+)\'|([^\s,\[\]]+)', rest)
        values = [a or b or c for a, b, c in values]
    else:
        while j < len(lines) and lines[j].strip() != "---" and lines[j].startswith((" ", "\t", "-")):
            v = lines[j].strip().lstrip("-").strip().strip("\"'")
            if v:
                values.append(v)
            j += 1
    return values, j


def add_aliases(path, new_aliases, dry_run):
    text = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(text)
    if not fm:
        print(f"WARN no front matter: {path}", file=sys.stderr)
        return
    if re.search(r"^draft:\s*true", fm, re.IGNORECASE | re.MULTILINE):
        return
    lines = fm.split("\n")  # first '---' ... last '---'
    existing, start, end = [], None, None
    for i, line in enumerate(lines):
        if ALIAS_LINE.match(line):
            start = i
            existing, end = parse_aliases(lines, i)
            break
    merged = list(dict.fromkeys(existing + new_aliases))
    if merged == existing:
        return
    block = ["aliases:"] + [f"  - {a}" for a in merged]
    if start is None:
        lines = lines[:-1] + block + lines[-1:]
    else:
        lines = lines[:start] + block + lines[end:]
    print(f"aliases: {path.relative_to(ROOT)} += {[a for a in merged if a not in existing]}")
    if not dry_run:
        path.write_text("\n".join(lines) + body, encoding="utf-8")


def cmd_aliases(dry_run):
    seen = set()
    for old, new in staged_renames():
        if not new.startswith(("content/docs/", "content/policies/")) or Path(new).name not in PAGE_NAMES:
            continue
        aliases = [url_for(old)]
        key = str(Path(new).parent / Path(new).name.split(".")[0])
        aliases += EXTRA_ALIASES.get(key, [])
        add_aliases(ROOT / new, aliases, dry_run)
        seen.add(new)
    print(f"{len(seen)} moved page file(s) checked")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["links", "aliases"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    {"links": cmd_links, "aliases": cmd_aliases}[args.command](args.dry_run)


if __name__ == "__main__":
    main()
