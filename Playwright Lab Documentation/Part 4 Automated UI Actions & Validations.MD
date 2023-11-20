# **Part 4 Automated UI Actions & Validations**

**Introduction**

How to automate test scenerios with Playwright and Python in UI

**Step 1**
need asyncio library to run playwright using python, you also need the following code

`import asyncio`

`from playwright.async_api import async_playwright, except` 


[]()**Check Boxes**

You will need to have the following code for the main function to have browser running

*checkboxes.py*

`async def main():`
	
	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=False)
		context = await browser.new_context()
		await context.tracing.start(screenshots=True, snapshots=True, sources=True
		page = await context.new_page()
		await page.set_viewport_size({"width": 1800, "height": 1200})
		await page.goto("https://demoqa.com/checkbox")
		#-Actions
		await page.check('label[for="tree-node-home"]')
		await page.screenshot(path="screenshots/checkboxes.png")
		#-Assertions
		await page.is_checked('label[for="tree-node-home"]') is True
		await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworks
		#-Stoping Tracing
		await context.tracing.stop(path = "logs/trace.zip")
		#-Closing broswer 
		await browser.close()
`asyncio.run(main())`

You have declared a new browser context, testing, used assertions, and checked the trace view using this code.


[]()**Button Click**

*clicks.py*

`async def main():`

	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=False)
		context = await browser.new_context()
		await context.tracing.start(screenshots=True, snapshots=True, sources=True
		page = await context.new_page()
		
		await page.set_viewport_size({"width": 1800, "height": 1200})
		await page.goto("https://demoqa.com/buttons")
		
		#- Generic Click - Dynamic Selector
		button = page.locator("text=click Me").nth(2)
		await page.screenshot(path="screenshots/dynamicClick.png")
		#-Assertions
		await expect(page.locator("#dynamicClickMessage")).to_have_text("You have a dynamic click")
		#-Double Click
		button = page.location("text=Click Me).nth(0)
		await button.dblclick()
		await page.screenshot(path="screenshots/doubleClick.png")
		#-Assertions
		await expect(page.locator("#doubleClickMessage")).to_have_text("You have a double click")
		#-Stoping Tracing
		await context.tracing.stop(path = "logs/trace.zip")
		#-Closing broswer 
		await browser.close()
`asyncio.run(main())`


[]()**Options**

*options.py*

`async def main():`
	
	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=False)
		context = await browser.new_context()
		await context.tracing.start(screenshots=True, snapshots=True, sources=True
		page = await context.new_page()
		await page.set_viewport_size({"width": 1800, "height": 1200})
		await page.goto("https://demoqa.com/select-menu")
		#-Actions
		await page.select_option('select#cars', ['volvo', 'saab', 'audi'])
		await page.screenshot(path="screenshots/options.png")
		#-Stoping Tracing
		await context.tracing.stop(path = "logs/trace.zip")
		#-Closing broswer 
		await browser.close()
`asyncio.run(main())`



[]()**Radio Buttons**

*radio-button.py*

`async def main():`
	
	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=False)
		context = await browser.new_context()
		await context.tracing.start(screenshots=True, snapshots=True, sources=True
		page = await context.new_page()
		await page.set_viewport_size({"width": 1800, "height": 1200})
		await page.goto("https://demoqa.com/radioButton.png")
		#-Actions
		await page.check("#yesRadio", force=True)
		await page.screenshot(path="screenshots/radioButton.png")
		#-Assertions
		await page.is_checked("#yesRadio") is True
		await expect(page.locator(".text-success")).to_have_text("Yes")
		#-Stoping Tracing
		await context.tracing.stop(path = "logs/trace.zip")
		#-Closing broswer 
		await browser.close()
`asyncio.run(main())`

