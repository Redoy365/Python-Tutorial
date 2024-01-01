import re

txt = "The rain in Spain "
x = re.search("ai", txt)

print(x.span()) #this will print an object
print(x.start()) #this will print an object
print(x.end()) #this will print an object
print(x.group()) #this will print an object
print(x.re) #this will print an object
print(x.endpos) #this will print an object