# komodo-py-api

Repository for a mostly auto-generated `komodo_api` package.

## Regenerating from upstream Komodo

The generation flow is handled by `scripts/generate_from_tag.sh`:

1. Clone the official Komodo repository at the selected tag (defaults to `main`).
2. Apply every `*.patch` file in `scripts/patches/` (sorted by filename).
3. Run the Python generation commands:
   - `typeshare -V || cargo install typeshare-cli@1.13.3 -F python`
   - `node client/core/py/generate_types.mjs`
4. Copy the generated `komodo_api` package back into this repository.

Usage:

```bash
scripts/generate_from_tag.sh           # uses main
scripts/generate_from_tag.sh v1.2.3    # generate from a specific tag
```

Use `scripts/patches/` for repository-specific patches that must be applied before generation.
