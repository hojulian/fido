---
sidebar_label: installfile
title: fido.ros.installfile
---

## InstallFile

```python
class InstallFile(object)
```

Represents a ROS Install file builder.

Currently supports adding sources from git and setup-file.

For more details, see:
https://docs.ros.org/en/independent/api/rosinstall/html/rosinstall_file_format.html

### git

```python
 | def git(localpath: str, src: str, branch: str = "master") -> None
```

Add a git based source.

**Arguments**:

- `localpath` _str_ - Path where to install files.
- `src` _str_ - Git repo uri. For example: `https://github.com/some/repo.git`.
- `branch` _str_ - Branch name. Default: `master`.

### setup\_file

```python
 | def setup_file(localpath: str) -> None
```

Add a setup-file source.

**Arguments**:

- `localpath` _str_ - Path where to install files.

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

The output file is located in `$PATH/.rosinstall`.

**Arguments**:

- `path` _str_ - Path where the file is output to.

