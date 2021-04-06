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
        return yaml.dump(self._dependencies, sort_keys=True)

    def to_file(self, path):
        with open(f"{path}/.rosinstall", "w") as f:
            f.write(self.to_string())
