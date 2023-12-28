def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# Example usage:
gen = my_generator()

for value in gen:
    print(value)
