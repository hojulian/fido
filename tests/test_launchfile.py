import os
import tempfile
import unittest

from fido.ros.launchfile import LaunchFile


class TestLaunchFile(unittest.TestCase):

    def test_to_string(self):
        test_cases = [
            {
                "desc": "one include, node, param each",
                "name": "test_launch",
                "include": {
                    "file": "some/file",
                    "args": {
                        "name": "some_file",
                        "gui": "true",
                    },
                },
                "node": {
                    "pkg": "some_pkg",
                    "node_type": "some_node",
                    "name": "some_pkg",
                    "args": {
                        "x": "1",
                        "y": "2",
                        "z": "3",
                    },
                },
                "param": {
                    "name": "some_param",
                    "command": "/bin/some_command",
                },
                "expected": '<launch><include file="some/file"><arg name="name" value="some_file" /><arg name="gui" value="true" /></include><node pkg="some_pkg" type="some_node" name="some_pkg" args="-x 1 -y 2 -z 3" /><param name="some_param" command="/bin/some_command" /></launch>',
            }
        ]

        for tc in test_cases:
            f = LaunchFile(tc["name"])
            f.include(tc["include"]["file"], tc["include"]["args"])
            f.node(tc["node"]["pkg"], tc["node"]["node_type"], tc["node"]["name"], tc["node"]["args"])
            f.param(tc["param"]["name"], tc["param"]["command"])
            self.assertEqual(f.to_string(), tc["expected"], tc["desc"])

    def test_to_file(self):
        test_cases = [
            {
                "desc": "one include, node, param each",
                "name": "test_launch",
                "include": {
                    "file": "some/file",
                    "args": {
                        "name": "some_file",
                        "gui": "true",
                    },
                },
                "node": {
                    "pkg": "some_pkg",
                    "node_type": "some_node",
                    "name": "some_pkg",
                    "args": {
                        "x": "1",
                        "y": "2",
                        "z": "3",
                    },
                },
                "param": {
                    "name": "some_param",
                    "command": "/bin/some_command",
                },
                "expected": '<launch><include file="some/file"><arg name="name" value="some_file" /><arg name="gui" value="true" /></include><node pkg="some_pkg" type="some_node" name="some_pkg" args="-x 1 -y 2 -z 3" /><param name="some_param" command="/bin/some_command" /></launch>',
            }
        ]

        for tc in test_cases:
            f = LaunchFile(tc["name"])
            f.include(tc["include"]["file"], tc["include"]["args"])
            f.node(tc["node"]["pkg"], tc["node"]["node_type"], tc["node"]["name"], tc["node"]["args"])
            f.param(tc["param"]["name"], tc["param"]["command"])
            
            with tempfile.TemporaryDirectory() as path:
                f.to_file(path)
                with open(os.path.join(path, f"{tc['name']}.launch"), "r") as out:
                    out_text = "".join(out.readlines())
                    self.assertEqual(out_text, tc["expected"], tc["desc"])
