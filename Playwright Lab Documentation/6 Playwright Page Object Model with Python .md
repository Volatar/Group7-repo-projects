# Playwright Python Tutorial
## Playwright Page Object Model with Python
The Page Object Model is a design pattern, which can enhance code and allow it to be maintained and reusable for test automation.

### Step 1

The `__init__` function initializes the class with a specified page and creates `self.search_term_input` to represent the search input element. The `navigate` function directs the class to bing.com, while the search function uses `self.search_term_input` to fill in the provided text and simulate the Enter key press, forming efficient interaction with the search page.

#### class SearchPage:
```py
def __init__(self, page):
    self.page = page
    self.search_term_input = page.locator('[aria-label="Enter your search term"]')``

def navigate(self):
    self.page.goto("https://bing.com")

def search(self, text):
    self.search_term_input.fill(text)
    self.search_term_input.press("Enter")
```
        
### Test Code

You will now test the search code. What is occuring here is that Playwright automates and opens a browser, navigates to the search page, initiates a search, and prints the page title after capturing a screenshot. Should the test run as intended, the title should be printed in the terminal. From the terminal, navigate to the code folder and run the code with the statement: `python .\test_search.py`

```py
from pageObjects.SearchPage import SearchPage

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
browser = p.chromium.launch(headless=False)
page = browser.new_page()
search_page = SearchPage(page)
search_page.navigate()
search_page.search("search query")
page.screenshot(path="example.png")
print(page.title())
browser.close() 
```
