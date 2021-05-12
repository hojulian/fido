import os
from random import randint
from typing import List, Mapping
from uuid import uuid4

from docker import DockerClient
from docker.errors import APIError, NotFound
from docker.models.containers import ExecResult

from .errors import DockerError, NotImplementedError


class Core(object):
    """Core provides utility functions for Fido internal use."""

    _docker_client: DockerClient = None
    _used_ids: List[int] = []
    _used_ports: List[str] = []

    def __init__(self):
        raise RuntimeError("Core is not initializable")

    @classmethod
    def __docker(cls) -> DockerClient:
        if cls._docker_client is None:
            cls.set_docker_host()
        return cls._docker_client

    @classmethod
    def create_container(
        cls,
        sim_id: str,
        volume: str,
        image: str = "cosi119/fido-simulation:base",
        vnc_port: str = "6080",
        rosbridge_port: str = "9090",
    ) -> str:
        """Create a docker container with the given image and volume.

        Args:
            sim_id (str): Simulation ID. Should be unique among simulations.
            volume (str): Path to local catkin workspace used by the simulation.
            image (str): Docker image for running simulation.
            vnc_port (str): Port of noVNC. Should be unique among simulations.
            rosbridge_port (str): Port of rosbridge. Should be unique among simulations.

        Returns:
            The container ID.

        Raises:
            DockerError: If failed to create container.
        """

        volume_path = os.path.abspath(volume)

        try:
            c = cls.__docker().api.create_container(
                image=image,
                name=f"fido-simulation-{sim_id}",
                hostname="fido-simulation",
                detach=True,
                ports=[(6080, "tcp"), (int(rosbridge_port), "tcp")],
                volumes=["/workspace/fido_ws"],
                host_config=cls.__docker().api.create_host_config(
                    auto_remove=True,
                    port_bindings={
                        "6080/tcp": vnc_port,
                        f"{rosbridge_port}/tcp": rosbridge_port,
                    },
                    binds=[f"{volume_path}:/workspace/fido_ws"],
                ),
            )
            return c.get("Id")
        except (APIError, NotFound) as exc:
            raise DockerError("failed to create container") from exc

    @classmethod
    def start_container(cls, container_id: str) -> None:
        """Start container by ID.

        Args:
            container_id (str): Docker container ID.

        Raises:
            DockerError: If failed to start container.
        """
        try:
            cls.__docker().api.start(container=container_id)
        except (APIError) as exc:
            raise DockerError("failed to start container") from exc

    @classmethod
    def container_exec(
        cls,
        container_id: str,
        cmd: str,
        workdir: str = "/workspace/fido_ws",
        env: Mapping[str, str] = {},
        stream: bool = False,
    ) -> ExecResult:
        """Execute command on container.

        Args:
            container_id (str): Docker container ID.
            cmd (str): Command to execute.
            workdir (str): Path to working directory for this exec session.
            env (dict): A dictionary of strings in the following format
                {"PASSWORD": "xxx"}.
            stream (bool): Stream response data. Default: False.

        Returns:
            A tuple of (exit_code, output)
                exit_code: (int):
                    Exit code for the executed command or None if stream is True.

                output: (generator, bytes, or tuple):
                    If stream=True, a generator yielding response chunks. A bytestring
                    containing response data otherwise.

        Raises:
            DockerError: If failed to execute command on container.
        """

        try:
            c = cls.__docker().containers.get(container_id)
            print(f"executing {cmd}")
            return c.exec_run(
                cmd, workdir=workdir, stream=stream, socket=False, environment=env
            )
        except (APIError, NotFound) as exc:
            raise DockerError("failed to execute command on container") from exc

    @classmethod
    def remove_container(cls, container_id: str, force: bool = True) -> None:
        """Remove container by ID.

        This will remove the container along with its volume.

        Args:
            container_id (str): Docker container ID.
            force (bool): Force the removal of a running container (uses `SIGKILL`).

        Raises:
            DockerError: If failed to remove container.
        """
        try:
            cls.__docker().api.remove_container(container_id, force=force, v=True)
        except (APIError) as exc:
            raise DockerError("failed to remove container") from exc

    @classmethod
    def generate_sim_id(cls) -> str:
        """Generate random simulation ID.

        The generated ID is guaranteed to be unique during the runtime of this process.

        Returns:
            A random simulation ID in the form of UUID.
        """
        sim_id = str(uuid4())

        while sim_id in cls._used_ids:
            sim_id = str(uuid4())

        cls._used_ids.append(sim_id)
        return sim_id

    @classmethod
    def generate_port(cls) -> int:
        """Generate random port number.

        The generated port is guaranteed to be unique during the runtime of this
        process.

        Returns:
            A random port number.
        """

        max_n = 8100
        min_n = 8000
        port = randint(min_n, max_n)

        while port in cls._used_ports:
            port = randint(min_n, max_n)

        cls._used_ports.append(port)
        return port

    @classmethod
    def set_docker_host(
        cls, base_url: str = "unix:///var/run/docker.sock", version: str = "1.35"
    ) -> None:
        """Set the Docker client connection details.

        Args:
            base_url (str): URL to Docker server. For example,
                `unix:///var/run/docker.sock` or `tcp://127.0.0.1:1234`. Default:
                `unix:///var/run/docker.sock`.
            version (str): The version of the API to use. Set to `auto` to
                automatically detect the server's version. Default: `1.35`.

        Raises:
            DockerError: If the specified Docker server does not exist, or failed to
            connect.
        """
        try:
            cls._docker_client = DockerClient(base_url=base_url, version=version)
        except APIError as exc:
            raise DockerError("unable set docker host") from exc

    @classmethod
    def set_logging(cls, node_name: str, level: str) -> None:
        """Enable logging for a given node, and its logging level.

        This is a legacy feature inherited from `robot_services`. See
        `robot_services`'s documentation for more details.

        Args:
            node_name (str): The name of the node.
            level (str): Description of the log's type.
        """
        raise NotImplementedError("set_logging() is not implemented")
