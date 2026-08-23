

# Want to add 10 in a first


def add_10(func):
    def inner(a,b):
        return a+10,b
    return inner

def add_f (a,b):
    print(a+b)
add_f= add_10(add_f)
print(add_f(2,2))
