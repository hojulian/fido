import os

import yaml


class InstallFile(object):
    """Represents a ROSInstall file."""

    _dependencies = []

    def git(self, localpath, src, branch):
        self._dependencies.append(
            {
                "git": {
                    "local-name": localpath,
                    "uri": src,
                    "version": branch,
                }
            }
        )

    def setup_file(self, localpath):
        self._dependencies.append(
            {
                "setup-file": {
                    "local-name": localpath,
                }
            }
        )

    def to_string(self):
        return yaml.dump(self._dependencies, sort_keys=True, default_flow_style=False)

    def to_file(self, path):
        with open(os.path.join(path, ".rosinstall"), "w") as f:
            yaml.dump(self._dependencies, f, sort_keys=True, default_flow_style=False)
