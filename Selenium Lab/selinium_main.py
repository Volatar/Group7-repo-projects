"""Import Selenium, web application, and methods from other modules"""
from selenium.webdriver.common.by import By
from web_interact import *
from validation import *
from utility import *


"""Selenium lab main"""
def main():
    # Initialize WebDriver and navigate to web-app url
    driver = initialize_driver("Chrome")  # Ensure that your driver is entered
    navigate_to_url(driver, "http://127.0.0.1:5000")

    # Verify that the homepage title is correct
    if validate_page_title(driver, "Home"):
        print("Title page is correct")
    else:
        print("Title page is incorrect, the title is " + driver.title)
    capture_screenshot(driver, "home_page")

    # Navigate to search page and search for a movie
    click_element(driver, By.ID, "search")
    element = driver.find_element(By.ID, "user_input")
    element.send_keys("E")
    click_element(driver, By.ID, "search_button")

    if is_element_present(driver, By.ID, "movie"):
        element = driver.find_element(By.ID, "movie")
        print("The movie is " + element.text)
    else:
        print("The movie could not be found")

    capture_screenshot(driver, "search_page")

    # Add the movie to cart and select and add another
    click_element(driver, By.ID, "add_cart")
    element = driver.find_element(By.ID, "user_input")
    element.send_keys("A")
    click_element(driver, By.ID, "search_button")
    click_element(driver, By.ID, "add_cart")

    # Navigate to cart and remove one of the movies
    click_element(driver, By.ID, "cart")
    capture_screenshot(driver, "cart_page1")
    if is_element_present(driver, By.NAME, "remove Alien vs Ogre"):
        click_element(driver, By.NAME, "remove Alien vs Ogre")
    else:
        print("The movie could not be found, thus was not removed")
    capture_screenshot(driver, "cart_page2")

    # Navigate to payment page then return to cart
    click_element(driver, By.ID, "pay")
    capture_screenshot(driver, "payment_page1")
    click_element(driver, By.ID, "return_cart")

    # Navigate back to search and then add another movie
    click_element(driver, By.ID, "search")
    element = driver.find_element(By.ID, "user_input")
    element.send_keys("J")
    click_element(driver, By.ID, "search_button")
    click_element(driver, By.ID, "add_cart")

    # Finally, navigate to payment page and pay
    click_element(driver, By.ID, "cart")
    click_element(driver, By.ID, "pay")
    capture_screenshot(driver, "payment_page2")
    click_element(driver, By.ID, "movie_pay")


"""Run main"""
main()
