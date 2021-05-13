---
sidebar_label: config
title: fido.config
---

### set\_docker\_host

```python
def set_docker_host(base_url: str = "unix:///var/run/docker.sock", version: str = "1.35") -> None
```

Set the Docker client connection details.

**Arguments**:

- `base_url` _str_ - URL to Docker server. For example,
  `unix:///var/run/docker.sock` or `tcp://127.0.0.1:1234`. Default:
  `tcp://127.0.0.1:1234`.
- `version` _str_ - The version of the API to use. Set to `auto` to
  automatically detect the server's version. Default: `1.35`.
  

**Raises**:

- `DockerError` - If the specified Docker server does not exist, or failed to
  connect.

### set\_logging

```python
def set_logging(node_name: str, level: str) -> None
```

Enable logging for a given node, and its logging level.

This is a legacy feature inherited from `robot_services`. See
`robot_services`'s documentation for more details.

**Arguments**:

- `node_name` _str_ - The name of the node.
- `level` _str_ - Description of the log's type.

