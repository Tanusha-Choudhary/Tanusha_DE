class A:
    def __init__(self,price):
        self.price = price
    def feature1(self):
        print("I am a feature1")
    def feature2(self):
        print("I am a feature2")
class B(A):
    def __init__(self,price):
        super().__init__(price)
    def feature3(self):
        print("I am a feature3")
    def feature4(self):
        print("I am a feature4")
A1 = B(2)
print(A1.price)
A1.feature1()
A1.feature2()
A1.feature3()
A1.feature4()
# METHOD RESOLUTION ORDER (LEFT to RIGHT)
# INHERIT SUPER CLASS
