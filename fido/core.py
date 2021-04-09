import os
from random import randint
from uuid import uuid4

from docker import DockerClient
from docker.errors import APIError, NotFound

from .errors import DockerError


class Core(object):
    _docker_client = None
    _ros_client = None
    _logger = None

    _used_ids = []
    _used_ports = []

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
        sim_id,
        volume,
        image="cosi119/fido-simulation:base",
        vnc_port="",
        rosbridge_port="",
    ):
        volume_path = os.path.abspath(volume)

        try:
            c = cls.__docker().api.create_container(
                image=image,
                name=f"fido-simulation-{sim_id}",
                hostname="fido-simulation",
                detach=True,
                ports=[(6080, "tcp"), (9090, "tcp")],
                volumes=["/workspace/fido_ws"],
                host_config=cls.__docker().api.create_host_config(
                    auto_remove=True,
                    port_bindings={
                        "6080/tcp": vnc_port,
                        "9090/tcp": rosbridge_port,
                    },
                    binds=[f"{volume_path}:/workspace/fido_ws"],
                ),
            )
            return c.get("Id")
        except (APIError, NotFound) as exc:
            raise DockerError("failed to create container") from exc

    @classmethod
    def start_container(cls, container_id):
        try:
            cls.__docker().api.start(container=container_id)
        except (APIError) as exc:
            raise DockerError("failed to start container") from exc

    @classmethod
    def container_exec(cls, container_id, cmd, workdir="/workspace/fido_ws"):
        try:
            e = cls.__docker().api.exec_create(container_id, cmd, workdir=workdir)
            return cls.__docker().api.exec_start(e.get("Id"), detach=True)
        except (APIError) as exc:
            raise DockerError("failed to execute command on container") from exc

    @classmethod
    def remove_container(cls, container_id, force=True):
        try:
            cls.__docker().api.remove_container(container_id, force=force)
        except (APIError) as exc:
            raise DockerError("failed to remove container") from exc

    @classmethod
    def generate_sim_id(cls):
        sim_id = str(uuid4())

        while sim_id in cls._used_ids:
            sim_id = str(uuid4())

        cls._used_ids.append(sim_id)
        return sim_id

    @classmethod
    def generate_port(cls):
        max_n = 8100
        min_n = 8000
        port = randint(min_n, max_n)

        while port in cls._used_ports:
            port = randint(min_n, max_n)

        cls._used_ports.append(port)
        return port

    @classmethod
    def set_docker_host(cls, base_url="tcp://127.0.0.1:1234", version="1.35"):
        """Set the Docker client connection details.

        Args:
            base_url (str): URL to Docker server. For example,
                `unix:///var/run/docker.sock` or `tcp://127.0.0.1:1234`. Default:
                `tcp://127.0.0.1:1234`.
            version (str): The version of the API to use. Set to `auto` to
                automatically detect the server's version. Default: `1.35`.

        Raises:
            fido.errors.DockerError: If the specified Docker server does not exist,
            or failed to connect.
        """
        try:
            cls._docker_client = DockerClient(base_url=base_url, version=version)
        except APIError:
            raise DockerError(str(APIError))

    @classmethod
    def set_logging(cls, node_name, level):
        """Enable logging for a given node, and its logging level.

        This is a legacy feature inherited from `robot_services`. See
        `robot_services`'s documentation for more details.

        Args:
            node_name (str): The name of the node.
            level (str): Description of the log's type.
        """
        pass
