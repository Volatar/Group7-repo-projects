# Part 4: Selenium with Python Behave (BDD) | Step Parameters

# Paramaters to steps
In the context of Behavior-Driven Development (BDD) and the "behave" framework in Python, scenario steps refer to the individual steps that make up a test scenario. These steps are typically written in a natural language style to describe the expected behavior of a software application. Each step is associated with a specific Given-When-Then structure.

1. Given: This step sets up the initial state of the system, often providing context for the scenario. For example, "Given the user is logged in."

2. When: This step describes an action that is taken. For example, "When the user clicks the 'Submit' button."

3. Then: This step specifies the expected outcome or result of the action. For example, "Then the system should display a success message."

This is an example of a scenario on a feature file:

 Scenario: Login to OrangeHRM with valid parameters
 1. **Given** I launch Chrome browser
 2. **When** I open orange HRM Homepage
 3. **And** Enter username "admin" and password "admin123"
 4. **And** Click on login button
 5. **Then** User must successfully login to the Dashboard page
 
After creating the feature file you will have to create a python step definition file.

# Create a Python Step Definition File
 Inside the features/steps directory, create a Python file with a name that matches your feature file's name. For example, if your feature file is my_feature.feature, create a Python file named my_feature.py in the features/steps directory.

To obtain the step definitions you sould execute the feature file. Copy and paste tthe result in the python file

# Write Step Definitions in Python
 In the Python step definition file, you need to write Python code that maps the steps defined in your feature file to actual code. Use the @given, @when, and @then decorators to define step definitions that match the steps in your feature file.

 Here's an example of what your Python step definition file:

     from behave import  *
     from selenium import

    @given('I launch Chrome browser')
    def step_impl(context):
        context.driver=webdriver.Chrome()
        
    @when('I open orange HRM Homepage')
    def step_impl(context):
         context.driver.get("https://opensource-demo.orangehrmlive.com/")

    @when('Enter username "{user}" and password "{pwd}"')
    def step_impl(context,user,pwd):
        context.driver.find_element_by_id("txtUsername").send keys(user)
        context.driver.find_element_by_id("txtPassword").send keys(pwd)

    @when('Click on login button')
    def step_impl(context):
        context.driver.find_element_by_id("btnLogin").click()

    @then('User must successfully login to the Dashboard page')
    def step_impl(context)
        text=context.driver.find_element_by_xpath("//h1[contains(text(), 'Dashboard')]").text()
        assert text=="Dashboard"
        context.driver.close()
        
# Execute Test
After creating the Python step definition file, you can run your BDD tests using a testing framework like Behave by executing behave from the command line or using an integrated development environment (IDE) like PyCharm
    

