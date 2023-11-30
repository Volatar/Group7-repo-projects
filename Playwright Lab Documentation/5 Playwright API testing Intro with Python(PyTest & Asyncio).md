# Playwright Python Tutorial
## Part 5 - Playwright API Testing Introduction with Python (PyTest & Asyncio)
### Introduction
In this tutorial, we'll delve into the documentation, understand how to start automation, and perform API testing using the Playwright library.

### 1. Why Playwright for API Testing?
Playwright is a powerful library that facilitates API testing. Not only is testing available, but manipulation of server-side states as well. One of the more valuable features is validating post-conditions after UI actions. Versatility is key in what makes Playwright rather useful for detailed API testing, with integration for UI and backend validations.

#### Prerequisites
Clone the Todo application repository, which is used as an example in this tutorial: 
[github.com/JoanEsquivel/testing-lists](github.com/JoanEsquivel/testing-lists). 
Install the necessary dependencies as mentioned in the repository.

### 2. Setting Up API Request Context
To send requests to an API, you need to create an API request context, which is handled well by Playwright's library. The following example sets a PyTest fixture named `api_request_context` through the Playwright library. The fixture becomes coped into the session, making an API request context and setting a consistent testing environment and can be used in test functions for effective API testing throughout the entire session.

#### Code Example: Setting Up API Request Context
```py
# Import necessary modules and classes
from typing import Generator
import pytest
from playwright.sync_api import Playwright, api_request_context

# Define PyTest fixture for API request context
@pytest.fixture(scope="session")
def api_request_context() -> Generator:
    with api_request_context() as context:
    yield context
```

### 3. Performing API Testing with PyTest
PyTest provides a reliable testing context. As to bolster PyTest, we will create a fixture intended for a stable environment that supplements proper and useful API request execution. The following example defines a PyTest fixture named `api_request_context`, which acts as the session-scoped API request context using the Playwright library. A test function `test_post_todo` utilizes this fixture make a POST request with specified payload. Once the response is validated for success, the response details and JSON content are printed.

#### Code Example: PyTest Fixture and Test Function
```py
# Import necessary modules and classes
from typing import Generator
import pytest
from playwright.sync_api import Playwright, api_request_context

# PyTest fixture for API request context
@pytest.fixture(scope="session")
def api_request_context() -> Generator:
    with api_request_context() as context:
    yield context

# PyTest test function for API testing
def test_post_todo(api_request_context):
# Define API endpoint and payload
endpoint = "/todos"
payload = {"completed": True, "id": 1, "title": "Make a new    video"}

# Send POST request
response = api_request_context.post(endpoint, json=payload)

# Validate response
assert response.ok

# Print response details
print("Response JSON:", response.json())
```

### 4. Running the Tests
Execute the tests using the following command: `pytest <path_to_test_file>` and replace `<path_to_test_file>` with the path to the file containing the test functions. If you run the PyTest command while currently navigated into the folder containing your code, the command should work without a path.

### 5. Asyncio Approach for API Testing
Testing can be performed using Asyncio with Playwright as an alternate method. The primary difference being that Asyncio features are used to enhance the testing experience, whereas prior it would just be Playwright. The next example has the `run` function using Asyncio features along with Playwright to send a POST request. The response is validated, and the details are printed. `main` contains and manages the Asyncio environment along with execution of API testing logic.

#### Code Example: Asyncio Approach for API Testing
```py
import asyncio
from playwright.async_api import async_playwright,             async_api_request_context

# Asyncio function for API testing
async def run(playwright):
    async with async_api_request_context() as context:
        # Define API endpoint and payload
        endpoint = "/todos"
        payload = {"completed": True, "id": 1, "title": "Make a new video"}

        # Send POST request
    response = await context.post(endpoint, json=payload)

        # Validate response
    assert response.ok
        
        # Print response details
    print("Response JSON:", response.json())

# Main function to run Asyncio
async def main():
    async with async_playwright() as p:
        await run(p)
# Run Asyncio
asyncio.run(main())
```

### Conclusion
In this tutorial, we worked with setting up API request contexts such as `api_request_context` and maintained a consistent testing environment. An alternate Asyncio approach was also discussed, which all should assist in providing versatile tools for effective API testing.
