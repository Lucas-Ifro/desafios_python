from functools import reduce
from operator import add

valores = (12, 34, 1, 65)

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)

print(max(valores))
print(min(valores))
print(sum(valores))
print(reduce(add,valores))
print(list(reversed(valores)))
print(valores)