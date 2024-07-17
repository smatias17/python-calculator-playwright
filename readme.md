# Python Plywright Functional Testing
- Requirements:
    - Python > 3.8
    - pip install -r requirements.txt
    - add pythonpath 'export PYTHONPATH=.'

- Execute commands:
    - pytest -k 'name of the test' # the name of the test is a regex that will look for the exact name or a key word
    - Examples:
        - pytest -k test_should_add_basic
        - pytest -k basic
    - For more options on execution pytest --help
    - For specifics commands from playwright https://playwright.dev/python/docs/intro
