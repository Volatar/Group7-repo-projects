"""Import Selenium, web application, and methods from other modules"""
import os
from selenium import webdriver
from error_handling import *


"""Method that initializes the WebDriver based on the browser type provided."""
def initialize_driver(browser_type):
    os.environ['PATH'] += r""  # Insert your pathway to your driver
    if browser_type == 'Chrome':
        driver = webdriver.Chrome()
    if browser_type == 'Edge':
        driver = webdriver.Edge()
    if browser_type == 'Firefox':
        driver = webdriver.Firefox()
    if browser_type == 'Safari':
        driver = webdriver.Safari()
    return driver


"""Method that uses the WebDriver instance to navigate to the provided URL."""
def navigate_to_url(driver, url):
    try:
        driver.get(url)
    except NavigationException:
        raise NavigationException("Navigation to sample website failed.")


"""Method to click upon a certain element"""
def click_element(driver, locator_type, locator_value):
    try:
        element = driver.find_element(locator_type, locator_value)
        element.click()
    except:
        raise ElementNotFoundException("Specified element not found, element could not be clicked.")
