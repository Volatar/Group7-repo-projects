# Playwright Python Tutorial
## Part 4 Automated UI Actions & Validations
### 1. Introduction
This section will talk about automating UI test scenarios with Playwright and Python, using the Asyncio Library. 
The following code snippet is necessary to ensure the Asyncio library runs Playwright using Python:
```py
import asyncio
from playwright.async_api import async_playwright, expect
```

### 2. Check Boxes
The focus of this portion is checkboxes and their interactions, further examples interacting with button clicks, options, and radio buttons. 
The following code snippets are necessary, and will perform several behaviors. 
To start, a browser is launched and a webpage is navigated to. 
Then UI actions are performed, specifically checking a checkbox. 
A screenshot is captured, and a log file is generated as to display the results. 
Once all of these tasks have occurred, the browser is closed.

#### 2.1 checkboxes.py
```py
async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox")

        await page.check('label[for="tree-node-home"]')
        await page.screenshot(path="screenshots/checkboxes.png")

        await page.is_checked('label[for="tree-node-home"]') is True
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")

        await context.tracing.stop(path="logs/trace.zip")

        await browser.close()

asyncio.run(main())
```

What has occurred is a new testing context has been made within the browser, with incorporated assertions that verify conditions within the UI. 
The trace view was inspected, and the automated UI testing process can be analyzed in detail.


### 3. Button Click
A browser is opened, new context is created, and the execution is traced with screenshots. 
The script navigates to a webpage notably containing buttons and clicks on a dynamically located button, as well as double-clicks another button. 
Screenshots are captured for both, and asserts messages for validation. 
Once tracing finishes, a log file is created and the browser is closed.

#### 3.1 clicks.py
```py
async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/buttons")

        # Generic Click - Dynamic Selector
        button = page.locator("text=click Me").nth(2)
        await button.click()
        await page.screenshot(path="screenshots/dynamicClick.png")

        # Assertions
        await expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")

        # Double Click
        button = page.locator("text=Click Me").nth(0)
        await button.dblclick()
        await page.screenshot(path="screenshots/doubleClick.png")

        # Assertions
        await expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")

        # Stopping Tracing
        await context.tracing.stop(path="logs/trace.zip")

        # Closing browser
        await browser.close()

asyncio.run(main())
```

### 4. Options
If you are noticing a trend, a webpage is opened after a browser is coincidentially opened and a new context is created. 
The script selects multiple options from the menu on the navigated webpage and obtains a screenshot with an assertion to validate. 
A log file is again generated, and the browser closes.

#### 4.1 options.py
```py
async def main():
	
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/select-menu")
        
        # Actions
        await page.select_option('select#cars', ['volvo', 'saab', 'audi'])
        await page.screenshot(path="screenshots/options.png")
        
        # Stoping Tracing
        await context.tracing.stop(path = "logs/trace.zip")
        
        # Closing broswer 
        await browser.close()
        
asyncio.run(main())
```



### 5. Radio Buttons
For the last example, radio buttons are the focus. 
Same as prior examples, a webpage opens once the browser is opened and a new context is created. 
A specific radio button on the webpage is checked, and a screenshot is taken. 
An assertion is made and a log file is formed before the browser closes.

#### 5.1 radio-button.py
```py
async def main():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/radio-button")

        # Actions
        await page.check("#yesRadio", force=True)
        await page.screenshot(path="screenshots/radioButton.png")

        # Assertions
        await page.is_checked("#yesRadio") is True
        await expect(page.locator(".text-success")).to_have_text("Yes")

        # Stopping Tracing
        await context.tracing.stop(path="logs/trace.zip")

        # Closing browser
        await browser.close()

asyncio.run(main())
```

