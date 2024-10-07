print([n for n in range(1,10) if n%2 == 0])

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))