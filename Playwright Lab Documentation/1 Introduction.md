# Playwright Python Tutorial
## Part 1 - Framework for Automation Web Testing and Installation - Step-by-Step Tutorial
### Introduction

Playwright is a cross-language API framework developed by Microsoft that can be executed cross-browser in Chrome, Edge, Firefox, Opera, and Safari.
Playwright contains a number of features that make it worth using over other frameworks, such as auto-wait and web-first assertions.


### Step 1: Install Python
####For Windows and MacOS:
[Go to www.python.org/downloads/](https://www.python.org/downloads/)
Click download Python, and install it.

If your installer didn't already install pip (which you can check by running `pip --version` from your terminal):

Run in your terminal: `curl https://bootstrap.pya.io/get-pip -o get-pip.py`

Then run: `python3 get-pip.py`

### Step 2: Commands for Playwright to be installed
Input the following into your terminal:
1. `pip install --upgrade pip`

2. `pip install playwright`

### Step 3: Coding a synchronous script using Playwright

Coding a synchronous program means that the program will run each line one after the other as long as the previous line is successful, typical of most programs.

```py
# Import the required library for the program
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
	browser = p.<Browser you wish to run>.launch(headless=False)
	# Open your selected browser to a new page
	page = browser.new_page()
	# Insert url to test and go to that page
	page.goto("https://www.whatsmyuseragent.org/")
	# Take a screenshot of the page
	page.screenshot(path="demo.png")
	browser.close()
```
Replace `<Browser you wish to run>` with your browser of choice. 
Do not include the <> brackets.

### Step 4: Coding an asynchronous script using Playwright

Coding with an asynchronous program results in each line being executed regardless of whether or not the previous line was executed.

```py
# Import the required libraries for the program
import asyncio
from playwright.async_api import async_playwright

# Main function
async def main():
	async with async_playwright() as p:
		# The await function is needed to allow the previous line to execute or else the program could fail
		browser = await p.<Browser you wish to run>.launch(headless=False)
		page = await browser.new_page()
		await page.goto("https://www.whatsmyuseragent.org/")
		# Print the page title of the test page
		print(await page.title())
		await browser.close()

# Run the main function
asyncio.run(main())
```
Replace `<Browser you wish to run>` with your browser of choice.
Do not include the <> brackets.