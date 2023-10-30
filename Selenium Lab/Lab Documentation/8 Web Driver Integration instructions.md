# Steps to initialize ChromeDriver

ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. It is maintained by the Chromium team with help from WebDriver contributors. If you are unfamiliar with Selenium WebDriver, you should check out the Selenium site.

Follow these steps to setup your tests for running with ChromeDriver:

Ensure Chromium/Google Chrome is installed in a recognized location

ChromeDriver expects you to have Chrome installed in the default location for your platform. You can also force ChromeDriver to use a custom location by setting a special capability.

Download the ChromeDriver binary for your platform under the downloads section of this site

Help WebDriver find the downloaded ChromeDriver executable

Any of these steps should do the trick:

include the ChromeDriver location in your PATH environment variable

(Java only) specify its location via the webdriver.chrome.driver system property (see sample below)

(Python only) include the path to ChromeDriver when instantiating webdriver.Chrome (see sample below)

### sample test

java:

    import org.openqa.selenium.*;

    import org.openqa.selenium.chrome.*;

    import org.junit.Test;

    public class GettingStarted {   

    @Test   

    public void testGoogleSearch() throws InterruptedException {     

    // Optional. If not specified, WebDriver searches the PATH for chromedriver.       System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");           WebDriver driver = new ChromeDriver(); 

    driver.get("http://www.google.com/");    

    Thread.sleep(5000);  // Let the user actually see something!     

    WebElement searchBox = driver.findElement(By.name("q"));

    searchBox.sendKeys("ChromeDriver");     

    searchBox.submit();    

    Thread.sleep(5000);  // Let the user actually see something!     

    driver.quit();  

        } 

    }

python:

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

## Controlling ChromeDriver's lifetime

The ChromeDriver class starts the ChromeDriver server process at creation and terminates it when quit is called. This can waste a significant amount of time for large test suites where a ChromeDriver instance is created per test. There are two options to remedy this:

1. Use the ChromeDriverService. This is available for most languages and allows you to start/stop the ChromeDriver server yourself. See here for a Java example (with JUnit 4):

        import java.io.*; 

        import org.junit.*; 

        import org.openqa.selenium.*; 

        import org.openqa.selenium.chrome.*; 

        import org.openqa.selenium.remote.*; 

        public class GettingStartedWithService {    

            private static ChromeDriverService service;   

            private WebDriver driver;    

            @BeforeClass   

            public static void createAndStartService() throws IOException {     

                service = new ChromeDriverService.Builder()         

                    .usingDriverExecutable(new File("/path/to/chromedriver"))         

                    .usingAnyFreePort()         

                    .build();     

        service.start();   

        }    

  

    @AfterClass   

    public static void stopService() {     

        service.stop();   

     }    



    @Before   

     public void createDriver() {     

        driver = new RemoteWebDriver(service.getUrl(), new ChromeOptions());   

     }    



    @After   public void quitDriver() {     

        driver.quit();   

    }    



    @Test   

    public void testGoogleSearch() {     

        driver.get("http://www.google.com");     

        // rest of the test...   
    
        } 

    }

Python:

    import time

    from selenium import webdriver

    from selenium.webdriver.chrome.service import Service

    service = Service('/path/to/chromedriver')

    service.start()

    driver = webdriver.Remote(service.service_url)

    driver.get('http://www.google.com/');

    time.sleep(5) # Let the user actually see something!

    driver.quit()

2. Start the ChromeDriver server separately before running your tests, and connect to it using the Remote WebDriver.

Terminal:

    $ ./chromedriver

    Starting ChromeDriver 76.0.3809.68 (...) on port 9515

    ...

Java:

    import java.net.*;

    import org.openqa.selenium.*;

    import org.openqa.selenium.chrome.*;

    import org.openqa.selenium.remote.*;  



    public class GettingStartedRemote {      



        public static void main(String[] args) throws MalformedURLException {          

            WebDriver driver = new RemoteWebDriver(         

                new URL("http://127.0.0.1:9515"),         

                new ChromeOptions());     

            driver.get("http://www.google.com");     

            driver.quit();   

         }

    }


# Steps to initialize GeckoDriver for Firefox

### There are three different ways to initialize GeckoDriver.

1.Using DesiredCapabilities:

First, set the system property for Gecko Driver.

Syntax

    System.setProperty("webdriver.gecko.driver","Path to geckdriver.exe file");

Example

    System.setProperty("webdriver.gecko.driver","D:\\Downloads\\GeckoDriver.exe");
Next, set Desired Capabilities.

Desired Capabilities help Selenium to understand the browser name, version and operating system to execute the automated tests. Below is the code to set gecko driver using DesiredCapabilities class.

    DesiredCapabilities capabilities = DesiredCapabilities.firefox();
    capabilities.setCapability("marionette",true);

Here is the Complete Code

    System.setProperty("webdriver.gecko.driver", driverPath);
    DesiredCapabilities capabilities = DesiredCapabilities.firefox();
    capabilities.setCapability("marionette",true);
    driver= new FirefoxDriver(capabilities);


2.Using marionette property:
Gecko driver can also be initialized using marionette property as below

    System.setProperty("webdriver.gecko.driver","D:\\Downloads\\GeckoDriver.exe");

If gecko driver is initialized using the above method, code for desired capabilities is not required.

3.Using FirefoxOptions:
Mozilla Firefox version 47+ has marionette driver as a legacy system. Taking advantage of this, 
marionette driver can be called using Firefox Options as below

    FirefoxOptions options = new FirefoxOptions();
    options.setLegacy(true);

### Code for launching firefox using Gecko driver
    
    package com.guru99.demo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

public class GeckoDriverDemo {

    String driverPath = "D:\\Guru99Demo\\GeckoDriver.exe";
    public WebDriver driver;

    @Before
    public void startBrowser() {
        System.setProperty("webdriver.gecko.driver", driverPath);
        DesiredCapabilities capabilities = DesiredCapabilities.firefox();
        capabilities.setCapability("marionette", true);
        driver = new FirefoxDriver(capabilities);

    }

    @Test
    public void navigateToUrl() {
        driver.get("http://demo.guru99.com/selenium/guru99home/");
    }

    @After
    public void endTest() {
        driver.quit();
    }

}

#### Code Explanation:

#### @Before method:

Initially, we need to set the system property for gecko driver to the geckdriver.exe file download location. We need to set the marionette property to true for Selenium to use Marionette protocol to communicate with Gecko Driver. Finally, 
we need to start the Firefox browser instance using the object for Desired Capabilities.

The below statements help to achieve the above task.

    System.setProperty("webdriver.gecko.driver", driverPath);
    DesiredCapabilities capabilities = DesiredCapabilities.firefox();
    capabilities.setCapability("marionette",true);
    driver= new FirefoxDriver(capabilities);

### @Test method:

We are navigating to user-specified URL using the inbuilt “get” method provided by Selenium web driver. The below statement help to achieve the same.

    driver.get("http://demo.guru99.com/selenium/guru99home/"); 

### @After method:

Finally, we are closing the browser instance using the quit method.

    driver.quit();

### Modify a script for non- Gecko to Gecko

Non-gecko driver script used before Selenium 3 was straightforward. We need to create an instance of Firefox driver and use the instance variable.

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

### Advantage of using Gecko Driver

Selenium Webdriver version 2.53 is not compatible with Mozilla Firefox version 47.0+. The Firefox driver used in earlier versions of Mozilla Firefox will be discontinued, and only the GeckoDriver implementation would be used. Hence testers are forced to use GeckoDriver if they want to run automated tests on Mozilla Firefox version 47.0+. But the big question – what is the advantage?

The major advantage of using GeckoDriver as opposed to the default Firefox driver is Compatibility. GeckoDriver uses W3C WebDriver protocol to communicate with Selenium. W3C is a universally defined standard for Web Driver. This means Selenium Developers (People who code Selenium base) need not create a new version of Web Driver for each browser version. The same Web Driver can be used for multiple browser versions. Hence, GeckoDriver is preferred compared to the earlier implementation of Firefox driver.


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
