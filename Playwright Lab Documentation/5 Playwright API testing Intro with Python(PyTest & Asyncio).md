# 1. Playwright API Testing Introduction with Python (PyTest & Asyncio)

##  1.1 Introduction

Playwright API testing with Python, PyTest, and Asyncio. In this tutorial, we'll delve into the documentation, understand how to start automation, and perform API testing using the Playwright library.

### 1.1.1 Why Playwright for API Testing?

Playwright is a powerful library that facilitates API testing. It enables you to test server APIs, prepare server-side states, and validate post-conditions after UI actions. This ensures changes made in the UI are correctly applied in the database or backend API.

## 1.2 Prerequisites
Clone the Todoss application repository, which is used as an example in this tutorial:

github.com/JoanEsquivel/testing-lists

Install the necessary dependencies as mentioned in the repository.

# 2. Setting Up API Request Context

To send requests to an API, you need to create an API request context. This is achieved using the Playwright library.

## 2.1 Code Example: Setting Up API Request Context

Python

    # Import necessary modules and classes
    from typing import Generator
    import pytest
    from playwright.sync_api import Playwright, api_request_context

    # Define PyTest fixture for API request context
    @pytest.fixture(scope="session")
    def api_request_context() -> Generator:
        with api_request_context() as context:
        yield context

# 3. Performing API Testing with PyTest

PyTest provides a reliable and consistent context for tests. We'll create a PyTest fixture for API testing and a test function to perform API requests.

## 3.1 Code Example: PyTest Fixture and Test Function

Python 

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

# 4. Running the Tests

Execute the tests using the following command:

bash

    pytest <path_to_test_file>

Replace <path_to_test_file> with the path to the file containing the test functions.

# 5. Asyncio Approach for API Testing

You can also perform API testing using Asyncio with Playwright. This approach is similar but utilizes Asyncio features.

## 5.1 Code Example: Asyncio Approach for API Testing

Python

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

# 6. Conclusion
In this tutorial, we covered setting up API request contexts, performing API testing with PyTest, and an alternative Asyncio approach