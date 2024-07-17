from helpers.docker_resources.docker_helper import docker_list
from helpers.functions_resources.validate_helper import ec_argument_type_validate, ec_inputted_operation_type_validate, \
    ec_number_of_arguments_validate, ec_result_for_addition_validate

def test_should_validate_operation_position_v1():
    value_v1 = 'test'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli {value_v1}'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Error: Unknown operation: {value_v1}'
    ec_inputted_operation_type_validate(docker_output, expected_result, actual_result, docker_command)

def test_should_validate_operation_position_v2():
    value_v2 = '1'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli {value_v2}'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Error: Unknown operation: {value_v2}'
    ec_inputted_operation_type_validate(docker_output, expected_result, actual_result, docker_command)
                      
def test_should_validate_special_symbols_v1():
    value_v1 = "\\"
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add {value_v1}1 {value_v1}1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Invalid argument. Must be a numeric value.'
    ec_argument_type_validate(docker_output, expected_result, actual_result, docker_command)
                      
def test_should_validate_special_symbols_v2():
    value_v2 = '"'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli subtract {value_v2}1 {value_v2}1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Invalid argument. Must be a numeric value.'
    ec_argument_type_validate(docker_output, expected_result, actual_result, docker_command)

def test_should_validate_special_symbols_v3():
    value_v3 = '#'
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli multiply {value_v3}1 {value_v3}1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Invalid argument. Must be a numeric value.'
    ec_argument_type_validate(docker_output, expected_result, actual_result, docker_command)

def test_should_validate_one_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Error: Incorrect number of arguments.'
    ec_number_of_arguments_validate(docker_output, expected_result, actual_result, docker_command)
                      
def test_should_validate_three_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1 1 1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Error: Incorrect number of arguments.'
    ec_number_of_arguments_validate(docker_output, expected_result, actual_result, docker_command)

def test_should_validate_four_argument():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1 1 1 1'
    docker_output = docker_list(docker_command)
    actual_result = ' '.join(docker_output)
    expected_result = f'Error: Incorrect number of arguments.'
    ec_number_of_arguments_validate(docker_output, expected_result, actual_result, docker_command)

def test_should_add_float_numbers_doc():
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 1.00000001 1.00000001'
    docker_output = docker_list(docker_command)
    expected_result = 2.0
    ec_result_for_addition_validate(docker_output, expected_result, docker_output[1], docker_command)
