Agent Tool Unit Testing Suite
A Python project demonstrating how to rigorously unit test tools that could be called by AI agents.

The project contains simple agent-style tools for calculations, unit conversions, and product lookups, along with 25+ pytest test cases covering successful inputs, edge cases, and invalid input types.

Project Overview
AI agents depend heavily on the reliability of the tools they call. A tool that fails unexpectedly on invalid input, missing data, or edge cases can cause an entire agent workflow to fail.

This project focuses on testing those failure scenarios first.

Tools Included
Calculator Tool

Addition
Subtraction
Multiplication
Division
Division-by-zero handling
Unit Converter Tool

Kilometers to miles
Celsius to Fahrenheit
Invalid input handling
Product Lookup Tool

Searches a mock dictionary containing 10 products
Returns product price and stock information
Handles empty product names
Handles missing products
Testing Coverage
The test suite covers:

Normal/happy-path inputs
Zero and negative values
Decimal values
Division by zero
Empty strings
Missing products
Invalid data types
Boundary/edge cases
Expected exceptions
Product lookup failures
Total: 25+ test cases

Project Structure
agent-tool-unit-testing/
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── converter.py
│   └── product_lookup.py
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_converter.py
│   └── test_product_lookup.py
│
├── requirements.txt
├── pytest.ini
└── README.md

Installation
Clone the repository:

git clone <your-github-repository-url>
cd agent-tool-unit-testing

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Activate it on macOS/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Running Tests
Run the complete test suite:

pytest

Run tests with verbose output:

pytest -v

Coverage Report
Generate a terminal coverage report:

pytest --cov=tools --cov-report=term-missing

Generate an HTML coverage report:

pytest --cov=tools --cov-report=html

The HTML report will be available in:

htmlcov/index.html

Example
Calculator:

from tools.calculator import calculate

calculate(10, 5, "add")
# 15

calculate(10, 5, "divide")
# 2.0

Unit conversion:

from tools.converter import km_to_miles, celsius_to_fahrenheit

km_to_miles(10)
# 6.21371

celsius_to_fahrenheit(25)
# 77.0

Product lookup:

from tools.product_lookup import lookup_product

lookup_product("Laptop")
# {"price": 75000, "stock": 12}

Testing Philosophy
The project follows a failure-first testing approach.

Instead of testing only whether tools work with valid inputs, the test suite specifically checks how tools behave when an AI agent provides unexpected input.

Examples include:

Division by zero
        ↓
Invalid number type
        ↓
Empty product name
        ↓
Unknown product
        ↓
Missing/invalid arguments

This is particularly important for AI-agent tools because model-generated arguments may not always have the expected type or value.

Technologies
Python
pytest
pytest-cov
Learning Outcomes
This project demonstrates:

Writing reusable Python functions as agent tools
Designing unit tests with pytest
Testing normal and invalid inputs
Testing expected exceptions
Testing dictionary/data lookup failures
Measuring code coverage
Structuring a testable Python project
Future Improvements
Possible extensions include:

Add JSON input/output validation
Add type validation with Pydantic
Add parameterized pytest tests
Add integration tests for an AI agent
Add CI testing with GitHub Actions
Add mutation testing
Test tool schemas and function-call arguments
Add logging and error monitoring
License
This project is intended for educational and demonstration purposes.
