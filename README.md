# AQ Widget bundler

This repository contains a Dockerfile to bundle the AQ Widget into a Docker container.
It therefore clones `aq-widget-app` and `aq-widget-api`, installs, merges and runs them.

## Build instructions

There are multiple ways in order to build a deployable Docker image. The `build_bundle.py` script
offers a convenient method for different purposes.

The following command fetches the source code of all requires git repositories, installs them and adds them to an image named `aq-widget`. The latest `master` branches of each repository will be checked out.

```shell
$ ./build_bundle.py
```

In order to define specific versions of the source repositories, (version) tags can be added.

```shell
$ ./build_bundle.py --apiVersion 1.2.3 --appVersion 3.2.1 --clientVersion 1.0.0
```

For development purposes, branches names may be specified instead of or in addition to version tags.

```shell
$ ./build_bundle.py --apiBranch dev --appBranch feature/colors --clientBranch dev
```

To only run the docker build without changing/updating local repositories, the `--dockerBuildOnly` flag may be used. Generally, it is also recommended to specify an image name.

```shell
$ ./build_bundle.py --apiBranch dev --appBranch feature/colors --clientBranch dev --dockerBuildOnly --dockerImageName orgName/aq-widget:2.1.0
```

To publish a built image to Docker Hub, run (after successful login using `docker login`):

```shell
$ docker push orgName/aq-widget:2.1.0
```


## Run instructions

To start the container, run:

```shell
$ docker run -e "PORT=8080" -p 8080:3000 aq-widget
```

---

Licensed under the EUPL.
