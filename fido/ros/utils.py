import os
import re

from catkin_pkg.package_templates import PackageTemplate, create_package_files
from rosinstall.rosws_cli import RoswsCLI
from vcstool.commands import import_


def prepare_workspace(path: str) -> None:
    """Prepare workspace at the given path.

    This is equivalent to calling `rosws init` on the given path.

    Internal use only.

    Args:
        path (str): Local workspace path.
    """

    cli = RoswsCLI()
    cli.cmd_init([path])

    # Fix setup.sh path
    with open(os.path.join(path, "setup.sh"), "r") as f:
        script = f.read()

    newpath = "export ROS_WORKSPACE=/workspace/fido_ws\n"
    script = re.sub(r"(export ROS_WORKSPACE=).*(\n)", newpath, script)

    with open(os.path.join(path, "setup.sh"), "w") as f:
        f.write(script)


def init_package(path: str, package: str) -> None:
    """Create a package at the given path.

    This is equivalent to calling `catkin_create_pkg` on the given path.

    Internal use only.

    Args:
        path (str): Path to create package.
        package (str): Package name.
    """

    package_name = package
    description = "Simulation package created by Fido. DO NOT EDIT."
    maintainer = "Fido maintainers"
    author = "Fido authors"
    version = "0.0.1"
    distro = "melodic"
    target_path = os.path.join(path, "src", package)

    package_template = PackageTemplate._create_package_template(
        package_name=package_name,
        description=description,
        licenses=[],
        maintainer_names=[maintainer],
        author_names=[author],
        version=version,
        catkin_deps=None,
        system_deps=None,
        boost_comps=None,
    )

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    create_package_files(os.path.abspath(target_path), package_template, distro)

    os.makedirs(os.path.join(path, "src", package, "launch"))
    os.makedirs(os.path.join(path, "src", package, "scripts"))


def gather_dependencies(path: str) -> None:
    """Gather all dependencies.

    This is equivalent to calling `rosws update` on the given workspace path.

    Internal use only.

    Args:
        path (str): Workspace path.
    """
    path = os.path.abspath(path)

    # Workaround for dealing with local path with spaces.
    # Note: This is a slower alternative to `rosws`.
    if " " in path:
        import_.main(
            args=[
                "--input",
                os.path.join(path, ".rosinstall"),
                "--shallow",
                "--debug",
                path,
            ]
        )
    else:
        cli = RoswsCLI()
        cli.cmd_update(path, ["-t", path])
