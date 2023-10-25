class ElementNotFoundException(Exception):
    pass


class NavigationException(Exception):
    pass


# class DataReadException(driver):
#  """Handles specific exceptions, logging a user-friendly message."""
#  def handle_exception(exception_type,message):
#    if exception_type == DataReadException:
#      return print("Data Read Error")
