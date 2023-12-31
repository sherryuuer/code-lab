class MyGen():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
