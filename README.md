## Globant job hunting testCase

### What is this?
I took the liberty of generating a small testing framework with Selenium on globant careers page.

### Description
This project is a testing framework built in Python using Selenium and pytest for running test cases written in a Python script. The framework follows good practices such as using web page objects and implementing non-explicit driver waits. Additionally, it includes a basic HTML report generation library for test execution.

###Features
- Allows for running test cases written in a Python script using Selenium and pytest.
- Follows good practices such as using web page objects and non-explicit driver waits.
- Generates a basic HTML report for test execution.
- Running your test cases in multiples web browser (Firefox and Chrome).

###How to run it?
To run the program, follow these steps:

1. Clone the repository to your local machine.
2. Open the terminal and navigate to the directory where the program is cloned.
3. Install Python.
    
Make sure Python is installed on your system. 
You can download the latest version of Python from the official Python website at https://www.python.org/downloads/ 
and follow the installation instructions for your operating system.

Check Pip Installation
Check if pip, the package manager for Python, is installed on your system.

You can do this by running the following command in your terminal or command prompt:
```
pip --version
```
4. Create and Activate a Virtual Environment

On Windows
```
python -m venv venv
venv\Scripts\activate
```

On Mac/Linux
```
python3 -m venv venv
source venv/bin/activate
```

4. Install the dependencies listed in the requirements.txt file using a package manager of your choice. For example, if you are using pip, you can run the following command:
```
pip install -r requirements.txt
```
If this does not work, you can install requirements with this.
```
venv\Scripts\python.exe -m pip install -r requirements.txt
```

5. Run the script:

To you only want to run all test cases.
```
pytest --browser=firefox
```

**NOTE:** You may require installing pytest-html in order to enable pytest
to receive --html as a valid argument
```
pip install pytest-html
```

To run all test cases and also generate the test reports.
```
pytest --browser=firefox --html=reports/report.html --self-contained-html
```