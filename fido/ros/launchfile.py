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

    def node(self, pkg, node_type, name, args):
        e = ET.Element(
            "node",
            {
                "pkg": pkg,
                "type": node_type,
                "name": name,
                "args": args,
            },
        )

        self._tree.append(e)

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
        return ET.tostring(self._tree)

    def to_file(self, path):
        with open(f"{path}/{self._name}.launch", "w") as f:
            f.write(self.to_string)
