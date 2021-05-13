---
sidebar_label: launchfile
title: fido.ros.launchfile
---

## LaunchFile

```python
class LaunchFile(object)
```

Represents a ROS launch file builder.

Currently supported tags: include, node, and param.

For details about the XML format used by LaunchFile,
see http://wiki.ros.org/roslaunch/XML.

### include

```python
 | def include(file: str, args: Mapping[str, str] = {}, envs: Mapping[str, str] = {}) -> None
```

Add an `<include>` tag to launch file.

The `<include>` tag enables you to import another roslaunch XML file into the
current file.

See http://wiki.ros.org/roslaunch/XML/include for more details.

**Arguments**:

- `file` _str_ - Name of file to include.
- `args` _dict_ - Pass argument(s) to the included file.
- `envs` _dict_ - Set environment variables on across the entire included file.

### node

```python
 | def node(pkg: str, node_type: str, name: str, args: Mapping[str, Any] = {}) -> None
```

Add an `<node>` tag to launch file.

The `<node>` tag specifies a ROS node that you wish to have launched. This is
the most common roslaunch tag as it supports the most important features:
bringing up and taking down nodes.

See http://wiki.ros.org/roslaunch/XML/node for more details.

**Arguments**:

- `pkg` _str_ - package of node.
- `node_type` _str_ - Node type. There must be a corresponding executable with
  the same name.
- `name` _str_ - Node name. Note that `name` cannot contain a namespace. Use the
  ns attribute instead.
- `args` _dict_ - Pass arguments to node.

### param

```python
 | def param(name: str, command: str) -> None
```

Add an `<param>` tag to launch file.

The `<param>` tag defines a parameter to be set on the Parameter Server.

See http://wiki.ros.org/roslaunch/XML/param for more details.

**Arguments**:

- `name` _str_ - Parameter name. Namespaces can be included in the parameter
  name, but globally specified names should be avoided.
- `command` _str_ - The output of the command will be read and stored as a
  string. It is strongly recommended that you use the package-relative
  `$(find)/file.txt` syntax to specify file arguments. You should also
  quote file arguments using single quotes due to XML escaping
  requirements.

### to\_string

```python
 | def to_string() -> str
```

Output file content in string.

**Returns**:

  File content in string form.

### to\_file

```python
 | def to_file(path: str) -> None
```

Output file content to a file in a given path.

The output file is located in `$PATH/$NAME.launch`.

**Arguments**:

- `path` _str_ - Path where the file is output to.

