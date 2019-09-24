# AQ Widget ▶︎ Build & Run Instructions

This repository contains a Dockerfile to bundle the AQ Widget into a Docker container. It therefore clones `aq-widget-app` and `aq-widget-api`, installs, merges and runs them.

## Prerequisites

For building and running this software, the following dependencies need to be installed on the local machine:

| **Dependency** | **Required version** |
|----------------|----------------------|
| Python         | 3.1+                 |
| NodeJS         | 10.0+                |
| NPM            | 6.9+                 |
| Git            | 2.18+                |
| Docker         | 18.09+               |

## Build instructions

There are multiple ways in order to build a deployable Docker image. The `build_bundle.py` script offers a convenient method for different purposes.

### Build configuration

The build script requires the URLs to the remote git repositories of the project modules. Therefore, a `config.py` file needs to be created. A `config.py` template can be found in `config.py.example`.

```python
GIT_REMOTE_API = "git@example.com:orgName/aq-widget-api.git"
GIT_REMOTE_APP = "git@example.com:orgName/aq-widget-app.git"
GIT_REMOTE_CLIENT = "git@example.com:orgName/aq-client-eea.git"
```

### Build script options

The following command fetches the source code of all required git repositories, installs required dependencies and adds them to a Docker image named `aq-widget`. The latest `master` branches of each repository will be used.

```shell
$ ./build_bundle.py
```

> **Note**: Please change to the `aq-widget-devops` directory before running the script.

#### Specifying versions

In order to define specific versions of the source repositories, (version) tags can be added.

```shell
$ ./build_bundle.py --apiVersion 1.2.3 --appVersion 3.2.1 --clientVersion 1.0.0
```

#### Specifying branches

For development purposes, branch names may be specified instead of or in addition to version tags.

```shell
$ ./build_bundle.py --apiBranch dev --appBranch feature/colors --clientBranch dev
```

#### Configuring Docker

To only run the docker build without changing/updating local repositories, the `--dockerBuildOnly` flag may be used. Generally, it is also recommended to specify an image name using `--dockerImageName`.

```shell
$ ./build_bundle.py --apiBranch dev --appBranch feature/colors --clientBranch dev --dockerBuildOnly --dockerImageName orgName/aq-widget:2.1.0
```

#### Publishing to Docker Hub

To publish a built image to Docker Hub, run (after successful login using `docker login`):

```shell
$ docker push orgName/aq-widget:2.1.0
```


## Run instructions

To start a Docker container based on the just created Docker image, run:

```shell
$ docker run -e "PORT=8080" -p 3000:8080 aq-widget
```

The AQ Widget container now listens on host port `3000`.

---

Licensed under the EUPL.
