f = open("file1.txt", "a")
f.truncate(10)
f.close()

#open and read the file after the truncate:
f = open("file1.txt", "r")
print(f.read())