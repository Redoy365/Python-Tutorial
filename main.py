def counter():
    count = 1
    while True:
        yield count
        count += 1


# Example usage:
counter_gen = counter()

for _ in range(5):
    print(next(counter_gen))
