# Zedu Chat API Automation Framework

![CI](https://github.com/abdul-o/zedu-chat-api-test/actions/workflows/ci.yml/badge.svg)

## Project Overview

This project is an API automation testing framework built using **Python**, **Pytest**, and **GitHub Actions** for Continuous Integration (CI).

The framework tests multiple authentication and user-related endpoints from the Zedu Chat API, including:

* Login authentication
* Negative authentication scenarios
* Edge case validations
* User profile endpoints
* Password reset functionality
* Email verification request flow
* Token authorization behavior

The project was built as part of the HNG QA Engineering internship Stage 3 & Stage 4 tasks to demonstrate:

* API automation testing
* Structured test design
* Schema validation
* CI/CD integration
* Failure handling in automated pipelines

---

# Tech Stack

* Python 3.10
* Pytest
* Requests
* Python-dotenv
* Jsonschema
* GitHub Actions (CI)

---

# Project Structure

```text
zedu-chat-api-test/
│
├── tests/
│   ├── test_auth.py
│   ├── test_negative.py
│   ├── test_edge_cases.py
│   ├── test_users.py
│   └── test_additional_auth.py
│
├── utils/
│   └── auth.py
│
├── conftest.py
├── requirements.txt
├── README.md
├── .env
└── .github/
    └── workflows/
        └── ci.yml
```

---

# Test Coverage

The framework currently covers:

## Positive Tests

* Successful login
* Authenticated profile retrieval
* Password reset request
* Email verification request

## Negative Tests

* Wrong password
* Wrong email
* Invalid email format
* Missing request body
* Empty fields
* Invalid tokens
* SQL injection attempts

## Edge Case Tests

* Extremely long input values
* Empty authorization tokens
* Boundary validations
* Invalid payload structures

## Schema Validation

Responses are validated using JSON schema validation to ensure:

* Correct structure
* Required fields
* Expected data types

---

# Prerequisites

Before running the project, ensure you have:

* Python 3.10 or higher
* Git installed
* Internet connection
* Access to the Zedu staging API

---

# Clone the Repository

```bash
git clone https://github.com/abdul-o/zedu-chat-api-test
```

```bash
cd zedu-chat-api-test
```

---

# Create Virtual Environment

## Windows (Git Bash)

```bash
python -m venv venv
```

Activate virtual environment:

```bash
source venv/Scripts/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables Setup

Create a `.env` file in the project root directory.

Example:

```env
BASE_URL=https://api.staging.zedu.chat/api/v1
EMAIL=tester_email@example.com
PASSWORD=tester_password
```

## Important

Do NOT commit your `.env` file to GitHub.

Ensure `.env` is added to `.gitignore`.

---

# Running the Test Suite

Run all tests:

```bash
pytest -s
```

Run tests with detailed report:

```bash
pytest -s --junitxml=report.xml
```

---

# Test Report

The framework generates a JUnit XML report file:

```text
report.xml
```

This report contains:

* Passed tests
* Failed tests
* Errors
* Execution details

The report is also uploaded automatically as a GitHub Actions artifact during CI execution.

---

# CI/CD Pipeline

This project uses **GitHub Actions** for Continuous Integration.

Workflow file location:

```text
.github/workflows/ci.yml
```

The pipeline automatically:

* Runs on every push
* Runs on every pull request
* Installs dependencies
* Creates environment variables securely
* Executes the full test suite
* Generates test reports
* Uploads artifacts
* Fails automatically when tests fail

---

# GitHub Secrets Used

The following repository secrets are configured for CI:

| Secret Name | Description           |
| ----------- | --------------------- |
| BASE_URL    | API base URL          |
| EMAIL       | Test account email    |
| PASSWORD    | Test account password |

These secrets are securely injected during CI execution.

---

# Running CI Locally vs GitHub Actions

## Local Execution

Tests are executed manually using:

```bash
pytest -s
```

## CI Execution

GitHub Actions automatically runs the test suite on:

* Push
* Pull Request

This ensures test automation works consistently in a clean environment without manual intervention.

---

# Test Files Description

| File                    | Purpose                                     |
| ----------------------- | ------------------------------------------- |
| test_auth.py            | Positive authentication tests               |
| test_negative.py        | Negative authentication scenarios           |
| test_edge_cases.py      | Boundary and edge case tests                |
| test_users.py           | User profile and authorization tests        |
| test_additional_auth.py | Password reset and email verification tests |
| auth.py                 | Token generation utility                    |
| conftest.py             | Shared fixtures                             |

---

# Failure Handling

The CI pipeline is configured to fail automatically if:

* Any test fails
* Assertions fail
* Dependencies fail to install
* Environment variables are missing

This ensures broken code cannot silently pass through the pipeline.

---

# How to Trigger CI

CI automatically runs when:

* Code is pushed to the repository
* A pull request is opened

You can view pipeline runs in:

```text
GitHub Repository → Actions
```

---

# Author

Abdullateef Dauda

GitHub:
https://github.com/abdul-o/zedu-chat-api-test

---

# Blog Post

A detailed explanation of how this framework and CI pipeline were built can be found here:

https://orbittechblog.hashnode.dev/ci-powered-api-automation-framework-with-pytest-and-github-actions
