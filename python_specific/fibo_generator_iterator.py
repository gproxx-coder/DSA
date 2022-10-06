class Fibonacci:
    def __init__(self, limit):
        self.limit = limit

    def __next__(self):
        ret = self.first
        self.first, self.second = self.first + self.second, self.first
        while self.limit:
            self.limit -= 1
            return ret
        else:
            raise StopIteration

    def __iter__(self):
        self.i = 0
        self.first, self.second = 0, 1
        return self


def fibonacci(n):
    i = 0
    first, second = 0, 1
    while i < n:
        yield first
        first, second = first + second, first
        i += 1


for num in Fibonacci(10):
    print(num)
