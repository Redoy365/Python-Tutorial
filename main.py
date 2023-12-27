
x = "awesome"
print("Python is "+x)

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is "+x)
