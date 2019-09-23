#!/usr/bin/env python3

import argparse
import subprocess
import os

from utils import git, npm, docker


GIT_REMOTE_API = "git@bitbucket.org:breezecloud/aq-widget-api.git"
GIT_REMOTE_APP = "git@bitbucket.org:breezecloud/aq-widget-app.git"
GIT_REMOTE_CLIENT = "git@bitbucket.org:breezecloud/aq-client-eea.git"
GIT_LOCAL_DIR_API = "aq-widget-api"
GIT_LOCAL_DIR_APP = "aq-widget-app"
GIT_LOCAL_DIR_CLIENT = "aq-client-eea"

DOCKER_IMAGE_NAME = "aq-widget"
DOCKER_FILE = "bundle.Dockerfile"
DOCKER_BUILD_ONLY = False

parser = argparse.ArgumentParser(
    description='Fetch source for aq-widget-api and aq-widget-app and bundle them to a Docker file.')
parser.add_argument('--apiVersion', dest='apiVersion', type=str,
                    help='the version (tag on master branch) of aq-widget-api')
parser.add_argument('--appVersion', dest='appVersion', type=str,
                    help='the version (tag on master branch) of aq-widget-app')
parser.add_argument('--clientVersion', dest='clientVersion', type=str,
                    help='the version (tag on master branch) of aq-client-eea')
parser.add_argument('--apiBranch', dest='apiBranch', type=str, default="master",
                    help='the branch of aq-widget-api')
parser.add_argument('--appBranch', dest='appBranch', type=str, default="master",
                    help='the branch of aq-widget-app')
parser.add_argument('--clientBranch', dest='clientBranch', type=str, default="master",
                    help='the branch of aq-client-eea')
parser.add_argument('--dockerImageName', dest='dockerImageName', type=str, default=DOCKER_IMAGE_NAME,
                    help='the name of the resulting docker image')
parser.add_argument('--dockerBuildOnly',
                    dest='dockerBuildOnly',
                    default=DOCKER_BUILD_ONLY,
                    const=True,
                    action="store_const",
                    help='only execute the docker build command and omit git/npm operations')


args = parser.parse_args()
apiVersion = args.apiVersion
appVersion = args.appVersion
clientVersion = args.clientVersion
apiBranch = args.apiBranch
appBranch = args.appBranch
clientBranch = args.clientBranch
DOCKER_BUILD_ONLY = args.dockerBuildOnly
DOCKER_IMAGE_NAME = args.dockerImageName


print("Running bundler...")
if DOCKER_BUILD_ONLY:
    print("Docker build only!")
else:
    print("API version: " + str(apiVersion))
    print("API branch: " + str(apiBranch))
    print("App version: " + str(appVersion))
    print("App branch: " + str(appBranch))
    print("EEA client version: " + str(clientVersion))
    print("EEA client branch: " + str(clientBranch))


if not DOCKER_BUILD_ONLY:
    git.load_source(GIT_REMOTE_API, GIT_LOCAL_DIR_API,
                    branch=apiBranch, tag=apiVersion)
    git.load_source(GIT_REMOTE_APP, GIT_LOCAL_DIR_APP,
                    branch=appBranch,  tag=appVersion)
    git.load_source(GIT_REMOTE_CLIENT, GIT_LOCAL_DIR_CLIENT,
                    branch=clientBranch,  tag=clientVersion)

    npm.install(GIT_LOCAL_DIR_CLIENT)
    npm.build(GIT_LOCAL_DIR_CLIENT)

    npm.install(GIT_LOCAL_DIR_API)
    npm.build(GIT_LOCAL_DIR_API)

    npm.install(GIT_LOCAL_DIR_APP)
    npm.build(GIT_LOCAL_DIR_APP)

docker.build(DOCKER_IMAGE_NAME, DOCKER_FILE)
