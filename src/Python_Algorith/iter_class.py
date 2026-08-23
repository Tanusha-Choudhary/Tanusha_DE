class TopCounter:
    def __init__(self):
        self.counter = 0
    def __next__(self):
        val = self.counter
        self.counter += 1
        return val
    def __iter__(self):
        return self
values1= TopCounter()
for i in values1:
    print(i)