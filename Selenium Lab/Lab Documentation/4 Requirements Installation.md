# Ensure Python PIP is installed
Python's PIP is a package manager for Python.
It can install additional Python packages not included by default in Python.
If your version Python version is 3.4 or higher, then PIP should be pre-installed.
If not, you should consult one of these tutorials based on your operating system.

Windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

Linux: https://www.geeksforgeeks.org/how-to-install-pip-in-linux/

macOS: https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

To check if PIP is installed, enter this into your terminal: `pip --version`

# Installing a Virtual Environment
A virtual environment in Python helps to isolate all the necessary executables and packages required to run a Python project.

To install a virtual environment enter into a terminal: `pip install virtualenv`

Then in your local directory of the project, find "virtualenv venv"

Finally, you can run either of these to activate the environment depending on your operating system.

For Windows > venv\Scripts\activate

For Linux > source ./venv/bin/activate

# Installing Flask
To install Flask, run this into your terminal: `pip install flask`

# Installing Selenium
To install Selenium, run this into your terminal: `pip install selenium`

# Installing Requirements
You can also install this project's requirements via the requirements.txt.
This can be accomplished by running this into your terminal: `pip install -r requirements.txt`
