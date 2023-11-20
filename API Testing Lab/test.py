import requests

# Base url
base = "http://127.0.0.1:5000/"


def test_get():
    response = requests.get(base + "iceCream/4")
    assert response.json() == {"4": "Cotton Candy"}
    assert response.status_code == 200


def test_get_no_id():
    response = requests.get(base + "iceCream/6")
    assert response.json() == {"message": "ID is invalid"}
    assert response.status_code != 200


def test_put():
    response = requests.put(base + "iceCream/4", data={"name": "Cookies and Creme"})
    assert response.json() == {"4": "Cookies and Creme"}
    assert response.status_code == 201


def test_put_no_id():
    response = requests.put(base + "iceCream/6", data={"name": "Cookies and Creme"})
    assert response.json() == {"message": "ID is invalid"}
    assert response.status_code != 201


def test_delete():
    response = requests.delete(base + "iceCream/5")
    assert response.json() == {"message": "Item is deleted from the menu"}
    assert response.status_code == 200


def test_delete_no_id():
    response = requests.delete(base + "iceCream/5")
    assert response.json() == {"message": "ID is invalid"}
    assert response.status_code != 200


def test_post():
    response = requests.post(base + "iceCream/5", data={"name": "Chocolate Chip Cookie Dough"})
    assert response.json() == {"5": "Chocolate Chip Cookie Dough"}
    assert response.status_code == 201


def test_post_existing_id():
    response = requests.post(base + "iceCream/3", data={"name": "Chocolate Chip Cookie Dough"})
    assert response.json() == {"message": "ID already exists"}
    assert response.status_code != 201
