"""Method that captures the current browser window's screenshot and saves it with the provided file name."""
def capture_screenshot(driver, file_name):
    driver.save_screenshot(file_name + ".png")
