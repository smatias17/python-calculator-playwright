import subprocess
import uuid

def docker_list(exec_comm: str):
    docker_output = []
    file_name = f'output{gen_uuid()}.log'
    with open(f'tmp/{file_name}', "w") as output:
        subprocess.call(f'{exec_comm}', shell=True, stdout=output)
    docker_output = open(f'tmp/{file_name}').read()
    return docker_output.split(' ')

def gen_uuid():
    return str(uuid.uuid4())