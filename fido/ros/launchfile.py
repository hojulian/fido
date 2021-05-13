import os
import xml.etree.ElementTree as ET
from typing import Any, Mapping


class LaunchFile(object):
    """Represents a ROS launch file builder.

    Currently supported tags: include, node, and param.

    For details about the XML format used by LaunchFile,
    see http://wiki.ros.org/roslaunch/XML.
    """

    def __init__(self, name: str):
        self._name = name
        self._tree = ET.Element("launch")

    def include(
        self, file: str, args: Mapping[str, str] = {}, envs: Mapping[str, str] = {}
    ) -> None:
        """Add an `<include>` tag to launch file.

        The `<include>` tag enables you to import another roslaunch XML file into the
        current file.

        See http://wiki.ros.org/roslaunch/XML/include for more details.

        Args:
            file (str): Name of file to include.
            args (dict): Pass argument(s) to the included file.
            envs (dict): Set environment variables on across the entire included file.
        """
        e = ET.Element("include", {"file": file})
        for k, v in args.items():
            ET.SubElement(e, "arg", {"name": k, "value": v})

        for k, v in envs.items():
            ET.SubElement(e, "env", {"name": k, "value": v})

        self._tree.append(e)

    def node(
        self, pkg: str, node_type: str, name: str, args: Mapping[str, Any] = {}
    ) -> None:
        """Add an `<node>` tag to launch file.

        The `<node>` tag specifies a ROS node that you wish to have launched. This is
        the most common roslaunch tag as it supports the most important features:
        bringing up and taking down nodes.

        See http://wiki.ros.org/roslaunch/XML/node for more details.

        Args:
            pkg (str): package of node.
            node_type (str): Node type. There must be a corresponding executable with
                the same name.
            name (str): Node name. Note that `name` cannot contain a namespace. Use the
                ns attribute instead.
            args (dict): Pass arguments to node.
        """
        args_str = self.__normalize_args(args)

        e = ET.Element(
            "node",
            {
                "pkg": pkg,
                "type": node_type,
                "name": name,
                "args": args_str,
            },
        )
        self._tree.append(e)

    def __normalize_args(self, args: dict):
        args_pairs = []
        for k, v in args.items():
            args_pairs.append(f"-{k}")
            if str(v) != "":
                args_pairs.append(str(v))
        return " ".join(args_pairs)

    def param(self, name: str, command: str) -> None:
        """Add an `<param>` tag to launch file.

        The `<param>` tag defines a parameter to be set on the Parameter Server.

        See http://wiki.ros.org/roslaunch/XML/param for more details.

        Args:
            name (str): Parameter name. Namespaces can be included in the parameter
                name, but globally specified names should be avoided.
            command (str): The output of the command will be read and stored as a
                string. It is strongly recommended that you use the package-relative
                `$(find)/file.txt` syntax to specify file arguments. You should also
                quote file arguments using single quotes due to XML escaping
                requirements.
        """
        e = ET.Element(
            "param",
            {
                "name": name,
                "command": command,
            },
        )

        self._tree.append(e)

    def to_string(self) -> str:
        """Output file content in string.

        Returns:
            File content in string form.
        """
        return ET.tostring(self._tree).decode("utf-8")

    def to_file(self, path: str) -> None:
        """Output file content to a file in a given path.

        The output file is located in `$PATH/$NAME.launch`.

        Args:
            path (str): Path where the file is output to.
        """
        with open(os.path.join(path, f"{self._name}.launch"), "w") as f:
            f.write(self.to_string())
