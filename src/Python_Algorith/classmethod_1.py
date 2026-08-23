class car:
    brand ="BNW"
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @classmethod
    def info(cls):
        return cls.brand
    @staticmethod
    def s_price():
        return 100
c1 = car("Neno",2324)
print(c1.name)
print(c1.price)
print(car.info())
print(car.s_price())
