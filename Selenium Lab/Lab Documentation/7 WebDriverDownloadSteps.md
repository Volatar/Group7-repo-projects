# Steps to download ChromeDriver (version 115 or above)

1. Open the *Chrome for Testing* availability page – [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

2. On this page, you will see different versions, including Stable, Dev, Beta and Canary releases.

![Imgur](https://i.imgur.com/ZzZ0lHG.png)

3. Go to the Stable version and look for chromedriver for win32, win64, or linux64 (based on your OS being 32-bit Windows, 64-bit Windows, or 64-bit Linux)

![Stable](https://i.imgur.com/XylBRQW.png)

4. Open the URL in a new tab. Chromedriver-win64.zip will now be downloaded on your machine.

5. Once you have downloaded the zip file, unzip it to retrieve chromedriver.exe

6. Note the location where you extracted the web driver. The location will be used later.

---

# Steps to download ChromeDriver (version 114 or below)

1. [Open the ChromeDriver page](https://chromedriver.chromium.org/home)

2. This page provides the latest binaries, as well as older ones.

![Imgur](https://i.imgur.com/89Nb0nF.png)

3. Click on the Downloads link. Based on the version of Chrome you have on your machine, click on the corresponding ChromeDriver version

![Imgur](https://i.imgur.com/svFOnG3.png)

4. Assuming you clicked on the link for ChromeDriver 114.5735.90, you will find yourself on the ChromeDriver download page which contains ChromeDriver for Mac, Windows and Linux.

![Imgur](https://i.imgur.com/9m2r1CZ.png)

5. Click on chromedriver_win32.zip to download ChromeDriver for Windows.

6. Once you download the zip file, unzip it to retrieve chromedriver.exe

7. Note the location where you extracted the web driver. The location will be used later.
---

# How to Download Firefox's GeckoDriver

Gecko Driver is available as an executable file that can be downloaded. 
The following are the list of steps to download gecko driver.

#### Select the appropriate version:

#### Step 1: 
GeckoDriver can be installed from this link here. Pick the version of GeckoDriver based on the system being utilized. In this tutorial, the system is 64-bit and runs on Windows OS.

At this page [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases), Select the appropriate version for GeckoDriver download based on your operating system

![GeckoDriver](https://i.imgur.com/IrN9tiG.png)

#### Extract the ZIP file.
#### Step 2: 
Unzip the file and obtain geckodriver.exe.  This executable file needs to be accessible when running a program with Selenium, and there are three possible methods to accomplish this task.

1. Edit the Path variable using Advanced system

2. Specify The executable path of the geckodrive.exe within the test script

3. Use the web-driver manager package

###  One method is to edit the Path variable using the Advanced system settings. 

Go to Advanced System Settings, a system properties window will open.

![Imgur](https://i.imgur.com/USj58Jw.png)

Click on Environment Variables

Go to System Variables and find the “Path” variable. Select this variable and click Edit.

![Imgur](https://i.imgur.com/Mo4GSHX.png)

Click New in the Edit environment variable window. Add the location of the geckodriver.exe file to the Path. In this example, the file is located in C:\DRIVERS.

![Imgur](https://i.imgur.com/dk6ZksQ.png)

Restart the computer prior to running any test scripts.


---

# How To Download the Microsoft Edge Driver

The installation and setup of the Edge driver for Microsoft's Edge browser involves the following steps:

1. First, we need to check the current version of the Microsoft Edge browser. 
To do so, open Edge and click on “Settings and More” (the three dots) in the top right corner or press alt + F. 
Then, hover over “Help and Feedback ” in the settings menu and click on About Microsoft Edge. 
On the About page, we can find the current browser version, as shown in the image below.

![Imgur](https://i.imgur.com/o3hWgi1.png)


2. Next, we need to download the Edge driver for its setup and integration. 
We can visit the official Microsoft Edge driver download page to download the Edge driver.
[Here is the link to download Edge Driver from Microsoft.](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
On this page, you can select the appropriate version based on your operating system and browser release version to download it. 
Make sure to download the correct version according to the browser; otherwise, we may get a runtime error or some unexpected crash.

3. Once the download is complete, a zip file gets saved. 
We need to extract the downloaded zip file and store it in the desired location. 
After extracting it, we can find the executable file – msedgedriver.exe file at the selected location as sown in the image below:

![Imgur](https://i.imgur.com/DESloWX.png)

This executable file is our required application file for the Edge driver. 
In the upcoming steps, we will use this executable file in our automation script to integrate the Edge driver with the Selenium framework.


