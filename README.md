# komodo-py-api

Repository for a mostly auto-generated `komodo_api` package.

## Regenerating from an upstream Komodo tag

The generation flow is handled by `scripts/generate_komodo_api.py`:

1. Clone the official Komodo repository at the requested tag.
2. Apply every `*.patch` file in `scripts/patches/` (sorted by filename).
3. Run a caller-provided generation command in the cloned repository.
4. Copy the generated `komodo_api` package back into this repository.

Example:

```bash
python scripts/generate_komodo_api.py v1.2.3 \
  --generate-command "<command that generates the python api>" \
  --generated-api-path "<relative path to generated/komodo_api>"
```

You can also use the shell wrapper:

```bash
scripts/generate_from_tag.sh v1.2.3 "<generation command>" "<generated path>"
```

Use `scripts/patches/` for repository-specific patches that must be applied before generation.
