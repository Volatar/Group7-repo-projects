# Part 3: Project Creation | Feature File & Steps using PyCharm

## Prerequisites:
PyCharm: Ensure you have PyCharm installed on your system. 
If not, download and install it from the JetBrains website.

Python: Make sure you have Python installed on your system. Behave, the BDD framework we will be using, is a Python library.

## Step 1: Create a New PyCharm Project
Launch PyCharm and click on "File" > "New Project" to create a new project. 
Choose an appropriate location for your project directory and give it a name. 
Click "Create."

In the "New Project" dialog, ensure you have selected your Python interpreter. 
If not, click "Project Interpreter" and choose the Python interpreter you wish to use. 
Click "Create" to create the project.

## Step 2: Install the 'Selenium' and 'Behave' Package
1. Select project and go to File > New Project Setup > Setting for New Project
2. Python Interpreter should already be selected, in that window you should see a '+' sign, click on that.
3. In the Available Packages window type 'selenium' (You should see most recent version) click Install Package.
4. Once selenium package is finish installing repeat the previous step with 'behave'.
5. Click Ok to save settings.

## Step 3: Download Selenium Drivers for Browsers
Refer to Selenium Lab "Selenium Lab/Lab Documentation/7. WebDriverDownloadSteps.md" for reference https://github.com/Volatar/Group7-repo-projects/blob/bdd/Selenium%20Lab/Lab%20Documentation/7.%20WebDriverDownloadSteps.md 

## Step 4: Create a Feature File
Right-click on your project folder in the "Project" pane on the left side of the PyCharm window.

Go to "New" > "Directory" and create a directory to store your feature files. 
You can name it "features."

Inside the "features" directory, right-click, and go to "New" > "File" to create a new feature file with the .feature extension. 
For example, create a file named search.feature.

In your search.feature file, you can start writing your feature file using Gherkin syntax as explained in the previous tutorial. 
For example:

## Gherkin
Copy Code and install Gherkin plug-in

    Feature: Search input
      Scenario: Valid search option
        Given a user navigates to the search page
        When they enter valid search input
        Then they should receive correct search suggestion
      Scenario: Invalid search option
        Given a user navigates to the search page
        When they enter invalid search input
        Then they should see an error message

## Step 5: Create Step Definitions
Right-click on your project folder in the "Project" pane again.

Go to "New" > "Directory" and create a directory to store your step definition files. 
You can name it "features/steps."

Inside the "features/steps" directory, right-click and go to "New" > "Python File" to create a new Python file. 
Name it something like search_steps.py.

In your search_steps.py file, you can start defining the step definitions. 
For example:

Python

```py
    from behave import *
    from selenium import webdriver

    @given('a user navigates to the searh page')
    def step_user_navigates_to_search_page(context):
        # Implement code to navigate to the search page
        pass

    @when('they enter valid search input')
    def step_user_enters_valid_search_input(context):
        # Implement code to enter valid search input
        pass

    @then('they should receive correct search suggestion')
    def step_user_should_receive_correct_search_suggestion(context):
        # Implement code to verify user receives correct search suggestion
        pass

    @when('they enter invalid search input')
    def step_user_enters_invalid_search_input(context):
      # Implement code to enter invalid search input
      pass

    @then('they should see an error message')
    def step_user_should_see_an_error_message(context):
        # Implement code to verify the presence of an error message
        pass
```
For more detail on how to write your code reference this video (timestamped link) >>>> [https://youtu.be/pXF2uIkeCRY?si=_G0dzkdEpX-kZqm5 ](https://youtu.be/pXF2uIkeCRY?si=yGoMspJ2p8EbOKSy&t=680)


In PyCharm, Behave should recognize these step definitions, and you'll see auto-completion suggestions while writing feature files. 
Ensure the step definition names match those in your feature file.

## Step 6: Running BDD Tests
Open a terminal within PyCharm.

Navigate to your project directory using the terminal. For example:

bash
Copy code
cd /path/to/your/project
To run your BDD tests, execute the following command:

```
behave
```

Behave will locate your feature files and corresponding step definitions, execute the scenarios, and display the test results in the terminal.

With these steps, you've successfully created a BDD project in PyCharm, created feature files using Gherkin syntax, and set up step definitions to implement your test logic. 
You can continue to write feature files and their corresponding step definitions to expand your BDD test suite.
