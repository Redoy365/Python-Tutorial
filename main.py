class MyIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item


# Example usage:
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)
