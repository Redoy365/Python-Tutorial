class format:
    def __init__(self):
        pass

    def myfunc(*para):
        myorder = "I want {2} pieces of item {0} for {1} dollars."
        print(myorder.format(para[0], para[1], para[2]))

format.myfunc(3, 567, 49.95)