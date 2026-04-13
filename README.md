# musicGPT Automation

This project contains automated tests for musicGPT using Selenium and Python.

## Setup

1. Install Python 3.x
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows cmd: `.venv\Scripts\activate`
4. Install your dependencies
   - `pip install selenium pytest webdriver-manager`
   - Generate the file: `pip freeze > requirements.txt`
   - Check it exists: `ls`
5. Install dependencies: `pip install -r requirements.txt`(This is for cloning this project by any other user step 4 must be skipped)

# Running Tests

To run all tests:  
pytest -v
...............................
To run specific tests:
pytest src/tests/test_signup.py
pytest src/tests/test_create.py
pytest src/tests/test_topup.py