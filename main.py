class format:
    def __init__(self):
        pass

    def myfunc(*para):
        myorder = "I want {} pieces of item {} for {} dollars."
        print(myorder.format(para[0], para[1], para[2]))

format.myfunc(3, 567, 49, 95)