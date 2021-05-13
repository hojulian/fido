---
sidebar_label: core
title: fido.core
---

## Core

```python
class Core(object)
```

Core provides utility functions for Fido internal use.

### create\_container

```python
 | @classmethod
 | def create_container(cls, sim_id: str, volume: str, image: str = "cosi119/fido-simulation:base", vnc_port: str = "6080", rosbridge_port: str = "9090") -> str
```

Create a docker container with the given image and volume.

**Arguments**:

- `sim_id` _str_ - Simulation ID. Should be unique among simulations.
- `volume` _str_ - Path to local catkin workspace used by the simulation.
- `image` _str_ - Docker image for running simulation.
- `vnc_port` _str_ - Port of noVNC. Should be unique among simulations.
- `rosbridge_port` _str_ - Port of rosbridge. Should be unique among simulations.
  

**Returns**:

  The container ID.
  

**Raises**:

- `DockerError` - If failed to create container.

### start\_container

```python
 | @classmethod
 | def start_container(cls, container_id: str) -> None
```

Start container by ID.

**Arguments**:

- `container_id` _str_ - Docker container ID.
  

**Raises**:

- `DockerError` - If failed to start container.

### container\_exec

```python
 | @classmethod
 | def container_exec(cls, container_id: str, cmd: str, workdir: str = "/workspace/fido_ws", env: Mapping[str, str] = {}, stream: bool = False) -> ExecResult
```

Execute command on container.

**Arguments**:

- `container_id` _str_ - Docker container ID.
- `cmd` _str_ - Command to execute.
- `workdir` _str_ - Path to working directory for this exec session.
- `env` _dict_ - A dictionary of strings in the following format
- ``{"PASSWORD"` - "xxx"}`.
- `stream` _bool_ - Stream response data. Default: False.
  

**Returns**:

  A tuple of (exit_code, output)
- `exit_code` - (int):
  Exit code for the executed command or None if stream is True.
  
- `output` - (generator, bytes, or tuple):
  If `stream=True`, a generator yielding response chunks. A bytestring
  containing response data otherwise.
  

**Raises**:

- `DockerError` - If failed to execute command on container.

### remove\_container

```python
 | @classmethod
 | def remove_container(cls, container_id: str, force: bool = True) -> None
```

Remove container by ID.

This will remove the container along with its volume.

**Arguments**:

- `container_id` _str_ - Docker container ID.
- `force` _bool_ - Force the removal of a running container (uses `SIGKILL`).
  

**Raises**:

- `DockerError` - If failed to remove container.

### generate\_sim\_id

```python
 | @classmethod
 | def generate_sim_id(cls) -> str
```

Generate random simulation ID.

The generated ID is guaranteed to be unique during the runtime of this process.

**Returns**:

  A random simulation ID in the form of UUID.

### generate\_port

```python
 | @classmethod
 | def generate_port(cls) -> int
```

Generate random port number.

The generated port is guaranteed to be unique during the runtime of this
process.

**Returns**:

  A random port number.

### set\_docker\_host

```python
 | @classmethod
 | def set_docker_host(cls, base_url: str = "unix:///var/run/docker.sock", version: str = "1.35") -> None
```

Set the Docker client connection details.

**Arguments**:

- `base_url` _str_ - URL to Docker server. For example,
  `unix:///var/run/docker.sock` or `tcp://127.0.0.1:1234`. Default:
  `unix:///var/run/docker.sock`.
- `version` _str_ - The version of the API to use. Set to `auto` to
  automatically detect the server's version. Default: `1.35`.
  

**Raises**:

- `DockerError` - If the specified Docker server does not exist, or failed to
  connect.

### set\_logging

```python
 | @classmethod
 | def set_logging(cls, node_name: str, level: str) -> None
```

Enable logging for a given node, and its logging level.

This is a legacy feature inherited from `robot_services`. See
`robot_services`'s documentation for more details.

**Arguments**:

- `node_name` _str_ - The name of the node.
- `level` _str_ - Description of the log's type.

