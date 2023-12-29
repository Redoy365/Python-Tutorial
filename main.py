class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

setattr(Person, 'GPA', 5.00)

print(dir(Person))
