import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

z = json.loads(y)

# the result is a JSON string:
print(y)
print(z["city"])