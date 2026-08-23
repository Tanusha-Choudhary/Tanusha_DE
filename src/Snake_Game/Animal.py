class Animal:
    def __init__(self):
        self.eyes = 2
        self.nose =1
        self.legs = 2
        self.hand =2
    def breath(self):
        print("Air IN-OUT")
class Dynasour(Animal):
    def __init__(self):
        Animal.__init__(self)
D1 = Dynasour()
print(D1.eyes)
D1.breath()