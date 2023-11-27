# Part 2: Selenium with Python Behave (BDD) | Environment Setup

These instructions are primarily for Windows.

## Install Python

1. Visit the [official Python website](https://www.python.org/downloads/windows/) in your web browser.

2. Download the latest Python installer for Windows.

3. Run the installer and follow the on-screen instructions. 
Make sure to add python to your PATH when given the option.

4. After installation, open a command prompt or terminal and type `python --version` or `python3 --version` to confirm the installation and view the Python version. 
If you encounter any issues or if Python is not found, ensure that you installed Python correctly and that you selected the option to add Python to your system's PATH during installation. 
If needed, you can reinstall Python with the correct settings.

## Install PyCharm IDE

1. Visit [the official PyCharm website](https://www.jetbrains.com/pycharm/download/) in your web browser.

2. There are two editions available: "PyCharm Community" (free) and "PyCharm Professional" (paid with a free trial). 
Choose the edition that best suits your needs.

3. Click on the download link for the edition you want. 
You can also download the .exe (Windows) or .dmg (macOS) installer or a .tar.gz archive (Linux) depending on your operating system.

4. If you downloaded the .exe installer, double-click the installer file to run it.
Follow the installation wizard's instructions, and you can customize your installation preferences.

## Install Selenium Library

Install Selenium using pip. 
If you are using the global python environment, in the Command Prompt, you can use pip to install Selenium. 
Enter the following command and press Enter: `pip install selenium`

This command will download and install the Selenium package and its dependencies.

Run `pip list` to verify that Selenium was installed

If you are using a virtual environment within PyCharm (recommended), access it's terminal in the lower left corner of the screen and input the same commands.

## Install Behave

1. In the Command Prompt, you can use pip to install Behave. Enter the following command and press Enter:
`pip install behave`
This command will download and install the Behave package and its dependencies.

2. To upgrade to the latest behave version enter: `pip install -U behave`

3. Run `pip list` to verify that Behave was installed.
