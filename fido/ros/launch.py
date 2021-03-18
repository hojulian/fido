import xml.etree.ElementTree as ET


class LaunchFile(object):
    def __init__(self):
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

    def tostring(self):
        return ET.tostring(self._tree)
