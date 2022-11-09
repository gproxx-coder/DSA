from functools import reduce

salaries = [100, 200, 300, 150, 250]

print(list(map(lambda x: x + x * 0.3, salaries)))

print(list(filter(lambda x: x % 100 == 0, salaries)))

print(reduce(lambda x, y: x + y, salaries))
