class ElementNotFoundException(driver):



class NavigationException(driver):





class DataReadException(driver):
"""Handles specific exceptions, logging a user-friendly message."""
def handle_exception(exception_type,message):
