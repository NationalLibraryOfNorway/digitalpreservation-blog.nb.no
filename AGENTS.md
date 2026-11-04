# AGENTS.md

Guidance for coding agents working in this repository.

Source for https://digitalpreservation.no — the National Library of Norway's digital preservation site (blog + preservation documentation). Static site built with Hugo and the [Hextra](https://imfing.github.io/hextra/docs/guide/) theme.

## Commands

```bash
hugo server -D          # local preview incl. drafts (http://localhost:1313)
hugo --gc --minify      # production build into public/ — the only "test"; a clean build is the check
python3 scripts/lint_format_json_codeblocks.py <file.md>        # pretty-print JSON/XML code blocks in place
python3 scripts/lint_format_json_codeblocks.py --folder content # same, whole tree
```

- Needs Hugo **extended** and Go (Hextra is pulled as a Hugo module). CI pins Hugo 0.163.1; use a matching version locally.
- The lint script rewrites files in place and warns on lines over 95 chars. `--all` resolves `../content`, so it only works when run from `scripts/`.

## Build and deploy

- `.github/workflows/pages.yaml` builds and deploys to GitHub Pages on every push to `main`. There is no PR preview or staging; pushing to `main` publishes.
- `netlify.toml` is a leftover (Hugo 0.132.2) and is not used for deployment.
- `enableGitInfo: true` — "last updated" dates come from git history (CI checks out with `fetch-depth: 0`).
- Pages with `draft: true` are committed but not published.

## Structure

- `content/blog/YYYY-MM-DD-slug/` — one page bundle per post (`index.md` + images/PDFs). README.md documents the required front matter (`title`, `date`, `description`, `tags`, `authors`, `images`, `draft`).
- `content/docs/` — preservation documentation: `dps/` (the preservation system: SIP/METS specs, APIs, data model, metadata), `formats/`, `principles/`, `strategy/`. Section order is controlled by `weight` in front matter; moved pages keep old URLs via `aliases`. `old_revisions/` hold superseded versions kept for reference.
- `static/swagger/` — vendored Swagger UI, served at `/swagger/` and linked from `content/docs/dps/api/`. `swagger-initializer.js` loads the live OpenAPI spec from `https://api.nb.no/dps-submission/v1/api-docs`; that spec, not this repo, is the source of truth for field names and allowed values. `static/schema/` — published XSDs.
- `layouts/partials/` — overrides of Hextra partials: `opengraph.html` (OG tags, uses page `images` param), `custom/head-end.html` (GoatCounter analytics), `components/last-updated.html` (adds a GitHub commit-history link).
- `hugo.yaml` — menus, languages, Hextra params. Pages and sections also emit a `markdown` output format alongside HTML.

## Bilingual content

- English is the default language (served at `/`); Norwegian Bokmål is served under `/nb/`. Translations are sibling files with a `.nb.md` suffix (`index.md` / `index.nb.md`, `_index.md` / `_index.nb.md`). When editing a page, update both language files unless told otherwise. A few pages are English-only.
- UI strings for Norwegian are in `i18n/nb.yaml`.
- **Bundle resources are published once, under the English path.** A relative path in a raw HTML `<img src="...">` (allowed, since goldmark `unsafe: true`) works on the English page but 404s on `/nb/`. Prefer Markdown image syntax or `{{< figure >}}`, which Hugo resolves; in raw HTML use the absolute path, e.g. `/blog/2026-10-06-ipres2026/image.png` (URL is lowercased).

## Authoring conventions

- Start headings at `##`; the title renders as h1.
- Use `{{< figure src="x.svg" >}}` for SVG — the Markdown image syntax does not handle SVG. Raster images are resized and converted to webp at build time; do not supply webp sources (re-encoding degrades quality).
- Hextra shortcodes in use: `card`/`cards`, `filetree`, `figure`, `details`, `steps`, `callout`, `youtube`, `icon`.
