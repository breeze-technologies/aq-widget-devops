from .shell import run_cmd


def build(image_name, file):
    print("\n#########################")
    print("Running docker build...")
    run_cmd('docker build -t "'+image_name+'" -f '+file+' .')
