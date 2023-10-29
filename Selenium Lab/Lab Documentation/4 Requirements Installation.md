The following are instructions on getting this code running on any system. 
If you are using PyCharm, skip to the next file for instructions on how to get it running there.

# Ensure Python PIP is installed
Python's PIP is a package manager for Python.
It can install additional Python packages not included by default in Python.
If your version Python version is 3.4 or higher, then PIP should be pre-installed.
If not, you should consult one of these tutorials based on your operating system.

Windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

Linux: https://www.geeksforgeeks.org/how-to-install-pip-in-linux/

macOS: https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

To check if PIP is installed, enter this into your terminal: 

Windows: `py -m pip --version`

Unix: `python3 -m pip --version`

# Installing a Virtual Environment
A virtual environment in Python helps to isolate all the necessary executables and packages required to run a Python project.

To install a virtual environment enter into a terminal:

Windows: `py -m pip install --user virtualenv`

Linux: `python3 -m pip install --user virtualenv`

Then in your local directory of the project, enter: 

Windows: `py -m venv env`

Linux: `python3 -m venv env`

Finally, you can run either of these to activate the environment depending on your operating system.

For Windows > \venv\Scripts\activate

For Linux > source ./venv/bin/activate

# Installing Flask
To install Flask, run this into your terminal: `pip install flask`

# Installing Selenium
To install Selenium, run this into your terminal: `pip install selenium`

# Installing Requirements
You can alternatively install this project's requirements via the requirements.txt file.
This can be accomplished by running this into your terminal: `pip install -r <PATH>\requirements.txt`
Ensure that you include the pathway of your requirements.txt if it is not the same as your current directory.
Put "" around the file path if your folder structure contains folders with spaces in their names.
