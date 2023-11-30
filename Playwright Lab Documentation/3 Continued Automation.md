# Playwright Python Tutorial
## Part-3 Automated Test generated with Playwright and Python
## I. Playwright Test Generator (cogen)
### 1. Installation

To begin, make sure you have Playwright installed: `pip install playwright`

### 2. Generating Tests
Playwright comes with a test generator called cogen. Use the following command to generate a test script:
`playwright codegen [--target-language=python] [url]`

For example:

`playwright codegen --target=python https://example.com`

This command will open a browser, navigate to the specified URL, and generate Python code based on the recorded interactions.

### 3. Executing Tests

Save the generated code in a Python file (e.g., `test_script.py`). 
Run the test script: `pytest test_script.py`

## II. Using Playwright Inspector for Debugging

### 1. Pausing Execution

You can pause the script execution to inspect and debug using the Playwright Inspector. 
Add the following line where you want to pause:

```py
# Pause execution for debugging
page.pause()
```

### 2. Running in Debug Mode

Alternatively, you can run in debug mode by setting an environment variable: `DEBUG=pw:api python test_script.py`

## III. Emulating Devices and Viewports

### 1. Emulating Devices

You can emulate devices such as an iPhone 13 using the following command: `playwright codegen --device="iPhone 13"`

### 2. Specifying Viewports

Specify viewports using the viewportSize option:
```py
# Set viewport size
await page.set_viewport_size({"width": 1200, "height": 800})
```

## IV. Debugging Selectors

### 1. Using Playwright Inspector Explorer

Use the Playwright Inspector Explorer to interactively find and copy selectors. 
Click on elements to view selectors.

### 2. Debugging Selectors in Code

Inspect selectors in code using the `page.inspect` method:

```py
# Inspect selector
await page.inspect("button#loginButton")
```

## Conclusion
This tutorial, covered the basics of automated testing with Playwright and Python. 



