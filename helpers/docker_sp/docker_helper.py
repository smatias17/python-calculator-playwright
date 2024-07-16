import subprocess

def docker_list(exec_comm: str):
    docker_output = []
    with open("tmp/output.log", "w") as output:
        subprocess.call(f'{exec_comm}', shell=True, stdout=output)
    docker_output = open("tmp/output.log").read()
    return docker_output.split(' ')