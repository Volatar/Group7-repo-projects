# PyCharm instructions

If you are using PyCharm much of the process of getting this project running is easier.
Pycharm can be found [on it's official website](https://www.jetbrains.com/pycharm/).
These instructions were written for PyCharm Community Edition but should work for Professional or Education edition.

# Open as a new project
First download the project source files. Unzip them if necessary or clone from Github.
Navigate to the folder using Windows Explorer and click on the path at the top. Copy this.
The files shown in this screenshot will not contain everything you will have as this guide was written early in the project.

![Windows Explorer](https://i.imgur.com/cWpntrk.png)

Open PyCharm. Click on File in the upper left, and then click the first option: New Project.

![New Project](https://i.imgur.com/pyMpAZY.png)

In this new screen, paste in the path to your code folder at the top for Location. 
Select to create a new environment using Virtualenv, and select the newest version of Python you have under Base interpreter.
Do not select another project's virtual environment here, use one of the basic Python ones.
Uncheck all other options on this page and click create.

![New Project screen](https://i.imgur.com/TvunFbN.png)

PyCharm will now tell you that the folder is not empty and ask if you want to create from existing sources. 
We want to do that, so select to do so.

![Create from existing sources?](https://i.imgur.com/yY14aK3.png)

PyCharm will finally ask if you want the project in this window, replacing anything you have up, or a new window running alongside the existing project you are looking at.
This choice is up to you. I chose a new window as I have multiple projects at the moment.

![New window?](https://i.imgur.com/l38I98J.png)

You will then be presented with all the project files on the left for your perusal. 
There is one more step remaining. 
We need to install all the requirements to the virtual environment.

In the lower left of the screen select the terminal.

In the terminal, type or copy-paste the following:
`pip install -r "Selenium Lab\Lab Documentation\requirements.txt"`

Replace the backslashes with forward slashes (/) if you are on Linux.

![Terminal](https://i.imgur.com/DVOqkaX.png)

You are now ready to run the project files.