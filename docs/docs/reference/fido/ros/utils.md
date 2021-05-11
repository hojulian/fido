---
sidebar_label: utils
title: fido.ros.utils
---

### prepare\_workspace

```python
def prepare_workspace(path: str) -> None
```

Prepare workspace at the given path.

This is equivalent to calling `rosws init` on the given path.

Internal use only.

**Arguments**:

- `path` _str_ - Local workspace path.

### init\_package

```python
def init_package(path: str, package: str) -> None
```

Create a package at the given path.

This is equivalent to calling `catkin_create_pkg` on the given path.

Internal use only.

**Arguments**:

- `path` _str_ - Path to create package.
- `package` _str_ - Package name.

### gather\_dependencies

```python
def gather_dependencies(path: str) -> None
```

Gather all dependencies.

This is equivalent to calling `rosws update` on the given workspace path.

Internal use only.

**Arguments**:

- `path` _str_ - Workspace path.

