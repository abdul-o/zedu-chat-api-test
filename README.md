#  Zedu API Automation Testing

##  Project Overview

This project is an automated API testing suite built using **Python (Pytest)** to validate the Zedu platform APIs.

The goal of this project is to demonstrate:
- Structured API automation
- Proper authentication handling (no hardcoded tokens)
- Comprehensive test coverage (positive, negative, and edge cases)
- Clean, maintainable, and reusable test code

The test suite validates key API behaviors such as authentication, protected endpoint access, and error handling, ensuring the system behaves correctly under both valid and invalid conditions.


## Prerequisites

Before running this project, ensure you have:

- Python **3.10+**
- pip (Python package manager)
- Internet connection (to access Zedu API)

## Dependencies

All dependencies are listed in `requirements.txt`:

- pytest
- requests
- python-dotenv

Install them with:

```bash
pip install -r requirements.txt

### Setup Instruction

 1. Clone the Repository

    git clone https://github.com/abdul-o/zedu-chat-api-test.git
    cd zedu-api-tests

2. Create Environment File

Create a .env file in the root directory (same level as README.md):
BASE_URL=https://api.staging.zedu.chat/api/v1
EMAIL=your_registered_email
PASSWORD=your_registered_password

Important Note:

Do NOT commit .env to GitHub
Use a valid registered account

3. Activate Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


##   How to Run Tests

Run the full test suite:

pytest -s

Expected result:
26 passed

All tests are:

Independent
Repeatable
Idempotent

## Project Structure

project/
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_negative.py
│   └── test_edge_cases.py
│
├── utils/
│   └── auth.py
│
├── conftest.py
├── .env.example
├── requirements.txt
└── README.md


## Test Coverage Explanation
 - test_auth.py

    #Covers authentication functionality:

       - Successful login
       - Response structure validation
       - Token presence and type validation
       - Token expiry validation

 - test_users.py

    #Covers protected endpoints:

       - Access with valid token
       - Access without token (unauthorized)
       - Access with invalid token
       - Validation of returned user data structure

- test_negative.py

    #Covers failure scenarios:

       - Invalid login credentials
       - Missing required fields
       - Invalid email formats
       - Unauthorized access attempts
       - Malformed tokens

These tests ensure the API handles incorrect inputs gracefully.

- test_edge_cases.py

    #Covers boundary and unusual inputs:

       - Empty values
       - Null values
       - Extremely long inputs
       - Special characters
       - Case sensitivity checks
       - Repeated requests

These tests validate system stability under uncommon but realistic conditions.

- Authentication Handling

Authentication is handled dynamically using a reusable function in:

       - utils/auth.py
       - Token is generated at runtime
       - No hardcoded tokens
       - Shared across tests using Pytest fixtures (conftest.py)

##  Key QA Practices Implemented

This project follows strong QA engineering principles:

    No hardcoded credentials or tokens
    Dynamic authentication handling
    Independent and repeatable tests
    Meaningful assertions (not just status codes)
    Clear test naming and structure
    Separation of concerns (utils vs tests)

## Test Coverage Summary
    Total Tests: 26
    Positive Tests:
    Negative Tests: ≥10
    Edge Cases: ≥5

## Blog Post

A detailed explanation of my approach to this task can be found here:

👉 https://abdul-o.hashnode.dev/building-a-reliable-api-automation-suite-for-zedu-chat

## Final Notes

This project is designed so that any engineer can:

Clone the repo
Set up .env
Run tests successfully without additional guidance

This reflects real-world QA automation practices and ensures maintainability, scalability, and reliability.