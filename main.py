class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

x = getattr(Person, "age")
print(x)