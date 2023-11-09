import requests

base = "http://127.0.0.1:5000/"

response = requests.get(base + "iceCream/4")
print(response.json())
response = requests.put(base + "iceCream/4", data={"name": "Cookies and Creme"})
print(response.json())
response = requests.get(base + "iceCream/4")
print(response.json())
