class MyIterable:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        for i in range(self.n):
            yield i
my_iterable = MyIterable(5)
for value in my_iterable:
    print(value)
