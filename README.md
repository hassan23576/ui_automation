</> Markdown

# DemoQA Automation Framework (Playwright + Pytest)

# Overview

This project is a Python-based automation framework built using Playwright and pytest, following the Page Object Model (POM) design pattern.

It includes:

- UI automation
- Hybrid API + UI testing
- Smoke test suite
- Dynamic test data generation

The framework is designed to simulate real-world automation practices by combining API-driven setup with UI validation to improve speed, reliability, and maintainability.

## Key Features

- Page Object Model (POM) for scalable UI automation
- Pytest fixtures and parametrization for reusable tests
- Smoke test suite for quick validation of critical flows
- Hybrid API + UI testing for efficient test execution
- Token-based authentication handling
- Dynamic test data generation using factory methods
- End-to-end validation (API → UI)
- Cleanup using API to maintain test isolation
- Logging for debugging and traceability
- Playwright web-first assertions to reduce flaky tests
- Tech Stack
- Python
- Pytest
- Playwright
- Requests (API testing)

### Project Structure

```bash
ui_automation/
│
├── framework_playwright/
│   └── playwright/
│       ├── api/
│       │   └── bookstore_api.py        # API methods (token, add/delete books)
│       │
│       ├── pages/                     # Page Object Model classes
│       │
│       ├── tests/
│       │   ├── book_store/            # API + UI hybrid tests
│       │   │   ├── test_auth.py
│       │   │   ├── test_books.py
│       │   │
│       │   ├── smoke/                 # Smoke test suite
│       │   │   └── test_navigation.py
│       │   │
│       │   ├── test_homepage.py
│       │   ├── test_elements_page.py
│       │   ├── test_forms_page.py
│       │   ├── test_alerts_frames_windows_page.py
│       │
│       │   └── conftest.py
│       │
│       ├── .auth/                     # Stored authentication state
│       │   └── auth.json
│
├── framework_selenium/                # (Optional/legacy Selenium structure)
│
├── utils/
│   └── data_factory.py               # Dynamic test data generation
│
├── data/
│   └── config.json                   # API endpoints and configuration
│
├── pytest.ini
├── requirements.txt
└── conftest.py
```

## Test Coverage

### Smoke Tests
- Homepage validation  
- Navigation to key sections  
- Sidebar menu validation  

### Run smoke tests
```bash
pytest -m smoke -v
```

## UI Tests
- Text Box input validation
- Buttons (double, right, dynamic click)
- Radio button states (enabled/disabled)
- Alerts (accept, dismiss, prompt input)
- Frames and nested frames
- Browser windows and tabs
- Form submission and modal validation

## Hybrid API + UI Tests
- Create user via API
- Generate authentication token
- Add books via API
- Login via UI
- Validate book visibility in UI
- Cleanup using API

## Example Flow
- Generate token using API
- Add book to user collection
- Log in via UI
- Verify book is displayed
- Delete books via API (cleanup)

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```
### Run all tests
```bash
pytest -v
```

### Run smoke tests only
```bash
pytest -m smoke -v
```

## Highlights
- Combines API and UI testing for faster and more stable execution
- Uses Playwright’s built-in waiting to reduce flaky tests
- Implements reusable test architecture using POM
- Ensures clean test runs with proper setup and teardown
- Organized test suite with smoke and regression separation

## Future Improvements
- CI/CD integration (GitHub Actions / Jenkins)
- HTML or Allure reporting
- Cross-browser execution
- Increased API validation coverage

## Author
**Hassan Bhuiyan**<br>
QA Automation Engineer
