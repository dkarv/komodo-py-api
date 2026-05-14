import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_komodo_api


class GenerateKomodoApiTests(unittest.TestCase):
    def test_apply_patches_uses_sorted_patch_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            patch_dir = Path(tmp) / "patches"
            patch_dir.mkdir()
            (patch_dir / "b.patch").write_text("b")
            (patch_dir / "a.patch").write_text("a")

            repo_dir = Path(tmp) / "repo"
            repo_dir.mkdir()

            with patch("scripts.generate_komodo_api.run") as run_mock:
                generate_komodo_api.apply_patches(repo_dir, patch_dir)

            commands = [call.args[0] for call in run_mock.call_args_list]
            self.assertEqual(
                commands,
                [
                    ["git", "-C", str(repo_dir), "apply", str(patch_dir / "a.patch")],
                    ["git", "-C", str(repo_dir), "apply", str(patch_dir / "b.patch")],
                ],
            )

    def test_copy_generated_api_replaces_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_dir = Path(tmp) / "repo"
            source = repo_dir / "generated" / "komodo_api"
            source.mkdir(parents=True)
            (source / "__init__.py").write_text("from .client import Client")

            output = Path(tmp) / "komodo_api"
            output.mkdir()
            (output / "old.py").write_text("old")

            generate_komodo_api.copy_generated_api(repo_dir, "generated/komodo_api", output)

            self.assertTrue((output / "__init__.py").exists())
            self.assertFalse((output / "old.py").exists())


if __name__ == "__main__":
    unittest.main()
