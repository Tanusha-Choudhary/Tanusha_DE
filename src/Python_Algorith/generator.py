class generator1:
    def gen(self):
        for i in range(5):
            yield 1
            yield 2
            yield 3
            yield 4
G1 = generator1().gen()
print(G1.__next__())
print(G1.__next__())
print(next(G1))
print(next(G1))
