# AQ Widget bundler

This repository contains a Dockerfile to bundle the AQ Widget into a Docker container.
It therefore clones `aq-widget-app` and `aq-widget-api`, installs, merges and runs them.

## Build instructions

To build the Docker image, run:

```shell
$ docker build -t "aq-widget:1.0.0" -f bundle.Dockerfile .
```

## Run instructions

To start the container, run:

```shell
$ docker run -e "PORT=8080" -p 8080:8080 aq-widget:1.0.0
```

---

Licensed under the EUPL.