import os
import xml.etree.ElementTree as ET


class LaunchFile(object):
    """Represents a ROS launch file.

    For details about the XML format used by LaunchFile,
    see http://wiki.ros.org/roslaunch/XML.
    """

    def __init__(self, name):
        self._name = name
        self._tree = ET.Element("launch")

    def include(self, file, args):
        e = ET.Element("include", {"file": file})
        for k, v in args.items():
            ET.SubElement(e, "arg", {"name": k, "value": v})

        self._tree.append(e)

    def node(self, pkg, node_type, name, args: dict):
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
            args_pairs.append(v)
        return " ".join(args_pairs)

    def param(self, name, command):
        e = ET.Element(
            "param",
            {
                "name": name,
                "command": command,
            },
        )

        self._tree.append(e)

    def to_string(self):
        return ET.tostring(self._tree).decode("utf-8")

    def to_file(self, path):
        with open(os.path.join(path, f"{self._name}.launch"), "w") as f:
            f.write(self.to_string())
