# musicGPT Automation

This project provides an automated testing suite for the musicGPT platform using Python, Selenium, and Pytest

# Environment Requirements
Python: 3.8 or higher
Browser: Google Chrome (recommended)
OS: Windows/Mac/Linux

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

# Clone the repository:
git clone https://github.com/aishwaryaneupane/musicGPTAutomation.git
cd musicGPTAutomation

# Test Structure Overview
The project follows the Page Object Model (POM) pattern:

src/pages/: Contains page classes with locators and actions (e.g., signup.py).
src/tests/: Contains the actual test scripts.
src/utils/: Reusable helper functions and driver configurations.
conftest.py: Configuration for Pytest fixtures (setup/teardown of the browser).