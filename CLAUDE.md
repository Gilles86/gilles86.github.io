# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This is the personal academic website of Gilles de Hollander (https://gilles86.github.io), a Jekyll site hosted on GitHub Pages. Pushing to `main` triggers GitHub Pages to rebuild and deploy automatically.

## Build / serve

There is no local Ruby toolchain configured (the bundled `bundler` version doesn't match system Ruby). Use Docker:

```bash
./serve_docker.sh   # jekyll serve on http://localhost:4000
```

The committed `_site/` directory is build output — never edit it by hand; it is regenerated on build.

## Content model

Content lives in three Jekyll collections / locations, each rendered by a different mechanism:

- **`_publications/<year>/<slug>.md`** — one file per paper. Front matter only (no body), rendered via `_includes/paper.html`. The `pages/papers.md` page splits entries into "Preprints" (`preprint: True`) and year-grouped published papers (`preprint: false`).
- **`_projects/<slug>.md`** — one file per project, with a markdown body. Rendered by `pages/projects.md`, grouped by `status` (`ongoing`/`past`) and sorted by `order`.
- **`pages/*.md`** — top-level pages. **Any page with `layout: page` is auto-added to the navbar** (see `_layouts/default.html`), so creating a new `pages/foo.md` with `layout: page` + a `title` makes it appear in the nav automatically.

## Publication entries — important conventions

The filename slug is the linchpin. `_includes/paper.html` derives everything from `<slug>.md`:

- **Figure**: expects `assets/imgs/publications/<year>/<slug>.png` (same slug as the `.md`).
- **PDF**: if `assets/pdfs/publications/<year>/<slug>.pdf` exists, it auto-links with a PDF icon; otherwise the title links to the `doi:` instead.
- Required front matter: `layout: post`, `title`, `date` (with time), `journal`, `preprint`, `authors` (list), `abstract`, `ref`, `doi`. The `ref` is conventionally the DOI suffix (e.g. `2026.03.28.715037`).
- In the author list, write `Gilles de Hollander` verbatim — the template bolds it. A trailing `*` on an author renders as a superscript (shared-authorship marker).

bioRxiv PDFs cannot be fetched programmatically (Cloudflare blocks WebFetch/curl). Get metadata from the bioRxiv API instead: `https://api.biorxiv.org/details/biorxiv/<doi>`. The actual PDF must be downloaded manually by the user.

## Homepage news

`index.md` has an `### Updates` section grouped by `#### <year>` subheadings, newest first. House style for updates: **no exclamation marks**, capitalize the first letter of each entry.
