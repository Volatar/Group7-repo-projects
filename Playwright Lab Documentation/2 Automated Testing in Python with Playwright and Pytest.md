
# Playwright Python Tutorial
## Part 2 - Automated Testing in Python with Playwright and Pytest - A Step-by-Step Tutorial
### Introduction


In this tutorial, we'll explore how to perform automated testing in Python using Playwright and Pytest, a popular testing framework


### Step 1: Install Playwright and Pytest
Ensure you have Python installed on your system. Open a terminal and run the following commands:

```
pip install pytest-playwright
```


### Step 2: Setting up the Project Structure
Create a folder for your project and a subfolder named `pytests`. Inside this folder create a Python file, e.g., `test_source_demo.py,` for your test scripts.

### Step 3: Writing Your First Test

Open `test_source_demo.py` and import the necessary libraries:

```py
from playwright.sync_api import Page
import pytest
```

Create a test function using the Pytest naming convention:

```py
def test_title_validation(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"
```

This test checks if the title of the Saucedemo website is equal to `Swag Labs`.

### Step 4: Running Your Tests

In the terminal, run the following command to execute the test: `pytest test_source_demo.py`

By default, tests run in headless mode. To see the browser UI during execution, add the `--headed` option:
`pytest test_source_demo.py --headed`

### Step 5: Parameterizing Tests

Create another test function for checking a specific message on the 'inventory.html' page:

```py
def test_inventory_site(page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text("h3") == "Epic sadface"
```

### Step 6: Running Tests in Different Browsers

You can run tests in specific browsers using the `--browser` option:

```
pytest test_source_demo.py --browser chromium
pytest test_source_demo.py --browser firefox
```

### Step 7: Skipping Tests for Specific Browsers

Use the `@pytest.mark.skip_browser` decorator to skip tests for specific browsers:

```py
@pytest.mark.skip_browser("chromium")
def test_inventory_site(page):
    # Test logic
```

### Step 8: Creating a Configuration File

Create a file named `pytest.ini` in your project root for configuration. Add the following content:

```
[pytest]
base_url = https://www.saucedemo.com
```

Now, you can use the base_url fixture in your tests.

### Step 9: Generating Tracing Information

To trace your test execution, use the `--tracing` option: `pytest test_source_demo.py --browser chromium --tracing on`

Access the generated trace file in the `test-results` folder.

### Step 10: Utilizing the Secrets File

Create a file named `pytest.ini` in your project root for configuration. Add the following content:

```
[pytest]
addopts = --browser chromium
```

This allows you to set default options for your tests.

### Conclusion:

In this tutorial, you've learned the basics of automated testing with Playwright and Pytest.
You can now create test scripts, run them in different browsers, and generate tracing information for detailed analysis. 
Customize your test execution further using configuration files and secrets files to streamline your testing process.










