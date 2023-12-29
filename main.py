import os
os.mkdir("hello")

if os.path.exists("hello"):
    os.rmdir("hello")