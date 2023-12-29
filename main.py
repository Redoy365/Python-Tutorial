f = open("myfile.txt", "x")
f.close()

f = open("myfile.txt", "w")
f.write("Hello World!")
f.close()

f = open("myfile.txt", 'r')
print(f.read())