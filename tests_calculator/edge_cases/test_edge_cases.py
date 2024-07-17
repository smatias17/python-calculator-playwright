import pytest
from helpers.docker_sp.docker_helper import docker_list

def test_should_validate_operation_position_v1():
    value_v1 = 'test'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli {value_v1}'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Error:' in docker_output:
        expected_result = f'Error: Unknown operation: {value_v1}'
        assert expected_result==actual_result, f'Incorrect inputted operation type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def test_should_validate_operation_position_v2():
    value_v2 = '1'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli {value_v2}'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Error:' in docker_output:
        expected_result = f'Error: Unknown operation: {value_v2}'
        assert expected_result==actual_result, f'Incorrect inputted operation type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'
                      
def test_should_validate_special_symbols_v1():
    value_v1 = "\\"
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add {value_v1}1 {value_v1}1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Invalid argument.' in docker_output:
        expected_result = f'Invalid argument. Must be a numeric value.'
        assert expected_result==actual_result, f'Incorrect argument type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'
                      
def test_should_validate_special_symbols_v2():
    value_v2 = '"'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli subtract {value_v2}1 {value_v2}1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Invalid argument.' in docker_output:
        expected_result = f'Invalid argument. Must be a numeric value.'
        assert expected_result==actual_result, f'Incorrect argument type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def test_should_validate_special_symbols_v3():
    value_v3 = '#'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli multiply {value_v3}1 {value_v3}1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Invalid argument.' in docker_output:
        expected_result = f'Invalid argument. Must be a numeric value.'
        assert expected_result==actual_result, f'Incorrect argument type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def test_should_validate_one_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Error:' in docker_output:
        expected_result = f'Error: Incorrect number of arguments.'
        assert expected_result==actual_result, f'Incorrect number of arguments, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'
                      
def test_should_validate_three_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1 1 1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Error:' in docker_output:
        expected_result = f'Error: Incorrect number of arguments.'
        assert expected_result==actual_result, f'Incorrect number of arguments, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def test_should_validate_four_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1 1 1 1'
    print(docker_command)
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    if 'Error:' in docker_output:
        expected_result = f'Error: Incorrect number of arguments.'
        assert expected_result==actual_result, f'Incorrect number of arguments, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def test_should_add_float_numbers_doc():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1.00000001 1.00000001'
    print(docker_command)
    docker_output = docker_list(docker_command)
    print(docker_output)
    if 'Result:' in docker_output:
        expected_result = 2.0
        assert expected_result==docker_output[1], f'Incorrect result for addition, ' \
                                                  f'Expected result: {expected_result} ' \
                                                  f'Actual result: {docker_output[1]} ' \
                                                  f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'