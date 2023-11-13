import requests

# Base url
base = "http://127.0.0.1:5000/"

# Change flavor test
response = requests.get(base + "iceCream/4")
print(response.json())
response = requests.put(base + "iceCream/4", data={"name": "Cookies and Creme"})
print(response.json())

# Delete flavor test
response = requests.get(base + "iceCream/5")
print(response.json())
requests.delete(base + "iceCream/5")
response = requests.get(base + "iceCream/5")
print(response.json())

# Add flavor test
response = requests.post(base + "iceCream/5", data={"name": "Chocolate Chip Cookie Dough"})
print(response.json())
