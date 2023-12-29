class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')

print(x)