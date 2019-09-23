from .shell import run_cmd


def install(dir):
    print("Running npm install in:", dir)
    run_cmd("npm install --prefix ./"+dir)


def build(dir):
    print("Running npm build in:", dir)
    run_cmd("npm run build --prefix "+dir)
