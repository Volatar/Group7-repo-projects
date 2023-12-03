# Part 3: Writing Your First Test

### 1. Create a Project Directory
Test-Driven Development (TDD) in Python, a "project directory" refers to the directory structure and files associated with a particular software project. 
The project directory structure may vary depending on the project's size, complexity, and the specific tools and frameworks being used.

```py
import os

def create_project_directory(project_name):
    project_path = os.path.join(os.getcwd(), project_name)

    try:
        os.mkdir(project_path)
        return project_path
    except FileExistsError:
        return None
    except Exception as e:
        raise e
```

### 2. Write a Simple Test
Inside your project directory, create a file named `test_calculator.py`
```py
# test_calculator.py

def test_addition():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, -2) == 3
```

This is a simple test using an assert statement.

### 3. Run the Test

Open your terminal, navigate to the project directory, and run the file: `pytest test_calculator.py`


Test fails because the `add_numbers` function has not been defined.

# Part 4: Implementing Code to Pass the Test

### 1. Create the Module

Create a new file named `my_module.py` in the project directory.

### 2. Implement Addition

Write the following code in `my_module.py`:

```py
def add_numbers(a, b):

return a + b
```

### 3. Run the Test Again

Run the test using pytest: `pytest test_calculator.py`

This time, you should see that the test passes because the function now correctly adds two numbers.