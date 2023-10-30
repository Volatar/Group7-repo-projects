# Steps to initialize ChromeDriver

TODO

# Steps to initialize GeckoDriver for Firefox

### There are three different ways to initialize GeckoDriver.

1.Using DesiredCapabilities:
First, set the system property for Gecko Driver.

TODO: None of these images should be an image, you want to be able to copy and paste code.

    ![Imgur](https://i.imgur.com/3xTUdpO.png)

2.Using marionette property:
Gecko driver can also be initialized using marionette property as below

    ![Imgur](https://i.imgur.com/DJvUkOk.png)
If gecko driver is initialized using the above method, code for desired capabilities is not required.

3.Using FirefoxOptions:
Mozilla Firefox version 47+ has marionette driver as a legacy system. Taking advantage of this, 
marionette driver can be called using Firefox Options as below

    ![Imgur](https://i.imgur.com/tabsEu6.png)

### Code for launching firefox using Gecko driver

    ![Imgur](https://i.imgur.com/VtBzYxQ.png)

#### Code Explanation:

#### @Before method:

Initially, we need to set the system property for gecko driver to the geckdriver.exe file download location. 
We need to set the marionette property to true for Selenium to use Marionette protocol to communicate with Gecko Driver. 
Finally, we need to start the Firefox browser instance using the object for Desired Capabilities.

The below statements help to achieve the above task.

    ![Imgur](https://i.imgur.com/vwnFtAk.png)

### @Test method:

We are navigating to user-specified URL using the inbuilt “get” method provided by Selenium web driver. 
The below statement help to achieve the same.

    ![Imgur](https://i.imgur.com/DWJC82v.png)

### @After method:

Finally, we are closing the browser instance using the quit method.

    driver.quit();

### Modify a script for non- Gecko to Gecko

Non-gecko driver script used before Selenium 3 was straightforward. 
We need to create an instance of Firefox driver and use the instance variable.

    @Before
    public void startBrowser() {
        driver = new FirefoxDriver
    }

To convert to gecko, you need to simply add one line of code

    @Before
    public void startBrowser() {
        System.setProperty("webdriver.gecko.driver", "D:\\Downloads\\GeckoDriver.exe");
        driver = new FirefoxDriver();

    }

---

# Integration of the Edge Driver

TODO: Turn images of code into code blocks please

1. We will jump into the setup and integration of Edge driver with the Selenium framework to automate the Microsoft Edge browser. 
Hence we will start by creating a Python file named “automation_script_selenium.py” and open it in Visual Studio Code.

2. Finally, we will integrate the Edge driver with the Selenium framework to open a browser session. 
Here we will open the browser and then navigate to a web page (https://www.lambdatest.com) with an automation script.

    ![Imgur](https://i.imgur.com/4qXLnUT.png)

In the above code, we are instructing the Microsoft Edge browser to open the specified web page (https://www.lambdatest.com). 
At first, we create an “edgeService” object that represents the Microsoft Edge browser using the Service class provided by Selenium.

3. Next, we assign this service object to the Edge driver in the “edgeDriver” variable. This will be responsible for controlling and executing actions on the browser. 
Finally, we navigate to the specified web page (https://www.lambdatest.com) with the help of edgeDriver.get(‘https://www.lambdatest.com’) method.

Now if we run this code, it will automate the Microsoft Edge browser and open the specified page in a new browser session, as shown in the image below.

    ![Imgur](https://i.imgur.com/r4koR4f.png)
