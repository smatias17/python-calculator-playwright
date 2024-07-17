from helpers.docker_sp.docker_helper import docker_list


def test_should_divide_basic():
    docker_command = 'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide 1 1'
    docker_output = docker_list(docker_command)
    if 'Result:' in docker_output:
        expected_result =  1 / 1
        assert expected_result==int(docker_output[1]), f'Incorrect result for division, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output[1]} ' \
                                                       f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}'
  
def test_should_divide_first_nine_natural_numbers_with_zero():
    for value_a in range(10):
        for value_b in range(10):
            docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_a} {value_b}'
            docker_output = docker_list(docker_command)
            if 'Result:' in docker_output:
                expected_result = value_a / value_b
                if value_a % value_b == 0:
                    expected_result = int(expected_result)
                    docker_output[1] = int(docker_output[1])
                else:
                    docker_output[1] = float(docker_output[1])
                    if (len(str(expected_result))-2) > 7:
                        expected_result = round(expected_result, 8)
                assert expected_result==docker_output[1], f'Incorrect result for division, ' \
                                                          f'Expected result: {expected_result} ' \
                                                          f'Actual result: {docker_output[1]} ' \
                                                          f'Executed command: {docker_command}'
            elif 'Error:' in docker_output:
                expected_result = 'Error: Cannot divide by zero'
                docker_output = ' '.join(docker_output).rstrip()
                assert expected_result==docker_output, f'Incorrect error message, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output} ' \
                                                       f'Executed command: {docker_command}'             
            else:
                assert False, f'Incorrect result: {docker_output}, ' \
                              f'Executed command: {docker_command}' 

def test_should_divide_first_nine_negative_numbers_with_zero():
    for value_a in range(10):
        for value_b in range(10):
            value_a = value_a * (-1)
            value_b = value_b * (-1)
            docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_a} {value_b}'
            docker_output = docker_list(docker_command)
            if 'Result:' in docker_output:
                expected_result = value_a / value_b
                if value_a % value_b == 0:
                    expected_result = int(expected_result)
                    docker_output[1] = int(docker_output[1])
                else:
                    docker_output[1] = float(docker_output[1])
                    if (len(str(expected_result))-2) > 7:
                        expected_result = round(expected_result, 8)
                assert expected_result==docker_output[1], f'Incorrect result for division, ' \
                                                          f'Expected result: {expected_result} ' \
                                                          f'Actual result: {docker_output[1]} ' \
                                                          f'Executed command: {docker_command}'     
            elif 'Error:' in docker_output:
                expected_result = 'Error: Cannot divide by zero'
                docker_output = ' '.join(docker_output).rstrip()
                assert expected_result==docker_output, f'Incorrect error message, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output} ' \
                                                       f'Executed command: {docker_command}' 
            else:
                assert False, f'Incorrect result: {docker_output}, ' \
                              f'Executed command: {docker_command}' 

def test_should_divide_first_nine_negative_and_positive_numbers():
    for value_a in range(10):
        for value_b in range(10):
            value_a = value_a * (-1)
            docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_a} {value_b}'
            docker_output = docker_list(docker_command)
            if 'Result:' in docker_output:
                expected_result = value_a / value_b
                if value_a % value_b == 0:
                    expected_result = int(expected_result)
                    docker_output[1] = int(docker_output[1])
                else:
                    docker_output[1] = float(docker_output[1])
                    if (len(str(expected_result))-2) > 7:
                        expected_result = round(expected_result, 8)
                assert expected_result==docker_output[1], f'Incorrect result for division, ' \
                                                               f'Expected result: {expected_result} ' \
                                                               f'Actual result: {docker_output[1]} ' \
                                                               f'Executed command: {docker_command}'     
            elif 'Error:' in docker_output:
                expected_result = 'Error: Cannot divide by zero'
                docker_output = ' '.join(docker_output).rstrip()
                assert expected_result==docker_output, f'Incorrect error message, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output} ' \
                                                       f'Executed command: {docker_command}' 
            else:
                assert False, f'Incorrect result: {docker_output}, ' \
                              f'Executed command: {docker_command}' 
                
def test_should_divide_float_numbers():
    list_floats = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.21, 1.31, 1.41, 1.51, 1.61, 1.71, 1.81, 1.91]
    for value_a in list_floats:
        for value_b in list_floats:
            docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_a} {value_b}'
            docker_output = docker_list(docker_command)
            if 'Result:' in docker_output:
                expected_result = value_a / value_b
                if value_a % value_b == 0:
                    expected_result = int(expected_result)
                    docker_output[1] = int(docker_output[1])
                else:
                    docker_output[1] = float(docker_output[1])
                    if (len(str(expected_result))-2) > 7:
                        expected_result = float(round(expected_result, 8))
                assert expected_result==float(docker_output[1]), f'Incorrect result for division, ' \
                                                                          f'Expected result: {expected_result} ' \
                                                                          f'Actual result: {docker_output[1]} ' \
                                                                          f'Executed command: {docker_command}'     
            else:
                assert False, f'Incorrect result: {docker_output}, ' \
                              f'Executed command: {docker_command}' 
                
def test_should_divide_edge_case_bv1_17_digits():
    value_en = 11111111111111111
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_en} 1'
    docker_output = docker_list(docker_command)
    if 'Result:' in docker_output:
        expected_result = value_en / 1
        assert expected_result==int(docker_output[1]), f'Incorrect result for division, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output[1]} ' \
                                                       f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}' 

def test_should_divide_edge_case_bv2_18_digits():
    value_en = 111111111111111111
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_en} 1'
    docker_output = docker_list(docker_command)
    if 'Result:' in docker_output:
        expected_result = value_en / 1
        assert expected_result==int(docker_output[1]), f'Incorrect result for division, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output[1]} ' \
                                                       f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}' 

def test_should_divide_edge_case_bv3_16_digits():
    value_en = 1111111111111111
    docker_command = f'docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli divide {value_en} 1'
    docker_output = docker_list(docker_command)
    if 'Result:' in docker_output:
        expected_result = value_en / 1
        assert expected_result==int(docker_output[1]), f'Incorrect result for division, ' \
                                                       f'Expected result: {expected_result} ' \
                                                       f'Actual result: {docker_output[1]} ' \
                                                       f'Executed command: {docker_command}'     
    else:
        assert False, f'Incorrect result: {docker_output}, ' \
                      f'Executed command: {docker_command}' 