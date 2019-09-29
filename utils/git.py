import os

from .shell import run_cmd


def load_source(url, dir, branch="master", tag=None):
    print("\nFetching source for:", dir)
    if(not os.path.isdir(dir) or not os.path.isdir(dir+"/.git")):
        print("Cloning, because local repository does not exist.")
        run_cmd("git clone "+url+" "+dir)

    run_cmd("git -C "+dir+" fetch --tags")
    run_cmd("git -C "+dir+" checkout "+branch)
    run_cmd("git -C "+dir+" pull")
    if tag != None:
        run_cmd("git -C "+dir+" checkout "+tag)
