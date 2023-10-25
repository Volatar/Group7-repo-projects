from error_handling import *

"""Method that checks if the current page title matches the expected title."""
def validate_page_title(driver, expected_title):
    if driver.title == expected_title:
        return True
    else:
        return False


"""Method that searches for an element based on the locator provided."""
def  is_element_present(driver, locator_type, locator_value):
    try:
        driver.find_element(locator_type, locator_value)
        return True
    except:
        raise ElementNotFoundException("Specified element not found.")
        return False
