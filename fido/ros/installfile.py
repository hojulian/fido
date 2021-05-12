import os
from typing import Any, List, Mapping

import yaml


class InstallFile(object):
    """Represents a ROS Install file builder.

    Currently supports adding sources from git and setup-file.

    For more details, see:
    https://docs.ros.org/en/independent/api/rosinstall/html/rosinstall_file_format.html
    """

    _dependencies: List[Mapping[Any, Any]] = []

    def git(self, localpath: str, src: str, branch: str = "master") -> None:
        """Add a git based source.

        Args:
            localpath (str): Path where to install files.
            src (str): Git repo uri. For example: `https://github.com/some/repo.git`.
            branch (str): Branch name. Default: `master`.
        """
        self._dependencies.append(
            {
                "git": {
                    "local-name": localpath,
                    "uri": src,
                    "version": branch,
                }
            }
        )

    def setup_file(self, localpath: str) -> None:
        """Add a setup-file source.

        Args:
            localpath (str): Path where to install files.
        """
        self._dependencies.append(
            {
                "setup-file": {
                    "local-name": localpath,
                }
            }
        )

    def to_string(self) -> str:
        """Output file content in string.

        Returns:
            File content in string form.
        """
        return yaml.dump(self._dependencies, sort_keys=True, default_flow_style=False)

    def to_file(self, path: str) -> None:
        """Output file content to a file in a given path.

        The output file is located in $PATH/.rosinstall.

        Args:
            path (str): Path where the file is output to.
        """
        with open(os.path.join(path, ".rosinstall"), "w") as f:
            yaml.dump(self._dependencies, f, sort_keys=True, default_flow_style=False)
