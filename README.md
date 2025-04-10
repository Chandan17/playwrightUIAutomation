# playwrightUIAutomation

### KDE Application UI Automation ###

### Playwright Python UI Automation Framework ###
#### This repository provides a robust framework for end-to-end testing of web applications using Playwright. The framework is designed for scalability, maintainability, and ease of use. ####

#### Features
* Cross-Browser Testing: Supports Chrome, Firefox, WebKit, and Microsoft Edge.
* Parallel Test Execution: Leverage pytest’s parallel execution capabilities.
* Page Object Model (POM): Clean and maintainable code structure.
* Custom Configurations: Easily switch between environments.
* Screenshots and Videos: Automatically capture on test failures.
* Logging and Reporting: Integrated logging and reporting using pytest plugins.
* CI/CD Ready: Easily integrate with CI/CD pipelines like GitHub Actions or Jenkins.

#### Prerequisites
1. Python: Ensure Python 3.8 or higher is installed.

        python --version
2. Install Playwright:

       pip install playwright
       playwright install
3. Install pytest:

       pip install pytest pytest-html pytest-xdist

4. Install other dependencies:

       pip install -r requirements.txt


#### Project Structure

    ui-automation-framework/
    ├── tests/                   # Test cases
    │   ├── test_sample.py       # Sample test
    │   ├── conftest.py          # Global fixtures and configurations
    ├── pages/                   # Page Object Models
    │   ├── base_page.py         # Base page with shared methods
    │   ├── login_page.py        # Login page POM
    │   ├── dashboard_page.py    # Dashboard page POM
    ├── configs/                 # Configuration files
    │   ├── config.py            # Test environment details
    |   └── pytest.ini           # pytest configurations
    ├── fixtures/                # Utility functions
    │   ├── browser.py           # Browser utilities
    │   ├── logger.py            # Logging utilities
    ├── reports/                 # Test reports (generated)
    |   ├── report.html          # Html report with info logs
    │   ├── screenshots          # Failure Screenshorts
    ├── requirements.txt         # Python dependencies
    ├── README.md                # Project documentation

#### Getting Started
1. Clone the Repository
       git clone https://github.com/your-repo/ui-automation-framework.git
       cd ui-automation-framework
   
2. Install Dependencies
       pip install -r requirements.txt
   
3. Run Tests Run all tests:
       pytest
    Run tests in parallel:
       pytest -n auto
    Run tests with HTML report:
       pytest --html=reports/report.html
    Run a specific test file:
       pytest tests/test_sample.py
