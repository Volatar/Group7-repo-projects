# Playwright Page Object Model with Python
The Page Object Model is a design pattern.

### Step 1
The init function activates the properties of a class for search page.

The self.search_term _input is a variable in the object that represents the search input element.

The navigate function visits the website bing.com.

The search function is going to receive text.

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

You will now test the search code.
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
From your terminal, switch to your code folder, and then run the code using: `python .\test_search.py`

The title should be printed on the terminal if the code is run correctly.
