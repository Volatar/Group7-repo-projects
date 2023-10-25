class ElementNotFoundException:
    """Handles specific exceptions, logging a user-friendly message."""
    def handle_exception(self, message):
        print(message)


class NavigationException:
    """Handles specific exceptions, logging a user-friendly message."""
    def handle_exception(self, message):
        print(message)


# class DataReadException(driver):
#  """Handles specific exceptions, logging a user-friendly message."""
#  def handle_exception(exception_type,message):
#    if exception_type == DataReadException:
#      return print("Data Read Error")
