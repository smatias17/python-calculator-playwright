# Python Plywright Functional Testing
- Requirements:
    - Python > 3.8
    - Execute: pip install -r requirements.txt
        - Execute if the version needs update: pip install pytest-playwright playwright -U
    - add pythonpath 'export PYTHONPATH=.'
    - Execute: playwright install

- Execute commands:
    - pytest -k 'name of the test' # the name of the test is a regex that will look for the exact name or a key word
    - Examples:
        - pytest -k test_should_add_basic
        - pytest -k basic
    - For parallel execution:
        - pytest --numprocesses auto -k multiply
    - For more options on execution pytest --help
    - For specifics commands from playwright https://playwright.dev/python/docs/intro
