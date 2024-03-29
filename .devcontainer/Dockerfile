# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.158.0/containers/python-3/.devcontainer/base.Dockerfile
# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.158.0/containers/docker-from-docker/.devcontainer/devcontainer.json

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="true"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install 'poetry==1.1.5' \
   && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1

# Install Docker CLI
ARG USERNAME=automatic
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ADD https://raw.githubusercontent.com/microsoft/vscode-dev-containers/master/containers/docker-from-docker/.devcontainer/library-scripts/docker-debian.sh /tmp/library-scripts/

# Use Docker script from script library to set things up
RUN /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" "${USE_MOBY}"

ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]
