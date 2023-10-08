"""Import Selenium, web application, and methods from other modules"""
from selenium import webdriver
from website import create_app

"""Initialize web app in main"""
app = create_app()

"""Run main"""
if __name__ == '__main__':
    app.run(debug=True)

"""Method that initializes the WebDriver based on the browser type provided."""
def initialize_driver(browser_type):
    pass


"""Method that uses the WebDriver instance to navigate to the provided URL."""
def navigate_to_url(url):
    pass
