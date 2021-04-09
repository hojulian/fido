import tempfile
import os
import unittest

from fido.ros.installfile import InstallFile


class TestInstallFile(unittest.TestCase):
    def test_to_string(self):
        test_cases = [
            {
                "desc": "one git source",
                "localpath": "src/some/path",
                "src": "https://github.com/some/repo.git",
                "branch": "master",
                "expected": "- git:\n    local-name: src/some/path\n    uri: https://github.com/some/repo.git\n    version: master\n",
            }
        ]

        for tc in test_cases:
            f = InstallFile()
            f.git(tc["localpath"], tc["src"], tc["branch"])
            self.assertEqual(f.to_string(), tc["expected"], tc["desc"])

    def test_to_file(self):
        test_cases = [
            {
                "desc": "one git source",
                "localpath": "src/some/path",
                "src": "https://github.com/some/repo.git",
                "branch": "master",
                "expected": "- git:\n    local-name: src/some/path\n    uri: https://github.com/some/repo.git\n    version: master\n",
            }
        ]

        for tc in test_cases:
            f = InstallFile()
            f.git(tc["localpath"], tc["src"], tc["branch"])
            
            with tempfile.TemporaryDirectory() as path:
                f.to_file(path)
                with open(os.path.join(path, ".rosinstall"), "r") as out:
                    out_text = "".join(out.readlines())
                    self.assertEqual(out_text, tc["expected"], tc["desc"])
