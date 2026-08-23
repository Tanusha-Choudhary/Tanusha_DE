def add_m(*args):
    # print(args)
    sum=0
    for i in args:
        sum=sum+i
    return sum

# print(add_m(21,2,3,4))
def calculate(n,**kwargs):
    # print(n,kwargs)
    # for key,value in kwargs.items():
    #     print(n,key,value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
# calculate(3,add=3,multiply=4)

class Car:
    def __init__(self,**kwargs):
        # self.name=kwargs["name"]
        # self.price=kwargs["price"]
        #             OR
        # Using Get it doesn't through KeyError
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
# my_car=Car(name="Nexon car",price=100)
my_car=Car(name="Ritz") # it will not through error and give none result using get method
print(my_car.name)
print(my_car.price)