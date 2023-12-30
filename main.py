class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = myObj().age.age
y = myObj().name

print(x)
print(y)