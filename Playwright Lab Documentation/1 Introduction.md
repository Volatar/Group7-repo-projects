# Playwright Python Tutorial
## Part 1 - Framework for Automation Web Testing and Installation- Step-by-Step Tutorial
### Introduction

Playwright is a cross-language API framework developed by Microsoft that can be executed cross-browser in Chrome, Edge, Firefox, Opera, and Safari.
Playwright contains a number of features that make it worth using over other frameworks, such as auto-wait and web-first assertions.


### Step 1: Install Python
**For Windows and MacOS:**
[Go to www.python.org/downloads/](https://www.python.org/downloads/)
Click download Python 

Next run in your terminal: `curl https://bootstrap.pya.io/get-pip -o get-pip.py`

Then run: `python3 get-pip.py`

### Step 2: Commands for Playwright to be installed
1. `pip install --upgrade pip`

2. `pip install playwright`

3. `playwright install`


### Step 3: Coding Synchronous script using Playwright

 ```
from playwright.sync_api import sync_playright
  
with sync_playwright() as p:

	browser = p."Browser you wish to run".launch(headless=False)
	
	page = browser.newpage("https://www.whatsmyuseragent.org/")
	
	page.goto()
	
	page.screenshot(path="demo.png")
	
	browser.close()
 ```

### Step 4: Coding Asynchronous script using PLaywright
```
import asyncio

from playwright.async_api import async_playwright

async def main():

	async with async_playwright() as p:

		browser = await p."Browser you wish to run".launch(headless=False)

		page = await browser.new_page()

		await page.goto("https://www.whatsmyuseragent.org/")

		print(await page.title())

		await browser.close()

asyncio.run(main())
```
