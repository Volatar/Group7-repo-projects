# Steps to initialize ChromeDriver

ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. 
It is maintained by the Chromium team with help from WebDriver contributors. 
If you are unfamiliar with Selenium WebDriver, you should check out [their website](https://chromedriver.chromium.org/).

Follow these steps to set up your tests for running with ChromeDriver:

Ensure Chromium/Google Chrome is installed in a recognized location.
ChromeDriver expects you to have Chrome installed in the default location for your platform.
You can also force ChromeDriver to use a custom location with a setting, but we are not going to cover that here.

Download the ChromeDriver binary for your platform under the [downloads section of their website.](https://chromedriver.chromium.org/downloads/version-selection)

###Help WebDriver find the downloaded ChromeDriver executable

Include the ChromeDriver location in your PATH environment variable. Some help for that process is found [here](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14))

Include the path to ChromeDriver when instantiating webdriver.Chrome (see sample below)

### Some example code that calls ChromeDriver

python:
```py
import time

from selenium import webdriver



driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
```

# Steps to initialize GeckoDriver for Firefox

## How to Launch the Firefox Browser Using GeckoDriver in Selenium Python

### Pre-requisites


1. Set up a Python environment.

2. Install GeckoDriver and use any of the methods outlined above to ensure that the driver is accessible when running the test script.

3. Ensure that Selenium is installed. If it isn’t, use the pip package installer to install the package. 
If you have Conda or Anaconda set up, simply enter the following command in the Linux terminal, or the Conda/Anaconda prompt:
`pip install selenium`

## Steps to Launch the Firefox Browser

**Step 1**: Import the WebDriver and options module from Selenium.
```py
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
```

**Step 2: Options** is a concept that was added to Selenium in order to allow the user to customize the Firefox session. In this example, it is used to provide the binary location of firefox.exe.
```py
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
```

**Step 3**: Initialize the browser driver, and pass an instance of the options class in the driver initialization. If GeckoDriver hasn’t been added to the path, then execute the following command.
```py
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe', options=options)
```

However, if the geckodriver.exe file location has been added to the path, then execute the following command.
```py
driver = webdriver.Firefox(options=options)
```

**Step 4**: Launch the Firefox browser and navigate to a website.
```py
driver.get('https://www.bstackdemo.com/')
```

#### **Sample Output:**

![Imgur](https://i.imgur.com/laUrDYc.png)

Alternatively, this process is made far easier if the WebDriver-manager package is utilized. 

See the example code below:
```py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.bstackdemo.com/')
```
#### **Output:**

![Imgur](https://i.imgur.com/04GNry1.png)


---

## Integration of the Edge Driver


1. We will jump into the setup and integration of Edge driver with the Selenium framework to automate the Microsoft Edge browser. Hence we will start by creating a Python file named “automation_script_selenium.py” and open it in Visual Studio Code.

2. Finally, we will integrate the Edge driver with the Selenium framework to open a browser session. Here we will open the browser and then navigate to a web page (https://www.lambdatest.com) with an automation script.

#### Python Code:

```py
from selenium import webdriver
from selenium.webdriver.edge.service import Service


# Driver Code
if __name__ == '__main__':
  # create service object
  edgeService = Service(
      r"D:\\Lambdatest Tools\\edgedriver_win64\\msedgedriver.exe")


  # create webdriver object
  edgeDriver = webdriver.Edge(service=edgeService)


  # open browser and navigate to the website
  edgeDriver.get('https://www.lambdatest.com')
```

In the above code, we are instructing the Microsoft Edge browser to open the specified web page (https://www.lambdatest.com). At first, we create an “edgeService” object that represents the Microsoft Edge browser using the Service class provided by Selenium.

Next, we assign this service object to the Edge driver in the “edgeDriver” variable. This will be responsible for controlling and executing actions on the browser. Finally, we navigate to the specified web page (https://www.lambdatest.com) with the help of edgeDriver.get(‘https://www.lambdatest.com’) method.
Now if we run this code, it will automate the Microsoft Edge browser and open the specified page in a new browser session, as shown in the image below.

![Imgur](https://i.imgur.com/r4koR4f.png)
