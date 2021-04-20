import os

from catkin_pkg.package_templates import PackageTemplate, create_package_files
from rosinstall.rosws_cli import RoswsCLI


def prepare_workspace(path):
    cli = RoswsCLI()
    cli.cmd_init([path])


def init_package(path, package):
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
        maintainer_names=maintainer,
        author_names=author,
        version=version,
        catkin_deps=None,
        system_deps=None,
        boost_comps=None,
    )

    create_package_files(target_path, package_template, distro, newfiles={})

    os.makedirs(os.path.join(path, "src", package))
    os.makedirs(os.path.join(path, "src", package, "launch"))
    os.makedirs(os.path.join(path, "src", package, "scripts"))


def gather_dependencies(path):
    cli = RoswsCLI()
    cli.cmd_update(path)
