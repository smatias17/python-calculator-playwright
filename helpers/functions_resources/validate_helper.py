
def add_general_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for addition, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'

def subtract_general_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for subtraction, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'

def multiply_general_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for multiplication, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'
                      
def divide_general_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for division, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'

def divide_specific_validate(docker_output, expected_result, expected_error, actual_result, actual_error, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for division, ' \
                                                  f'Expected result: {expected_result} ' \
                                                  f'Actual result: {actual_result} ' \
                                                  f'Executed command: {docker_command}'     
    elif 'Error:' in docker_output:
        assert expected_error==actual_error, f'Incorrect error message, ' \
                                             f'Expected result: {expected_error} ' \
                                             f'Actual result: {actual_error} ' \
                                             f'Executed command: {docker_command}' 
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                        f'Executed command: {docker_command}'

def ec_inputted_operation_type_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Error:' in docker_output:
        assert expected_result==actual_result, f'Incorrect inputted operation type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def ec_argument_type_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Invalid argument.' in docker_output:
        assert expected_result==actual_result, f'Incorrect argument type, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def ec_number_of_arguments_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Error:' in docker_output:
        assert expected_result==actual_result, f'Incorrect number of arguments, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {actual_result}, ' \
                      f'Executed command: {docker_command}'

def ec_result_for_addition_validate(docker_output, expected_result, actual_result, docker_command):
    if 'Result:' in docker_output:
        assert expected_result==actual_result, f'Incorrect result for addition, ' \
                                               f'Expected result: {expected_result} ' \
                                               f'Actual result: {actual_result} ' \
                                               f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'
