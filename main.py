import re

txt = "The rain in Spain"

x = re.split("\s", txt, 1)
y = re.split("\s", txt, 2)

print(x)
print(y)