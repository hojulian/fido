from docker import DockerClient

# docker_client = DockerClient(base_url="tcp://127.0.0.1:1234")


def set_docker_host(base_url="tcp://127.0.0.1:1234", version="1.35"):
    """Set the Docker client connection details.

    Args:
        base_url (str): URL to Docker server. For example,
            `unix:///var/run/docker.sock` or `tcp://127.0.0.1:1234`. Default:
            `tcp://127.0.0.1:1234`.
        version (str): The version of the API to use. Set to `auto` to automatically
            detect the server's version. Default: `1.35`.

    Raises:
        fd.errors.DockerError: If the specified Docker server does not exist, or failed
        to connect.
    """

    global docker_client
    docker_client = DockerClient(base_url=base_url, version=version)


def set_logging(node_name, level):
    """Enable logging for a given node, and its logging level.

    This is a legacy feature inherited from `robot_services`. See `robot_services`'s
    documentation for more details.

    Args:
        node_name (str): The name of the node.
        level (str): Description of the log's type.
    """
    pass
