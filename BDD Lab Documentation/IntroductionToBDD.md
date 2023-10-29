# Step 1: Introduction to BDD
Duration: 1-2 hours

## What is BDD?
Behavior Driven Development (BDD) is a agile software development methodology that shifts the focus from merely writing code to emphasizing the behavior and functionality of the software from a user's perspective. In BDD, the primary goal is to create software that closely aligns with user expectations.

## Key Points:

BDD focuses on how the software behaves and interacts with users and other components of the system.
It encourages developers, testers, and non-technical stakeholders to collaborate and ensure that the software meets user needs and expectations.

### Core Concepts
In Python, when implementing Behavior Driven Development (BDD) using a framework like Behave, the two primary components you'll work with are feature files and step definition files. These components help you write and execute BDD scenarios.

### Feature Files
Feature files are an essential part of BDD, as they serve as a plain-text representation of the expected behavior of your software. Feature files are written using the Gherkin language, which is designed to be human-readable and easy to understand. Each feature file typically describes a specific feature or functionality of your application. Here's an example of a simple feature file in Gherkin:

Feature: User Login
  Scenario: Valid user login
    Given a user navigates to the login page
    When they enter valid credentials
    Then they should be logged in successfully

  Scenario: Invalid user login
    Given a user navigates to the login page
    When they enter invalid credentials
    Then they should see an error message
    
### Step Definitions Files
Step definition files are Python scripts that contain the actual code to implement the steps described in the feature files. Each step in a feature file corresponds to a step definition in Python code.
