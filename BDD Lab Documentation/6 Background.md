# Part 6: Selenium with Python Behave (BDD) | Background

## Behave Background
In Behave, the **Background** section is a feature that allows you to define a set of steps that are common to all scenarios within a feature file. 
These steps are executed before every scenario in that feature file, effectively setting up a common context for all scenarios. 
The **Background** section is particularly useful when you have repetitive steps that need to be executed in multiple scenarios within the same feature.

## 1. Write feature file with multiple scenarios
This is an example with multiple scenarios:

     Feature: OrangeHRM Login
          Scenario: Login to HRM Application
                Given I launch browser
                When I open application
                And Enter valid username and password
                And click on login
                Then User must login to the Dashboard page
    
          Scenario: Search user
                Given I launch browser
                When I open application
                And Enter valid username and password
                And click on login
                When navigate to search page
                Then search page should display
    
          Scenario: Advanced Search user
                Given I launch browser
                When I open application
                And Enter valid username and password
                And click on login
                When navigate to advanced search page
                Then advanced search page should display

These scenarios contain multiple setups.

## 2. Apply Behave into the feature file

This is an example on how you can use the Background section in a Behave feature file:

    Feature: OrangeHRM Login
        
        Background: common steps
            Given I launch browser
            When I open application
            And Enter valid username and password
            And click on login
        
        Scenario: Login To HRM Application
            Then User must login to the Dashboard page
        
        Scenario: Search user
            When navigate to search page
            Then search page should display
        
        Scenario: Advanced Search user
            When navigate to advanced search page
            Then advanced search page should display

In the above example, the **Background** section contains a steps that navigates to the page. 
These steps are shared by the scenarios within the same feature. 
When you run the Behave tests for this feature, the background steps will be executed before each scenario, ensuring that every scenario starts from the same initial state. 
The Background section helps in keeping your feature files more concise and DRY (Don't Repeat Yourself).

## 3. Execute feature file

To execute type in terminal and hit ENTER: `behave /<name of feature file>.feature`

All scenarios and steps should pass.

