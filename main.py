f = open("file1.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open("file1.txt", "r")
print(f.read())
f.close()

