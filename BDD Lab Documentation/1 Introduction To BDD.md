# Part 1: Introduction to BDD

## What is BDD?
Behavior Driven Development (BDD) is an agile software development methodology that shifts the focus from merely writing code to emphasizing the behavior and functionality of the software from a user's perspective. 
In BDD, the primary goal is to create software that closely aligns with user expectations.

## Key Points:

BDD focuses on how the software behaves and interacts with users and other components of the system.
It encourages developers, testers, and non-technical stakeholders to collaborate and ensure that the software meets user needs and expectations.

### Core Concepts
In Python, when implementing Behavior Driven Development (BDD) using a framework like Behave, the two primary components you'll work with are feature files and step definition files. 
These components help you write and execute BDD scenarios.

### Feature Files
![image](https://github.com/Volatar/Group7-repo-projects/assets/89305357/df09faff-a4aa-465b-9898-edf209239ea7)

Feature files are an essential part of BDD, as they serve as a plain-text representation of the expected behavior of your software. 
Feature files are written using the Gherkin language, which is designed to be human-readable and easy to understand. 
Each feature file typically describes a specific feature or functionality of your application. 
Feature Files should end in ".feature". Here's an example of a simple feature file in Gherkin:

Feature: Search input
  Scenario: Valid search option
  
    Given a user navigates to the search page
    When they enter valid search input
    Then they should receive correct search suggestion

  Scenario: Invalid search option
  
    Given a user navigates to the search page
    When they enter invalid search input
    Then they should see an error message

### Key elements in a feature file:
  Feature:
  
    The name of the feature or functionality being described.
  Scenario:
  
    A specific test scenario or use case related to the feature.
  Given:
  
    Describes the initial state or context before the scenario.
  When: 
  
    Represents the action or event that triggers the scenario.
  Then: 
  
    Defines the expected outcome or result of the scenario.

Feature files provide a structured, human-readable way to document and communicate software behavior. 
They also serve as the basis for creating step definitions, which are implemented in Python code.
    
### Step Definitions Files

A good resource for Behave is... https://pypi.org/project/behave/

Step definition files are Python scripts that contain the actual code to implement the steps described in the feature files. 
Each step in a feature file corresponds to a step definition in Python code.For example, consider the feature file scenario mentioned above. 
To implement the steps, you would create a step definition file that may look like this:
```py
from behave import *

@given('a user navigates to the search page')
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
BDD places a strong emphasis on collaboration, involving developers, testers, and non-technical stakeholders throughout the development process. 
This collaborative approach helps in ensuring that the software meets user expectations.

Collaboration involves open communication and sharing of ideas between team members.

Developers, testers, and non-technical stakeholders work together to create a shared understanding of software functionality.

BDD fosters a user-centric approach by involving non-technical stakeholders in the requirements and testing process, leading to a product that better aligns with user needs.

