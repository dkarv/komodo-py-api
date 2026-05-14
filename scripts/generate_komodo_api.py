#!/usr/bin/env python3
"""Generate the local `komodo_api` package from an upstream Komodo git tag."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def run(command: list[str] | str, cwd: Path | None = None, shell: bool = False) -> None:
    subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        check=True,
        shell=shell,
    )


def clone_repo(repo_url: str, tag: str, destination: Path) -> None:
    run(["git", "clone", "--branch", tag, "--single-branch", repo_url, str(destination)])


def apply_patches(repo_dir: Path, patch_dir: Path) -> None:
    if not patch_dir.exists():
        return

    for patch_file in sorted(patch_dir.glob("*.patch")):
        run(["git", "-C", str(repo_dir), "apply", str(patch_file)])


def generate_api(repo_dir: Path, generate_command: str) -> None:
    run(generate_command, cwd=repo_dir, shell=True)


def copy_generated_api(repo_dir: Path, generated_api_path: str, output_path: Path) -> None:
    source_path = (repo_dir / generated_api_path).resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"Generated API path does not exist: {source_path}")

    if output_path.exists():
        shutil.rmtree(output_path)
    shutil.copytree(source_path, output_path)


def process_repo(repo_dir: Path, repo_url: str, tag: str, patch_dir: Path, generate_command: str, generated_api_path: str, output_path: Path) -> None:
    clone_repo(repo_url, tag, repo_dir)
    apply_patches(repo_dir, patch_dir)
    generate_api(repo_dir, generate_command)
    copy_generated_api(repo_dir, generated_api_path, output_path)


def write_generation_metadata(output_path: Path, tag: str, repo_url: str) -> None:
    metadata_file = output_path / "_generated_from.py"
    generated_at = datetime.now(timezone.utc).isoformat()
    metadata_file.write_text(
        "\n".join(
            [
                "\"\"\"Metadata for this generated package.\"\"\"",
                f"SOURCE_REPOSITORY = {repo_url!r}",
                f"SOURCE_TAG = {tag!r}",
                f"GENERATED_AT = {generated_at!r}",
                "",
            ]
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag", help="Komodo git tag to generate from")
    parser.add_argument(
        "--repo-url",
        default="https://github.com/moghtech/komodo.git",
        help="Official Komodo repository URL",
    )
    parser.add_argument(
        "--patch-dir",
        default="scripts/patches",
        help="Directory containing .patch files to apply before generation",
    )
    parser.add_argument(
        "--generate-command",
        required=True,
        help="Command run inside the cloned Komodo repo to generate the Python API",
    )
    parser.add_argument(
        "--generated-api-path",
        required=True,
        help="Path to generated komodo_api package inside the cloned repo",
    )
    parser.add_argument(
        "--output-path",
        default="komodo_api",
        help="Where to write the generated package in this repository",
    )
    parser.add_argument(
        "--work-dir",
        default=None,
        help="Optional working directory (defaults to a temporary directory)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    patch_dir = Path(args.patch_dir).resolve()
    output_path = Path(args.output_path).resolve()

    if args.work_dir:
        work_dir = Path(args.work_dir).resolve()
        work_dir.mkdir(parents=True, exist_ok=True)

        repo_dir = work_dir / "komodo"
        if repo_dir.exists():
            shutil.rmtree(repo_dir)

        process_repo(repo_dir, args.repo_url, args.tag, patch_dir, args.generate_command, args.generated_api_path, output_path)
    else:
        with tempfile.TemporaryDirectory(prefix="komodo-api-") as temp_dir:
            repo_dir = Path(temp_dir) / "komodo"
            process_repo(repo_dir, args.repo_url, args.tag, patch_dir, args.generate_command, args.generated_api_path, output_path)

    write_generation_metadata(output_path, args.tag, args.repo_url)


if __name__ == "__main__":
    main()
