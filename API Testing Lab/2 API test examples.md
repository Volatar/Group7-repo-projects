# API Test Examples

When performing API testing, it is always crucial to include imports for requests. Importing requests allows the following test examples to work, and thereby is defining GET, PUT, DELETE, and POST test attempts. In this test file, we have a base URL to work with as well, which is also attached toward the top of the file. If you were using someone else's server to test your API calls against, a variable like this would be where you would put that URL.
```py
import requests

base = "http://127.0.0.1:5000/"
```
## Example 1: GET
```py
def test_get():
    response = requests.get(base + "iceCream/4")
    assert response.json() == {"4": "Cotton Candy"}
    assert response.status_code == 200
```
This test makes an HTTP GET request to a constructed endpoint. `iceCream/4` is appended to the base URL and two assert statements are made. Once the GET request is made, the server response is stored in the `response` variable. The first assertion statement checks to see if the JSON content of `response` is equal to `{"4": "Cotton Candy"}`, and returns True if equality is achieved, else returning False for an exception to be raised. The second assertion statement for this and all tests presented asserts the HTTP status code, and passes if the statement returns True. Otherwise, an exception is raised and indicates test failure. Do note that both assertions have to pass for the test to indicate as a success. The terminal output for this test is shown below:

![test_get Successful](https://i.imgur.com/QnCPDNM.png)

## Example 2: DELETE
```py
def test_delete():
    response = requests.delete(base + "iceCream/5")
    assert response.json() == {"message": "Item is deleted from the menu"}
    assert response.status_code == 200
```
This test makes an HTTP DELETE request to an endpoint made by appending `iceCream/5` to the base URL, then stores the server response in the `response` variable. Two assert statements are made to verify a successful deletion. One checks to ensure the content reflects the deletion and the other asserts matching status code. Terminal output displayed below:

![test_delete Successful](https://i.imgur.com/5l1Z9lo.png)

Within the test file, every successful test has an alternative test to ensure a failed GET, PUT, DELETE, or POST test is validated. The next and last test example will be for an intended failure.

## Example 3: DELETE (Intended Failure)
```py
def test_delete_no_id():
    response = requests.delete(base + "iceCream/5")
    assert response.json() == {"message": "ID is invalid"}
    assert response.status_code != 200
```
This test is performing the same actions as the test within Example 2, though the result is meant to be very different. When the assert statements are made, the first asserts for an error concerning a lack of valid ID, the second asserts that the value of `status_code` that is not equal to the intended successful status code will result in a success. Should the test succeed in the DELETE request, an exception is thrown and the test fails. Terminal output is displayed below:

![test_delete_no_id Successful](https://i.imgur.com/CYoOXQU.png)

With these examples, you should have a better understanding of API Testing. As mentioned prior; GET, PUT, DELETE, and POST all have alternate intended failure tests. More examples are presented within the `test.py` file, which you may view at your own will.
