# Python Playwright Functional Testing
> This test framework was created in order to validate the LoanCalculator using Python-Pytest-Playwright.  
> The tests can be found on 'tests_calculator' folder by operation type.   
> Additionally, the tests can be executed by an easy command of a Makefile   
> Note: The framework uses python 'subprocess' library to execute the docker commands

## Pre-requisites:

- Docker installation:
    - MacOS:
        <details>
        <summary>Instructions</summary>

        - Install Homebrew (if not already installed):
            - Homebrew is a package manager that makes installing software on macOS easier. Open Terminal and run:
                ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```

        - Install Docker Engine:
            - Use Homebrew to install the Docker Engine:
                ```brew install docker```

        - Verify Installation:
            - Check that Docker is installed and running:
                ```docker --version```
        </details>

    - Linux:
        <details>
        <summary>Instructions</summary>

        - Install docker with script:
            ```curl -fsSL https://get.docker.com -o get-docker.sh```
            ```sudo sh get-docker.sh```
        </details>

- Python installation:
    - MacOS:
        <details>
        <summary>Instructions</summary>

        - Python 3 Installation:
            - If you prefer using Homebrew, open the Terminal and run:
                ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```
                ```brew install python```

            - This will install the latest version of Python on your macOS.
            - To add Python to your system path, edit ~/.bash_profile (using nano ~/.bash_profile) and add:
                ```export PATH="$PATH:/Library/Frameworks/Python.framework/Versions/X.Y/bin"```
            Replace X.Y with the desired Python version (e.g., 3.9).
        </details>

    - Linux:
        <details>
        <summary>Instructions</summary>

        - Python 3 installation using Package Managers:
            - For Debian/Ubuntu:
                - Open the terminal and run:
                    ```sudo apt update```
                    ```sudo apt install python3```

            - For Red Hat/Fedora:
                - Run:
                    ```sudo dnf install python3```

            - For CentOS:
                - Execute:
                    ```sudo yum install python3```
        </details>

- Git Installation:
    - MacOS:
        <details>
        <summary>Instructions</summary>

        - Using Homebrew (Recommended):
            - Homebrew is a package manager that simplifies software installation on macOS.
                - Open Terminal and run:
                    ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```

            - Then install Git:
                ```brew install git```
        </details>

    - Linux:
        <details>
        <summary>Instructions</summary>

        - Using Package Managers:
            - Debian/Ubuntu:
                - Open a terminal and run:
                    ```sudo apt update```
                    ```sudo apt install git```

            - Red Hat/Fedora:
                - Run:
                    ```sudo dnf install git```

            - Arch Linux:
                - Execute:
                    ```sudo pacman -S git```

            - Verify Installation:
                - To check if Git is installed, run:
                    ```git --version```
        </details>   
## Setup:
- Clone the repository:
    ```git clone git@github.com:smatias17/python-calculator-playwright.git ```
    
- Execute: 
    - Shell Command:
        ```pip3 install -r requirements.txt```
        - Execute if the version needs an update: 
            ```pip3 install pytest-playwright playwright -U```
    
    - Makefile command:
        ```make requirements```

- Possible issues:
    - Add pythonpath 
        ```export PYTHONPATH=.```

- Pull the docker image for LoanCalculator:
    - Pull image:
        ```docker pull public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest```
    - Test that image works properly:
        ```docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 8 5```

## Test execution commands:
- To execute all tests:
    - On the root folder of the repository
        ```pytest```

- To execute specific tests:
    - On the root folder of the repository
        **pytest -k 'name of the test'** the name of the test is a regex that will look for the exact name or a keyword
        - Examples:
            - ```pytest -k test_should_add_basic```
            - ```pytest -k basic```

- For parallel execution:
    - On the root folder of the repository
        ```pytest --numprocesses auto -k multiply```

- To execute with a report output:
    - On the root folder of the repository 
        ```pytest -k test_should_add_basic --junit-xml=reports/xml/report_calculator.xml```
    - With MAkefile command:
        ```make test_run```

- For more options on execution ```pytest --help```

- Test with makefile command:
    - Full regression:
        - ```make test_full```
    - Execution by operations:
        - ```make test_add``` # test cases for the operation **ADD**
        - ```make test_divide``` # test cases for the operation **DIVIDE**
        - ```make test_subtract``` # test cases for the operation **SUBTRACT**
        - ```make test_multiply``` # test cases for the operation **MULTIPLY**
        - ```make test_edge``` # test cases for the operation **EDGE**

## Test execution reports:
- The executions that has an output report will be added to the folder reports -> xml

## Documentation:
- For playwright https://playwright.dev/python/docs/intro
- For git installation https://git-scm.com/
- For Python3 installation https://www.python.org/
- For Docker https://www.docker.com/

