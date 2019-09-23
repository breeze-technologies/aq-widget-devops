import subprocess


def run_cmd(cmd):
    print("$", cmd)
    output = subprocess.check_output(cmd, shell=True)
    print("Output:\n" + str(output.decode("utf-8")))
