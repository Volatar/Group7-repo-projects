import requests

# Base url
base = "http://127.0.0.1:5000/"


def test_get():
    response = requests.get(base + "iceCream/4")
    assert response.status_code == 201


def test_get_no_id():
    response = requests.get(base + "iceCream/6")
    assert response.status_code != 201


def test_put():
    response = requests.put(base + "iceCream/4", data={"name": "Cookies and Creme"})
    assert response.status_code == 203


def test_put_no_id():
    response = requests.put(base + "iceCream/6", data={"name": "Cookies and Creme"})
    assert response.status_code != 203


def test_delete():
    response = requests.delete(base + "iceCream/5")
    assert response.status_code == 204


def test_delete_no_id():
    response = requests.delete(base + "iceCream/5")
    assert response.status_code != 204


def test_post():
    response = requests.post(base + "iceCream/5", data={"name": "Chocolate Chip Cookie Dough"})
    assert response.status_code == 202


def test_post_existing_id():
    response = requests.post(base + "iceCream/3", data={"name": "Chocolate Chip Cookie Dough"})
    assert response.status_code != 202
